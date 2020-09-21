# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:39:42 2019
主成分分析pca
@author: windows
"""
# %% PCA类的主要输入参数有以下几个：
#参数n_components：指定希望PCA降维后的特征维度数目。
 #直接指定降维到的维度数目,也可以指定主成分的方差和所占的最小比例阈值 
 #还可以将参数设置为"mle",用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维。
 #默认值，即不输入n_components，此时n_components=min(样本数，特征数)。
#参数whiten ：判断是否进行白化，即归一化，默认值是False，即不进行白化。
#参数svd_solver：即指定奇异值分解SVD的方法，由于特征分解是奇异值分解SVD的一个特例，一般的PCA库都是基于SVD实现的。
# 属性explained_variance_，它代表降维后的各主成分的方差值。方差值越大，则说明越是重要的主成分。
# 属性explained_variance_ratio_，它代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的主成分

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

data_df = pd.read_excel(r'E:\大学\大学课程\专业课程\《MATLAB数据分析与数据挖掘》源数据和代码\MATLAB数据分析与数据挖掘\chapter4\示例程序\data\principal_component.xls')
pca = PCA()#保留所有成分
pca.fit(data_df)# 传入我们的数据
coeff = pca.components_ #返回模型的各个特征向量(单位特征向量)，一行一行的？
print(pca.explained_variance_) #查看降维后的各主成分的方差值(主成分特征根)
print(pca.explained_variance_ratio_) # 查看降维后的各主成分的方差值占总方差值的比例
print(pca.explained_variance_ratio_.cumsum())# 计算累计贡献率
X_new = pca.transform(data_df) # !有什么卵用？

# %% 
pca3=PCA(n_components=3) # 设置降维后的特征数目
pca3.fit(data_df) # 传入我们的数据
coeff3 = pca3.components_ #返回模型的各个特征向量(单位特征向量)
X_new3 = pca3.transform(data_df) # 得到降维后的新数据，仍然是numpy的array形式
print(pca3.explained_variance_) #查看降维后的各主成分的方差值(主成分特征根)
print(X_new)
Z = np.dot(data_df, coeff3.T) # 得到主成分矩阵！！！！！
# %%
pca95p=PCA(n_components=0.95) # 设置降维后的特征数目，累计贡献率至少95%
pca95p.fit(data_df) # 传入我们的数据
coeff95p = pca95p.components_

# %% 例子
#X_pca=np.array(X_pca) # 先变为数组？事实证明不需要
#a=PCA(n_components=3) # 设置降维后的特征数目
#a.fit(X_pca) # 传入我们的数据
#X_new=a.transform(X_pca) # 得到降维后的新数据，仍然是numpy的array形式
#a.inverse_transform(X_new)# 还原(恢复)
