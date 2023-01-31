
import numpy as np

def display_list_of_grades(gradesFinal,grades):
    
    #Written by Albert Frisch Møller (s214610@dtu.dk)
    #
    #display_list_of_grades displays a list of the grades for each assignment
    # and a numpy array of each students name and their final grade
    #
    #Input: gradesFinal = gradesRound(gradesFinal) and grades = gradesLoad(filename)
    #
    #Output: A numpy array containing every grade for each assignment and the final grade
    # for each student
    
    print("\n")
    
    #Setting initial conditions
    
    t = 1
    
    #Determining the number of columns 
    
    N = len(grades.iloc[1,:])
    
    for i in range(2,N):
        
        #initiallizing an empty array with enough space to include the string ' Assignment ' 
        
        raw_grades = "             "
        
        for p in range(N-1):
            
            #Ignoring any grades that are "Not A Number"
            
            if str(grades.iloc[:,i][p]) == 'nan':
            
                continue
            
            else: 
            
                #Appending each grade for the ith assignment to raw_grades
                
                raw_grades = np.append(raw_grades,str(grades.iloc[:,i][p])+',')
               
        raw_grades[0] = 'Assignment' + str(t) + ':'
    
        print(raw_grades)
        
        print("\n")
        
        t+= 1

    names = grades['Name'].values
    
    sorted_names = np.sort(names)
    
    print("\n")
        
    print("List of students and there final grades in alphabetical order:")
        
    print("\n")
    
    for r in range(len(names)):
        
        I = (np.where(names == sorted_names[r]))[0][0]
        
        print(np.array([sorted_names[r] + ':' + str(gradesFinal[I])]))
        