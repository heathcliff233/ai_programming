# -*- coding: utf-8 -*-
"""
Basic idea of the program:
     1. Grab a few webpages from sina and extract the roll news subjects
     2. Segment words using Python the package jieba
         2.1 Filter out the stop words
         2.2 Only keep nouns
     3. Load all the words(with some appearing multiple times) into the package wordcloud
     4. That's it!

@author: Dazhuang
	 
"""

import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import re
import requests
from scipy.misc import imread
from wordcloud import WordCloud

def fetch_sina_news():
#    <d p="15.56200,1,25,16777215,1556013801,0,55c4619c,15137047079550976">(.*?)</d>
    PATTERN = re.compile('<d p=".*?">(.*?)<\/d>')
    BASE_URL = 'http://comment.bilibili.com/83089367.xml'
    with open('/Users/apple/Documents/Jupytor_Notebook/ai_programming/4.23/sina_news_wordcloud/subjects.txt ', 'w', encoding='gb18030') as f:
         r = requests.get(BASE_URL)
         data = r.text.encode('utf-8').decode('unixode-esacpe')
         p = re.findall(PATTERN, data)
            
         for s in p:
             f.write(s)
    
def extract_words():
    with open('/Users/apple/Documents/Jupytor_Notebook/ai_programming/4.23/sina_news_wordcloud/subjects.txt ','r', encoding='utf-8') as f:
        news_subjects = f.readlines()
    
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    
    newslist = []
    
    
    
    for subject in news_subjects:
        if subject.isspace():
            continue
        
        # segment words line by line
        p = re.compile("n[a-z0-9]{0,2}")    # n, nr, ns, ... are the flags of nouns
        word_list = pseg.cut(subject)     
        for word, flag in word_list:
            if word not in stop_words and p.search(flag) != None:
                newslist.append(word)
    
#    print(newslist)
#    print(word_list)
    content = {}
    for item in newslist:
        content[item] = content.get(item, 0) + 1
    
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "/Users/apple/Documents/Jupytor_Notebook/ai_programming/4.23/sina_news_wordcloud/mickey.png "))
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="black", mask=mask_image, max_words=5,).generate_from_frequencies(content)
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    
if __name__ == "__main__":
    fetch_sina_news()
    extract_words()
