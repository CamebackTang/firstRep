# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
# Importing the libraries
import numpy as np
import pandas as pd
# Importing the dataset
dataset = pd.read_csv(r'C:\Users\Administrator\Desktop\chap4.csv')
X_yesno = dataset.iloc[:,[1,2]]
X = dataset.iloc[:, np.arange(3,5)]
y = dataset.iloc[:, -1]

#%% 把变量替换成数值
#1、离散特征的取值之间没有大小的意义，比如color：[red,blue],那么就使用one-hot编码 
#2、离散特征的取值有大小的意义，比如size:[X,XL,XXL],那么就使用数值的映射{X:1,XL:2,XXL:3} 

data['w'] #选择表格中的'w'列，使用类字典属性,返回的是Series类型
data[['w']] #选择表格中的'w'列，返回的是DataFrame属性
data.irow(0)  #取data的第一行
data.icol(0)  #取data的第一列
data.iloc[-1]  #选取DataFrame最后一行，返回的是Series
data.iloc[-1:]  #选取DataFrame最后一行，返回的是DataFrame

# 替换成0-1变量
y = [0 if i=='False.' else 1 for i in y] 
X_dummy = pd.get_dummies(X_yesno)
X['Int\'l Plan'] = X_dummy.iloc[:,1] # 增加一列
X['VMail Plan'] = X_dummy.iloc[:,3]  # 增加一列


dataset = pd.read_csv('Social_Network_Ads.csv')
# 把 Gender 列中的 Male变成1，Female变成0
#------ 采用映射
Gender_Mapping = {'Male':1, 'Female':0}
dataset['Gender'] = dataset['Gender'].map(Gender_Mapping) #使用类字典属性
#dataset.Gender与dataset['Gender']是等价的, #使用点属性
#------ 采用replace函数替换(多个值替换成少数词时比较爽)
dataset['Gender'] = dataset['Gender'].replace(['Male','男'], 1)
dataset['Gender'] = dataset['Gender'].replace(['Female','女'], 0)
#------ 使用pd.get_dummies进行one-hot 独热向量化（One Hot Vectorization）
Gender_dummier = pd.get_dummies(dataset.Gender)
#pd.get_dummies(trainSet, columns)方法可以保留非分类变量!!!
df = pd.get_dummies(dataset, columns=['Gender']) #删除，添加新的多列
 
#dummy不好处理Cabin（船舱号）这种标称属性，因为他出现的变量比较多。
#所以Pandas有一个方法叫做factorize()，它可以创建一些数字，来表示类别变量，
#对每一个类别映射一个ID，这种映射最后只生成一个特征，不像dummy那样生成多个特征。
dataset['gender'] = pd.factorize(dataset.Gender)[0] # 增加新列
dataset['Gender'] = pd.factorize(dataset.Gender)[0] # 直接替换原数据

#将数据Binning化后，要么将数据factorize化，要么dummies化。
dataset['Age_bin'] = pd.qcut(dataset['Age'],5)
print(dataset['Age_bin'].head())
# factorize
dataset['Age_bin_id'] = pd.factorize(dataset['Age_bin'])[0]
# dummies
Age_bin_dummies_df = pd.get_dummies(dataset['Age_bin']).rename(columns=lambda x: 'Age_' + str(x))
dataset = pd.concat([dataset, Age_bin_dummies_df], axis=1)
#%%
