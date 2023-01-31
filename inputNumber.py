

def inputNumber(prompt):
    
    #Written by Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    #
    #inputNumber requests the user to enter a number 
    #
    #Usage: num = inputNumber(prompt)
    
    
    while True: 
        
        try:
            
            num = float(input(prompt))
            
            break
        
        except ValueError: 
            
            pass
        
    return num