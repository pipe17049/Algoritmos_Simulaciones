
n = int(input())

carpeta_mark="Mark"
diccionario_carpetas={}
diccionario_carpetas[carpeta_mark] = {}

ubicacion_actual="/"+ carpeta_mark

def imprimir ( directorio_padre, directorios , nivel ):
    
    print(directorio_padre +":") 
    for directorio_hijo in directorios:
        print("--"*(nivel+1), end="")
        imprimir(directorio_hijo,directorios[directorio_hijo],nivel+1)
  
        

for i in range(n):
    instruccion , argumento = input().split(" ")

    if instruccion == 'cd':
        if argumento == "..":
            ubicacion_actual="/" .join(ubicacion_actual.split("/")[:-1]) 
        else:
            ubicacion_actual= ubicacion_actual+"/"+argumento
    else: print("ER")
        

imprimir("Mark",diccionario_carpetas["Mark"],0)