
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
while front_is_clear():
    move()
