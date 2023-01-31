
import pandas as pd

def gradesLoad(filename):
    
    # Written by Albert Frisch Møller (s214610@dtu.dk) 
    #
    # gradesLoad stores the data from filename as a pandas dataframe
    # and returns the pandas dataframe as grades
    #
    #Usage: grades = gradesLoad(filename)
    #
    #Input: filename - a valid csv file
    #
    #Output: grades - a pandas dataframe
    
    grades = pd.read_csv(filename)
    
    return grades