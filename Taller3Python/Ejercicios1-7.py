        #jr 2
def Dados():
    import random
    num_secreto =random.randint(1,6)
    print("¿Cual será el npumero Secreto? 🤫")
    numeroA= 0
    NumeroB = 0
    print("     Es turno de Alvaro")
    print("prueba tu suete")
    while numeroA != num_secreto and NumeroB != num_secreto:
        numeroA=int(input("-->"))
        if numeroA == num_secreto:
            print("🎉Felicidades Alvaro! El numero secreto es:",num_secreto)
        if numeroA < num_secreto:
            print("el numero es mayor ⬆️")
        elif numeroA > num_secreto:
            print("El numero es menor ⬇️")
            print("Siguiente jugador")
        print("-----------------")
        print("     turno de Barbara")
        print("prueba tu suete")
        NumeroB=int(input("-->"))
        if NumeroB==num_secreto:
            print("🎉Felicidades Barbara! El numero secreto es:",num_secreto)
        if NumeroB < num_secreto:
            print("el numero es mayor ⬆️")
        elif NumeroB > num_secreto:
            print("El numero es menor ⬇️")
        else:
            print("Siguiente jugador")

        
        

        # jr 3
def alum_sexo ():
    print("Ingresa el nombre del alumn")
    nom_alumno= input("--> ")
    print(f"El sexo de {nom_alumno} es (M o F) ")
    sexo_alumno=input("--> ")
    if sexo_alumno=="f":
        if nom_alumno <= "m":
            print (f"{nom_alumno} Pertenece al grupo A")
        else:
            print(f"{nom_alumno} Pertenece al grupo B")
    else:
        if nom_alumno >= "m":
            print(f"{nom_alumno} Pertenece al grupo A")
        else:
            print(f"{nom_alumno} Pertenece al grupo B")
        #jr 4 Sala de Juegos
def Juegos():
    print("Bienvenido, por favor ingresa tu edad")
    User_edad=int(input("-- > "))
    if User_edad < 4:
        print ("La entrada para ti es gratis")
    elif User_edad > 4 and User_edad < 18:
        print(f"Con {User_edad} años debes pagar: 30.000")
    else:
        print(f"Con {User_edad} años debes pagar: 50.000")

        #jr 5 Contraseña
def Contraseña():
    Clave_correcta="12345"
    Clave_ingresada=0
    while Clave_ingresada != Clave_correcta:
        print("Ingresa tu contraseña")
        Clave_ingresada= input("-- >")
        if Clave_ingresada != Clave_correcta:
            print(f"{Clave_ingresada} No es la contraseña correcta")
        else:
            print("La contraseña es correcta")

def Iva():
    print("Ingresa el valor del producto")
    Precio_produc=float(input("--> "))
    print("¿Tienes el Iva del producto? (s/n)")
    true=input("--> ")
    if true == "s":
        print("Ingresa el iva")
        IVA=int(input("--> "))
        print(f"el precio del producto con el {IVA}% de iva es de: ",(Precio_produc*IVA)/100)
    else:
        print("por defecto se aplicara el 19% de iva a tu producto")
        print("el precio del producto es de: ", (Precio_produc*21)/100 )
        
        
        
def Menu():
    print("Nuestros programas son los siguientes")
    print("-------------------------")
    print("1. Dados")
    print("-------------------------")
    print("2. Clasificación de alumnos")
    print("-------------------------")
    print("3. Arcade")
    print("-------------------------")
    print("4. Contraseña")
    print("-------------------------")
    print("5. Iva")
    print("-------------------------")
    print("6.Abandonar")
    print("-------------------------")
    print("Digita el numero con la opción ")
    
    
    
    Juego_elegido=int(input("--> "))
    if Juego_elegido==1:
        print("Quieres jugar a los dados? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("ingreso realizado")
            print("-------------------------")
            Dados()
        else:
            print("Regresemos al menú")
            Menu()

    elif Juego_elegido==2:
        print("Quieres Clasificar a tus alumnos? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("ingreso realizado")
            print("-------------------------")
            alum_sexo()
        else:
            print("Regresemos al menú")
            Menu()

    elif Juego_elegido==3:
        print("Quieres ir al arcade? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("ingreso realizado")
            print("-------------------------")
            Juegos()
        else:
            Menu()
            
    elif Juego_elegido==4:
        print("Mirar tu contraseña? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("ingreso realizado")
            print("-------------------------")
            Contraseña()
        else:
            print("Regresemos al menú")
            Menu()
            
    elif Juego_elegido==5:
        print("Algún producto que registrar? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("ingreso realizado")
            print("-------------------------")
            Iva()
        else:
            print("Regresemos al menú")
            Menu()
            
    else:
        print("Deseas salir? s/n")
        confirmación=input("---> ")
        if confirmación=="s":
            print("Salida exitosa")
            print("")
            print("Hasta la proxima ejecución")
            print("")
        else:
            print("Regresemos al menú")
            Menu()
            
Menu()


