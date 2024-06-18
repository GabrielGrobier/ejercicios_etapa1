'''
Ejercicio 4: Gestión de Tareas
 Requisito 1: Añadir Tarea
Crea una función que permita al usuario añadir tareas a una lista.
Requisito 2: Mostrar Tareas
Crea una función que muestre todas las tareas a un diccionario .
Esto debe ser manejado desde un menú :


'''
tareas={

}
def agregar_tarea(nombreTarea, descripcion):
    tareas[nombreTarea]=descripcion
    print("tarea agregada ")

def mostrar_tareas(tareas):
    for tarea in tareas:
      print(tarea)


print(
   '''
    1.- agreagr tarea
    2.- mostrar tareas 

    '''    )
op = int(input("que desea hacer : "))
if op ==1:
   nombre=input("ingrese el nombre de la tarea ")
   descripcion= input("ingrese detalle de la tarea ")
   agregar_tarea(nombre,descripcion)
if op ==2:
   mostrar_tareas(tareas)

   