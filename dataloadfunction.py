# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 09:26:16 2018

@author: Jonas Erichsen s175408

"""
import numpy as np
import pandas as pd
def load_measurements(filename,fmode):
    #loads the the file into a matrix
    matrix=np.loadtxt(open(filename,"rb"),delimiter=",")
#----------------choice of forward---------------------------------------------
    if fmode=="forward fill":
        #removes invalid measurments in first row
        while True:
            nanInFile = False
            if -1 in matrix[0, 6:10]:
                nanInFile = True
                print("Error! First line in {} is corrupted, and has been deleted".format(filename))
            if nanInFile == True:
                matrix = matrix[1:np.size(matrix[:, 0]) + 1, :]
            else:
                break
        #turns the vektor into a dataframe
        df=pd.DataFrame(matrix)
        #replaces all -1 with NaN
        df[df == -1] = np.nan
        #uses pandas forwardfill function
        matrix=df.fillna(method="ffill")
        #change from dataframe to array
        matrix=matrix.values
        #defining the time vector and the data vector
        tvec=matrix[:,0:6]
        data=matrix[:,6:11]
#--------------------choice of backward----------------------------------------
    elif fmode=="backward fill":
        #removes invalid measurments in the last row
        while True:
            nanInFile = False
            if -1 in matrix[np.size(matrix[:, 0]) - 1, 6:10]:
                nanInFile = True
                print("Error! Last line in {} is corrupted, and has been deleted".format(filename))
            if nanInFile == True:
                matrix = matrix[0:np.size(matrix[:, 0]) - 1, :]
            else:
                break
        #turns the vektor into a dataframe
        df=pd.DataFrame(matrix)
        #replaces all -1 with NaN
        df[df == -1] = np.NaN
        #uses pandas backwardfill function
        matrix=df.fillna(method="bfill")
        #change for dataframe to array
        matrix=matrix.values
        #defining the time vector and the data vector
        tvec=matrix[:,0:6]
        data=matrix[:,6:11]
    
#------------------choice of drop----------------------------------------------
    elif fmode=="drop":
        for i in range (np.size(matrix[:,0])):
            if matrix[i,6]<0 or matrix[i,7]<0 or matrix[i,8]<0 or matrix[i,9]<0:
                matrix[i,0]=-1
        matrix=matrix[matrix[:,0]>=0]
        #defining the time vector and the data vector
        tvec=matrix[:,0:6]
        data=matrix[:,6:11]
    return (tvec, data)
    

