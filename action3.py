import pandas as pd
import numpy as np
from pandas import DataFrame

#数据加载
df = pd.read_csv('car_complain.csv',encoding= 'utf-8')
df.to_excel('car_complain.xlsx',sheet_name='car_data',index= False)
# print(df)
df = df.drop('problem',axis=1).join((df.problem.str.get_dummies(',')))
print(df)
# 数据清洗
def f(x):
    x = x.replace('一汽-大众','一汽大众')
    return  x
df['brand'] = df['brand'].apply(f)
# 品牌投诉总数
result = df.groupby(['brand'])['id'].agg(['count'])
print(result)
#品牌问题个数
tags = df.columns[7:]
print(tags)
result2 = df.groupby(['brand'])[tags].agg(['sum'])
print(result2)
#车型投诉总数
result2 = result.merge(result2,left_index = True,right_index = True,how = 'left') #合并result和result2
print(result2)
result2.reset_index(inplace=True)  #释放索引brand为正常列
print(result2)
result2.to_csv('./result.csv')

#按照count，从大到小进行排序
result2 = result2.sort_values('count',ascending=False)
print(result2)



