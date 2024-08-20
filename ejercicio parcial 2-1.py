# Definir la clase para el nodo de la lista
class Nodo:
    def __init__(self, nombre, edad, tipoEmpleo, sueldo, sexo):
        # Cada nodo tiene un dato y una referencia al siguiente nodo
        self.nombre = nombre
        self.edad = edad
        self.tipoEmpleo = tipoEmpleo
        self.sueldo = sueldo
        self.sexo = sexo
        self.siguiente = None

# Inicializar la cabeza de la lista como None
cabeza_lista = None


contador = 0
contadorA = 0
contadorI = 0
contadorT = 0



# Bucle para permitir al usuario ingresar datos hasta que desee parar
while True:
    
    print("opciones del sistema")
    opc = input('''1: agregar usuario
2: salir: ''')
    opc = int(opc)
    
    if opc == 1:
    # Solicitar al usuario que ingrese un dato
     dato_nombre = input("Ingrese el nombre (o 'stop' para detenerse): ")
     dato_edad = input("Ingrese su edad (o 'stop' para detenerse): ")
     dato_tipoEmpleo = input('''que empleo tienes? 
            1) administrativo
            2) ingeniero
            3) tecnologico
            (o 'stop' para detenerse): ''')
     dato_sexo = input("Ingrese su sexo  (o 'stop' para detenerse): ")
     dato_sueldo = input("Ingrese su sueldo (o 'stop' para detenerse): ")
     contador += 1
    

     
    if dato_tipoEmpleo == "1":
        dato_tipoEmpleo = "administrativo"
        contadorA += 1
    if dato_tipoEmpleo == "2":
        dato_tipoEmpleo = "ingeniero"
        contadorI += 1
    if dato_tipoEmpleo == "3":
        dato_tipoEmpleo = "tecnologico"
        contadorT += 1
   
  
        
    # Verificar si el usuario desea detenerse
    if opc == 2:
     break
    
    elif opc >= 1000:
     print("no es una opccion valida")


    # Crear un4
    # 1nuevo nodo con el dato ingresado
    nuevo_nodo = Nodo(dato_nombre, dato_edad, dato_sueldo, dato_tipoEmpleo, dato_sexo)

    # Enlazar el nuevo nodo al final de la lista
    if cabeza_lista is None:
        # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
        cabeza_lista = nuevo_nodo
    else:
        # Si la lista no está vacía, buscar el último nodo y enlazar el nuevo nodo
        nodo_actual = cabeza_lista
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo

# Imprimir la lista enlazada

# Inicializar el nodo actual al principio de la lista
nodo_actual = cabeza_lista

# Recorrer la lista e imprimir cada dato de nodo
print("Lista enlazada creada:")
while nodo_actual:
    print("nombre: " + nodo_actual.nombre, end=" -> ")
    print("edad: " + nodo_actual.edad, end=" -> ")
    print("sexo: " + nodo_actual.sexo, end=" -> ")
    print("empleo: " + nodo_actual.sueldo, end=" -> ")
    print("sueldo: " + nodo_actual.tipoEmpleo, end=" ->  \n")
    
    
    # Avanzar al siguiente nodo
    nodo_actual = nodo_actual.siguiente

# Imprimir "None" al final de la lista
print(f"cuatos adminostradores hay: {contadorA}")
print(f"cuatos ingenieros hay: {contadorI}")
print(f"cuatos tecnologicos hay: {contadorT}")

nuevo_nodo_sueldo = Nodo(dato_sueldo)

print(nuevo_nodo_sueldo)

