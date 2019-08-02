""" Quiz_2: Descripción:
 El mundo requiere que el robot recoga las semillas (cuadrado) 
 y plante margaritas en su lugar. El mundo es de 5x5 y las 
 semillas se encuentran en (1, 1), (1, 5), (5, 5), (5, 1). 
 Autor: Sebastian Varon
 Fecha: 2/08/19
""" 
"""
Funcionalidad: Reeborg siembra una margarita.
Pre: En la posicion actual de reeborg debe haber un objeto 
para recoger y reeborg tener una margarita para colocar.
Pos: Reeborg recoge y siembra con exito la margarita.
"""
def siembra():
        take()
        put("daisy")        
"""
Funcionalidad: Reeborg recorre el mundo y planta todas las margaritas.
Pre: Reeborg está en la posición (1,1) y mira al Este. 
Pos: Reeborg está en la posición (1,1), tiene 4 semillas (cuadrados) y mira al Norte.
"""
def plantar(): 
        repeat 2:
            siembra()
            repeat 4:
                move()
            siembra()
            turn_left()
            repeat 4:
                move()
            turn_left()
        turn_left()
plantar()
        
    
    
       
    

        

      
  
