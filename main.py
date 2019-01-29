import requests as r
from bs4 import BeautifulSoup as bs
import re

def get_list():
    schools=['北京大学']
    return schools

def download_html(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    try:
        txt=r.get(url,allow_redirects=False,headers=headers)
        txt.encoding='utf-8'
        return txt.text
    except:
        return None

def parse_html(html):
    soup=bs(html,'lxml')
    intr=soup.find_all('div', attrs={'class': 'lemma-summary'})[0]
    s = intr.get_text()
    #替换形如[1]的文字......
    pattern=re.compile(r'\[.*?\]')
    s=re.sub(pattern,'',s)
    return s

def save(txt):
    with open('school_list.txt','a+',encoding='utf-8') as wfile:
        wfile.write(txt)

if __name__=='__main__':
    schools=get_list()
    for re_school in schools:
        url='https://baike.baidu.com/item/{school}'.format(school=re_school)
        html=download_html(url)
        content=parse_html(html)
        s=re_school+content
        save(s)
        print('已获得'+re_school+'的简介')
