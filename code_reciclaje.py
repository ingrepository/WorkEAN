"""
Descripción: Reeborg debera limpiar la cuadra, debe
reciclar los elementos encontrados en la basura,
si es comida imprimira "Para compostaje" y si no
debera imprimir "Para reciclaje", posteriormente debe
regresar a la posición (1,1).
Objetos que acepta en mapa:"token""apple""banana"
"carrot""square""star""strawberry""triangle"
Autor:Sebastian Varon
"""
"""
Funcionalidad:Reeborg recoja el objeto y lo clasifica,
si es residuo de comida o cualquier otro elemento.
Pre: Haber un objeto en la posición actual.
Pos: Recoge el objeto y retorna un True o False
"""
def reciclar():
    ob=object_here()
    for obj_name in (ob):
        if object_here("apple") or object_here("banana") or object_here("strawberry") or object_here("carrot"): 
            print("He encontrado un/a:",obj_name)
            take(obj_name)
            return False
        if object_here("token") or object_here("triangle") or object_here("square") or object_here("star"):
            print("He encontrado un/a:",obj_name)
            take(obj_name)
            return True        
"""
Funcionalidad:Que desplaza a reeborg hasta la posición (1,1).
Pre:No haber obstáculo detrás de reeborg.
Pos:Da un giro de 180°grados y se desplaza hasta tener 
un obstáculo en frente
"""
def volver_a_casa():
    repeat 2:
        turn_left()
    while front_is_clear():
        move()
"""
Funcionalidad:Que desplaza a Reeborg hasta el primer 
elemento que encuentre.
Pre:No haber obstáculo en frente
Pos:Imprime la clasificicaion del elemento "compostaje" o "reciclaje"
y se desplaza una posición.
"""
def buscar_basura():
    print("Bienvenido Reeborg limpiara la cuadra:")
    print("Desplazandome...🤖👣")
    while front_is_clear():
        move()
        while object_here():
            if reciclar() == False:
                print("Para compostaje")
            else:
                print("Para reciclar")
    print("Volviendo al punto de partida...🏁")
    volver_a_casa()
    print("¡Meta alcanzada!")
buscar_basura()
