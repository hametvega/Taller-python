#from statistics import multimode


Lista_de_numeros=[]
cantidad=0
borrarse=()
def añadir_numero():
    Repetir_ciclo=int(input("cunatos numeros deseas guardar "))
    for x in range (Repetir_ciclo):
        print("Ingresa el numero que deseas guardar:")
        numero=int(input("--->  "))
        Lista_de_numeros.append(numero)
    borrarse=numero
    
    print("los numeros de la lista son")
    print(Lista_de_numeros)
    print("-------------------")
    print("Deseas guardar más números (s/n)")
    Desición=input("--> ")
    if Desición=="s":
        añadir_numero()
    
def Borrar_ultimo(Lista_de_numeros,ultimo):
    ultimo_tabla=len (Lista_de_numeros)
    ultimo_tabla-=1
    print("¿desea borrar un numero de la lista? (s/n)")
    pregunta=input("--> ")
    if pregunta=="s":
        print("De no conocer la posición se borrara el ultimo numero")
        borrar=print("¿Borrar un número en especifico? (s/n)")
        input("---> ")
        if borrar=="s":
            print(Lista_de_numeros)
            cantidad=len(Lista_de_numeros)
            print(f"La posición minima es 1 y la pisición maxima es {cantidad}")
            posición=int(input("--> "))
            if posición < 1 or posición > cantidad:
                print("la posición esta fuera del rango")
            posición-=1
        elif borrar!="s":
            print("se borrara el ultimo numero de la lista")
            del Lista_de_numeros[ultimo_tabla]
    print(Lista_de_numeros)
    

def Posición_y_número():
    print("Esta es la lista con sus datos")
    print(Lista_de_numeros)
    cantidad=len(Lista_de_numeros)
    print("-------------------")
    print("Digita primero la posición donde quedara el dato")
    print(f"La posición minima es 1 y la pisición maxima es {cantidad}")
    posición=int(input("--> "))
    if posición < 1 or posición > cantidad:
        print("la posición esta fuera del rango")
    posición-=1
    print("-------------------")
    print("Digita el dato que deseas añadir")
    nuevo_dato=int(input("-->"))
    Lista_de_numeros.insert(posición,nuevo_dato)
    print("-------------------")
    print("Esta es la lista modificada")
    print(Lista_de_numeros)
    reinicio=input("¿Desea segur modificando la lista? (s/n)")
    if reinicio=="s":
        Posición_y_número()

    
    
    
    
    
def Candtidad_de_datos():
    long_datos= len (Lista_de_numeros)
    
    print("la cantidad de datos que tienes guardados son")
    print (long_datos)

def contar_repetidos(Lista_de_numeros):
    print("ingresa un numero para saber si esta repetido")
    input("---> ")
    repetidos=[]
    archivo=[]
    cont_repe=0
    for n in Lista_de_numeros:
        if n not in archivo:
            archivo.append(n)
            cont_repe+=1
        else:
            repetidos=n
        
    print(f"el numero {repetidos} esta {cont_repe} veces en la lista")
        
    
    
print ("Esta es la lista final",Lista_de_numeros)
    
def menu():
    print("bienedo al menu")
    print("¿que desea hacer?")
    print("")
    print("1. Añadir numeros")
    print("")
    print("2. añadir numero en una posición especifica")
    print("")
    print("3. saber la cantidad de datos guardados")
    print("")
    print("4. Eliminar numeros de la lista")
    print("")
    print("5. Saber cuantas veces se repite un dato")
    print("")
    print("Ingresa el numero con la opción")
    print("6. Abandonar")
    Desición=input("--> ")
    if Desición==1:
        print("1. Añadir numeros")
        añadir_numero()

    elif Desición==2:
        print("2. añadir numero en una posición especifica")
        Posición_y_número()

    elif Desición==3:
        print("3. saber la cantidad de datos guardados")
        Candtidad_de_datos()


    elif Desición==4:
        print("4. Eliminar numeros de la lista")

        Borrar_ultimo(Lista_de_numeros,borrarse)
            
    elif Desición==5:
        print("5. Saber cuantas veces se repite un dato")

        contar_repetidos(Lista_de_numeros)
    else:
        print("Gracias hasta una proxima ejecución")
        print("")
        
    
    
menu()


