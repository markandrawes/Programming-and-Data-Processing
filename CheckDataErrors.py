
import numpy as np


def CheckDataErrors(grades):
    
    """
    Written by Mark Andrawes (s214654@student.dtu.dk)
    
    CheckDataErrors searches through the given data and checks for errors:
    repeated studentIDs and grades that do not lie on the 7-step-scale.
    
    INPUT: grades = gradesLoad(filename)
    
    OUTPUT: A print statement saying if errors were found, and, if so,
            what errors specifically.    
    """
    

# 1. Checking if there are students with the same student ID:
            
    if len(list(grades['StudentID'].unique())) < len(grades.index):
        
        print('\nError: repeated StudentID detected.')
        
    else: 
       
        print('\nThere were no errors detected for StudentIDs.')
        

# 2. Checking if a grade does not lie on the 7-step-scale:
    
    allgrades = np.array([])
    
    invalidgrades = np.array([])
    
        
    for i in range(2, len(grades.columns)):
        
        allgrades = np.append(allgrades, [grades.iloc[:,i]])
                
    
    for i in range(0,len(allgrades)):
        
        if (allgrades[i] != -3 and allgrades[i] != 0 and allgrades[i] != 2 and allgrades[i] != 4 and 
            allgrades[i] != 7 and allgrades[i] != 10 and allgrades[i] != 12 and np.isnan(allgrades[i])==False):
        
            invalidgrades = np.append(invalidgrades, allgrades[i]) 
      
    if len(invalidgrades) == 1: 
        
        print('Error: 1 grade in the data set does not lie on the 7-step-scale.\n')    
        
        Error_Detected = True
        
        print("\nPlease go to option 1. in the menu to load another data set.")
    
    elif len(invalidgrades) > 1:     
        
        print('Error: ' + str(len(invalidgrades)) + ' grades in the data set do not lie on the 7-step-scale.\n')    
    
        Error_Detected = True    
    
        print("\nPlease go to option 1. in the menu to load another data set.")
    
    elif len(invalidgrades) == 0:
        
        print('There were no errors detected for invalid grades.\n') 

        Error_Detected = False

    return Error_Detected

