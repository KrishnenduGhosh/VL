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
	similarity=(log(max(len(backlinks_1),len(backlinks_2)))-log(len(link_intersection)))/(log(num_of_wiki)-log(min(len(backlinks_1),len(backlinks_2))))
	return similarity

def graph_construction(data_dict,type_sim=0,type_graph=0,threshold=0):
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
		similarity=dice_coefficient(dict_backlinks[i[0]],dict_backlinks[i[1]])
		#print(i[0],i[1],similarity)
		if(similarity<=threshold):
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

def run(ff,dir_in_path,sim,graph,threshold):
    off_topics = []
    for filename in sorted(os.listdir(dir_in_path)):
#        print("File: " + filename)
        file_path="./"+dir_in_path+"/"+filename
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            if (len(data) > 2):
                my_graph= graph_construction(data,sim,graph,threshold) #
                v=[i for i, x in enumerate(my_graph.degree()) if x == 0]
                my_graph.delete_vertices(v)
                off_topics.extend(ff(my_graph))
    return off_topics

def predict(t):
    C = 0
    P = 0
    CP = 0
    dir_json_path="./5_Tagged/" ##Tagged
    dir_in_path="./4_Out_pkl/"+t
    dir_out_path="./5_Off/"
#    if not os.path.exists(dir_out_path):
#        os.makedirs(dir_out_path)
    type_sim = [0,1]
    type_graph = [0,1]
#    threshold = [0.0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05]
    threshold = [0.0]
    wdata = []
    for s in type_sim:
        for g in type_graph:
    	    for th in threshold:
                C = 0
                P = 0
                CP = 0
                olist = []
                glist = []
                olist.extend(run(community_construction_1,dir_in_path,s,g,th)) ## function name
                print("course: ",t,"sim: ",s," graph: ",g," threshold: ",th)
                with open(dir_json_path + t +'.json') as json_file:
                    data = json.load(json_file)
                    for d in data:
                        offlist = []
                        for o in olist:
                            if o in d['topics']:
                                offlist.append(o)
       	                wdata.append({'id': d['id'],'text': d['text'],'topics': d['topics'],'mentions': d['mentions'],'gold': d['gold'],'off': list(set(offlist))})
       	                for gg in d['gold']:
                            glist.append(gg)
                print("len(glist): ",len(glist)," list(set(glist)): ",len(list(set(glist)))," len(olist): ",len(olist)," list(set(olist)): ",len(list(set(olist))))
       	        c, p, cp = evaluate(list(set(olist)),list(set(glist)))
                pre = cp / p
                rec = cp / c
                fsc = (2 * pre * rec) / (pre + rec)
                print('P: ' + str(pre) + '/R: ' + str(rec) + '/F: ' + str(fsc))
                C += c
       	        P += p
       	        CP += cp
       	        print('Course: ' + t + '/sim: ' + str(s) + '/graph: ' + str(g) + '/threshold: ' + str(th) + '/measure: 1/c: ' + str(c) + '/p: ' + str(p) + '/cp: ' + str(cp))
                with open(dir_out_path + t + '_' + str(s) + '_' + str(g) + '_' + str(th) + '_1.json', 'w') as outfile: ## function name
                    json.dump(wdata, outfile, indent=4)
#    print('C: ' + str(C) + '/P: ' + str(P) + '/CP: ' + str(CP))
    pre = CP / P
    rec = CP / C
    fsc = (2 * pre * rec) / (pre + rec)
#    print('P: ' + str(pre) + '/R: ' + str(rec) + '/F: ' + str(fsc))

def evaluate(olist, glist):
    CP = 0
    for o in olist:
        for g in glist:
            if o==g:
                CP += 1
#    print("C: ",C,"P: ",P,"CP: ",CP)
    return(len(glist), len(olist), CP)

if __name__=="__main__":
    topics=['AI','DSA','GT','NLP','ML','CA']
#    topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
    for topicname in topics:
#        print(topicname)
        predict(topicname)
    print("Off-keys predicted...........")
