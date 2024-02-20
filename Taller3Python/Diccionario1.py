Frutas ={

}
Frutas["Nombre de la fruta"]="1. manzana", "2. pera", "3. mango", "4. durazno"
Frutas["Precio"]=2000,1800,900,1200,700


def Consultas():
    print("Estas son las frutas con sus nombres")
    for clave,valor in Frutas.items():
        print(clave + ":" , valor)
    print("")
    print("ingresa el número de la fruta que desea comprar")
    fruta=int(input("--> "))
    
    
    if fruta==1:
        print("Llevaras manzanas")
        print("¿Cuantas desea llevar?")
        
        cantidad=int(input("--> "))
        precio_final=2000*cantidad
        print(f"Elcosto total por llevar {cantidad} manzanas(s) es de: ",precio_final)
        print("¿Cuantas desea llevar?")
        
        print("¿realizar otra consulta? (s/n)")
        nueva_consulta=input("--> ")
        
    elif fruta==2:
        print("llevaras peras")
        
        cantidad=int(input("--> "))
        precio_final=1800*cantidad
        print(f"Elcosto total por llevar {cantidad} pera(s) es de: ",precio_final)
        print("¿realizar otra consulta?")
        nueva_consulta=input("--> ")
        
    elif fruta==3:
        print("llevaras mangos")
        print("¿Cuantas desea llevar?")
        cantidad=int(input("--> "))
        precio_final=900*cantidad
        print(f"Elcosto total por llevar {cantidad} mango(s) es de: ",precio_final)
        print("¿realizar otra consulta?")
        nueva_consulta=input("--> ")
        
    elif fruta==4:
        print("llevaras duraznos")
        print("¿Cuantas desea llevar?")
        cantidad=int(input("--> "))
        precio_final=700*cantidad
        print(f"Elcosto total por llevar {cantidad} durazno(s) es de: ",precio_final)
        print("¿realizar otra consulta?")
        nueva_consulta=input("--> ")
        
    else:
        print("la opcion no esta contemplada")
        print("¿realizar otra consulta?")
        nueva_consulta=input("--> ")
        if nueva_consulta=="s":
            Consultas()
        else:
            ("hasta una proxima ejecución")
            
    
Consultas()