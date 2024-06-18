'''
Ejercicio Nombre Apellido :
Requisito 1 
construya una función que permita recibir nombre y apellido solicitado al usuario guardar cada uno de estos en una lista independiente 
Requisito 2
Poder buscar por nombre para luego mostrar nombre y apellido  


'''
#construir listas vacias para almacenar datos 
nombres=[]
apellidos=[]

#construir funciones con parametro que almacene informacion dentro de las listas correspondiente 
def guardar_nombre(nombre,apellido):
    #se entrega variable de la funcion para que se almacene en la lista 
    nombres.append(nombre)
    apellidos.append(apellido)
    #se muestra en pantalla que el dato quedo almacenado correctamente 
    print("Datos almacenado correctamente ")

#funcion que permite bucar datos 
def buscar_dato(nombre):
    #se comprueba que el dato ingresado existe dentro de la lista 
    if nombre in nombres:
        #si este existe entonces se obtiene su posicion(indice)
        indice= nombres.index(nombre)
        #Como el apellido fue guardado al mismo momento que el nombre estan en la misma posicion 
        #por lo cual se pued obtener con la posicion del nombre 
        apellido = apellidos[indice]
        #se muestra en pantalla que el dato fue encontrado 
        print("dato encontrado ")
        print(f"{nombre} su apellido es {apellido}")

#construccion del menu con un while True 
while True :
    print(
        '''
        1.- Ingresar dato 
        2.- buscar dato 
        3.- salir 

        ''')
    #se valida la opcion escogida
    op = int(input("ingrese una opcion : "))
    if op == 1:
        #se solicita los datos al usuario para ser almacenados 
        nombre_recibido = input("ingrese el nombre que desea guardar : ")
        apellido_recibido = input("Ingrese el apellido  : ")
        # se ejecuta la funcion construida al principio y se pasan como parametros la respuesta del usuario 
        guardar_nombre(nombre_recibido,apellido_recibido)
    if op ==2:
            nombre_solicitado= input("Escriba el nombre que desea buscar : ")
            # se ejecuta la funcion construida al principio y se pasan como parametros la respuesta del usuario 
            buscar_dato(nombre_solicitado)
    if op ==3:
         break

        
        
