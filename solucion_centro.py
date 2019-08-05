"""
 Descripciòn:
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

def giro():
    repeat 2:
        turn_left()
def putt(x):
    x=int(x/2)
    repeat int x:    
        move()
    put()

cont=1
while front_is_clear():
    cont +=1
    move()
    if wall_in_front():
        giro()
        break 
putt(cont)

        

      
  
