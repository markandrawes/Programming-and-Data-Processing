
import numpy as np

from roundGrade import roundGrade

def computeFinalGrades(grades):
    
    # Written by Albert Frisch Møller (s214610@dtu.dk)
    #
    # computeFinalGrades compute the final grade for each student where rounding and other 
    # coniditions have been implemented
    #
    #Input: grades = gradesLoad(filename)
    #
    #Output: finalGrades - a numpy array containing the final grade of every student
    
    
    gradesFinal = np.zeros(len(grades))
     
    N = len(grades.iloc[1,:])
    
    n = len(grades.iloc[:,1])    

    for i in range(n):
        
        #Handling the special case where a grade of -3 has been given: 
                       
        if np.amin(grades.iloc[i,2:N]) == -3:
            
            gradesFinal[i] = -3
            
            continue
        
        #Handling the special case where a student has completed one assignment
        
        if np.count_nonzero(grades.iloc[i,2:N] >=0) == 1:
            
            I = (np.where(grades.iloc[0,2:N] >=0))[0]
            
            gradesFinal[i] = grades.iloc[i,2+I[0]]
            
            continue 
        
        if np.count_nonzero(grades.iloc[i,2:N] >=0) > 1:
            
            #Determining the number of missing assignments 
            
            t = len(grades.iloc[i,2:N]) - np.count_nonzero(grades.iloc[i,2:N] >=0)
            
            p = 2
            
            #While-looping to find the lowest grade a student got for all their assignments 
            
            while p != N-1:
                
                #Determining the lowest grade for each student
                
                if grades.iloc[i,p] == np.amin(grades.iloc[i,2:N]):
                    
                    grades.iloc[i,p] = 0
                    
                    #Taking the average by taking into account t
                        
                    gradesFinal[i] = (np.sum(grades.iloc[i,2:N]))/(len(grades.iloc[i,2:N])-1-t)
                    
                    break
                    
                else: 
                    
                    p+=1 
                    
    gradesFinal = roundGrade(gradesFinal)
    
    return gradesFinal 