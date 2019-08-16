"""
Descripción:
Reeborg dibuja lineas de estrellas en un mundo 10x10,
reeborg tiene estrallas ilimitadas.
Fecha: 16/08/2019
Autor: Sebastian Varon
"""
"""
Funcionalidad: Practicidad para girar 180 grados.
Pre:Valido
Pos:Realiza el giro de 180 grados.
"""
def turn_180():
    #Da giro de 180 grados
    repeat 2:
        turn_left()
"""
Funcionalidad: Practicidad para girar 270 grados.
Pre:Valido
Pos:Realiza el giro de 180 grados.
"""        
def turn_270():
    #Da giro de 270 grados
    repeat 3:
        turn_left()
"""
Funcionalidad: Practicidad para el uso del repeat.
Pre:Tener una acción(move,turn_left,etc) y numero de repeticiones.
Pos:Realiza la acción el numero de veces solicitado.
"""
def repeat(fn,n):
    #Realiza un ciclo un numero de veces definidas 
    #Una acción
    for i in range (n):
        fn()
"""
Funcionalidad: Practicidad para el uso del repeat.
Pre:Tener dos acciones(move,turn_left,etc) y numero de repeticiones.
Pos:Realiza la acción el numero de veces solicitado.
"""
def repeat1(fn, fn1, n):
    #Realiza un ciclo un numero de veces definidas 
    #Dos acciones
    for i in range (n):
        fn()
        fn1()
"""
Funcionalidad: Reeborg realiza un desplazamiento y coloca estrellas.
Pre:Reeborg mira sentido Este y mapa despejado sentido Norte
Pos:Reeborg va desde (1,1) hasta (1,y)
y pone en cada casilla una estrella hasta llegar 
a la posición (limit,y).
"""
        
def draw_a_line(y,limit): 
    print("Desplazandome...🏃👣")
    turn_left()
    #Practibilidad de funcion repeat:movemos
    repeat(move,y-1)
    put()
    #Da giro de 270 grados
    turn_270
    #Practibilidad de funcion repeat:movemos y colocamos obj
    repeat1(move,put,limit)
"""
Funcionalidad: Reeborg realiza un desplazamiento hasta llegar a (1,1).
Pre:Reeborg mira sentido este.
Pos:Reeborg va hasta la casilla (1,1) y mira en sentido Este..
"""
def go_back_home():
    turn_270()
    #Ciclo permite mover a reebort hasta topar con un obstaculo
    while front_is_clear():
        move()
    turn_270()
    #Ciclo permite mover a reebort hasta topar con un obstaculo
    while front_is_clear():
        move()
    #Da giro de 180 grados
    turn_180()
           
draw_a_line(3,0) 
go_back_home()
draw_a_line(4,3)
go_back_home()
draw_a_line(6,9)
go_back_home()
draw_a_line(8,4)
go_back_home()
draw_a_line(9,1)
go_back_home()



    

