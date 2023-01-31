
import numpy as np

def roundGrade(grades):
    
    # Written by Albert Frisch Møller (s214610@dtu.dk) 
    #
    # roundGrade rounds the grades to the nearest grading on the grading scale
    #
    # Usage: gradesFinal = roundGrade(gradesFinal)
    #
    # Input: grades = gradesLoad(filename)
    #
    # Output: gradesRounded - a numpy array containing each grade rounded to the nearest
    # Grade from the grading scale
    
    grading_scale = np.array([-3,0,2,4,7,10,12])
    
    gradesRounded = np.zeros(len(grades))
    
    for i in range(len(grades)):
    
        #Grades beyond or below the grading scale will be set to the value itself
        
        if grades[i] <= -3 or grades[i] >= 12: 
            
            gradesRounded[i] = grades[i]
         
        #Computing the distance each grade is to the grading scale   
         
        dist = abs(grading_scale - grades[i])
        
        gradesRounded[i] = grading_scale[np.argmin(dist)]
        
    return gradesRounded

