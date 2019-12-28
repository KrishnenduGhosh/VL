import os
import word2vec
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

def write_result():
  dir_in1='./6_Retrieved/'
  dir_out='./8_Result/trec_eval/test'
  topics=['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  rtdata = []
  for t in topics:
    with open(dir_in1 + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
#        qid = d['id'] + ":"
        for i in range(0,len(d['off'])):
          qid = d['id'] + ":" + d['off'][i].replace(" ","_") #
          docs = d['ret'][i]
          scores = d['score'][i]
          for j in range(0,len(docs)):
            docno = docs[j] #
            sim = scores[j] #
            rank = (j+1) #
            rtdata.append(qid + " > " + qid + ":" + docno + " " + str(rank) + " " + str(sim) + " RT")
  rtdata = sorted(set(rtdata))
  for rt in rtdata:
    file1 = open(dir_out + "/RT.txt","a")
    file1.write(rt + "\n")
    file1.close()

def retrieve():
  schema = Schema(vid=TEXT(stored=True), text=TEXT(stored=True), topics=TEXT(stored=True))
  ix = create_in("index", schema)
  writer = ix.writer()
  dir_in='./5_Off/'
  dir_out_path='./6_Retrieved/'
  topics=['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  print("Creating index.......")
  for t in topics:
    print(t)
    with open(dir_in + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        writer.add_document(vid=d['id'], text=d['text'], topics=d['topics'])
  writer.commit()
  
  print("Retrieving segments.......")
  for t in topics:
    print(t)
    wdata = []
    with open(dir_in + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        tlist = []
        tslist = []
        for o in d['off']:
          with ix.searcher() as s:
            q1 = QueryParser("text", ix.schema).parse(o)
            results = s.search(q1, limit = 10)
            rlist = []
            slist = []
            for r in results:
              rlist.append(r['vid'])
              slist.append(r.score)
            tlist.append(rlist)
            tslist.append(slist)
            wdata.append({'id': d['id'],'text': d['text'],'topics': d['topics'],'mentions': d['mentions'],'off': d['off'],'ret': tlist,'score': tslist})
#            for r in results:
#              print("Retrieved segment: ",r['vid']," with score: ",r.score)
    with open(dir_out_path + t + '.json', 'w') as outfile: ## function name
      json.dump(wdata, outfile, indent=4)

def main(): #main for menu
  start_time = time.time()
#  retrieve()
  print("Retrieval over...........")
  write_result()
  print("Exuction time: ", (time.time() - start_time))

if __name__ == '__main__':
  main()
