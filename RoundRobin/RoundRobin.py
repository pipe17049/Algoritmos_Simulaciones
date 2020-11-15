import queue
 
cantidad_procesos, quantum = input().split()
cantidad_procesos = int(cantidad_procesos)
quantum = int(quantum)
 
procesos = queue.Queue()
listos = queue.Queue()
 
 
for i in range(cantidad_procesos):
    id_proceso, tiempo_ejecucion, tiempo_llegada = input().split()
    tiempo_llegada = int(tiempo_llegada)
    tiempo_ejecucion = int(tiempo_ejecucion)
    
    procesos.put({"id_proceso": id_proceso,
                  "tiempo_llegada": tiempo_llegada,
                  "tiempo_ejecucion": tiempo_ejecucion})
 
listos.put(procesos.get())
 
tiempo = 0
 
while not procesos.empty() or not listos.empty():
    proceso_inicial = listos.get()
    tiempo+= min(quantum, proceso_inicial["tiempo_ejecucion"])
    
    #dependiendo del tempo, se mueven los procesos a listos para procesar por la cpu.
    while not procesos.empty():
        if procesos.queue[0]["tiempo_llegada"]<= tiempo:
            listos.put(procesos.get())
        else:
            break
 
        
    if proceso_inicial["tiempo_ejecucion"] <= quantum:
        print(proceso_inicial["id_proceso"], tiempo)
    else:
        proceso_inicial["tiempo_ejecucion"] = proceso_inicial["tiempo_ejecucion"] - quantum
        listos.put(proceso_inicial)