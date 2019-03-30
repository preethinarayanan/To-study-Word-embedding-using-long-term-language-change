#!/usr/bin/env python
# coding: utf-8

# In[23]:


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
        
    


# In[24]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[25]:


print(download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))


# In[30]:


def save_parse_results(page_url: str, output_file: str):
    titles, texts = download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I', verbose=True)

    if len(titles) != len(texts):
        sys.stderr.write('Parsing error on page: {}'.format('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))
        sys.stderr.flush()
        return False

    with open(pnvol1.txt, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


# In[31]:


print(save_parse_results('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I', 'output1.txt'))


# In[7]:


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
        print(p)


# In[8]:


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


# In[9]:


print(download_single_article('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_II'))


# In[37]:


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


# In[38]:


print(debug())


# In[33]:


from bs4 import BeautifulSoup
import requests
import sys


def parse_volumes_1to6(page_url: str, verbose=False): 
    """
    This function works for pages: https://zh.wikisource.org/wiki/古文觀止/卷{i}
    where i = 1 to 6
    """
    response = requests.get('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I')
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
        print('Parsing {} done.'.format('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))
        print('# of headlines:', len(titles))
        print('# of text:', len(texts))
    
    return (titles, texts)


def save_parse_results(page_url: str, output_file: str):
    titles, texts = parse_volumes_1to6('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I', verbose=True)

    if len(titles) != len(texts):
        sys.stderr.write('Parsing error on page: {}'.format('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I'))
        sys.stderr.flush()
        return False

    with open(a.txt, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


# In[36]:


print(parse_volumes_1to6('https://en.wikisource.org/wiki/Personal_Narrative_of_a_Pilgrimage_to_Al_Madinah_and_Meccah/Volume_I', verbose=False))


# In[ ]:




