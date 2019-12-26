import os
import word2vec
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import nltk
from lib.textsplit.tools import get_penalty, get_segments
from lib.textsplit.algorithm import split_optimal, split_greedy, get_total
import re

corpus_path = './lib/text8'  # be sure your corpus is cleaned from punctuation and lowercased
if not os.path.exists(corpus_path):
    get_ipython().system(u'wget http://mattmahoney.net/dc/text8.zip')
    get_ipython().system(u'unzip {corpus_path}')
wrdvec_path = './lib/wrdvecs-text8.bin'
if not os.path.exists(wrdvec_path):
    get_ipython().magic(u"time word2vec.word2vec(corpus_path, wrdvec_path, cbow=1, iter_=5, hs=1, threads=4, sample='1e-5', window=15, size=200, binary=1)")
model = word2vec.load(wrdvec_path)
wrdvecs = pd.DataFrame(model.vectors, index=model.vocab)
filename = "./lib/finalized_model.sav"
pickle.dump(model, open(filename, 'wb'))
del model
print(wrdvecs.shape)
nltk.download('punkt')
sentence_analyzer = nltk.data.load('tokenizers/punkt/english.pickle')

segment_len = 20  # segment target length in sentences
topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
for topicname in topics:
    print(topicname)
    dir_name='./2_Text/'+topicname
    dir_out_path='./3_Segment/'+topicname
    if not os.path.exists(dir_out_path):
            os.makedirs(dir_out_path)
    for lec_name in os.listdir(dir_name):
        book_path=dir_name+'/'+lec_name
        book = topicname+'_lec_'+lec_name
        out_path = dir_out_path+'/'+lec_name+"/"
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        with open(book_path, 'rt') as f:
            text = " ".join(f.readlines()[6:]).replace('', '')
            text = re.sub(r'((Refer Slide Time:\s*[0-9][0-9]\s*:\s*[0-9][0-9]))','', text)
            text = re.sub(r'((Refer Slide Time:\s*[0-9]\s*:\s*[0-9][0-9]))','', text)
            text = re.sub(r'((\s*[0-9][0-9]\s*:\s*[0-9][0-9]))','', text)
            text = re.sub(r'((\s*[0-9]\s*:\s*[0-9][0-9]))','', text)
            text = text.strip().replace('()', '').replace('\n',' ').replace("‘", "'").replace("’", "'")
        sentenced_text = sentence_analyzer.tokenize(text)
        vecr = CountVectorizer(vocabulary=wrdvecs.index)
        sentence_vectors = vecr.transform(sentenced_text).dot(wrdvecs)
        if(len(sentence_vectors) > 40):
            penalty = get_penalty([sentence_vectors], segment_len)
            optimal_segmentation = split_optimal(sentence_vectors, penalty, seg_limit=250)
            segmented_text = get_segments(sentenced_text, optimal_segmentation)
            for i, segment_sentences in enumerate(segmented_text):
                segment_str = ''.join(segment_sentences)
                with open(out_path+str(i)+'.txt', "w") as text_file:
                    text_file.write("%s" % segment_str.strip().replace(".", ". ").replace("?", "? ").replace("\\s+", "\\s"))
            greedy_segmentation = split_greedy(sentence_vectors, max_splits=len(optimal_segmentation.splits))
            greedy_segmented_text = get_segments(sentenced_text, greedy_segmentation)
            lengths_optimal = [len(segment) for segment in segmented_text for sentence in segment]
            lengths_greedy = [len(segment) for segment in greedy_segmented_text for sentence in segment]
            df = pd.DataFrame({'greedy':lengths_greedy, 'optimal': lengths_optimal})
            totals = [get_total(sentence_vectors, seg.splits, penalty) 
                  for seg in [optimal_segmentation, greedy_segmentation]]

print("Segmentation over...........")
