autorizados=[]# creamos listas vacias para completarla con un diccionario

denegados=[]# creamos listas vacias para completarla con un diccionario

CONTRASENA = "reposo_estelar_1522"

opcion = True # variable para while

titulo = "  Gestión de Accesos  " # para imprimir el titulo de las opciones

#########################################################################################

def autorizar():
    global autorizados
    print("Por favor ingrese los siguientes datos: ")
    legajo = input("Legajo: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    autorizados.append({"legajo": legajo, "nombre": nombre, "apellido": apellido}) #abrimos lista para cargar datos
    print("los datos ingresados son: ", autorizados[-1])
    
def denegar():
    global denegados
    print("Por favor ingrese los siguientes datos:")
    legajo = input("Legajo: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    denegados.append({"legajo": legajo, "nombre": nombre, "apellido": apellido}) #abrimos lista para cargar datos
    print("ha ingresado", denegados[-1])

def mostrar():
    global autorizados 
    global denegados 
    listar = input("Ingrese:\n [1] para ver listado de autorizados.\n [2] para ver listado de denegados.\n Opción a ver: ")
    if listar =="1": 
        print ("la lista de autorizados es:", autorizados)
    elif listar =="2": 
        print ("la lista de denegados es:", denegados)
    else:
        print ("la opción elegida es inválida")

def borrar():
    global autorizados  # Se declara la variable en el ámbito global
    global denegados    # Se declara la variable en el ámbito global
    legajo = input("Por favor ingrese el legajo a borrar: ")
    encontrado = False
    
    for persona in autorizados:
        if persona["legajo"] == legajo:
            autorizados.remove(persona)
            encontrado = True
            print("Datos borrados de autorizados:", persona)
            break  # Salir del bucle después de encontrar y eliminar
    
    if not encontrado:
        for persona in denegados:
            if persona["legajo"] == legajo:
                denegados.remove(persona)
                encontrado = True
                print("Datos borrados de denegados:", persona)
                break  # Salir del bucle después de encontrar y eliminar
    
    if not encontrado:
        print("Por favor verifique el legajo ingresado. No se pudo encontrar en la base.")


def solicitar_contrasena():
    intento = 0
    while intento < 3:
        contrasena = input("Ingrese la contraseña para acceder al sistema: ")
        if contrasena == CONTRASENA:
            return True
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
            intento += 1
    print("Número máximo de intentos alcanzado. El programa se cerrará.")
    return False

#########################################################################################

if solicitar_contrasena():
    while opcion:
        print()
        print(titulo.center(40, "*"))
        print()
        print("""\
Ingrese la opción deseada:
[1] Otorgar accesos
[2] Denegar accesos 
[3] Imprimir lista de permitidos ó denegados
[4] Eliminar datos
[5] Salir del programa
""")
    
        seleccion = input("Opción seleccionada: ")

        match seleccion:
            case '1':
                autorizar()
            case '2':
                denegar()
            case '3':
                mostrar()
            case '4':
                borrar()
            case '5':
                opcion = False
                print("Gracias por usar el sistema de Gestión de Accesos")
            case _:
                print("Ha seleccionado una opción incorrecta")
                print("Por favor verifique el legajo ingresado. No se pudo encontrar en la base.")
else:
    print("Acceso denegado.")