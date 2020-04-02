import time
import os

try:
       
    def Introducir_datos_provincia(lista_provincias):
        provincia=input("Introduce el nombre de la provincia : ")

        lista_provincias.append(provincia)

        return(lista_provincias)
        
    def Introducir_casosconfirmados(lista_casosconfirmados):
      
        casosconfirmados=input ("Introduce el numero de casos confirmados: ")
        lista_casosconfirmados.append(casosconfirmados)
        return(lista_casosconfirmados)
    def Introducir_casosnuevos(lista_casosnuevos):
          
        casosnuevos=input ("Introduce el numero de nuevos casos: ")
        lista_casosnuevos.append(casosnuevos)
        return(lista_casosnuevos)   
    
    def Visualizar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos):
        n_elementos_lista=len(lista_provincias)
        print("El número de elementos de la lista según la función len es", n_elementos_lista)
        print("Provincia ,Casos confirmados y Nuevos")
        print("--------------------------------")
        for indice in range(0,n_elementos_lista):
            
            print(lista_provincias[indice],"\t",lista_casosconfirmados[indice], lista_casosnuevos[indice])
        
        input("\nPulse una tecla para continuar ....")

    def Buscar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos):
        prov=input("Introduce el nombre de la provincia: ")
        if prov in lista_provincias: 
            indice=lista_provincias.index(prov)
            print("En la provincia: ", prov, "hay ",lista_casosconfirmados[indice],"casos confirmados","y",lista_casosnuevos[indice],"casos nuevos hoy")
        else: 
            print("La provincia no existe en la base de datos, o igual esta la primera letra en MAYUS o el nombre entero en MAYUS o minus")
        input("\nPulse una tecla para continuar ....")

    def Modificar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos):

        provincia=input("Introduce el nombre de la provincia: ")
        if provincia in lista_provincias: 
   
            casosnuevos_hoy=int(input("Introduce el numero de casos confirmados de hoy: "))
            casostotales_hoy=int(input("Introduce el numero de casos totales a dia de hoy: "))
            indice=lista_provincias.index(provincia)
            lista_casosconfirmados[indice]=casostotales_hoy
            lista_casosnuevos[indice]=casosnuevos_hoy
            print("el nuevo numero de casos confirmados en: ", provincia, " es",lista_casosconfirmados[indice],"de los cuales hoy han sido",lista_casosnuevos[indice])
        else: 
            print("La provincia no esta en la lista")
        input("\nPulse una tecla para continuar ....")



    lista_provincias=[]
    lista_casosconfirmados=[]
    lista_casosnuevos=[]
     
    while True:
        os.system ("cls")  
        print("Situación epidemiológica del coronavirus (COVID-19) en Castilla y León ")
        print ("Actualización diaria. Datos a ",time.strftime("%d/%m/%y"))
        print("\t1.- Introduce datos (provincia, confirmados y nuevos)")
        print("\t2.- visualizar datos(provincia, confirmados y nuevos)")
        print("\t3.- Numero Total de casos Confirmados y Nuevos en la provincia ")
        print("\t4.- Modificar el numero de casos (confirmados y nuevos)")
        print("\t5.- Salir")
        opcion=int(input("Introduce la opcion que deseas :"))
        if opcion==1:
           
            lista_provincias=Introducir_datos_provincia(lista_provincias)
            lista_casosconfirmados=Introducir_casosconfirmados(lista_casosconfirmados)
            lista_casosnuevos=Introducir_casosnuevos(lista_casosnuevos)
            
        elif opcion==2:
            Visualizar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos)
        elif opcion==3:
            Buscar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos)
        elif opcion==4:
            Modificar_datos(lista_provincias,lista_casosconfirmados,lista_casosnuevos)
        else:
            break

    
except ValueError:
    print("ERROR AL CONVERTIR A ENTERO.")
except Exception as e: # OJO SIEMPRE LA ULTIMA
    print(" error no previsto del tipo ", type(e).__name__ )