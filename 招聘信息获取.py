# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 12:58:13 2019

@author: windows
"""
#%% 项目介绍
# =============================================================================
# 爬取“2019年广州市高校毕业生大型供需见面会（华南理工大学）”的合适的工作介绍
# 爬取企业编号、企业名称、企业提供的职位、职位介绍JD_超链接t0文字、招聘人数
# 按关键词筛选，关键词列表 keywords = ['数据', '机器学习', '算法工程师', 'AI']
# 
# 要获取的信息：
#企业编号、企业链接、企业名称
#企业名称、公司性质、公司简介、招聘职位
#职位链接、职业名称、专业、招聘人数
#
# =============================================================================

#%%
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

#output_filename = "java招聘信息汇总.xls"
output_filename = "招聘信息汇总——数据.xls"
keywords = ['数据', '机器学习', '算法工程师', 'AI']
#keywords = ['嵌入式']
#keywords = ['数据']
#keywords = ['Java','java','JAVA']#,'开发'] #工程师
page_list = []
cno_list = []
cname_list = [] 
chref_list = []
jname_list = []
jhref_list = []
c_type_info_list = []
c_brief_info_list =[]
j_type_info_list = []
j_brief_info_list =[]

meetingNo = str(4302) # 也可以弄个列表，爬取多个招聘会
urlhead = 'http://gzbys.job168.com:8080'
page = 0
while 1:
    page = page +1
    url = urlhead + '/companyOfTheMeetingListWeb.action?page='+ \
            str(page) + '&meetingNo=' + meetingNo
    html = requests.get(url).text
    soup = BeautifulSoup(html,'lxml') # type(soup): bs4.BeautifulSoup
    
    rows = soup.find_all('div',attrs={'class':'row'}) # type(rows): bs4.element.ResultSet
    if rows == []: break
    for row in rows: # type(rows): bs4.element.Tag
        com = row.find('div',attrs={'class':'company eps'})
        cno = com.span.text # 企业编号
        cname = com.a.text  # 企业名称
        chref = urlhead + com.a['href'] # 企业链接
        jobs = row.find('div',attrs={'class':'jobs'}) # type(jobs): bs4.element.Tag
        jobs = jobs.find_all('a')
        for job in jobs:
            jhref = urlhead + job.get('href') # 职位链接
            jname = job.text # 职位名称
            for keyword in keywords:
                if keyword in jname:
                    page_list.append(page)
                    cno_list.append(cno)
                    cname_list.append(cname)
                    chref_list.append(chref)
#                    jname_list.append(jname)
                    jhref_list.append(jhref)
                    # 进入chref以获取企业类型、企业简介、[联系方式、招聘职位列表]
                    html = requests.get(chref).text
                    soup = BeautifulSoup(html,'lxml')
                    c_type_info = soup.find('div', attrs={'class':'info'}).string
                    c_brief_info = soup.find('div', attrs={'class':'cont'}).text.replace(' ','')
                    c_type_info_list.append(c_type_info)
                    c_brief_info_list.append(c_brief_info)
                    # 进入jhref以获取职位名称(含有人数)、职位信息、职位要求、[联系方式、其他招聘职位列表]
                    html = requests.get(jhref).text
                    soup = BeautifulSoup(html,'lxml')
                    jname = soup.find('div', attrs={'class':'name'}).text
                    jname_list.append(jname) # 
                    conts = soup.find_all('div', attrs={'class':'cont'})   
                    j_type_info = conts[0].text.replace(' ','').replace('\n','').replace('\r','')
                    j_brief_info = conts[1].text.replace(' ','').replace('\r\n','')
                    j_type_info_list.append(j_type_info)
                    j_brief_info_list.append(j_brief_info)
                    break
        
dic = {'所在页码':page_list,
       '企业编号':cno_list,
       '企业名称': cname_list,
       '企业链接': chref_list,
       '企业类型': c_type_info_list,
       '企业简介': c_brief_info_list,
       '职位名称': jname_list,
       '职位链接': jhref_list, 
       '职位信息': j_type_info_list,
       '职位简介': j_brief_info_list,       
       }
df = pd.DataFrame(dic)
df.to_excel(output_filename)

#%%

#关键词列表是否在字符串中出现
#字符串是否包含有关键词列表的某些关键词
#list_a = ['134','a','b']
#str_a = '134edacf42r23f'
#for a in list_a:
#    if str_a.count(a):
#        print("字符串中存在{}".format(a))
#holijoblis = soup.find_all('div', attrs={'class':'job'})
