import operator 

n , q = input().split(" ")

n= int(n)       # Numero de procesos
q = int(q)      # Numero de quantum

numproceso = []  # Donde se guarda los numeros de id de cada proceso
proceso = []    # Donde se guarda el burst time de cada proceso  
delay = []      # Donde se guarda los tiempos  de retardo o delay de la llegada de los procesos
cola = []       # Donde se guarda los procesos que quedan en la cola
ejecucion = []  # Donde se ejecuta el proceso en un tiempo quantum

tiempot = [0 for x in range(n)]  #Arreglo donde se guarda la salida del algoritmo


totaltiempo=0   # La suma de los tiempos de burst de todos los procesos

cont = 0        #contador tiempo de burst para hacer la comparacion
cont2 = 0         #contador auxiliar para recorrido de procesos nuevos de entrada



#Ingresar el numero de datos n que se tomo arriba y colocar 3 datos, #proceso , tiempo de burst , delay de llegada
for i in range(n):
   
    proc , tim , despl = input().split(" ")

    aux = int(proc)                 #Convertir variable proc en entero y guarda en aux
    aux1 = int(tim)                 #Convertir variable tim en entero y guarda en aux1
    aux2 = int(despl)               #Convertir variable despl en entero y guarda en aux2
   
    numproceso.append(aux)          #Agregar en arreglo numproceso el # del proceso
    proceso.append(aux1)            #Agregar en proceso el tiempo de burst
    delay.append(aux2)              #Agregar en delay el tiempo de retraso o delay
    totaltiempo+=aux1               #Acumulador Tiempo total de ejecucion (Suma todo los tiempo de burst)
    

for timep in range (totaltiempo+1):     #Ciclo for para el tiempo con la variable timep hasta que llege al acumulador + 1
    if len(ejecucion)==0:               #Pregunta si hay en ejecucion algun elemento
        ejecucion.append(cont2)             #Agrega a ejecucion el proceso que ingrese
        cont2+=1                            #Aumenta contador cont2 , que se encarga de la entrada de los procesos
    elif timep == delay[cont2]:         #Pregunta si el tiempo transcurrido total es igual al delay del proceso que sigue

        cola.append(cont2)                  #Agrega a la cola el proceso que llego
        cont2+=1                            #Aumenta contador cont2 , que se encarga de la entrada de los procesos
        if cont2==n: cont2=0                #Si cont2 llega al numero de elementos n, resetear
    
    else: None



    #Caso cuando el tiempo que requiere el proceso en ejecucion es menor que el quantu
    if cont>=0 and cont < q and cont>=proceso[ejecucion[0]]:             #Compara si la variable cont esta entre 0 y el quantum y si es igual al tiempo de proceso
        tiempot[ejecucion[0]]=timep                                     #Manda el tiempo que lleva transcurrido desde que llego al arreglo tiempot
        if len(cola)>0:                                                 #Compara si hay elementos en cola
            ejecucion[0]=cola.pop(0)                                        #Elimina el proceso del sistema y pasa el primero de la cola a ejecucion
        cont=1                                                          #Resetea contador que es el que compara quantum a 1

    #Caso cuando el contador de quantum es igual al quantum
    elif cont == q:                                                     #Compara si cont es igual a quantum
        proceso[ejecucion[0]]-=q                                        #Resta en proceso el tiempo que se ejecuto
        if proceso[ejecucion[0]] == 0:                                  #Compara si proceso ejecucion despues de la resta llego a ceo
            tiempot[ejecucion[0]]=timep                                     #Manda el tiempo que lleva transcutrrido desde que llego al arreglo tiempot
            if len(cola)>0:                                                 #Compara si la cola no esta vacia
                ejecucion[0]=cola.pop(0)                                        #Elimina el proceso del sistema y pasa el primero de la cola a ejecucion
        else:               
            aux3 = ejecucion[0]                                             #Guardo el No proceso en ejecucion a la variable aux3
            if len(cola)>0:                                                 #Compara si hay elementos en cola

                ejecucion[0]=cola.pop(0)                                        #Para el primer elemento en cola a ejecucion
                cola.append(aux3)                                               #Pasa el proceso que termino tiempo al final de la cola
            
        cont=1                                                              #Reset contador quantum
    else:
        cont+=1                                                         #Si no es ningun caso aumenta el tiempo de contador quantum
    
#Convertir 2 listas ( numproceso es donde guardo los # de proceso y tiempot son las salidas del algoritmo)
diccionario = dict(zip(numproceso,tiempot))
#Organizacion del diccionario por los valores 
diccionario2 =  sorted(diccionario.items(), key=operator.itemgetter(1))

for name in enumerate(diccionario2):
    print(name[1][0],diccionario[name[1][0]])
