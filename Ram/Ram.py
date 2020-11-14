n = int(input())

com1="load" #Comando 1
com2="unload" #Comando 2

ram = {}



for x in range(n):

    entrada = input()
    comando = entrada.split(" ")[0]

    if comando == com1 or comando == com1.upper() or comando == com1.capitalize():  #Compara si la entrada del comando es igual a load
        ''' Arg1 es la posicion de memoria'''
        arg1= entrada.split(" ")[1]
        #Arg2 es el numero de proceso
        arg2= entrada.split(" ")[2]

      
        if ram.get(arg1): #Compara si hay un registro o llave arg1 en RAM
            print("La posicion de memoria "+arg1+" ya estaba ocupada con el proceso "+ram[arg1])
        else:
            ram[arg1]=arg2
            print("La carga del proceso "+arg2+ " en la posicion de memoria "+arg1+" fue exitosa")
      
        
    elif comando == com2 or comando == com2.upper() or comando == com2.capitalize(): #Compara si la entrada del comando es igual a unload

        #Arg3 Posicion Memoria a liberar
        arg3 = entrada.split(" ")[1]
        if ram.get(arg3):

            ram.pop(arg3)

    else:
        print("Comando ingresado no correcto")
