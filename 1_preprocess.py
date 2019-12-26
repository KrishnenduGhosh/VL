import urllib.request as urllib2
import urllib.parse
from bs4 import BeautifulSoup
from math import log
from igraph import *
import time
import re
import tagme
import pickle
import json
import random

def preprocess():
  ctr = 0
  directory = "./1_Data/"
  dir_out_path = "./2_Text/"
  if not os.path.exists(dir_out_path):
    os.makedirs(dir_out_path)
  for x in os.walk(directory):
    if(str(x[0]) != directory):
      odirectory = x[0].replace("s+","\ ")
      folder = odirectory.split("/")
#      print("odirectory: " + odirectory)
      if not os.path.exists(dir_out_path + folder[len(folder)-1]):
#        print("not exists")
        os.makedirs(dir_out_path + folder[len(folder)-1])
    for y in x:
      for z in y:
        if(z.endswith(".pdf")):
#          print("Running: " + "pdftotext " + odirectory + "/" + z)
          ctr=ctr+1
          os.system("pdftotext " + odirectory + "/" + z)
          os.system("mv " + odirectory + "/" + z.replace(".pdf",".txt") + " " + odirectory.replace("1_Data","2_Text") + "/")
  print("Preprocessing over for " + str(ctr) + " files")


if __name__=="__main__":
  preprocess()
  print("Preprocessed ...........")
