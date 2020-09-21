# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:03:12 2019

@author: windows
"""
#%%
import numpy as np
import pandas as pd
from sklearn import tree
import pydotplus
import graphviz
from IPython.display import Image  

data_df = pd.read_excel(r'E:\大学\大学课程\专业课程\《MATLAB数据分析与数据挖掘》源数据和代码\MATLAB数据分析与数据挖掘\chapter5\示例程序\data\sales_data.xls')
data_dummy = pd.get_dummies(data_df) # 将分类变量变为数值
# 设左分支为是，可取“否列”，则否为1、是为0，“是否周末_否 <= 0.5”
data_dummy = data_dummy.iloc[:,[1,3,5,7]]
#在决策树分类时，criterion可选择“gini”，表示采用基尼系数，即CART算法；
#在决策树分类时，criterion可选择“entropy”，表示采用信息增益。
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(data_dummy.iloc[:,0:3].values, data_dummy.iloc[:,3].values) #.value取出array

with open('sales.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file = f)

cols = data_dummy.columns
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names = cols[:len(cols)-1],
                                class_names = ['high','low'],
                                filled = True)
# 画图方式 1
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png()) # 画图
graph.write_pdf("sales.pdf")# 中文乱码
# 画图方式 2（推荐）
#graph = graphviz.Source(dot_data)
#graph #可以有中文显示

#%% iris例子
from sklearn.datasets import load_iris
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") #结果为'iris.pdf'
graph

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)
graph
#%%
#sklearn.tree.DecisionTreeClassifier(criterion=’gini’*, splitter=’best’, max_depth=None, 
#                                    min_samples_split=2, min_samples_leaf=1, 
#                                    min_weight_fraction_leaf=0.0, max_features=None, random_state=None,
#                                    max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None,
#                                    class_weight=None, presort=False)
#DecisionTreeRegressor(criterion=’mse’, splitter=’best’, max_depth=None, 
#                      min_samples_split=2, min_samples_leaf=1, 
#                      min_weight_fraction_leaf=0.0,max_features=None,random_state=None, 
#                      max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, presort=False)
