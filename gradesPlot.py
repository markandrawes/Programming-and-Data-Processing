

import numpy as np

import matplotlib.pyplot as plt

import math

def gradesPlot(gradesFinal, grades):         
    
    """
    Written by Mark Andrawes (s214654@student.dtu.dk)
    
    gradesPlot plots a bar graph of the final grade for each student, as well
    as a line and scatter graph of all individual grades and the average for 
    each assignment
    
    INPUT: gradesFinal = gradesRound(gradesFinal) and grades = gradesLoad(filename)
    
    OUTPUT: The two plots as described above.    
    """


# Plot 1:

#Gathering the y-values: total number of students achieving a specific grade.

    Grade1 = np.count_nonzero(gradesFinal==-3)         
    Grade2 = np.count_nonzero(gradesFinal==0)      
    Grade3 = np.count_nonzero(gradesFinal==2)       
    Grade4 = np.count_nonzero(gradesFinal==4)      
    Grade5 = np.count_nonzero(gradesFinal==7)      
    Grade6 = np.count_nonzero(gradesFinal==10)  
    Grade7 = np.count_nonzero(gradesFinal==12)   
   
    Totals = [Grade1, Grade2, Grade3, Grade4, Grade5, Grade6, Grade7]    
    bars = ('-3','0','2','4','7','10','12')    
    spread = np.arange(len(bars))
    
    plt.xticks(spread, bars)    
    plt.bar(spread, Totals)    
    plt.xlabel('Final Grades')    
    plt.ylabel('Number of Students')   
    plt.title('Final Grades')    
    plt.show()

        #-------------------------------------------------------    
    
# Plot 2:
        
#Gathering the averages for the line plot.
    
    yvalues = np.array([])    
    xvalues = range(1, len(grades.columns)-1)    
      
    for i in range(2, len(grades.columns)):
       
       yvalues = np.append(yvalues,np.mean(grades.iloc[:,i]))       
        
 # Setting the x-axis to only integer values.  
 
    new_x = range(math.floor(min(xvalues)), math.ceil(max(xvalues))+1)    
  
#Gathering data points for scatter plot of each individual grade. 
    
    xvalues2 = np.repeat(xvalues,len(grades.index))    
    yvalues2 = np.array([])
    
    for i in range(2, len(grades.columns)):
 
       yvalues2 = np.append(yvalues2, [grades.iloc[:,i]])

#Next we add a random number between -0.1 and 0.1 to x and y coordinates of each
#data point, in order to tell apart overlapping data points.        
   
    xvalues2 = [i+np.random.uniform(-0.1,0.1,1) for i in xvalues2]
    yvalues2 = [i+np.random.uniform(-0.1,0.1,1) for i in yvalues2]
    
#Lastly, we plot the line graph and the scatter plot, including a legend.
    
    plt.figure(figsize=(9,7))    
    plt.title('Grades Per Assignment')    
    plt.xlabel('Assignment Number')   
    plt.ylabel('Grade')  
    plt.xticks(new_x)  
    plt.plot(xvalues, yvalues, color='blue', label = 'Average Grade Per Assignment')
    plt.scatter(xvalues2,yvalues2,color='green', label = 'Grade Points')   
    plt.legend()     
    plt.show()