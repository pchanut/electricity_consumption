#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
"""

import numpy as np

def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    # number. Repeats until user inputs a valid number.
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num



def displayMenu(options):
# DISPLAYMENU Displays a menu of options, ask the user to choose an item
# and returns the number of the menu item chosen.
#
#    Usage: choice = displayMenu(options)
#
# Input options Menu options (array of strings)
# Output choice Chosen option (integer)
#
# Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
# Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
# Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Please choose a menu item: ")
    
    return choice