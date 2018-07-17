# -*- coding: utf-8 -*-

import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
import cvplot

N = 1000

plt.figure(1)
start = time.time() 
loopNum = 100  
for i in range(loopNum):
    x = np.arange(N)/N+i/100
    y = np.sin(x*10)*1
    if 1:
        graph = cvplot.cvplot(x,y,ylim=(-1.1, 1.1),pcolor=(0,200,0),gcolor=(0,0,0),acolor=(255,255,255))
        cv2.imshow("cvplot",graph) 
        cv2.waitKey(1)
    else:
        plt.clf()
        plt.plot(x,y)
        plt.pause(.001)
    

print(time.time() - start)
