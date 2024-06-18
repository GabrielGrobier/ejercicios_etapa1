'''
.- construya una función que permita calcular la edad del usuario según el año de nacimiento preguntado 
	Requisitos:
•	La función debe recibir el año de nacimiento como argumento.
•	La función debe devolver la edad calculada.


'''
#se construye una funcion con parametro que recibe la edad del usuario
def calcular_edad(anio):
    anio_actual =2024
    edad = anio_actual-anio
    #retorna el resultado que en este caso sera la edad 
    return edad



# se solicita el año de nacimiento del usuario 
anio = int(input("ingrese el año de nacimiento para calcular su edad : "))
#Se almacena el valor retornado por a funcion dentro una variable 
edad = calcular_edad(anio)
# se muestra el resultado solicitado 
print(f"su edad es {edad}")