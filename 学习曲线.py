# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 22:18:15 2019

@author: windows
"""

#%% 学习曲线
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures #
from sklearn.linear_model import LinearRegression

# 生成200个点
n_dots = 200
X = np.linspace(0,1, n_dots)
y = np.sqrt(X) + 0.2*np.random.rand(n_dots) - 0.1
# 因为sklearn的接口里，要求用到 n_sample x n_feature 的矩阵
# 所以需要转化成 200*1 的矩阵
X = X.reshape(-1,1)
y = y.reshape(-1,1)

#%%
# 需要构造一个多项式模型。
# Pipeline意思是流水线，即这个流水线里可以包含多个数据处理模型，处理完一个处理下一个。
def polynomial_model(degree= 1):
    polynomial_features = PolynomialFeatures(degree= degree, include_bias= False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    return pipeline
#%%
#learning_curve()函数，它会自动把训练样本的数量按照预定的规则逐渐增加，
#然后画出不同训练样本数量时的模型准确性。其中train_sizes参数就是变化规则。
#比如 train_sizes = np.linspace(0.1, 1.0, 5),默认值
def plot_learning_curve(estimator, title, X, y, ylim= None, cv= None,
                        n_jobs=1, train_sizes= np.linspace(0.1, 1.0, 5)):
    from sklearn.model_selection import learning_curve
    import matplotlib.pyplot as plt
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim) # 星号什么意思
    plt.xlabel('training examples')
    plt.ylabel('score')
    train_sizes, train_scores, test_scores = learning_curve(#-----
            estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()
    
    plt.fill_between(train_sizes, 
                     train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, color='r', alpha=0.25)
    plt.fill_between(train_sizes, 
                     test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, color='g', alpha=0.25)
    plt.plot(train_sizes, train_scores_mean, 'o-', color='r', label='Training score')
    plt.plot(train_sizes, test_scores_mean, 'o-', color='g', label='Cross-validation score')
    plt.legend(loc= 'best')
    return plt

#%%
# 使用polynomial_model()函数构造3个模型，分别是
# 一阶多项式、三阶多项式、十阶多项式，并画出这3个模型的学习曲线。
from sklearn.model_selection import ShuffleSplit
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
titles = ['Learning curve (underFitting)',
         'Learning curve',
         'Learning curve (overfitting)']
degrees = [1,3,10]
plt.figure(figsize=(18,4), dpi=200)
for i in range(len(degrees)):
    plt.subplot(1,3, i+1)
    plot_learning_curve(polynomial_model(degrees[i]), titles[i],
                        X, y, ylim=(0.75, 1.01), cv=cv)
plt.show()
#%% 



#%%
