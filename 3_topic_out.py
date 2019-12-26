#import the library used to query a website
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import tagme
import pickle

topics = ['PSP','NLP','ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']

tagme.GCUBE_TOKEN = "0b4eed68-e456-4488-a5a6-7a608ea7e32b-843339462"

for topicname in topics:
	print(topicname)
	dir_name='./3_Segment/'+topicname #'./dataset/'+topicname+'_text'
	dir_out_path='./4_Topic_pkl/'+topicname
	if not os.path.exists(dir_out_path):
			os.makedirs(dir_out_path)
	for lec_name in os.listdir(dir_name):
#		print(lec_name)
		book_path=dir_name+'/'+lec_name
#		print("book_path1: ",book_path)
		topics=[]
#		print("book_path2: ",book_path)
		for para_name in os.listdir(book_path):
			para_path=book_path+'/'+para_name
#			print("para_path: ",para_path)
			out_path = dir_out_path+'/'+lec_name+".pkl"
			with open(para_path, 'rt') as f:
				text = " ".join(f.readlines())
#			print("text: ",text)
			resp = tagme.annotate(text)
#			print("resp: ",resp)
			topics_list=[]
			if (resp!=None and resp.get_annotations(0.4)!=None):
				for ann in resp.get_annotations(0.4):
					topics_list.append(ann.entity_title)
			topics_list=list(set(topics_list))
			topics.extend(topics_list)
		topics=list(set(topics))
#		print("topics: ",topics)
		with open(out_path, 'wb') as f:
			pickle.dump(topics, f)
