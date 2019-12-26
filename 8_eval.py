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
  dir_out='./8_Result/'
  topics=['AI','DSA','GT','NLP','ML','CA']
#  topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
  for t in topics:
    with open(dir_in1 + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        for i in range(0,len(d['off'])):
          qid = d['off'][i] #
          docs = d['ret'][i]
          scores = d['score'][i]
          for j in range(0,len(docs)):
            docno = docs[j] #
            sim = scores[j] #
            rank = (j+1) #
            file1 = open(dir_out + "/RT.txt","a")
            file1.write(qid + " > " + qid + "_" + docno + " " + str(rank) + " " + str(sim) + " RET")
            file1.close()
    with open(dir_in2 + t +'.json') as json_file:
      data = json.load(json_file)
      for d in data:
        for i in range(0,len(d['off'])):
          qid = d['off'][i] #
          docs = d['ret'][i]
          scores = d['score'][i]
          for j in range(0,len(docs)):
            docno = docs[j] #
            sim = scores[j] #
            rank = (j+1) #
            file1 = open(dir_out + "/RR.txt","a")
            file1.write(qid + " > " + qid + "_" + docno + " " + str(rank) + " " + str(sim) + " RER")
            file1.close()

def main(): #main for menu
  write_result()

if __name__ == '__main__':
  main()

