#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Alexander Brems s174565
This function takes an input of the time vector and converts it into one of
three formats depending on what period (what it's currently aggregated to)
it's currently in. if the period is either month or day the format of the date
is chaged to the following format:
y/month/d.
If the period is either in the format hour or minSec, the output format is:
y/month/d - h/min/s
If the period is in hour of the day the output is a vector containing the hours
from 0 to and including 23
"""

import numpy as np
def convert_time(tvec, period):
    striVec = np.array(["month", "day", "hour", "minSec"])
    convTvec = np.zeros(np.size(tvec[:, 0])).astype(str)
    if period in striVec[0:2]:
        for i in range(np.size(tvec[:, 0])):
            convTvec[i] = "{:.0f}/{:.0f}/{:.0f}".format(tvec[i,0], tvec[i,1], tvec[i,2])
    elif period in striVec[2:4]:
        for i in range(np.size(tvec[:, 0])):
            convTvec[i] = "{:.0f}/{:.0f}/{:.0f} - {:.0f}:{:.0f}:{:.0f}".format(tvec[i,0], tvec[i,1], tvec[i,2], tvec[i,3], tvec[i,4],tvec[i,5])
    elif period == "hour of the day":
        convTvec = np.arange(24)
    return convTvec

