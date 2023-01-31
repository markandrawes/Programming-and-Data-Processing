
from gradesLoad import gradesLoad
from displayMenu import displayMenu
from computeFinalGrades import computeFinalGrades
from display_list_of_grades import display_list_of_grades
from CheckDataErrors import CheckDataErrors
from gradesPlot import gradesPlot

# Main script written by Mark Andrawes (s214654@student.dtu.dk) 
# and Albert Frisch Møller (s214610@student.dtu.dk)

options = ["Load new data","Check for data errors","Generate plots","Display list of grades","Quit"]

# Initializing conditions

filename_accepted = False

data_loaded = False

choice = displayMenu(options)

while choice != 5:
    
    if choice == 1:
        
        filename = input("Please enter your filename: ")
        
        while filename_accepted == False: 
        
            try:
                
                gradesLoad(filename)
                
                break
                
            except FileNotFoundError:
                    
                filename_accepted = False
                    
                print("\nInvalid filename - not in directory.")
                
                print("\nPlease try again.")
                
                filename = input("Please enter your filename: ")
                
        grades = gradesLoad(filename)
        
        data_loaded = True
        
        print("\n")
        
        print("Grades have now been loaded.\n")
        
        #Number of students
        
        o = len(grades['Name'])
        
        #Number of assignments
        
        O = len(grades.iloc[0,:]) - 2
        
        print("{} {} {} {} {} {}".format("There are", str(O),"assignments", "and", str(o), "students"))
        
        print("\n")
        
        choice = displayMenu(options)
        
        print("\n")
        
    elif choice == 2:
        
        if data_loaded == False:
            
            print("\nData has not been loaded. Please go to option 1. Load new data in the menu\n")
        
            choice = displayMenu(options)
            
            print("\n")
         
        elif data_loaded == True:    
            
            grades = gradesLoad(filename)
            
            CheckDataErrors(grades)
            
            choice = displayMenu(options)
            
            print("\n")
            
            #----------------------------------------------           
            
    elif choice == 3:
        
        if data_loaded == False:
            
            print("\nData has not been loaded. Please go to option 1. Load new data in the menu\n")
        
            choice = displayMenu(options)
         
        elif data_loaded == True: 
            
            grades = gradesLoad(filename)
            
            Error = CheckDataErrors(grades)
            
            if Error == False: 
                
                gradesFinal = computeFinalGrades(grades)
            
                gradesPlot(gradesFinal, grades)
            
                choice = displayMenu(options)
                
                print("\n")
            
            if Error == True:
                
                choice = displayMenu(options)
                
                print("\n")
            
            #----------------------------------------------
            
    elif choice == 4: 
        
        if data_loaded == False:
            
            print("\nData has not been loaded. Please go to option 1. Load new data in the menu\n")
        
            choice = displayMenu(options)
            
            print("\n")
         
        elif data_loaded == True:  
            
            grades = gradesLoad(filename)
            
            Error = CheckDataErrors(grades)
            
            if Error == False: 
                
                gradesFinal = computeFinalGrades(grades)
            
                display_list_of_grades(gradesFinal,grades)
                
                print("\n")
                
                choice = displayMenu(options)
                
                print("\n")
            
            if Error == True:
                
                print("\n")
                
                choice = displayMenu(options)
            
            #----------------------------------------------     
            
    elif choice == 5:
         
         break



 

