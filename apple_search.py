'''
 Descripciòn:
 El mundo requiere que el robot realice una busqueda 
 hasta encontrar la posicion donde se encuentra el 
 objeto (manzana) , el robot recoge el objeto (manzana) 
 y se desplace hasta la casa. 
 Autor: Sebastian Varon
 Fecha: 31/07/19
"""
"""
Funcionalidad: Reeborg busca la manzana
Pre: Reeborg esta frente/mirando el objetivo.
Pos: Reeborg se desplaza 4 posiciones en x.
'''
def search_en_fila(): #Busca un objeto en una linea de 4 pasos
    repeat 4:
        if object_here():
            take()
            break
        else:
            move()     
 
"""
Funcionalidad: Reeborg gira 3 veces
Pre: verdadero
Pos: Reeborg gira tres veces.
el objeto
"""
def giro3():
    repeat 3:
            turn_left()
"""
Funcionalidad: Reeborg busca y encuentra la manzana en
un mundo 5x5, una vez lo encuentre, termina.
Pre: Reeborg esta (1,1) & mira hacia el este.
Pos: Reeborg se ubica hasta la posicion donde esta 
el objeto
"""    
def world_search():
    if front_is_clear():
        search_en_fila() 
        turn_left()
        move()
        turn_left()
        search_en_fila()
        giro3()
        move()
        giro3()
        search_en_fila()        
world_search()

def volver_casa()
      

        
    