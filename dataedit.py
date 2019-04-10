#!/usr/bin/env python
# coding: utf-8

# In[120]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I')
    soup = BeautifulSoup(response.content, 'lxml')

    for p in soup.select('.mw-parser-output > p'):
        p = remove_embedded_tag(p, 'span')
        p = remove_embedded_tag(p, 'br')
        print(p.text)
        
   # "I think this is correct. whatever, ..."


# In[33]:


"I think this is correct. whatever, ...".split()


# In[121]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[34]:


print(download_single_article('https://en.wikisource.org/wiki/%22Dey_Ain%27t_No_Ghosts%22'))


# In[122]:


z= download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I')
print(z)


# In[77]:


def save_parse_results(page_url: str, output_file: str):
    titles, texts = download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I')

    if len(titles) != len(texts):
     
        sys.stderr.write('Parsing error on page: {}'.format('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))
        sys.stderr.flush()
        return False

    with open(output_file, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


# In[ ]:





# Volume 2:

# In[164]:


def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_II')
    soup = BeautifulSoup(response.content, 'lxml')

    for p in soup.select('.mw-parser-output > p'):
        p = remove_embedded_tag(p, 'span')
        p = remove_embedded_tag(p, 'br')
        print(p.text)


# In[165]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[166]:


print(download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_II'))


# In[167]:


def debug():
    # 卷2 最后两篇
    # titles, text = parse_one_page('https://zh.wikisource.org/wiki/古文觀止/卷2', verbose=True)
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_II')
    soup = BeautifulSoup(response.content, 'lxml')

    container = soup.select('div.mw-parser-output')[0]
    print('# of children:', len(list(container.children)))
    # for child in container.children:
    #     print(child.name)
    # print('# of p:', len(container.select('p')))
    for h2 in soup.select('.mw-parser-output > h2'):
        print('h2: {}'.format(h2.text))
        p = h2.find_next_sibling('p')
        p = p.find_next_sibling('p')
        print('p: {}'.format(p.text[:10])) 

    pass


# In[168]:


print(debug())


# In[31]:


from bs4 import BeautifulSoup
import requests
import sys


def parse_volumes_1to6(page_url: str, verbose=False): 
    """
    This function works for pages: https://zh.wikisource.org/wiki/古文觀止/卷{i}
    where i = 1 to 6
    """
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'lxml')

    # Count the number of <span> elements with class="mw-headline"
    # titles = soup.find_all('span', attrs={'class':'mw-headline'})
    titles = soup.select('.mw-parser-output > h2 > span.mw-headline')
    # for h in titles:
    #     print(h.text)
    titles = [t.text for t in titles]
    
    # Extract the text for each article
    texts = []
    for h2 in soup.select('.mw-parser-output > h2'):
        p = h2.find_next_sibling('p')
        p = p.find_next_sibling('p')

        # Remvoe the embedded <small> tags
        s = p.find('small')
        while s:
            _ = s.extract()
            s = p.find('small')
        
        # Remove spaces in string
        cleaned = p.text.replace(' ', '').strip()
        texts.append(cleaned)
    
    if verbose:
        print('Parsing {} done.'.format('https://en.wikisource.org/wiki/A_Family_Sketch'))
        print('# of headlines:', len(titles))
        print('# of text:', len(texts))
    
    return (titles, texts)


def save_parse_results(page_url: str, output_file: str):
    titles, texts = parse_volumes_1to6('https://en.wikisource.org/wiki/A_Family_Sketch', verbose=True)

    if len(titles) != len(texts):
        sys.stderr.write('Parsing error on page: {}'.format('https://en.wikisource.org/wiki/A_Family_Sketch'))
        sys.stderr.flush()
        return False

    with open(output_file, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


# In[224]:


print(parse_volumes_1to6('https://en.wikisource.org/wiki/A_Family_Sketch'))


# In[ ]:


save_parse_results(page_url ="'https://en.wikisource.org/wiki/A_Family_Sketch", output_file = "")


# In[ ]:





# In[32]:


print(save_parse_results('https://en.wikisource.org/wiki/Lake_Ngami/Chapter_1', 'tes.txt'))


# Vol 3 extracting clean text

# In[181]:


def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_III')
    soup = BeautifulSoup(response.content, 'lxml')

    for p in soup.select('.mw-parser-output > p'):
        p = remove_embedded_tag(p, 'span')
        p = remove_embedded_tag(p, 'br')
        print(p.text)


# In[182]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[183]:


print(download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_III'))


# extracting clean text from portal exploration asia

# In[228]:


def parse_single_volume(url):
    """
    This function all articles in one 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    Args
        url: the url for a volume, e.g., https://zh.wikisource.org/wiki/古文觀止/卷7
    Return
    """
    response = requests.get('https://en.wikisource.org/wiki/%22A_Morris_for_May-Day%22')
    soup = BeautifulSoup(response.content, 'lxml')

    titles = []
    for h2 in soup.select('.mw-parser-output > h2 > .mw-headline'):
        titles.append(h2.text)
    
    texts = []
    for h2 in soup.select('.mw-parser-output > h2'):
        p = h2.find_next_sibling('p')
        p = p.find_next_sibling('p')

        # Remvoe the embedded <small> tags
        s = p.find('small')
        while s:
            _ = s.extract()
            s = p.find('small')
        
        # Remove spaces in string
        cleaned = p.text.replace(' ', '').strip()
        cleaned = cleaned.replace('\"', '')
        texts.append(cleaned)
    
    return (titles, texts)


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[229]:


https://en.wikisource.org/wiki/Portal:Exploration#Asia
        


# In[230]:


print(parse_single_volume('https://en.wikisource.org/wiki/%22A_Morris_for_May-Day%22'))


# In[1]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/%22A_Morris_for_May-Day%22')
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

print(download_single_article('https://en.wikisource.org/wiki/%22A_Morris_for_May-Day%22'))


# In[ ]:


print(download_single_article('https://en.wikisource.org/wiki/%22A_Morris_for_May-Day%22'))


# In[225]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/A_Family_Sketch')
    soup = BeautifulSoup(response.content, 'lxml')

    for p in soup.select('.mw-parser-output > p'):
        p = remove_embedded_tag(p, 'span')
        p = remove_embedded_tag(p, 'br')
        print(p.text)


# In[226]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[227]:


print(download_single_article('https://en.wikisource.org/wiki/A_Family_Sketch'))


# In[236]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/%22Them_Others%22')
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

print(download_single_article('https://en.wikisource.org/wiki/%22Them_Others%22'))


# In[239]:


def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Bad_Medicine')
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

print(download_single_article('https://en.wikisource.org/wiki/Bad_Medicine'))


# In[240]:


def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/%22Bill_Bailey%22')
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

print(download_single_article('https://en.wikisource.org/wiki/%22Bill_Bailey%22'))


# In[243]:


#https://en.wikisource.org/wiki/%22Bones_and_I%22/Chapter_1
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/%22Thou_Art_the_Man%22')
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

print(download_single_article('https://en.wikisource.org/wiki/%22Thou_Art_the_Man%22'))    
    


# In[250]:


#https://en.wikisource.org/wiki/%22Timber%22/Chapter_1
#https://en.wikisource.org/wiki/%22Bones_and_I%22/Chapter_1
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/%22Call_to_Renewal%22_Keynote_Address')
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

print(download_single_article('https://en.wikisource.org/wiki/%22Call_to_Renewal%22_Keynote_Address'))    
        
    


# In[255]:


#https://en.wikisource.org/wiki/Once_a_Week_(magazine)/Series_1/Volume_5/%22Cato%22_on_the_boards
    
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Once_a_Week_(magazine)/Series_1/Volume_5/%22Cato%22_on_the_boards')
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

print(download_single_article('https://en.wikisource.org/wiki/Once_a_Week_(magazine)/Series_1/Volume_5/%22Cato%22_on_the_boards'))        


# In[257]:


def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/The_Last_Galley_(collection)/%22De_Profundis%22')
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

print(download_single_article('https://en.wikisource.org/wiki/The_Last_Galley_(collection)/%22De_Profundis%22'))      


# Vol 1 counting words and tokens

# In[139]:


file = open('vol_nop.txt', 'r')
book = file.read()


def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def count_word(tokens, token):
    count = 0

    for element in tokens:
        # Remove Punctuation
        word = element.replace(",","")
        word = word.replace(".","")

        # Found Word?
        if word == token:
            count += 1
    return count
    
    
# Tokenize the Book
words = tokenize()

# Get Word Count
word = 'day'
frequency = count_word(words, word)
print('Word: [' + word + '] Frequency: ' + str(frequency))


# family sketch tokens

# In[ ]:





# In[4]:


file=open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


# In[ ]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[5]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[6]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print  ("Number of Words: ", len(lines_in_file.split()))


# In[ ]:





# In[150]:


file=open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


# In[14]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1844_thouarthteworks.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[15]:


from collections import Counter

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1844_thouarthteworks.txt") as f:
    wordcount = Counter(f.read().split())
    
print(wordcount)


# In[16]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1844_thouarthteworks.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print  ("Number of Words: ", len(lines_in_file.split()))


# In[152]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[ ]:





# In[153]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print  ("Number of Words: ", len(lines_in_file.split()))


# In[148]:


from collections import Counter

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt") as f:
    wordcount = Counter(f.read().split())
    
print(wordcount)


# In[7]:


from collections import Counter

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt") as f:
    wordcount = Counter(f.read().split())
    
print(wordcount)


# In[8]:


count = {}
for w in open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt").read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print ("%s was found %d times" % (word, times))


# In[9]:


words = []
count = 0

with open ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt","r") as f:
    # Get a list of lines in the file and covert it into a set
    words = set(f.readlines()) 
    count = len(words) 

print(count)


# In[10]:


with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1837familysketch.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[11]:


words = []
count = 0

with open ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1844_thouarthteworks.txt","r") as f:
    # Get a list of lines in the file and covert it into a set
    words = set(f.readlines()) 
    count = len(words) 

print(count)


# In[12]:


with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1844_thouarthteworks.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[ ]:





# In[154]:


count = {}
for w in open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt").read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print ("%s was found %d times" % (word, times))


# In[157]:


words = []
count = 0

with open ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt","r") as f:
    # Get a list of lines in the file and covert it into a set
    words = set(f.readlines()) 
    count = len(words) 

print(count)


# In[158]:


with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol_nop.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[171]:


def parse_single_volume(url):
    """
    This function all articles in one 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    Args
        url: the url for a volume, e.g., https://zh.wikisource.org/wiki/古文觀止/卷7
    Return
    """
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I')
    soup = BeautifulSoup(response.content, 'lxml')

    titles = []
    for h2 in soup.select('.mw-parser-output > h2 > .mw-headline'):
        titles.append(h2.text)
    
    texts = []
    for h2 in soup.select('.mw-parser-output > h2'):
        p = h2.find_next_sibling('p')
        p = p.find_next_sibling('p')

        # Remvoe the embedded <small> tags
        s = p.find('small')
        while s:
            _ = s.extract()
            s = p.find('small')
        
        # Remove spaces in string
        cleaned = p.text.replace(' ', '').strip()
        cleaned = cleaned.replace('\"', '')
        texts.append(cleaned)
    
    return (titles, texts)


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[172]:


print(parse_single_volume('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))


# Counting number of tokens and words in vol 2

# In[174]:


file=open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


# Number of tokens in vol 2

# In[175]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[176]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print  ("Number of Words: ", len(lines_in_file.split()))


# In[177]:


from collections import Counter

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt") as f:
    wordcount = Counter(f.read().split())
    
print(wordcount)


# In[178]:


count = {}
for w in open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt").read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print ("%s was found %d times" % (word, times))


# In[179]:


words = []
count = 0

with open ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt","r") as f:
    # Get a list of lines in the file and covert it into a set
    words = set(f.readlines()) 
    count = len(words) 

print(count)


# In[180]:


with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol2_personalnartive.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# vol 3 counting unique words and tokens

# In[195]:


file=open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


# In[196]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of Words: " , len(nltk_tokens))


# In[197]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()

    print (lines_in_file.split())
    print ("\n")
    print  ("Number of Words: ", len(lines_in_file.split()))


# In[198]:


from collections import Counter

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt") as f:
    wordcount = Counter(f.read().split())
    
print(wordcount)


# In[199]:


count = {}
for w in open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt").read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
for word, times in count.items():
    print ("%s was found %d times" % (word, times))


# In[200]:


words = []
count = 0

with open ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt","r") as f:
    # Get a list of lines in the file and covert it into a set
    words = set(f.readlines()) 
    count = len(words) 

print(count)


# In[201]:


with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/vol3_pn.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[19]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1861_onceaweekmag.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1861_onceaweekmag.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[20]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1907_morismayday.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1907_morismayday.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[21]:



import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1911_lastgalley.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1911_lastgalley.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[22]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1915_billbailey.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1915_billbailey.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[23]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1917_themothers.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1917_themothers.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[24]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1923old_badmeedicine.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1923old_badmeedicine.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[25]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2006_calltorenewal.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2006_calltorenewal.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[49]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1924-wecrowntheeking.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1924-wecrowntheeking.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[39]:


print(download_single_article('https://en.wikisource.org/wiki/Dorinda_Dares'))


# In[36]:


print(download_single_article('https://en.wikisource.org/wiki/%22Dorinda_Dares%22'))
    
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1913_noghos.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1913_noghos.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")    


# In[47]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/We_Crown_Thee_King')
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


# In[48]:


print(download_single_article('https://en.wikisource.org/wiki/We_Crown_Thee_King'))


# In[51]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/In_War_Time_(Whittier)/%22Ein_Feste_Burg_Ist_Unser_Gott%22')
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
print(download_single_article('https://en.wikisource.org/wiki/In_War_Time_(Whittier)/%22Ein_Feste_Burg_Ist_Unser_Gott%22'))


# In[52]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1864_1stunsergot.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1864_1stunsergot.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")    


# In[67]:


from bs4 import BeautifulSoup
import requests
import sys
def download_single_article(url):
    """
    This function works for a single article in 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表
    """
    response = requests.get('https://en.wikisource.org/wiki/Enemies_from_Within')
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


# In[68]:


print(download_single_article('https://en.wikisource.org/wiki/Enemies_from_Within'))


# In[69]:


#1950_enemiesfrmwitin
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1950_enemiesfrmwitin.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1950_enemiesfrmwitin.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")    


# In[79]:


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
#print(download_single_article('https://en.wikisource.org/wiki/The_Spell_of_the_Yukon_and_Other_Verses/%22Fighting_Mac%22'))


# In[84]:


print(download_single_article('https://en.wikisource.org/wiki/Zut-Ski'))


# In[86]:


#1924-zuttski
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1924-zuttski.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1924-zuttski.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")    


# In[89]:


print(download_single_article('https://en.wikisource.org/wiki/The_Tents_of_Kedar'))


# In[111]:


#2009_thetentsofkedar
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_thetentsofkedar.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_thetentsofkedar.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[101]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_I'))


# In[123]:


#2012_Captaincourageous
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Captaincourageous.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Captaincourageous.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[102]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_II'))


# In[122]:


#2012_chap2captaincourageous
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap2captaincourageous.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap2captaincourageous.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[103]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_III'))


# In[121]:


#2012_captinncoru_chap3
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_captinncoru_chap3.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_captinncoru_chap3.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[104]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_IV'))


# In[120]:


#2012pub_chap4_captcour
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012pub_chap4_captcour.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012pub_chap4_captcour.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[105]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_V'))


# In[119]:


#2012_chap5_capco
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap5_capco.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap5_capco.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[106]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_VI'))


# In[118]:


#2012_chap6_capcc
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap6_capcc.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap6_capcc.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[107]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_VII'))


# In[117]:


#2012_chap7_capcour
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap7_capcour.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap7_capcour.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[108]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_VIII'))


# In[115]:


#2012_chap8_capcon
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap8_capcon.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap8_capcon.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[109]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_IX'))


# In[114]:


#2012_chap9_capcon
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap9_capcon.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap9_capcon.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[110]:


print(download_single_article('https://en.wikisource.org/wiki/Captains_Courageous/Chapter_X'))


# In[112]:


#2012_chap10_Capcon
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap10_Capcon.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_chap10_Capcon.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[ ]:


https://en.wikisource.org/wiki/Kim/Chapter_1
    


# In[126]:


print(download_single_article('https://en.wikisource.org/wiki/Poor_Dear_Mamma'))


# In[131]:



import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_poordear.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_poordear.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[127]:


print(download_single_article('https://en.wikisource.org/wiki/The_World_Without'))


# In[136]:


#2009_worldwithout
import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_worldwithout.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_worldwithout.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[128]:


print(download_single_article('https://en.wikisource.org/wiki/The_Tents_of_Kedar'))


# In[135]:


#2009_tentsofkedar

import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_tentsofkedar.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_tentsofkedar.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[129]:


print(download_single_article('https://en.wikisource.org/wiki/The_Garden_of_Eden'))


# In[134]:


#2009_gardenofeden

import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_gardenofeden.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_gardenofeden.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[130]:


print(download_single_article('https://en.wikisource.org/wiki/Fatima_(Kipling)'))


# In[133]:


#2009_fatimakipling

import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_fatimakipling.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2009_fatimakipling.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[141]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/A_Friend%27s_Friend'))


# In[142]:


#1887_plaintales

import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_plaintales.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_plaintales.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[148]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/The_Madness_of_Private_Ortheris'))


# In[149]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_plaintalhills.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_plaintalhills.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[1]:


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


# In[14]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/The_Daughter_of_the_Regiment'))


# In[15]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_plaintales_daugterregiment.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_plaintales_daugterregiment.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[19]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/A_Bank_Fraud'))


# In[20]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_bankfraud_plaintales.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_bankfraud_plaintales.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[30]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/The_Taking_of_Lungtungpen'))


# In[32]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_palintalestakingoflungtungapen.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_palintalestakingoflungtungapen.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[37]:


print(download_single_article('https://en.wikisource.org/wiki/Plain_Tales_from_the_Hills/The_Three_Musketeers'))


# In[38]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_3musketerrs_plaintales.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1887_3musketerrs_plaintales.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[16]:


print(download_single_article('https://en.wikisource.org/wiki/Life%27s_Handicap/The_Finances_of_the_Gods'))


# In[17]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_lifehandicap_financeofgods.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_lifehandicap_financeofgods.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[20]:


print(download_single_article('https://en.wikisource.org/wiki/Life%27s_Handicap/The_Amir%27s_Homily'))


# In[21]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_lifehandicap_amirhomily.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_lifehandicap_amirhomily.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[31]:


print(download_single_article('https://en.wikisource.org/wiki/The_Courting_of_Dinah_Shadd'))


# In[32]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1890_courtingofdinansha.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1890_courtingofdinansha.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[40]:


print(download_single_article('https://en.wikisource.org/wiki/The_Return_of_Imray'))


# In[41]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_returnofimray.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_returnofimray.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[ ]:





# In[40]:


print(download_single_article('https://en.wikisource.org/wiki/The_Return_of_Imray'))


# In[41]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_returnofimray.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_returnofimray.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[45]:


print(download_single_article('https://en.wikisource.org/wiki/%22Love-o%27-Women%22'))


# In[46]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_loveowomen.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_loveowomen.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[81]:


print(download_single_article('https://en.wikisource.org/wiki/A_Sahibs%27_War'))


# In[82]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1901_sahibswar.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1901_sahibswar.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[127]:


print(download_single_article('https://en.wikisource.org/wiki/At_Twenty-Two'))


# In[128]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_at22.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_at22.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[129]:


print(download_single_article('https://en.wikisource.org/wiki/The_Big_Drunk_Draf%27'))


# In[131]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_bigdrunkdraf.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_bigdrunkdraf.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[132]:


print(download_single_article('https://en.wikisource.org/wiki/Black_Jack'))


# In[133]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_blackjack.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_blackjack.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[135]:


print(download_single_article('https://en.wikisource.org/wiki/A_Deal_in_Cotton'))


# In[137]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1907_dealncotton.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1907_dealncotton.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[139]:


print(download_single_article('https://en.wikisource.org/wiki/The_Drums_of_the_Fore_and_Aft'))


# In[140]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_drums.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_drums.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[148]:


print(download_single_article('https://en.wikisource.org/wiki/The_Finest_Story_in_the_World'))


# In[149]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_fineshstory.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_fineshstory.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[150]:


print(download_single_article('https://en.wikisource.org/wiki/Garm_%E2%80%94_a_Hostage'))


# In[151]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1899_garmhostage.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1899_garmhostage.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[152]:


print(download_single_article('https://en.wikisource.org/wiki/The_God_from_the_Machine'))


# In[153]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_godfrommachine.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_godfrommachine.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[154]:


print(download_single_article('https://en.wikisource.org/wiki/An_Habitation_Enforced'))


# In[155]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1905_habitationenforced.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1905_habitationenforced.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[158]:


print(download_single_article('https://en.wikisource.org/wiki/The_Honours_of_War'))


# In[159]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_honorsofwar.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_honorsofwar.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[160]:


print(download_single_article('https://en.wikisource.org/wiki/The_House_Surgeon'))


# In[161]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1909_hosesurgeon.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1909_hosesurgeon.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[162]:


print(download_single_article('https://en.wikisource.org/wiki/In_Flood_Time'))


# In[163]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_infloodtime.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_infloodtime.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[165]:


print(download_single_article('https://en.wikisource.org/wiki/The_Last_Relief'))


# In[166]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_lastrelief.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1891_lastrelief.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[167]:


print(download_single_article('https://en.wikisource.org/wiki/The_Legs_of_Sister_Ursula'))


# In[168]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_legsofsis.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_legsofsis.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[170]:


print(download_single_article('https://en.wikisource.org/wiki/Little_Foxes'))


# In[171]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1909_lilfoxes.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1909_lilfoxes.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[172]:


print(download_single_article('https://en.wikisource.org/wiki/%22Love-o%27-Women%22'))


# In[173]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_loveowomen27.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1893_loveowomen27.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[175]:


print(download_single_article('https://en.wikisource.org/wiki/The_Man_Who_Would_Be_King'))


# In[176]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_themanwhowouldbeking.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_themanwhowouldbeking.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[177]:


print(download_single_article('https://en.wikisource.org/wiki/The_Mother_Hive'))


# In[178]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1908_motherhive.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1908_motherhive.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[179]:


print(download_single_article('https://en.wikisource.org/wiki/Mrs._Hauksbee_Sits_Out'))


# In[180]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1890_mrshau.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1890_mrshau.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[181]:


print(download_single_article('https://en.wikisource.org/wiki/My_Own_True_Ghost_Story'))


# In[182]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_ownghoststsry.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_ownghoststsry.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[184]:


print(download_single_article('https://en.wikisource.org/wiki/On_the_City_Wall'))


# In[185]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_onthecitywall.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_onthecitywall.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[187]:


print(download_single_article('https://en.wikisource.org/wiki/The_Phantom_%E2%80%99Rickshaw'))


# In[188]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1885_phatamricksw.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1885_phatamricksw.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[190]:


print(download_single_article('https://en.wikisource.org/wiki/Private_Learoyd%27s_Story'))


# In[191]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_prvateleoyardstory.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_prvateleoyardstory.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[192]:


print(download_single_article('https://en.wikisource.org/wiki/The_Puzzler'))


# In[193]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1906_puzzler.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1906_puzzler.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[195]:


print(download_single_article('https://en.wikisource.org/wiki/The_Sending_of_Dana_Da'))


# In[196]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_sendingoddanada.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_sendingoddanada.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[197]:


print(download_single_article('https://en.wikisource.org/wiki/The_Solid_Muldoon'))


# In[198]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_solidmuldon.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_solidmuldon.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[201]:


print(download_single_article('https://en.wikisource.org/wiki/The_Strange_Ride_of_Morrowbie_Jukes'))


# In[202]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1885_starngeride.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1885_starngeride.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[206]:


print(download_single_article('https://en.wikisource.org/wiki/The_Village_That_Voted_the_Earth_Was_Flat'))


# In[207]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1917_villagethatvoted.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1917_villagethatvoted.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[210]:


print(download_single_article('https://en.wikisource.org/wiki/With_the_Main_Guard'))


# In[211]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_withmainguard.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1888_withmainguard.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[223]:


print(download_single_article('https://en.wikisource.org/wiki/1932_Royal_Christmas_Message'))


# In[224]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1932_royalchrist.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1932_royalchrist.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[242]:


print(download_single_article('https://en.wikisource.org/wiki/Appletons%27_Cyclop%C3%A6dia_of_American_Biography/Kipling,_Rudyard'))


# In[243]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1900_appletoncyclopedia.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1900_appletoncyclopedia.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[250]:


print(download_single_article('https://en.wikisource.org/wiki/Stories_Three'))


# In[251]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_stories_rudyarkipling.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_stories_rudyarkipling.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[252]:


print(download_single_article('https://en.wikisource.org/wiki/Muck-a-Muck'))


# In[253]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1867_muckamuck.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1867_muckamuck.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[254]:


print(download_single_article('https://en.wikisource.org/wiki/Terence_Denville'))


# In[255]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_terancedenvile.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_terancedenvile.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[256]:


print(download_single_article('https://en.wikisource.org/wiki/Selina_Sedilia'))


# In[257]:


import nltk

FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_selinasedisa.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_selinasedisa.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[258]:


print(download_single_article('https://en.wikisource.org/wiki/Condensed_Novels/Preface'))
#https://en.wikisource.org/wiki/Condensed_Novels/Preface


# In[259]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_novels_preface.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_novels_preface.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[260]:


#https://en.wikisource.org/wiki/The_Ninety-Nine_Guardsmen
print(download_single_article('https://en.wikisource.org/wiki/The_Ninety-Nine_Guardsmen'))
    


# In[261]:


#2012_99guradmen.txt
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_99guradmen.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_99guradmen.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[262]:


#https://en.wikisource.org/wiki/The_Garden_of_Years_and_Other_Poems/To_the_Reader
print(download_single_article('https://en.wikisource.org/wiki/The_Garden_of_Years_and_Other_Poems/To_the_Reader'))
        


# In[275]:


#1904_grradenofyears
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1904_grradenofyears.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/1904_grradenofyears.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[266]:


print(download_single_article('https://en.wikisource.org/wiki/The_Dweller_of_the_Threshold'))
    


# In[276]:


#2012_dwellerofthreshold
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_dwellerofthreshold.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_dwellerofthreshold.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[267]:


print(download_single_article('https://en.wikisource.org/wiki/The_Haunted_Man'))
    


# In[277]:


#2012_hauntedman
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_hauntedman.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_hauntedman.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[268]:


print(download_single_article('https://en.wikisource.org/wiki/Miss_Mix'))
    


# In[278]:


#2012_missmax
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_missmax.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_missmax.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[269]:


print(download_single_article('https://en.wikisource.org/wiki/Mr._Midshipman_Breezy'))
    


# In[283]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_midshipbrezzy.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_midshipbrezzy.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[270]:


print(download_single_article('https://en.wikisource.org/wiki/Mary_McGillup'))
    


# In[284]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_marygilup.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_marygilup.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[271]:


print(download_single_article('https://en.wikisource.org/wiki/No_Title'))
    


# In[285]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_notitle.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_notitle.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[274]:


print(download_single_article('https://en.wikisource.org/wiki/The_Heritage_of_Dedlow_Marsh'))
    


# In[286]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_heritage.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2011_heritage.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[289]:


print(download_single_article('https://en.wikisource.org/wiki/Openings_in_the_Old_Trail/IX'))
    


# In[290]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[291]:


print(download_single_article('https://en.wikisource.org/wiki/Openings_in_the_Old_Trail/IV'))
    


# In[293]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail4.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail4.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[294]:


print(download_single_article('https://en.wikisource.org/wiki/Openings_in_the_Old_Trail/II'))
    


# In[295]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail2.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_openingsoldtrail2.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[296]:


print(download_single_article('https://en.wikisource.org/wiki/The_Convalescence_of_Jack_Hamlin'))
    


# In[297]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_covalesence.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_covalesence.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[298]:


print(download_single_article('https://en.wikisource.org/wiki/Dick_Boyle%27s_Business_Card'))
    


# In[299]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_dickboyle.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_dickboyle.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[300]:


print(download_single_article('https://en.wikisource.org/wiki/Dan%27l_Borem'))
    


# In[301]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_danborem.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_danborem.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[302]:


print(download_single_article('https://en.wikisource.org/wiki/Adventures_of_John_Longbowe,_Yeoman'))
    


# In[303]:


FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Advnofjohn.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Advnofjohn.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[304]:


#https://en.wikisource.org/wiki/Golly_and_the_Christian
print(download_single_article('https://en.wikisource.org/wiki/Golly_and_the_Christian'))
    


# In[309]:


#2012_gollychris
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_gollychris.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_gollychris.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[305]:


print(download_single_article('https://en.wikisource.org/wiki/The_Stolen_Cigar_Case'))
    


# In[308]:


#2012_Stolencigar
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Stolencigar.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_Stolencigar.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[306]:


print(download_single_article('https://en.wikisource.org/wiki/Rupert_the_Resembler'))
    


# In[307]:


#2012_ruperttherese
FileName = ("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_ruperttherese.txt")

with open(FileName, 'r') as file:
    lines_in_file = file.read()
    
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print (nltk_tokens)
    print ("\n")
    print ("Number of tokens: " , len(nltk_tokens))

with open("C:/Users/preek/Desktop/SDSU MIS/MIS 790/2012_ruperttherese.txt", "r") as file:
    lines = file.read().splitlines()

    uniques = set()
    for line in lines:
        uniques |= set(line.split())

    print(f"Unique words: {len(uniques)}")


# In[337]:


import re
s = print(download_single_article('https://en.wikisource.org/wiki/Rupert_the_Resembler'))
#s = re.sub(r'[^\w\s]','',s)


# In[312]:


import string
tr = str.maketrans("", "", string.punctuation)
s.translate(tr)    


# In[313]:


table = str.maketrans({key: None for key in string.punctuation})
new_s = s.translate(table)   


# In[314]:


s.translate(s, string.punctuation)


# In[317]:


import re, string
#s = "string. With. Punctuation?" # Sample string 
out = re.sub('[%s]' % re.escape(string.punctuation), '', s)


# In[319]:


letters_only = re.sub("[^a-zA-Z]",  # Search for all non-letters
                          " ",          # Replace all non-letters with spaces
                          str(s))


# In[320]:


print(letters_only)


# In[323]:


import string
letters_only.translate(str.maketrans({a:None for a in string.punctuation}))


# In[326]:


import re
out = re.sub(ur'[^\w\d\s]+', '', s)


# In[331]:


s = re.sub(r'[^\w\s]','',str(s))
re.split(r'\s*', str(s))


# In[329]:


s.translate(s, string.punctuation)


# In[333]:


import string
s.strip(string.punctuation)


# In[336]:


' '.join(word.strip(string.punctuation) for word in s.split())
#"Hello world I'm a boy you're a girl"


# In[343]:


import string

"".join(str(s) for s in str(s) if str(s) not in string.punctuation)


# In[347]:


import string
s.translate(s, string.punctuation)


# In[ ]:




