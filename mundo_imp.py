cont =5
print(cont)
lista = [3, 5, 7]
print(lista)
if int(cont) == lista:
    cont = int (cont)
    for _ in range (cont):
        move()
def giro():
    repeat 2:
        turn_left()       
cont=1
while front_is_clear():
    cont +=1
    move()
    if wall_in_front():
        giro()
        break 
      
cont=int (cont/2)
print(cont)
for _ in range (cont):
    move()
put()
lista = [3,5,7,9,11,13,15,17,19]

if cont == lista:
    cont = int (cont)
    for _ in range (cont):
        move()
else:   
    cont = int (cont-1)
    for _ in range (cont):
        move()
        