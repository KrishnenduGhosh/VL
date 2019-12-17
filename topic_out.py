#import the library used to query a website
import os
import tagme
import pickle

#topics=['PSP']
#topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
topics = ['ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']

tagme.GCUBE_TOKEN = "0b4eed68-e456-4488-a5a6-7a608ea7e32b-843339462"

for topicname in topics:
	print(topicname)
	dir_name='./3_Segment/'+topicname #'./dataset/'+topicname+'_text'
	dir_out_path='./4_Topic_pkl/'+topicname
	if not os.path.exists(dir_out_path):
			os.makedirs(dir_out_path)
	for lec_name in os.listdir(dir_name):
		print(lec_name)
		book_path=dir_name+'/'+lec_name
		if os.path.exists(book_path):
			continue
		topics=[]
		for para_name in os.listdir(book_path):
			para_path=book_path+'/'+para_name
			out_path = dir_out_path+'/'+lec_name+".pkl"
			with open(para_path, 'rt') as f:
				text = " ".join(f.readlines())
			resp = tagme.annotate(text)
			topics_list=[]
			if (resp!=None and resp.get_annotations(0.6)!=None):
				for ann in resp.get_annotations(0.6):
					topics_list.append(ann.entity_title)
			topics_list=list(set(topics_list))
			topics.extend(topics_list)
		topics=list(set(topics))
		with open(out_path, 'wb') as f:
			pickle.dump(topics, f)



#['Regular expression', 'Stop words', 'Crazy Little Thing', 'Natural Language Toolkit', 'Sentiment analysis', 'Letter case', 'N-gram', 'Word2vec', 'Kaggle', 'Genetic discrimination', 'The We and the I', 'We in Here', 'Python (programming language)', 'Semantics', 'When We On', 'Word embedding']
