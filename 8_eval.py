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

def write_result():
  dir_in1='./6_Retrieved/'
  dir_in2='./7_Reranked/'
  dir_out='./8_Result/trec_eval/test'
  topics=['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  rtdata = []
  rrdata = []
  for t in topics:
    with open(dir_in1 + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        qid = d['id'] + "_" 
        for i in range(0,len(d['off'])):
          qid = qid + d['off'][i].replace(" ","_") #
          docs = d['ret'][i]
          scores = d['score'][i]
          for j in range(0,len(docs)):
            docno = docs[j] #
            sim = scores[j] #
            rank = (j+1) #
            rtdata.append(qid + " > " + qid + "_" + docno + " " + str(rank) + " " + str(sim) + " RT")
    with open(dir_in2 + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        qid = d['id'] + "_" 
        for i in range(0,len(d['off'])):
          qid = qid + d['off'][i].replace(" ","_") #
          docs = d['ret'][i]
          scores = d['score'][i]
          for j in range(0,len(docs)):
            docno = docs[j] #
            sim = scores[j] #
            rank = (j+1) #
            rrdata.append(qid + " > " + qid + "_" + docno + " " + str(rank) + " " + str(sim) + " RR")
  rtdata = sorted(set(rtdata))
  rrdata = sorted(set(rrdata))
  for rt in rtdata:
    file1 = open(dir_out + "/RT.txt","a")
    file1.write(rt + "\n")
    file1.close()
  for rr in rrdata:
    file1 = open(dir_out + "/RR.txt","a")
    file1.write(rr + "\n")
    file1.close()

def main(): #main for menu
  write_result()

if __name__ == '__main__':
  main()

