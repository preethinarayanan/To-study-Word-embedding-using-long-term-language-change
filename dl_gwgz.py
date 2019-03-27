from bs4 import BeautifulSoup
import requests
import sys


def parse_one_page(page_url: str, verbose=False): 
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
    text = []
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
        text.append(cleaned)
    
    if verbose:
        print('Parsing {} done.'.format(page_url))
        print('# of headlines:', len(titles))
        print('# of text:', len(text))
    
    return (titles, text)


def download_page(page_url: str, output_file: str):
    titles, text = parse_one_page(page_url, verbose=True)

    if len(titles) != len(text):
        sys.stderr.write('Parsing error on page: {}'.format(page_url))
        sys.stderr.flush()
        return False

    with open(output_file, 'w') as f:
        for i in range(len(titles)):
            f.write('==========\n')
            f.write(titles[i] + '\n')
            f.write(text[i] + '\n')
    return True


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
        print(p)


def remove_embedded_tag(container, tag: str):
    """
    Remove all `tag` elements in `container` element
    """
    t = container.find(tag)
    while t:
        _ = t.extract()
        t = container.find(tag)
    return container


def main():
    # 卷1 -> 周文
    # 卷2 -> 周文
    # 卷3 -> 周文
    # 卷4 -> 秦文
    # 卷5 -> 汉文
    # 卷6 -> 汉文
    urls1 = ['https://zh.wikisource.org/wiki/古文觀止/卷{}'.format(i) for i in [1,2,3,4,5,6]]
    for i, url in enumerate(urls1):
        download_page(url, '{}.txt'.format(i+1))


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
    url = 'https://zh.wikisource.org/wiki/%E9%99%B3%E6%83%85%E8%A1%A8_(%E8%A5%BF%E6%99%89)'
    download_single_article(url)


if __name__ == "__main__":
    # main()
    # debug()
    test()