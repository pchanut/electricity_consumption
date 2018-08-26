#!/usr/bin/env python3
# -*- coding: utf-8 -*-1
"""
@author: Alexander Brems s174565, Philippe Chanut s176561 and Jonas Erichsen s175408
"""

#loads functions
import numpy as np
import pandas as pd
from aggregate_measurements import *
from displayMenu import *
from dataloadfunction import *
from print_statistics import *
from plotfunction import *
from changeUnit import *

# Define menu items
menuItems = np.array(["Load data", "Aggregate data", "Display statistics", "Visualize electricity consumption", "Quit"])

# Define empty file variable1
file = ""
# define plot array, which will be used in the plot function to determine which
# which zones to plot
plot = np.array([True, True, True, True, True])
# and error message used multible times in the script
errorFileNotLoaded = "\n\n*************************\nError! File is not loaded\n*************************\n"
# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)
    
    # Menu item chosen
    # ------------------------------------------------------------------
    # @author Jonas Erichsen s175408
    # 1. Load data
    if choice == 1:
        # Ask user to input name of file they wish to load
        menuFmode = np.array(["forward fill", "backward fill", "drop"])
        # Ask user how they wish to handle corrupted data
        while True:
            print("\n\n----------------------------------------------------------\nHow do you wish for corrupted measurements to be handled?: \n----------------------------------------------------------\n")
            choiceFmode = displayMenu(menuFmode)
            fmode = menuFmode[int(choiceFmode) - 1]
            break
        #Asks the user which file they wish to load
        file = input("\n\n---------------------------------------------------\nPlease enter the name of the file you wish to load: \n---------------------------------------------------\n\n> ")
        print("")
        #userinput for the file
        try:
            (tvec, data) = load_measurements(file, fmode)
            tvec_a = tvec
            (data_a, unit) = changeUnit(data, "Wh")
            period = "minSec"
       #error message if no file is found
        except:
            print("\n\n***************************************************\nError! Unable to detect file or invalid file format\n***************************************************\n")
            file = ""
  # ------------------------------------------------------------------
  # @author Alexander Brems s174565
  # 2. Aggregate data
    elif choice == 2:
        if file == "":
            # Display error message if no file is loaded
            print(errorFileNotLoaded)
        #ask user to pick which unit they want to aggregate the data by
        else:
            menuAgg = np.array(["Hour", "Day", "Month", "Hour of the day", "Reset to non-aggregated data (minutes and seconds)", "Return"])
            menuAggVec = np.array(["hour", "day", "month", "hour of the day"])
            while True:
                choiceAgg = displayMenu(menuAgg)
                # defines the time and data vectors and converts the unit if
                # the average of the data set is above or below a threshold
                if choiceAgg in np.arange(1, 5):
                    period = menuAggVec[int(choiceAgg) - 1]
                    (tvec_a, data_a) = aggregate_measurements(tvec, data, period)
                    unit = "Wh"
                    (data_a, unit) = changeUnit(data_a, unit)
                    #tells user file is loaded succesfully
                    print("\n\n-------------------------------------\nMeasurements set to {} succesfully\n-------------------------------------\n".format(period))
                    break
                #user resets data back to non-aggregated
                elif choiceAgg == 5:
                    tvec_a = tvec
                    (data_a, unit) = changeUnit(data, "Wh")
                    period = "minSec"
                    print("\n\n---------------------------\nMeasurements reset succesfully\n---------------------------\n")
                    break
                #user can return to the mainmenu
                elif choiceAgg == 6:
                    break
    # ------------------------------------------------------------------
    # @author Alexander Brems s174565
    # 3. Datastatistics
    elif choice == 3:
        if file == "":
            # Display error message
            print(errorFileNotLoaded)
            #gives the statistics based on current dataset
        else:
            print_statistics(data_a, period, unit)
    # ------------------------------------------------------------------
    # @author Jonas Erichsen s175408
    # 4. Plot data
    elif choice == 4:
        if file == "":
            # Display error message
            print(errorFileNotLoaded)
        else:
            while True:
                #the user can choose between the different zones, and how many
                #they want shown in the plot
                menuPlot = np.array(["Show consumption zone 1: {}", "Show consumption zone 2: {}", "Show consumption zone 3: {}", "Show consumption zone 4: {}", "Show combined consumption: {}", "Plot electricity consumption over time", "Return"])
                for i in range(5):
                    menuPlot[i] = menuPlot[i].format(plot[i])
                choicePlot = displayMenu(menuPlot)
                if choicePlot in np.arange(1, 6):
                    if plot[int(choicePlot) - 1] == True:
                        plot[int(choicePlot) - 1] = False
                    else:
                        plot[int(choicePlot) - 1] = True
                #plots the graphs based on chosen zones
                elif choicePlot == 6:
                    if np.size(tvec_a[:, 0]) > 30:
                        print("\n*****************************************************************************\nWarning! The user is NOT advised to plot functions with more than 30 elements\n                  The current data set has {} elements\n*****************************************************************************\n".format(np.size(tvec_a[:, 0])))
                        print("----------------------------------------\nDo you still wish to plot your data set?\n----------------------------------------\n")
                        menuWarn = np.array(["Yes", "No"])
                        while True:
                            choiceWarn = displayMenu(menuWarn)
                            if choiceWarn == 1:
                                warnProceed = True
                                break
                            elif choiceWarn == 2:
                                warnProceed = False
                                break
                    elif np.size(tvec_a[:, 0]) <= 30:
                        warnProceed = True
                    if warnProceed == True:
                        plotFunction(tvec_a, data_a, period, plot, unit)
                        print("")
                #returns the user to main menu
                elif choicePlot == 7:
                    break
    # ------------------------------------------------------------------
    # 5. Quits the program
    elif choice == 5:
        break









