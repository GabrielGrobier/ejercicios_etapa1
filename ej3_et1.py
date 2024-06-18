'''
Ejercicio 3: Calcular Promedio de Calificaciones

 	Requisito 1: Calcular Promedio
Crea una función que reciba una lista de calificaciones y devuelva el promedio.

Requisito 2: Validar Entradas
Valida que las calificaciones estén entre 0 y 10.

'''
#construccion de lista para almacenar las notas 
notas= []

#funcion que permite calcular las notas 
def calcular_nota(notas,cantidad):
    sumanotas=0
    #recorre la lista de notas y comienza a sumarlas 
    for nota in notas:
        sumanotas = sumanotas+nota
    #cuando termina saca el promedio por la cantidad que el usuario coloco 
    promedio =sumanotas/cantidad
    return promedio


cantidad=int(input("cuantas notas desea agregar "))
for i in range(cantidad):
    nota = int(input(f"ingrese la {i+1} nota : "))
    while nota < 0 or nota >10:
        print("error , la nota debe ser entre 0 y 10  ")
        nota = int(input(f"ingrese la {i+1} nota : "))

    notas.append(nota)

promedio = calcular_nota(notas,cantidad)

print(f"el promedio es {promedio}")