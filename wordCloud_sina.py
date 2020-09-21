# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 08:57:53 2019

@author: windows
"""

import os
import jieba.posseg as pseg
import matplotlib.pyplot as plt
import re
import requests
#import time
from scipy.misc import imread
from wordcloud import WordCloud

def fetch_sina_new():
    BASE_URL = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.8880846484760281&callback=jQuery111204210199663404002_1566782356551&_=1566782356555'
    PATTERN = re.compile('"title":(.*?),')
    MAX_PAGE_NUM = 10
    html = ''
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        for i in range(1, MAX_PAGE_NUM+1):
            print('Downloading page #{}'.format(i))
            html = html + requests.get(BASE_URL + str(i) + '.shtml', verify='./2.crt').text
#        html = requests.get(BASE_URL).text
        data = html.encode('utf-8').decode('unicode-escape')
        rst = re.findall(PATTERN, data)
        for s in rst:
            f.write(s)
        
def extract_words():    
    with open('subjects.txt', 'r', encoding='utf-8') as f:
        new_subjects = f.readlines()
        
    #去除停用词
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    newslist = []
    for subject in new_subjects:
        if subject.isspace():
            continue
        # segment words line by line
        # n, nr, ns, ... are the flags of nouns
        # 新闻标题中的名词更能代表热点
        # 选择所有的名词放到一个列表中
        p = re.compile("n[a-z0-9]{0,2}")
        word_list = pseg.cut(subject) #逐行用jieba分词，单行分词的代码如下：
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                newslist.append(word)
    # 手动计算词频
    content = {}
    for item in newslist:
        content[item] = content.get(item, 0) +1

    # 基于一些图的轮廓来设置词云形状
    d = os.path.dirname('D:\Spyder_Workspace\mickey.jpg')#去掉文件名，返回目录 
    mask_image = imread(os.path.join(d, "mickey.jpg"))#python路径拼接
    # 利用WordCloud函数基于'词频'创建词云,选词频最高的10个
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="white",\
         mask = mask_image, max_words=202).generate_from_frequencies(content)
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    
    
if __name__ == "__main__":
    fetch_sina_new()
    extract_words()
