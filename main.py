from __future__ import absolute_import, division, print_function, unicode_literals
import os
import time
import pickle
import sys
import tagme
import json

def main():
  start_time = time.time()
  while True:
    print("Menu: (1)Preprocess (2)Segment (3)Find Topic (4)Find Off-topic (5)Retrieval (6)Re-ranking (7)Evaluate (8)Quit")
    choice = str(input(">>> ")).lower().rstrip()
    if choice=='1':
      os.system("python3 preprocess.py")
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='2':
      os.system("python3 para_split.py")
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='3':
      topic()
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='4':
      os.system("python3 off_predict.py")
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='5':
      os.system("python3 retrieval.py")
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='6':
      os.system("python3 rerank.py")
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='7':
      evaluate()
      print("Exuction time: ", (time.time() - start_time))
    elif choice=='8':
      break
    else:
      print("Invalid choice, please choose again\n")
  print("Thanks for retrieving.")

def topic():
  os.system("python3 tag.py")
  os.system("python3 topic_out.py")
  os.system("python3 off_out.py")
#  os.system("python3 post_annotation.py")
  print("Tagging over...........")

def evaluate():
  os.system("python3 eval.py")
  print("Evaluation over...........")

if __name__ == "__main__":
  tagme.GCUBE_TOKEN = "0b4eed68-e456-4488-a5a6-7a608ea7e32b-843339462"
  main()
