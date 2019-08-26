"""
Descripcion: Este programa esta diseñado para desplazar a Reeborg en forma de alfil 
en un tablero 8x8 debera contar con la funcion mov_alfil que tiene parametros
(direccion, pasos) donde 1<=pasos<8 y direccion 1<=direccion<=4 tal que represente
el plano cartesiano.
Autor: Sebastian Varon, Michael Garzoon, Sergio Jimenez
Fecha:26/08/2019
"""
def giro180():
    repeat 2:
        turn_left()
def giro270():
    repeat 3:
        turn_left()
def zigzag_4(x):
    var=True
    cont=0
    while front_is_clear(): 
        repeat 2:    
            giro270()
            move()
        giro180()
        cont=cont+1
        if object_here():
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_2(cont)
            break
        if cont==x:
            break
    return var        
def zigzag_3(x):
    var=True
    cont=0
    while front_is_clear(): 
        repeat 2:
            turn_left()
            move()
        giro180()
        cont=cont+1
        if object_here():
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_1(cont)
            break
        if cont==x:
            break
        
    return var        
def zigzag_2(x):
    var=True
    cont=0
    while front_is_clear():        
        repeat 2:
            move()
            turn_left()
        giro180()
        cont=cont+1
        if object_here(): 
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_4(cont)
            break
        if cont==x:
            break
    return var
def zigzag_1(x):
    var=True
    cont=0
    while front_is_clear():
        move()
        giro270()
        move()
        turn_left() 
        cont=cont+1
        if object_here(): 
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_3(cont)
            break
        if cont==x:
            break
    return var      
"""
Descripcion:
Pre: Reeborg esta mirando hacia al Norte
Pos: Reeborg termina en posicion (direccion, pasos) simpre que el movimiento sea valido
"""
def mov_alfil(direc,pasos):
    if 1<=direc<=4 and 1<=pasos<8:
        print("Direccion:",direc)
        print("Pasos:",pasos)
        if direc == 1:
            zigzag_1(pasos)
        if direc == 2:
            zigzag_2(pasos) 
        if direc == 3:
            zigzag_3(pasos) 
        if direc == 4:
            zigzag_4(pasos)
    else:
        print("No cumple las condiciones iniciales")
        
mov_alfil(4,2)        
