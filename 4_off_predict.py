from __future__ import absolute_import, division, print_function, unicode_literals
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
import os
import time
import sys

def logg(val):
	if val == 0.0:
		return 1.0
	else:
		return log(val) 

def plot_graph(my_graph):
	layout=my_graph.layout()
	#plot(my_graph,layout=layout,bbox = (1000, 1000), margin = 100)

def dice_coefficient(backlinks_1, backlinks_2):
	link_intersection=list(backlinks_1.intersection(backlinks_2))
	similarity=(2.0*len(link_intersection))/(len(backlinks_1)+len(backlinks_2))
	return similarity

def NGD(backlinks_1, backlinks_2):
	num_of_wiki=45627664
	link_intersection=list(backlinks_1.intersection(backlinks_2))
	if len(link_intersection) == 0:
		similarity=0.0
	else:
		similarity=1-(log(max(len(backlinks_1),len(backlinks_2)))-log(len(link_intersection)))/(log(num_of_wiki)-log(min(len(backlinks_1),len(backlinks_2)))) 
	return similarity

def graph_construction(data_dict,type_sim,threshold):
	backlinks=[]
	concepts_list=[]
	for concept in data_dict.keys():
		concepts_list.append(concept)
		backlinks.append(set(data_dict[concept]))
	dict_backlinks=dict(zip(concepts_list,backlinks))
	num_concepts=len(concepts_list)	
	edge_list=[ (concepts_list[i],concepts_list[j]) for i in range(0,num_concepts) for j in range(i+1,num_concepts) ]
	my_graph=Graph()
	my_graph.add_vertices(concepts_list)
	my_graph.vs["label"] = my_graph.vs["name"]
	my_graph.add_edges(edge_list)
	my_graph.es["weight"]=1.0
	edges_to_be_deleted=[]
	for i in edge_list:
		similarity1=dice_coefficient(dict_backlinks[i[0]],dict_backlinks[i[1]])
		similarity2=NGD(dict_backlinks[i[0]],dict_backlinks[i[1]])
		similarity=(similarity1 * type_sim)+(similarity2 * (1-type_sim))/2
		if(similarity < threshold):
			edges_to_be_deleted.append((i[0],i[1]))
		my_graph[i[0],i[1]]=similarity
	my_graph.delete_edges(edges_to_be_deleted)
	return my_graph

def graph_construction1(data_dict,type_sim,threshold):
	backlinks=[]
	concepts_list=[]
	for concept in data_dict.keys():
		concepts_list.append(concept)
		backlinks.append(set(data_dict[concept]))
	dict_backlinks=dict(zip(concepts_list,backlinks))
	num_concepts=len(concepts_list)	
	edge_list=[ (concepts_list[i],concepts_list[j]) for i in range(0,num_concepts) for j in range(i+1,num_concepts) ]
	my_graph=Graph()
	my_graph.add_vertices(concepts_list)
	my_graph.vs["label"] = my_graph.vs["name"]
	my_graph.add_edges(edge_list)
	my_graph.es["weight"]=1.0
	edges_to_be_deleted=[]
	for i in edge_list:
		if type_sim == 0:
			similarity=dice_coefficient(dict_backlinks[i[0]],dict_backlinks[i[1]])
		else:
			similarity=NGD(dict_backlinks[i[0]],dict_backlinks[i[1]])
		if(similarity < threshold):
			edges_to_be_deleted.append((i[0],i[1]))
		my_graph[i[0],i[1]]=similarity
	my_graph.delete_edges(edges_to_be_deleted)
	return my_graph

def community_construction_1(my_graph): #Optimal Modularity
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_optimal_modularity(weights= my_graph.es["weight"]) 
#	print("Optimal Modularity")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_2(my_graph): #Walktrap
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_walktrap(weights=edge_weights, steps=4) 
#	print("Walktrap")
#	print(community.as_clustering())
	giant=community.as_clustering().giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_3(my_graph): #Edge Betweenness
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_edge_betweenness(clusters=None, directed=False, weights=edge_weights) 
#	print("Edge Betweenness")
#	print(community.as_clustering())
	giant=community.as_clustering().giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_4(my_graph): #Multi-level
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_multilevel(weights= my_graph.es["weight"]) 
#	print("Multi-level")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_5(my_graph): #Fast-greedy
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_fastgreedy(weights= my_graph.es["weight"]) 
#	print("Fast-greedy")
#	print(community)
	giant=community.as_clustering().giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_6(my_graph): #Eigen-vector
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_leading_eigenvector(weights= my_graph.es["weight"]) 
#	print("Eigen-vector")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_7(my_graph): #Spinglass
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_spinglass(weights= my_graph.es["weight"]) 
#	print("Spinglass")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_8(my_graph): #Label Propagation
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_label_propagation(weights= my_graph.es["weight"]) 
#	print("Label Propagation")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def community_construction_9(my_graph): #Infomap
	edge_weights=my_graph.es["weight"]
	community=my_graph.community_infomap() 
#	print("Infomap")
#	print(community)
	giant=community.giant()
	giant_subgraph_nodes=giant.vs["name"]
	my_graph_nodes=my_graph.vs["name"]
	off_topic_nodes=list(set(my_graph_nodes)-set(giant_subgraph_nodes))
	return off_topic_nodes

def run(ff,dir_in_path,sim,threshold):
	off_topics = []
	if threshold == 0.0:
		th = 1
	elif threshold < 0.04:
		th = 3
	elif threshold < 0.1:
		th = 9
	elif threshold < 0.2:
		th = 14
	else:
		th = 1
	for filename in sorted(os.listdir(dir_in_path)):
#		print("File: " + filename)
		file_path="./"+dir_in_path+"/"+filename
		with open(file_path, 'rb') as f:
			data = pickle.load(f)
			if (len(data) > th):
				my_graph= graph_construction(data,sim,threshold) #
				v=[i for i, x in enumerate(my_graph.degree()) if x == 0]
				my_graph.delete_vertices(v)
				off_topics.extend(ff(my_graph))
	return off_topics

def predict(t,s,th):
	dir_json_path="./5_Annotated/" ##Tagged
	dir_in_path="./4_Out_pkl/"+t
	dir_out_path="./5_Off/"
	if not os.path.exists(dir_out_path):
		os.makedirs(dir_out_path)
	olist = []
	glist = []
	wdata = []
	olist.extend(run(community_construction_1,dir_in_path,s,th)) ## function name
	with open(dir_json_path + t +'.json') as json_file:
		data = json.load(json_file)
		for d in data:
			offlist = []
			for o in olist:
				if o in d['topics']:
					offlist.append(o)
			for gg in d['gold']:
				glist.append(gg)
			wdata.append({"id":d['id'],"text":d['text'],"topics":d['topics'],"mentions":d['mentions'],"gold":d['gold'],"off":list(set(offlist))})
	c, p, cp = evaluate(list(set(olist)),list(set(glist)))
	filename=os.path.join(dir_out_path, t+".json")
	with open(filename, 'w') as outfile:
		json.dump(wdata, outfile, indent=4)
	if p != 0:
		pre = cp / p
	else:
		pre = 0.0
	if c != 0:
		rec = cp / c
	else:
		rec = 0.0
	if (pre + rec) != 0:
		fsc = (2 * pre * rec) / (pre + rec)
	else:
		fsc = 0.0
	print('Course: ' + t + ' sim: ' + str(s) + ' threshold: ' + str(th) + ' P: ' + str(round(pre, 2)) + ' R: ' + str(round(rec, 2)) + ' F: ' + str(round(fsc, 2)))
	return (c,p,cp)

def evaluate(olist, glist):
	CP = 0
	for o in olist:
		for g in glist:
			if o==g:
				CP += 1
#	print("C: ",C,"P: ",P,"CP: ",CP)
	return(len(glist), len(olist), CP)

if __name__=="__main__":
	topics=['AI','DSA','GT','NLP','ML','CA']
#	topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
	type_sim = [1.0]
	threshold = [0.0]
#	threshold = [0.0,0.01,0.02,0.04,0.06,0.08,0.1]
	for s in type_sim:
		for th in threshold:
			C = 0
			P = 0
			CP = 0
			for topicname in topics:
				c, p, cp = predict(topicname,s,th)
				C += c
				P += p
				CP += cp
			if P != 0:
				pre = CP / P
			else:
				pre = 0.0
			if C != 0:
				rec = CP / C
			else:
				rec = 0.0
			if (pre + rec) != 0:
				fsc = (2 * pre * rec) / (pre + rec)
			else:
				fsc = 0.0
			print('P: ' + str(round(pre, 2)) + ' R: ' + str(round(rec, 2)) + ' F: ' + str(round(fsc, 2)))
	print("Off-keys predicted...........")
