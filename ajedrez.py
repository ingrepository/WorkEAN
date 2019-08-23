def giro180():
    repeat 2:
        turn_left()
def giro270():
    repeat 3:
        turn_left()
def zigzag_3(x):
    var=True
    cont=0
    while front_is_clear(): 
        cont=cont+1
        repeat 2:
            turn_left()
            move()
        giro180()
        if cont==x:
            break
        if object_here():
            var=False
            zigzag_1(cont)
            break
    return var        
def zigzag_1(x):
    var=True
    cont=0
    while front_is_clear():
        cont=cont+1
        move()
        giro270()
        move()
        turn_left()  
        if cont==x:
            break
        if object_here():            
            zigzag_3(cont)
            var=False
            break
    return var        

def zigzag_4():
    cont=0
    repeat 2:
        cont=cont+1
        repeat 2:    
            giro270()
            move()
        giro180()
    print(cont)   

        
#m=input()  
zigzag_1(5)


    

    


                    
                    

                


    


        
        




        

                             
