# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:43:28 2019

@author: windows
"""
#%% 项目简介
#基于 MovieLens 100k 数据集中 男性女性对电影的评分
#来是判断男性还是女性,对电影评分的差异性更大。

#评分均值统计，可以得到男女各自最喜爱的 10 部电影
#男性还是女性电影评分的差异性大小则可以利用 '标准差'

# 利用 pandas 中的数据透视表 pivot_table()函数对数据进行聚合
#%% 
import pandas as pd
import numpy as np

# u.data评分数据
rnames = ['user_id','item_id','rating','timestamp']
rdata_df = pd.read_table(r'ml-100k\u.data',
     sep='\t', names = rnames, engine='python')
# u.item电影数据
# u.user用户数据
unames =  ['user_id','age','gender','occupation','zip_code']
udata_df = pd.read_table(r'ml-100k\u.user',\
     sep='\|', names = unames, engine='python')

# 选择有需要的数据，提高效率
ratings_df = pd.DataFrame()
users_df = pd.DataFrame()
ratings_df['user_id'] = rdata_df['user_id']
ratings_df['rating'] = rdata_df['rating']
users_df['user_id'] = udata_df['user_id']
users_df['gender'] = udata_df['gender']
# 将数据合并
rating_df = pd.merge(users_df, ratings_df)
# 数据透视表pivot_table()函数对数据进行聚合,把两个属性整合成一个idx
gender_table = pd.pivot_table(rating_df,\
   index=['gender','user_id'],values='rating')
gender_df = pd.DataFrame(gender_table) # 好像本来就是df。。。
# 分男女
Female_df = gender_df.query("gender == ['F']")
Male_df = gender_df.query("gender == ['M']")
Female_std = np.std(Female_df)
Male_std = np.std(Male_df)
print('Gender\tstd','\nF\t%.6f'%Female_std,'\nM\t%.6f'%Male_std)
#结论：女生的电影评分差异性更大

rating_df.groupby('gender')['rating'].std()

