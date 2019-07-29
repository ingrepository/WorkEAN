"""Descripcion: El mundo requiere que el robot realice una caminata
en forma  zic zac hasta llegar al otro extremo del mapa 5x5.
    Autor: Sebastian Varon
    Fecha: 29/07/2019
   """ 
#print("Hola soy Reeborg's\n¡Bienvenido a mi mundo!\n ¡Comenzare mi misión!")

"""
Funcionalidad:Desplazamiento
Pre:Reeborg comienza en (1,1)
Pos:Reeborg esta en (5,1) / Reeborg esta en (1,5)
"""        
def walk(): #
    if (front_is_clear()):
        repeat 4:
            move()
    if (wall_in_front()):
        turn_left()
        if (front_is_clear()):
            repeat 4:
                move()    
"""
Funcionalidad:
Pre:reeborg mira al norte
Pos:reeborg mira al oriente
"""
def turn_right(): #Giro derecha
    repeat 3:
        turn_left()

"""
Funcionalidad:Reeborg llega hasta (5,5)
Pre:Reeborg esta en la (1,1) && Reeborg camina hacia el norte
Pos:Reeborg esta en (5,5)
"""
def walk_zigzag():
    repeat 4:
        move()
        turn_right()
        move()
        turn_left()
walk_zigzag()
