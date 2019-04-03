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


# In[223]:


from bs4 import BeautifulSoup
import requests
import sys


def parse_volumes_1to6(page_url: str, verbose=False): 
    """
    This function works for pages: https://zh.wikisource.org/wiki/古文觀止/卷{i}
    where i = 1 to 6
    """
    response = requests.get('https://en.wikisource.org/wiki/A_Family_Sketch')
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

    with open(ouput_file, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


# In[224]:


print(parse_volumes_1to6('https://en.wikisource.org/wiki/A_Family_Sketch'))


# In[220]:


print(save_parse_results('https://en.wikisource.org/wiki/Lake_Ngami/Chapter_1', 'tes'))


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


# In[ ]:




