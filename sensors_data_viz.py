# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:39:42 2020

@author: krish
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time


plt.style.use('ggplot')
time.sleep(1)
ii = 1000 # number of points
t1 = time.time()



gyrodata = pd.read_csv('D:/samples/Gyroscope-1385974ed5904a438616ff7bdb3f74395F1FC69C-0E70-48A1-ADA3-BFDA75D9D8AD.csv')
cols = list(gyrodata.columns)
del cols[1]
gyrodata = gyrodata[cols]


magndata = pd.read_csv('D:/samples/Magnetometer-1385974ed5904a438616ff7bdb3f74395F1FC69C-0E70-48A1-ADA3-BFDA75D9D8AD.csv')
cols = list(magndata.columns)
del cols[1]
magndata = magndata[cols]


accdata = pd.read_csv('D:/samples/Accelerometer-1385974ed5904a438616ff7bdb3f74395F1FC69C-0E70-48A1-ADA3-BFDA75D9D8AD.csv')
cols = list(accdata.columns)
del cols[1]
accdata = accdata[cols]


fig,axs = plt.subplots(3,1,figsize=(20,10),sharex=True)
cmap = plt.cm.Set1
#final_data = [data.iloc[:, col] for col in range(1, len(cols))]

final_data = gyrodata.values
ax = axs[0]
t_vec = [i for i in range(final_data.shape[0])]
for zz in range(1,np.shape(final_data)[1]):
    data_vec = [ii[zz] for ii in final_data]
    ax.plot(t_vec,data_vec,label=cols[zz],color=cmap(zz))
ax.legend(bbox_to_anchor=(1.12,0.9))
ax.set_ylabel('Angular Vel. [dps]',fontsize=12)


final_data = accdata.values
ax2 = axs[1]
t_vec = [i for i in range(final_data.shape[0])]
for zz in range(1,np.shape(final_data)[1]):
    data_vec = [ii[zz] for ii in final_data]
    ax2.plot(t_vec,data_vec,label=cols[zz],color=cmap(zz))
ax2.legend(bbox_to_anchor=(1.12,0.9))
ax2.set_ylabel('acceleration data. [g]',fontsize=12)


final_data = magndata.values
ax3 = axs[2]
t_vec = [i for i in range(final_data.shape[0])]
for zz in range(1,np.shape(final_data)[1]):
    data_vec = [ii[zz] for ii in final_data]
    ax3.plot(t_vec,data_vec,label=cols[zz],color=cmap(zz))
ax3.legend(bbox_to_anchor=(1.12,0.9))
ax3.set_ylabel('Magnetic field. [dps]',fontsize=12)
ax3.set_xlabel('Time [s]',fontsize=14)

fig.align_ylabels(axs)
plt.show()