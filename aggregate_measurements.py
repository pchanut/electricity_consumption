#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Philippe Chanut s176561

This function aggregates measurements in data either per 'hour', 'day', 'month' or 'hour of the day'
Returns a matrix of aggregated measurement data_a and of time peiods 'tvec_a'

Input:
    tvec = matrix N x 6 or time points in name columns year-month-day-hour-min-s
    data = matrix N x 4 of measurements for 4 zones
    period = string with value 'hour', 'day', 'month' or 'hour of the day'

Output:
    tvec_a = matrix M x 6 of time points indicating beginning of time period
    data_a = matrix of aggregated measurements. Average if aggregated by "hour of the day"

"""

import numpy as np

def aggregate_measurements(tvec, data, period):
    # define different possible periods for aggregation
    Agg = np.array(['month', 'day', 'hour'])
    
    if period in Agg:
        # create a loop instead of copying code for periods 'month', 'day'. 'hour'
        i = int(np.where(Agg == period)[0])
        i = i +2 # find how many columns in tvec should be used based on index of period
        # for ex if period = month, i = 2 and we look at year + month
        
        # find unique rows, their indexes and how many
        matrix = tvec[:, 0:i]      
        (u, index, counts) = np.unique(matrix, return_index=True, return_counts=True, axis=0) #Scypi
        M = np.shape(u)[0] # number of rows
        # create and fill-in data_a and tvec_a
        data_a = np.zeros((M,4))
        tvec_a = np.zeros((M, 6))
        for i in range(M):
            tvec_a[i,:] = tvec[index[i]]
            for j in range(index[i], index[i] + counts[i]):
                data_a[i,:] = data_a[i,:] + data[j,:]
                
        return (tvec_a, data_a)
    
    #-------------------
    elif period == 'hour of the day':
        data_a = np.zeros((24,4))
        tvec_a = np.zeros((24,6))
        for i in range(24):
            # select data for hours = i
            d = data[tvec[:,3] == i] 
            # fill in data_a and tvec_a
            data_a[i] = np.mean(d, axis = 0)
            tvec_a[i,3] = i
            
        return (tvec_a, data_a)
    
    else:
        print("Period should be 'month', 'day', 'hour' or 'hour of the day' ")
        
    
    



        
        
     