# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from datetime import datetime

plt.plot(np.arange(10))


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

plt.plot(np.random.randn(50).cumsum(),'k--')


ax1.hist(np.random.randn(60),bins = 20,color = 'k',alpha = 0.5)

ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))


fig ,axs = plt.subplots(2,2)

axs[0,1].plot(np.arange(10))
axs[0,0].hist(np.random.randn(60),bins = 20,color = 'k',alpha = 0.5)
axs[1,0].scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))


plt.plot(np.arange(10),'ko--')


plt.plot(np.random.randn(30).cumsum(),'ko--')


fig ,axs = plt.subplots(2,2)

rec = plt.Rectangle((5,5),10,20,color = 'k',alpha = 0.3)
axs[0,1].add_patch(rec)


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ax.set_xticks([0,250,500,750,1000])
ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'])
ax.set_title('hcq')
ax.set_xlabel('stage')

fig.savefig('test.svg',dpi = 400)


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(np.random.randn(1000).cumsum(),label = 'one')#默认蓝
ax.plot(np.random.randn(1000).cumsum(),'k--',label = 'two')#k是黑色
ax.plot(np.random.randn(1000).cumsum(),'k--',color = 'red',label = '_nolengend')
ax.legend(loc = 'best')


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rec = plt.Rectangle((0.1,0.1),0.2,0.3,color = 'k',alpha = 0.3)
cir = plt.Circle((0.5,0.5),0.1,color = 'red',alpha =0.3)
tri = plt.Polygon([(0.15, 0.15), (0.35, 0.4), (0.2, 0.6)],alpha =0.3)
ax.add_patch(rec)
ax.add_patch(cir)
ax.add_patch(tri)


















































