
n = int(input())

carpeta_mark="Mark"
diccionario_carpetas={}
diccionario_carpetas[carpeta_mark] = {}

ubicacion_actual="/"+ carpeta_mark


        

for i in range(n):
    instruccion , argumento = input().split(" ")

    if instruccion == 'cd':
        if argumento == "..":
            ubicacion_actual="/" .join(ubicacion_actual.split("/")[:-1]) 
        else:
            ubicacion_actual= ubicacion_actual+"/"+argumento
    else: print("ER")
        

