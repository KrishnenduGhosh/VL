#import the library used to query a website
import json

topics=['CA']
topics1 = ['CA', 'ML', 'NLP', 'AI', 'GT', 'DSA']
topics2 = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NMP', 'MA3', 'DMS', 'FAL', 'CG', 'CN', 'DAA', 'CD', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']

print("Statistics for Dataset Data 1 Annotated so far")
ctr1 = 0 # Number of segments
ctr2 = 0 # Number of concepts
ctr3 = 0 # Number of words
ctr4 = 0 # Number of courses
for topicname in topics:
	dir_name='./Topic/'+topicname+'.json'
	with open(dir_name, 'rt') as f:	
		data = json.load(f)
		for d in data:
#			print("d['topics']: ",d['topics']," size: ",len(d['topics']))
			ctr2 += len(d['topics'])
#			print("d['text']: ",d['text']," size: ",len(d['text']))
			ctr3 += len(d['text'])
		ctr1 += len(data)
print("Number of segments: ", ctr1)
print("Number of concepts: ", ctr2)
print("Number of words: ", ctr3)
print("Number of courses: ", len(topics))

print("Statistics for Dataset Data 1")
ctr1 = 0 # Number of segments
ctr2 = 0 # Number of concepts
ctr3 = 0 # Number of words
ctr4 = 0 # Number of courses
for topicname in topics1:
	dir_name='./Topic/'+topicname+'.json'
	with open(dir_name, 'rt') as f:	
		data = json.load(f)
		for d in data:
#			print("d['topics']: ",d['topics']," size: ",len(d['topics']))
			ctr2 += len(d['topics'])
#			print("d['text']: ",d['text']," size: ",len(d['text']))
			ctr3 += len(d['text'])
		ctr1 += len(data)
print("Number of segments: ", ctr1)
print("Number of concepts: ", ctr2)
print("Number of words: ", ctr3)
print("Number of courses: ", len(topics1))

print("Statistics for Dataset Data 2")
ctr1 = 0 # Number of segments
ctr2 = 0 # Number of concepts
ctr3 = 0 # Number of words
ctr4 = 0 # Number of courses
for topicname in topics2:
	dir_name='./Topic/'+topicname+'.json'
	with open(dir_name, 'rt') as f:	
		data = json.load(f)
		for d in data:
#			print("d['topics']: ",d['topics']," size: ",len(d['topics']))
			ctr2 += len(d['topics'])
#			print("d['text']: ",d['text']," size: ",len(d['text']))
			ctr3 += len(d['text'])
		ctr1 += len(data)
print("Number of segments: ", ctr1)
print("Number of concepts: ", ctr2)
print("Number of words: ", ctr3)
print("Number of courses: ", len(topics2))
