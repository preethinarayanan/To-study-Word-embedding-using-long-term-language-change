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
        print('Parsing {} done.'.format(page_url))
        print('# of headlines:', len(titles))
        print('# of text:', len(texts))
    
    return (titles, texts)


def save_parse_results(page_url: str, output_file: str):
    titles, texts = parse_volumes_1to6(page_url, verbose=True)

    if len(titles) != len(texts):
        sys.stderr.write('Parsing error on page: {}'.format(page_url))
        sys.stderr.flush()
        return False

    with open(output_file, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(texts[i] + '\n')
    return True


def parse_single_volume(url):
    """
    This function all articles in one 卷{i}, where i = 7 to 12
    E.g., 卷7 No. 1: 李密 陈情表

    Args
        url: the url for a volume, e.g., https://zh.wikisource.org/wiki/古文觀止/卷7
    Return

    """
    response = requests.get(url)
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


def parse_volumes_8to12(page_url):
    """
    Parse articles one by one and return for those in Volume 8 to 12
    Args
    page_url: https://zh.wikisource.org/wiki/古文觀止
    """
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, 'lxml')
    base_url = 'https://zh.wikisource.org/'

    for i, h2 in enumerate(soup.select('.mw-parser-output > h2')):
        if i >= 8: # 8 because there is a preface
            ol = h2.find_next_sibling('ol')
            
            titles = []
            for li in ol.find_all('li'):
                a = li.find_all('a')
                titles.append(a[1]['title'])
                url = a[1]['href']
                parse_one_article(base_url + url)


def parse_one_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    pass


def main():
    # 卷1 -> 周文
    # 卷2 -> 周文
    # 卷3 -> 周文
    # 卷4 -> 秦文
    # 卷5 -> 汉文
    # 卷6 -> 汉文
    urls1 = ['https://zh.wikisource.org/wiki/古文觀止/卷{}'.format(i) for i in [1,2,3,4,5,6]]
    for i, url in enumerate(urls1):
        save_parse_results(url, 'vol_{}.txt'.format(i+1))
    
    # 卷7 -> 六朝 唐文
    url_v7 = 'https://zh.wikisource.org/wiki/古文觀止/卷7'
    save_parse_results(url_v7, 'vol_7.txt')

    # 卷8 -> 唐文
    # 
    


def debug():
    # 卷2 最后两篇
    # titles, text = parse_one_page('https://zh.wikisource.org/wiki/古文觀止/卷2', verbose=True)
    response = requests.get('https://zh.wikisource.org/wiki/古文觀止/卷2')
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


def test():
    # url = 'https://zh.wikisource.org/wiki/古文觀止/卷7'
    # titles, texts = parse_single_volume(url)
    # print(len(titles), len(texts))

    page_url = 'https://zh.wikisource.org/wiki/古文觀止'
    parse_volumes_8to12(page_url)


if __name__ == "__main__":
    # main()
    # debug()
    test()