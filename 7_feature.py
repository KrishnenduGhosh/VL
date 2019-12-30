import os
import word2vec
from math import log
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk
from lib.textsplit.tools import get_penalty, get_segments
from lib.textsplit.algorithm import split_optimal, split_greedy, get_total
import re
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import scoring
import time
import json
import collections

tri = {'define','defined','definition'}

def logg(n):
  if n > 0:
    return log(n)
  else:
    return 0

def NGD(backlinks_1, backlinks_2):
  num_of_wiki=45627664
  link_intersection=list(backlinks_1.intersection(backlinks_2))
  similarity=(logg(max(len(backlinks_1),len(backlinks_2)))-logg(len(link_intersection)))/(logg(num_of_wiki)-logg(min(len(backlinks_1),len(backlinks_2))))
  return similarity

def f1(topics, offtopic, data): #aws for <topics,offtopic,data> pair
#  print("topics: ",topics,"offtopic: ",offtopic,"data: ",len(data))
  aws = 0
  for t in topics:
    if t in data.keys():
      aws += NGD(data[t],data[offtopic])
  if len(topics) > 1:
    aws = aws / (len(topics)-1)
  return aws

def f2(topics, offtopic, data): #nm for <topics,offtopic,data> pair
  nm = 0
  topics.append(offtopic)
  for i in range(0,len(topics)):
    for j in range(0,len(topics)):
      if i != j:
        if topics[i] in data.keys():
          l1 = data[topics[i]]
          if topics[j] in l1:
            nm += 1
  if len(topics) > 2:
    nm = (nm / 2) / ((len(topics)-1) * (len(topics)-2))
  return nm

def fo(text, concept): # fo for <text,concept> pair
  return text.find(concept)

def co(sent, concept): # co for <sent,concept> pair
  ctr = 0
  words = sent.replace("[^A-Za-z0-9\\s+-,.;!?'\"]", "").split(" ")
  if concept in words:
    for t in tri:
      if t in words:
        ctr += 1
  if ctr > 0:
    return 1
  else:
    return 0

def max_tf(text): # maxtf for <words> pair
  words = text.replace("[^A-Za-z0-9\\s+]", "").split(" ")
  mapp = {}
  for w in words:
    mapp[w] = text.find(w)
  maxx = 0
  for m in mapp:
    if mapp[m] > maxx:
      maxx = mapp[m]
  return maxx

def tf(text, concept): # normalized tf for <text,concept> pair
#  print("text: ", text, "concept: ", concept)
  ctr = text.find(concept)
  maxtf = max_tf(text)
  if maxtf != 0:
    return 0.5 + (0.5 * (ctr / maxtf))
  else:
    return 0.5

def idf(offtopic, doc, vid): # idf for a <concept>
#  print("offtopic: ", offtopic, "doc: ", len(doc), "vid: ", vid)
  N = 0
  df = 0
  idpart = vid.split("_")
  for d in doc:
    if d.startswith(idpart[0]):
      N += 1
      occ = doc[d].find(offtopic)
      if occ > 0:
        df += 1
#  print("N: ", N, "df: ", df)
  if (df+1) != 0:
    idf = log(len(doc)/(df+1))
  return idf

def f3(text, topics, offtopic, data): # pc for <topics,offtopic,data> pair
  pc = 0
  if len(topics) == 0:
    pc = 1 - (fo(text,offtopic) / len(text))
  else:
    tot = 0
    for c in topics:
      tot += fo(text,c)
    if tot != 0:
      pc = 1 - ( (len(topics) * fo(text,offtopic)) / tot )
  return pc

def f4(text, topics, offtopic, data): # dc for <topics,offtopic,data> pair
  dc = 0
  sents = text.split("[!?.]")
  for s in sents:
    dc += co(s,offtopic)
  if dc > 0:
    dc = 1
  return dc

def f5(vid, text, offtopic, doc): # dc for <topics,offtopic,data> pair
#  print("text in f5: ",text)
  tfidf = 0
  words = text.split(" ")
  if tf(text,offtopic) > 0:
    tfidf = tf(text,offtopic) * idf(offtopic, doc, vid)
  return tfidf

def get_text(vid): #returns text for a given vid
  text = ''
  dir_dict='./4_Topic/'
#  print("vid in get_text: ",vid) # ./Segment/PSP_lec1_0"
  idpart = vid.split("_")
  with open(dir_dict + idpart[0] + ".json", 'rb') as f:
    data = json.load(f)
    for d in data:
      if d['id'].endswith(vid):
#        print("d['id']: ",d['id'])
#        print("vid: ",vid)
        text = d['text']
  return text

def get_topics(vid): #returns topics for a given vid
  topics = []
  dir_dict='./6_Retrieved/'
#  print("vid: ",vid)
  idpart = vid.split("_")
  with open(dir_dict + idpart[0] + ".json", 'rb') as f:
    data = json.load(f)
    for d in data:
      if d['id'] == vid:
        topics = d['topics']
  return topics

def merge(x, y):
  z = x.copy()
  z.update(y)
  return z

def get_dict(vid): #returns topics for a given vid
  dir_dict1='./4_Out_pkl/'
#  print("vid: ",vid)
  idpart = vid.split("_")
  data = {}
  for filename in sorted(os.listdir(dir_dict1 + idpart[0])):
    file_path = dir_dict1+idpart[0]+"/"+filename
    with open(file_path, 'rb') as file1:
      data1 = pickle.load(file1)
      data = merge(data, data1)
  return data

def rerank(vid, offtopic, ret, score, doc): #For given <offtopic,ret,score> pair modify <ret,score> pair
  rscore = []
  for j in range(0,len(ret)):
    rscore.append(0)
  dir_dict1='./4_Out_pkl/'
  dir_dict2='./6_Retrieved/'
  if len(ret) > 0:
    for i in range(0,len(ret)): # PSP_lec9_15
#      print("len(ret): ",len(ret),"len(score): ",len(score))
#      print("vid: ",vid,"ret[i]: ",ret[i],"offtopic: ",offtopic)
      topics = get_topics(ret[i])
      data = get_dict(vid)
      data.update(get_dict(ret[i]))
      text = get_text(ret[i])
#      print("topics: ",len(topics))
#      print("ret: ",len(ret))
      aws = f1(topics, offtopic, data)
      nm = f2(topics, offtopic, data)
      pc = f3(text, topics, offtopic, data)
      dc = f4(text, topics, offtopic, data)
      tfidf = f5(vid, text, offtopic, doc)
#      print(i)
      w = [0.000201,-0.023396,0.003563,-0.025573,0.0,-0.22064]
      rscore[i] = w[0] * score[i] + (w[1] * aws) + (w[2] * nm) + (w[3] * pc) + (w[4] * dc) + (w[5] * tfidf) ## test with different weights
      f = open("./7_Reranked/rerank.txt","a")
      towrite = vid + "," + offtopic.replace(" ","_") + "," + ret[i] + "," + str(round(score[i],2)) + "," + str(round(aws,2)) + "," + str(round(nm,2)) + "," + str(round(pc,2)) + "," + str(round(dc,2)) + "," + str(round(tfidf,2))
      f.write(towrite + "\n")
      f.close()
#      print("topics: ",topics,"aws: ",aws,"nm: ",nm,"pc: ",pc,"dc: ",dc,"tfidf: ",tfidf)
  sorted_rmap = sorted(zip(rscore,ret))
  rlist = [point[1] for point in sorted_rmap]
  return rlist

def load():
  doc = {}
  dir_in='./6_Retrieved/'
  topics = ['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  for t in topics:
    with open(dir_in + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        doc.update({d['id'] : d['text']})
  return doc

def run(doc):
  dir_in='./6_Retrieved/'
  dir_out_path='./7_Reranked/'
  topics=['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  print("Reranking segments.......")
  for t in topics:
    print(t)
    wdata = []
    with open(dir_in + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        re = []
        olist = d['off']
        rlist = d['ret']
        slist = d['score']
        for i in range(0,len(d['off'])):
          o = olist[i]
          r = rlist[i]
          s = slist[i]
          re.append(rerank(d['id'],o,r,s,doc))

def main(): #main for menu
  start_time = time.time()
  doc = load()
  run(doc)
  print("Exuction time: ", (time.time() - start_time))

if __name__ == '__main__':
  main()

