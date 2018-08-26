#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alexander Brems s174565

This function takes an imput of the data set and the current unit, and converts
the unit to the optimal format. We have decided that the for the data set to be
in the optimal format, the average data should be within the boundaries of 
1 <= np.average(data) > 1000.
This function runs a while loop until the average data is within the boundaries
"""

import numpy as np
def changeUnit(data_a, unit):
    unitVec = np.array(["muWh", "mWh", "Wh", "kWh", "MWh", "GWh", "TWh", "PWh"]) 
    while True:
        j = 0
        averageData = np.average(data_a)
        if averageData >= 1000 and (unit in unitVec[0: 7]):
            data_a = data_a * (1/1000)
            for i in range(8):
                if unit == unitVec[i]:
                    newUnit = i + 1
                    j = 1
            unit = unitVec[newUnit]
        elif averageData < 1 and (unit in unitVec[1: 8]):
            data_a = data_a * 1000
            for i in range(8):
                if unit == unitVec[i]:
                    newUnit = i - 1
                    j = 1
            unit = unitVec[newUnit]
        if j == 0:
            break
    return(data_a, unit)
    