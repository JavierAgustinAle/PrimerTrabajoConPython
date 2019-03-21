import subprocess


#Variables
producto1 = "Cafe solo"

producto2 = "Cafe con leche"

producto3= "Chocolate"

precio1= 1.00

precio2= 1.10

precio3= 1.30

opcion= "1"

total= 0

#bucle de repeticion del programa

while(opcion != 0 ):
    subprocess.call(["cmd.exe", "/C", "cls"])
    print(f"Seleccione una opcion del menu      Importe actual: {total:.2f} pesos \n")
    print("\t1.", producto1 )
    print("\t2.",producto2)
    print("\t3.",producto3)
    print("\t0. Salir")
    opcion = input(" Haga su eleccion: ")

    if (opcion=="1"):
        print(f"\n Ha elegido {producto1} que vale {precio1} pesos")
        total += precio1

    elif (opcion=="2"):
        print(f"\n Ha elegido {producto2} que vale {precio2} pesos")
        total += precio2

    elif (opcion=="3"):
        print(f"\n Ha elegido {producto3} que vale {precio3} pesos")
        total += precio3

    elif(opcion=="0"):
        print(f"\n\n Compra finalizada por valor de {total} pesos")
        break
    else:
        print("\n Opcion no valida")







