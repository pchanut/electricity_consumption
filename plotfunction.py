# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:04:48 2018

@author: Philippe Chanut s176561 and Jonas Erichsen s175408
"""

import numpy as np
import matplotlib.pyplot as plt
from convert_time import *

def plotFunction(tvec_a,data_a, period, plot, unit):
    if np.size(data_a[:,0]) <= 6:
        # line 15-31 is taken from https://matplotlib.org/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py
        N = np.size(data_a[:,0])
        #number of x values
        x = np.arange(N)
        labels = convert_time(tvec_a, period)
        #defining the y values based on zones
        zone1 = data_a[:,0]
        zone2 = data_a[:,1]
        zone3 = data_a[:,2]
        zone4 = data_a[:,3]
        width = 0.35
        #plotting the bars on top of each other
        plt.bar(x, zone1, width, color="y", label = "Zone 1")
        plt.bar(x, zone2, width, bottom=zone1, color="b",label = "Zone 2")
        plt.bar(x, zone3, width, bottom=(zone1+zone2), color="r",label = "Zone 3")
        plt.bar(x, zone4, width, bottom=(zone1+zone2+zone3), color="g",label = "Zone 4")
        #plot labels
        plt.ylabel('consumption in {}'.format(unit))
        plt.xlabel("{}".format(period))
        plt.xticks(x, labels, rotation='vertical')
        plt.title("Consumption per zone per {}".format(period))
        #choose the place of the legend box
        plt.legend(bbox_to_anchor=(1,0.6))
        print("Since there are less than 25 measuremnts, all zones are plotted in bar chart")
        plt.show()
        if period == "minSec":
            print("\n*minSec is either minutes or seconds depending on what the standard unit of the loaded file is\n")
    else:
        #define labels
        labels = convert_time(tvec_a, period)
        x = np.arange(np.size(labels))
        y = data_a
        #plot labels and titel
        plt.title("Consumption per zone per {}".format(period))
        plt.xlabel("Consumption per zone per {}".format(period))
        plt.ylabel("Consumption in {}".format(unit))
        plt.xticks(x, labels, rotation='vertical')
        # determining which plots to show, based on the user preference stored
        # in the plot vector
        for i in range(4):
            if plot[i] == True:
                plt.plot(x, y[:, i], label="Zone {}".format(i + 1))
        if plot[4] == True:
            overallData = np.zeros(np.size(x))
            for i in range(np.size(x)):
                overallData[i] = np.sum(data_a[i, :])
            plt.plot(x, overallData,label="All Zones")
        plt.legend(bbox_to_anchor=(1,0.6))
        plt.show()
        if period == "minSec":
            print("\n*minSec is either minutes or seconds depending on what the standard unit of the loaded file is\n")