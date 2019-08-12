
energia=7
cont=0
manzana=0
manza=0
tulipan=0
medicina=0
goloso=0
pasos=0
while not wall_in_front():
    if energia >= 1:
        print("tulipan:",tulipan)
        move()
        pasos=pasos+1
        energia=energia-tulipan
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
            if tulipan >1:
                tulipan=tulipan*2
        if object_here("triangle"):
            print("Ostia! :) Encontre una medicina ahora sere inmune al tulipan")
            tulipan=0
            take("triangle")
        if object_here("token"):
            print("Rayos!:( encontre un goloso ahora perdere mis reservas")
            goloso=1+1
            take("token")
            while manza>0:
                manza=manza-1
                put("apple")
                print("deje",manza+1,"manzana")
        if tulipan == 0:
            print("Reboorg esta sano") 
        else:
            print("Reboorg tiene alergia x",tulipan)
       
print("Total numero de pasos dado por Reboorg:",pasos)
print("Energia actual:",energia)



      

      
      
