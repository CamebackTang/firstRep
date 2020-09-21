# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:34:17 2019

@author: windows
"""

import pandas as pd
from sqlalchemy import create_engine
# 数据库类型 + 数据库驱动名称 :// 用户名 : 口令 @ 机器地址 : 端口号 / 数据库名
engine = create_engine('mysql+pymysql://root:123@localhost:3306/sc_sys')
sql = '''
select * from tb_class;
'''
df = pd.read_sql_query(sql, engine)
print(df)
df1 = pd.DataFrame({'id':[123], 'name':['Liuyun']})
## 将新建的 DataFrame 储存到当前数据库的数据表 stu 中
df1.to_sql('stu', engine)
# df2.to_sql('scores', engine, index = False) # 不储存 index 列

df2 = pd.read_sql_query('select * from stu;', engine)
print(df2)
