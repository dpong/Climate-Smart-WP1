# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 23:22:58 2018

@author: SDLab - JH
"""
import numpy

def RainfallAmountGeneration(rainmean,distribution):
    rrain=numpy.random.random_sample()
    if(distribution=='expon'):
        rainfall=rainmean*(-numpy.log(1-rrain))
    else:
        rainfall=rainmean*(-numpy.log(1-rrain))
    return rainfall

def RainfallGeneration(rainmean, pd, pdw, pdd, mday,distribution):
    rday=numpy.random.random_sample()
    if(rday<pd):
        dryday=True
        rainfall=0
    else:
        dryday=False
        rainfall=RainfallAmountGeneration(rainmean,distribution)
    print(str(1)+'\t'+ str(rainfall))
    for i in range(1,mday):
        rday=numpy.random.random_sample()
        if(dryday):
            if(rday<pdd):
                rainfall=0
                dryday=True
            else:
                rainfall=RainfallAmountGeneration(rainmean,distribution)
                dryday=False
        else:
            if(rday<pdw):
                rainfall=0
                dryday=True
            else:
                rainfall=RainfallAmountGeneration(rainmean,distribution)
                dryday=False
        print(str(i+1)+'\t'+ str(rainfall))

RainfallGeneration(10, 0.6, 0.4, 0.7, 31, 'expon')
