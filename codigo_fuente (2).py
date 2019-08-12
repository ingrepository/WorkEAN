"""
Descripciòn:
El mundo requiere que el robot desplace hasta la casilla (5,5)
recorriendo todo el mundo en forma de zigzag debera tener en cuenta
si encuentra alguno de estos objetos 
Manzana (apple): Es el alimento de Reeborg, le proporciona la energía 
suficiente para desplazarse por su mundo. Una manzana le da la energía
para caminar hasta 7 casillas. Puede comerse hasta 3 manzanas seguidas
y puede recolectar las que no se coma.
Goloso (token): Se come todas las manzanas que Reeborg haya recolectado
hasta ese punto.
Tulipán (tulip): Le generan una fuerte alergia a Reeborg.
Le restan energía: cada movimiento le cuesta el doble. 
Se vuelve inmune cuando consigue la medicina.
Medicina (triangle): Es el antídoto cuando se enferma 
a causa de un Tulipán. También funciona como vacuna cuando
aún no se ha enfermado.  

 Autor: Sebastian Varon
 Fecha: 11/08/19
""" 
"""
Funcionalidad: Reeborg recorre una casilla y analiza los diferentes casos.
Pre: En la posicion actual de reeborg no debe haber una pared.
Pos: Reeborg se desplaza una posicion y verifica todos los casos
"""
def cada_paso ():
    global energia,cont,manzana,manza,tulipan,medicina,pasos,alergia
    if energia >= 1:        
        alergia=tulipan*2
        move()
        pasos=pasos+1
        energia=energia-alergia
        if alergia == 0:
            energia=energia-1
        if manzana>0:
            cont=cont+1
            if (manza > 0) and (cont >=7):
                print("En hora buena :) tienes reserva y has recorrido",cont,"pasos\nsin toparte con un goloso.")
                energia=energia+7
                manza=manza-1
                cont=0
                print("Energia repuesto sumada:",energia)
        print("Energia actual:",energia)
        if object_here("apple"):
            print("Encontre una manzana")
            manzana=manzana+1
            take("apple")
            if manzana <4:
                energia=energia+7
                print("Energia sumada:",energia)
            if manzana >3:
                manza=manza+1
                print("Manzanas recoloectadas:",manza)             
        if object_here("tulip"):
            print("Rayos!:( encontre un tulipan ahora tengo alergia")
            tulipan=tulipan+1
            take("tulip")
        if object_here("triangle"):
            print("Ostia! :) Encontre una medicina ahora sere inmune al tulipan")
            tulipan=0
            take("triangle")
        if object_here("token"):
            print("Rayos!:( encontre un goloso ahora perdere mis reservas")
            take("token")
            while manza>0:
                manza=manza-1
                put("apple")
                print("deje",manza+1,"manzana")
        if tulipan == 0:
            print("Reeboorg esta sano") 
        else:
            print("Reeborg tiene alergia x",tulipan)
    else:
       print("Suerte para la proxima!\nReeborg no tiene enegia suficiente para desplazarse\npor lo cual no podra llegar a la meta :(")
       #El break aqui no es valido , no encuentro la forma de cerrar el ciclo
"""
Funcionalidad: Reeborg recorre en sentido derecha.
Pre: En la posicion actual de reeborg debe estar mirando hacia este.
Pos: Reeborg se desplaza en linea recta y al terminar desplaza una 
posicion hacia el norte y queda mirando al oeste.
"""           
def mov_derecha ():
    if energia >= 1: 
        while not wall_in_front():
            cada_paso()  
        turn_left()
        cada_paso()
        turn_left()
    else:
        print("Suerte para la proxima!\nReeborg no tiene enegia suficiente para desplazarse\npor lo cual no podra llegar a la meta :(")
"""
Funcionalidad: Reeborg recorre en sentido izquierda.
Pre: En la posicion actual de reeborg debe estar mirando hacia oeste.
Pos: Reeborg se desplaza en linea recta y al terminar desplaza una 
posicion hacia el norte y queda mirando al este.
"""   

def mov_izquierda ():
    if energia >= 1: 
        while not wall_in_front():
            cada_paso()    
        repeat 3:
            turn_left()
        cada_paso()
        repeat 3:
            turn_left()
    else:
        print("Suerte para la proxima!\nReeborg no tiene enegia suficiente para desplazarse\npor lo cual no podra llegar a la meta :(")
energia=7
cont=0
manzana=0
manza=0
tulipan=0
medicina=0
pasos=0
alergia=0


mov_derecha()
mov_izquierda()
mov_derecha()
mov_izquierda()
mov_derecha()

print("Energia actual:",energia)
print("Total numero de pasos dado por Reboorg:",pasos)
