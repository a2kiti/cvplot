# -*- coding: utf-8 -*-


import cv2
import numpy as np

#Drawing graph by Oencv
def cvplot(x,y,wW=500,wH=300,gW=None,gH=None,xlim=None,ylim=None,pcolor=(255,100,0),gcolor=(255,255,255),acolor=(0,0,0),linesize=2,scaleDisplay=True):
    
    #Graph size to window size
    if gW is None:
        gW = int(wW*0.75)
    if gH is None:
        gH = int(wH*0.75)
    
    #window
    window = np.ones([wH,wW,3],np.uint8) * np.array(gcolor,np.uint8)
    #graph
    graph = np.ones([gH,gW,3],np.uint8) * np.array(gcolor,np.uint8)
    
    #Setting display data range
    if xlim is None:
        xlim = (np.min(x),np.max(x))
    ind = [x>=xlim[0]]
    x=x[ind]
    y=y[ind]
    ind = [x<=xlim[1]]
    x=x[ind]
    y=y[ind]
    if ylim is None:
        ylim = (np.min(y),np.max(y))
    ind = [y>=ylim[0]]
    x=x[ind]
    y=y[ind]
    ind = [y<=ylim[1]]
    x=x[ind]
    y=y[ind]
    
    #Applying x and y to the area of the graph
    ix = (x - xlim[0]) * gW * 0.9 / (xlim[1] - xlim[0])
    iy = gH - (y - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0])
    
    data1 = np.hstack((np.round(ix).astype(np.int32),np.round(iy).astype(np.int32))).reshape(2,len(ix)).T
    data2 = np.roll(data1,-1,axis=0)
    data = np.hstack((data1,data2)).reshape(len(ix),2,2)[:-1]
    cv2.drawContours(graph, data, -1, pcolor, linesize)
    
    #Filling outside the area
#    iyover = int(np.round(gH - (ylim[0] - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0]))) - (linesize - 1)
#    graph[iyover:,:] = np.array(gcolor,np.uint8)
#    iyover = int(np.round(gH - (ylim[1] - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0]))) + (linesize)
#    graph[:iyover,:] = np.array(gcolor,np.uint8)
    
    
    window[(wH-gH)//2:(wH-gH)//2+gH,(wW-gW)//2:(wW-gW)//2+gW] = graph
    #Axis
    ySize = 10
    axis = []
    #x-axis
    axis.append([((wW-gW)//2, wH-(wH-gH)//2), ((wW-gW)//2+gW, wH-(wH-gH)//2)])
    axis.append([((wW-gW)//2+gW - ySize, wH-(wH-gH)//2 - ySize), ((wW-gW)//2+gW, wH-(wH-gH)//2)])
    axis.append([((wW-gW)//2+gW - ySize, wH-(wH-gH)//2 + ySize), ((wW-gW)//2+gW, wH-(wH-gH)//2)])
    
    #y-axis
    axis.append([((wW-gW)//2, wH-(wH-gH)//2), ((wW-gW)//2,(wH-gH)//2)])
    axis.append([((wW-gW)//2 - ySize, (wH-gH)//2 + ySize), ((wW-gW)//2,(wH-gH)//2)])
    axis.append([((wW-gW)//2 + ySize, (wH-gH)//2 + ySize), ((wW-gW)//2,(wH-gH)//2)])
    
    #Origin of the graph
    if scaleDisplay == True:
        x0 = 0
        ix0 = (x0 - xlim[0]) * gW * 0.9 / (xlim[1] - xlim[0]) + (wW-gW)//2
        if ix0 < wW-(wW-gW)//2 - 30 and ix0 > (wW-gW)//2 + 30:
            axis.append([(int(round(ix0)), wH-(wH-gH)//2), (int(round(ix0)), wH-(wH-gH)//2-ySize)])
            cv2.putText(window, str(x0), (int(round(ix0))-4*len(str(x0)), wH-(wH-gH)//2+20), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
        x0 = xlim[0]
        ix0 = (x0 - xlim[0]) * gW * 0.9 / (xlim[1] - xlim[0]) + (wW-gW)//2
        #axis.append([(int(round(ix0)), wH-(wH-gH)//2), (int(round(ix0)), wH-(wH-gH)//2-ySize)])
        cv2.putText(window, str(x0), (int(round(ix0))-4*len(str(x0)), wH-(wH-gH)//2+20), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
        x0 = xlim[1]
        ix0 = (x0 - xlim[0]) * gW * 0.9 / (xlim[1] - xlim[0]) + (wW-gW)//2
        axis.append([(int(round(ix0)), wH-(wH-gH)//2), (int(round(ix0)), wH-(wH-gH)//2-ySize)])
        cv2.putText(window, str(x0), (int(round(ix0))-4*len(str(x0)), wH-(wH-gH)//2+20), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
        
        y0 = 0
        iy0 = gH - (y0 - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0]) + (wH-gH)//2
        if iy0 < wH-(wH-gH)//2 - 30 and iy0 > (wH-gH)//2 + 30:
            axis.append([((wW-gW)//2 + ySize, int(round(iy0))), ((wW-gW)//2,int(round(iy0)))])
            cv2.putText(window, str(y0), ((wW-gW)//2-5-8*len(str(y0)), int(round(iy0))+5), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
        y0 = ylim[0]
        iy0 = gH - (y0 - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0]) + (wH-gH)//2
        #axis.append([((wW-gW)//2 + ySize, int(round(iy0))), ((wW-gW)//2,int(round(iy0)))])
        cv2.putText(window, "{0:.2f}".format(y0), ((wW-gW)//2-5-8*len("{0:.2f}".format(y0)), int(round(iy0))+5), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
        y0 = ylim[1]
        iy0 = gH - (y0 - ylim[0]) * gH * 0.9 / (ylim[1]-ylim[0]) + (wH-gH)//2
        axis.append([((wW-gW)//2 + ySize, int(round(iy0))), ((wW-gW)//2,int(round(iy0)))])
        cv2.putText(window, "{0:.2f}".format(y0), ((wW-gW)//2-5-8*len("{0:.2f}".format(y0)), int(round(iy0))+5), cv2.FONT_HERSHEY_PLAIN, 0.8, acolor, 1, cv2.LINE_AA)
    
    cv2.drawContours(window, np.array(axis), -1, acolor, linesize)

    return window.astype(np.uint8)


