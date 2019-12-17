#import the library used to query a website
import os
import tagme
import pickle
import urllib.request as urllib2
import urllib.parse
from bs4 import BeautifulSoup
from math import log
from igraph import *
from selenium import webdriver
import time
import re


def scrape_func(concept_name):
	query = urllib.parse.quote(concept_name)
	wiki = "https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/"+query+"&limit=500"
	options = webdriver.FirefoxOptions()
	options.add_argument('-headless')
	
	driver = webdriver.Firefox(firefox_options=options)
	driver.get(wiki)
	regex=re.compile(r'Talk:|User:|User talk:')
	answer=[]
	while(1):
		soup = BeautifulSoup(driver.page_source,"lxml")
		links=soup.find(id="mw-whatlinkshere-list")
		try:
			list_it=links.children
		except:
			return []
	
		for i in list_it:
			if(i !="\n"):
				name_tag=i.find('a')
				answer.append(name_tag.text)
				sub_list=i.find('ul')
				if(sub_list != None):
					for li in sub_list:
						if(li!="\n"):
							names=li.find('a')
							answer.append(names.text)
		try:
			continue_link = driver.find_element_by_link_text('next 500')
			#print(len(answer))
			if(len(set(answer))>=20000):
				break
			continue_link.click()
		except:
			break

	driver.quit()
	return answer

#topics=['NLP']
topics = ['ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']

for topicname in topics:
	print(topicname)
	dir_name='4_Topic_pkl/'+topicname #'./dataset/'+topicname+'_text'
	dir_out_path='4_Out_pkl/'+topicname
	if not os.path.exists(dir_out_path):
			os.makedirs(dir_out_path)
	for lec_name in os.listdir(dir_name):
#	for lec in range(1,len(os.listdir(dir_name))+1):
		print(lec_name)
#		lec_name='lec'+str(lec)+'.txt.pkl'
#		print(lec_name)
		out_path = dir_out_path+'/'+lec_name
		if os.path.exists(out_path):
			continue
		topic_path=dir_name+'/'+lec_name
		concepts_list= pickle.load(open(topic_path,"rb"))
#		print(concepts_list)

		backlinks=[]
		for concept in concepts_list:
			backlinks.append(set(scrape_func(concept)))
		
		dict_backlinks=dict(zip(concepts_list,backlinks))
		
		with open(out_path, 'wb') as f:
			pickle.dump(dict_backlinks, f)
		# my_graph= graph_construction(concepts_list,1,threshold=0)
		# with open(dir_out_path, 'wb') as f:
		# 	pickle.dump(my_graph, f)

