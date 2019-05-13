#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')

    for p in soup.select('.mw-parser-output > p'):
        p = remove_embedded_tag(p, 'span')
        p = remove_embedded_tag(p, 'br')
        print(p.text)
        
def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[5]:


print(download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))


# Extracting tokens and unique words

# In[6]:


import nltk

FileName = "Name of text file with location.txt"

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("Name of text file with location.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[ ]:


def some_func(line):
    new_line = line.strip().lower()
    # convert to loser case
    
    return new_line

results = []

with open('Name of text file.txt', 'r') as f:
    count = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        new_line = some_func(line)
        count += 1
        results.append(new_line)
    print(count)
    
with open('new preprocessed name of text file.txt', 'w') as f:
    for l in results:
        f.write(l + '\n')


# Writing processed articles into a new file

# In[ ]:


import string
import re
x = [''.join(c for c in s if c not in string.punctuation) for s in results]
print(x)
with open('finalcleanfile.txt', 'w') as g:
    for l in x:
        g.write(l + '\n')


# Extracting tokens and unique words from clean file

# In[ ]:


import nltk

FileName = ("Location of clean article.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("location of clean article.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# Modelling

# In[ ]:


words = []
for line in open('name of cleantextfile.txt'):
    words.append(line.split())  
print(words) 

with open('newfileformodel.txt', 'w') as filehandle:  
    for listitem in words:
        filehandle.write('%s\n' % listitem)


# In[ ]:


from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec


path2 = get_tmpfile("word2vecyear1.model")

model23 = Word2Vec(my_texts1, size=100, window=5, min_count=5, workers=4)
model23.save("word2vecyear1.model")


modelyear1 = Word2Vec.load("word2vecyear1.model")
modelyear1.train(newfileformodel, total_examples=1, epochs=1)
print(modelyear1)

# numpy vector of a word
from gensim.models import KeyedVectors

path21 = get_tmpfile("wordvectorsyear1.kv")

modelyear1.wv.save('path/modelyear1.wv')
wv3 = KeyedVectors.load("modelyear1.wv", mmap='r')

from gensim.test.utils import datapath

wv3_from_text = KeyedVectors.load_word2vec_format(datapath('word2vec_pre_kv_c'), binary=False)  # C text format
wv3_from_bin = KeyedVectors.load_word2vec_format(datapath("euclidean_vectors.bin"), binary=True)  # C bin format

word_vectors_year1 = modelyear1.wv

from gensim.test.utils import common_texts
from gensim.models import Phrases

bigram_transformer = Phrases(newfileformodel)
model_year1 = Word2Vec(bigram_transformer[newfileformodel], min_count=5)

model_file1 = Word2Vec(min_count=5)
model_file1.build_vocab(newfileformodel)  # prepare the model vocabulary
model_file1.train(newfileformodel, total_examples=model_file1.corpus_count, epochs=model_file1.iter)  # train word vectors


# In[ ]:


similarities2 = modelyear2.wv.evaluate_word_pairs(datapath('wordsim353.tsv'))

print(similarities2)

analogy_scores2 = modelyear2.wv.evaluate_word_analogies(datapath('questions-words.txt'))
print(analogy_scores2)

