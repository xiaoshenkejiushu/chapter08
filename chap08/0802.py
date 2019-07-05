# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from datetime import datetime


#s1 =  pd.Series(np.random.randn(10).cumsum(),index = np.arange(0,100,10))
#s1.plot()
#
#df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
#               columns=['A', 'B', 'C', 'D'],
#               index=np.arange(0, 100, 10))
#
#df.plot()
#
#
#print(np.random.randn(10, 4).cumsum())#加不加0是总的加和和按行加和的区分。
#
#
#fig , axs = plt.subplots(2,2)
#
#data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'))
#
#data.plot(kind = 'bar',ax = axs[0,0],color = 'red',alpha = 0.5)
#
#data.plot(kind='barh', ax=axs[0,1], color='k', alpha=0.7)



df = pd.DataFrame(np.random.rand(6, 4),
               index=['one', 'two', 'three', 'four', 'five', 'six'],
               columns=pd.Index(['A', 'B', 'C', 'D'], name='Genus'))
df.plot(kind='bar') # 默认并列柱状图,默认会把index放在x，col为第二层，相当于双层索引把，多个series的绘图

df.plot(kind = 'bar',stacked = True,alpha = 0.3)



tips = pd.read_csv("tips.csv")
print(tips)

part_counts = pd.crosstab(tips['day'],tips['size'])#计数并统计，相当于unstack的功能。
print(part_counts)


part_counts = part_counts.iloc[:,1:5]
print(part_counts)

party_pcts = part_counts.div(part_counts.sum(1).astype(float), axis=0)

party_pcts.plot(kind = 'bar')

tips['tip_pct'] = tips['tip']/tips['total_bill']
print(tips['tip_pct'])
tips['tip_pct'].plot(kind = 'kde')
tips['tip_pct'].hist(bins=50)



comp1 = np.random.normal(0,1,size = 200)
comp2 = np.random.normal(20,10,size = 200)

values = pd.Series(np.concatenate([comp1,comp2]))
values.hist(bins=100,color = 'k',alpha =0.3,normed =True)
values.plot(kind ='kde')


macro = pd.read_csv('macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna() # 对数运算后求差值
trans_data.head()


plt.scatter(trans_data['m1'], trans_data['unemp'])
plt.title('Changes in log %s vs. log %s' % ('m1', 'unemp'))


pd.plotting.scatter_matrix(trans_data, diagonal='kde', color='k', alpha=0.3) # 任意2个指标的散点图，主对角线画密度函数。





















































