
from inputNumber import inputNumber

import numpy as np

options = ["Load new data","Check for data errors","Generate plots","Display list of grades","Quit"]

def displayMenu(options):
    
    #Written by Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    #
    #displayMenu displays the different options the user can choose from
    #it returns the number of the option chosen
    #
    #Usage: choice = displayMenu(options)
    #
    #Input: options - a list of different strings
    #
    #Output: choice - user inputted integer
    
    for i in range(len(options)):
        
        print("{:d}. {:s}".format(i+1, options[i]))
        
    choice = 0
    
    while not(np.any(choice == np.arange(len(options))+1)):
        
        choice = inputNumber("Please choose a menu item: ")
        
    return choice




    