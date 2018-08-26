#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alexander Brems s174565
This function takes an input of the data set, the current period, and the unit
in which the data set is currently in. it makes a table with the minimum value,
the percentiles of 25%, 50%, and 75%, and the maximum value for each of the
zones and the sum of all the zones
"""

import numpy as np
import pandas as pd

def print_statistics(data, period, unit):
    tableVec = np.zeros([5,5])
    percentileVec = np.array([0, 25, 50, 75, 100])
    for j in range(4):
        for i in range(5):
            tableVec[j, i] = np.percentile(data[:, j], percentileVec[i])
    for i in range(5):
        tableVec[4, i] = np.sum(tableVec[0:4, i])
    xLabels = np.array(["Minimum", "1. quart.", "2. quart.", "3. quart.", "Maximum"])
    yLabels = np.array(["1", "2", "3", "4", "All"])
    table = pd.DataFrame(tableVec, yLabels, xLabels)
    table = table.round(2)
    table.columns.name = "Zone"
    print("\n-------------------------------------------------------\n***          Consumption of {} per {}          ***\n-------------------------------------------------------\n{}\n-------------------------------------------------------\n".format(unit, period, table))
    if period == "minSec":
        print("*minSec is either minutes or seconds depending on what the standard unit of the loaded file is\n")



