#EJERCICIO 1
def números_primos(número):
    for i in range(1,número+1):
        div1 = i%2
        div2 = i%3
        div3 = i%5
        div4 = i%7
        if div1!=0 and div2!=0 and div3!=0 and div4!=0:
            print(i)

número=int(input("Ingrese un número:    "))
print("Voy a mostrarle un los números primos entre el 1 y su número")
números_primos(número)

#Ejercicio 2
def Preparaciòn():
    entrada=str(input("Ingrese un condimento:    "))
    while entrada != "salir":
        print("El condimento",entrada,"ha sido agregado")
        entrada=str(input("Ingrese un condimento o salir:    "))
    
#Ejercicio 3
def hacer_remera(talle,mensaje=""):
    print("Se va a crear una remera de talle",talle,"que diga",mensaje)

talle=str(input("Ingrese un talle:  "))
mensaje=str(input("Ingrese un mensaje que le gustarìa que contenga la remera:   "))
hacer_remera(talle,mensaje)

hacer_remera(talle=str(input("Ingrese un talle:  ")),mensaje=str(input("Ingrese un mensaje que le gustarìa que contenga la remera:   ")))

#Ejercicio 4
def fibonacci(n):
    n1=1
    n2=1
    while True:
        print(0)
        print(1)
        print(1)
        for i in range(n-3):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)
        break

n=int(input("Ingrese la cantidad de números de Fibonacci:   "))
fibonacci(n)


#Ejercicio 5
print("Bienvenido a una de las máquinas de la red Banelco de operaciones bancarias.") 
NyA = str(input("Ingrese su Nombre y Apellido:  "))
DNI1 = int(input("Ingrese su número de DNI:  "))
FdN = str(input("Ingrese su fecha de nacimiento:    "))
MdlC = int(input("Ingrese el monto de la compra:    "))
print("______________________________________________________________")
print("")
print("                      MENÚ DE OPERACIONES")
print("Ingrese 1 para calcular su CUIL")
print("Ingrese 2 para saber su fecha de cumpleaños")
print("Ingrese 3 si quiere saber el valor final de su compra(SU COMPRA+IVA)")
print("Ingrese 'SALIR' para salir del menú")
opción = int(input("OPCIÓN: "))

def menú_de_operaciones_bancarias(NyA,DNI,FdN,MdlC):
    if opción==1:
        print("Su CUIL es XY",DNI,"D")
        género = int(input("Presione 1 si es HOMBRE o 2 si es MUJER:     "))
        if género == 1:
            mul1=2*5
            mul2=0*4
            mul3=(DNI//10000000)*3
            DNI = DNI-10000000
            mul4=(DNI//1000000)*2
            DNI = DNI-1000000
            mul5=(DNI//100000)*7
            DNI = DNI-100000
            mul6=(DNI//10000)*6
            DNI = DNI-10000
            mul7=(DNI//1000)*5
            DNI = DNI-1000
            mul8=(DNI//100)*4
            DNI = DNI-100
            mul9=(DNI//10)*3
            DNI = DNI-10
            mul10=(DNI//1)*2
            suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9 + mul10
            div = suma%11
            resta = 11-div
            print("Su CUIL es 20 -",DNI1,"-",resta)
        elif género==2:  
            mul1=2*5
            mul2=7*4
            mul3=(DNI//10000000)*3
            DNI = DNI-10000000
            mul4=(DNI//1000000)*2
            DNI = DNI-1000000
            mul5=(DNI//100000)*7
            DNI = DNI-100000
            mul6=(DNI//10000)*6
            DNI = DNI-10000
            mul7=(DNI//1000)*5
            DNI = DNI-1000
            mul8=(DNI//100)*4
            DNI = DNI-100
            mul9=(DNI//10)*3
            DNI = DNI-10
            mul10=(DNI//1)*2
            suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9 + mul10
            div = suma%11
            resta = 11-div
            print("Su CUIL es 27 -",DNI1,"-",resta)
    elif opción==2:
        print("Su fecha de cumpleaños es el",FdN)
    elif opción==3:
        porcentaje=MdlC/100
        porcentaje2=porcentaje*21
        suma=MdlC+porcentaje
        print("El valor de su compra más el IVA es de",suma)

menú_de_operaciones_bancarias(NyA,DNI1,FdN,MdlC)

#Ejercicio 6
print("Bienvenido a una de las máquinas de la red Banelco de operaciones bancarias.") 
NyA = str(input("Ingrese su Nombre y Apellido:  "))
DNI1 = int(input("Ingrese su número de DNI:  "))
FdN = str(input("Ingrese su fecha de nacimiento:    "))
MdlC = int(input("Ingrese el monto de la compra:    "))
print("______________________________________________________________")
print("")
print("                      MENÚ DE OPERACIONES")
print("Ingrese 1 para calcular su CUIL")
print("Ingrese 2 para saber su fecha de cumpleaños")
print("Ingrese 3 si quiere saber el valor final de su compra(SU COMPRA+IVA)")
print("Ingrese 'SALIR' para salir del menú")
opción = int(input("OPCIÓN: "))

def menú_de_operaciones_bancarias(NyA,DNI,FdN,MdlC):
    if opción==1:
        print("Su CUIL es XY",DNI,"D")
        género = int(input("Presione 1 si es HOMBRE o 2 si es MUJER:     "))
        if género == 1:
            mul1=2*5
            mul2=0*4
            mul3=(DNI//10000000)*3
            DNI = DNI-10000000
            mul4=(DNI//1000000)*2
            DNI = DNI-1000000
            mul5=(DNI//100000)*7
            DNI = DNI-100000
            mul6=(DNI//10000)*6
            DNI = DNI-10000
            mul7=(DNI//1000)*5
            DNI = DNI-1000
            mul8=(DNI//100)*4
            DNI = DNI-100
            mul9=(DNI//10)*3
            DNI = DNI-10
            mul10=(DNI//1)*2
            suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9 + mul10
            div = suma%11
            resta = 11-div
            print("Su CUIL es 20 -",DNI1,"-",resta)
        elif género==2:  
            mul1=2*5
            mul2=7*4
            mul3=(DNI//10000000)*3
            DNI = DNI-10000000
            mul4=(DNI//1000000)*2
            DNI = DNI-1000000
            mul5=(DNI//100000)*7
            DNI = DNI-100000
            mul6=(DNI//10000)*6
            DNI = DNI-10000
            mul7=(DNI//1000)*5
            DNI = DNI-1000
            mul8=(DNI//100)*4
            DNI = DNI-100
            mul9=(DNI//10)*3
            DNI = DNI-10
            mul10=(DNI//1)*2
            suma = mul1 + mul2 + mul3 + mul4 + mul5 + mul6 + mul7 + mul8 + mul9 + mul10
            div = suma%11
            resta = 11-div
            print("Su CUIL es 27 -",DNI1,"-",resta)
    elif opción==2:
        print("Su fecha de cumpleaños es el",FdN)
    elif opción==3:
        porcentaje=MdlC/100
        porcentaje2=porcentaje*21
        suma=MdlC+porcentaje
        print("El valor de su compra más el IVA es de",suma)

menú_de_operaciones_bancarias(NyA,DNI1,FdN,MdlC)

#Ejercicio 7
entrada1 = input("Ingrese un numero:       ")
entrada2 = input("Ingrese un numero:     ")
print("Ingrese 1 si desea SUMAR los números")
print("Ingrese 2 si desea RESTAR los números")
print("Ingrese 3 si desea MULTIPLICAR los número")
print("Ingrese 4 si desea DIVIDIR los números")
print("Ingrese 5 si desea obtener la DIVISIÓN ENTERA de los números")
print("Ingrese 6 si desea obtener el MÓDULO de los números")
print("Ingrese '7' para salir del menú")
print("______________________________________________________________")
print("")
print("                      MENÚ DE OPERACIONES")
opción = str(input("OPCIÓN: "))
if opción==1:
    suma = entrada1+entrada2
    print("La suma de los números es:",suma)
elif opción==2:
    if entrada1>entrada2:
        resta1 = entrada1 - entrada2
        print("La resta de",entrada1,"-",entrada2,"es de:",resta1)
    elif entrada2>entrada1:
        resta2 = entrada2 - entrada1
        print("La resta de",entrada2,"-",entrada1,"es de:",resta2)
elif opción==3:
    multi = entrada1*entrada2
    print("El resultado de la multiplicación es:",multi)
elif opción==4:
    if entrada1>entrada2:
        div1 = entrada1/entrada2
        print("El cociente de",entrada1,":",entrada2,"es de:",div1)
    elif entrada2>entrada1:
        div2 = entrada2/entrada1
        print("El cociente de",entrada2,":",entrada1,"es de:",div2)
elif opción==5:
    if entrada1>entrada2:
        dive1 = entrada1//entrada2
        print("El cociente de la DIVISIÓN ENTERA de",entrada1,":",entrada2,"es de:",dive1)
    elif entrada2>entrada1:
        dive2 = entrada2//entrada1
        print("El cociente de la DIVISIÓN ENTERA de",entrada2,":",entrada1,"es de:",dive2)
elif opción==6:
    if entrada1>entrada2:
        modu1 = entrada1%entrada2
        print("El módulo de",entrada1,":",entrada2,"es:",modu1)
    elif entrada2>entrada1:
        modu2 = entrada2%entrada1
        print("El módulo de",entrada2,":",entrada1,"es:",modu2)
elif opción==7:
    print("Usted ha salirdo del menú")

#Ejercicio 8
print(          "Bienvenido al sistema de conversión de medidas de Joaquín Rodríguez")
print("")
print("_______________________________________________________________________________")
print("")
print("Ingrese 1 para convertir GRAMOS A LIBRAS")
print("Ingrese 2 para convertir LIBRAS A GRAMOS")
print("Ingrese 3 para convertir CENTÍMETROS A PULGADAS")
print("Ingrese 4 para convertir PULGADAS A CENTÍMETROS")
print("Ingrese 5 para convertir KILÓMETROS A MILLAS")
print("Ingrese 6 para convertir MILLAS A KILÓMETROS")
opción = int(input("Su opción:  "))
print("_______________________________________________________________________________")
print("")
if opción==1:
    gramos=int(input("Ingrese la cantidad de gramos:    "))
    mul1 = gramos*0.00220462
    print(gramos,"convertido a LIBRAS es igual a",mul1)

elif opción==2:
    libras=int(input("Ingrese la cantidad de LIBRAS:    "))
    mul2 = libras*453.592
    print(libras,"convertido a GRAMOS es igual a",mul2)

elif opción==3:
    cm=int(input("Ingrese los CENTÍMETROS que desea convertir:  "))
    mul3 = cm*0.393701
    print(cm,"convertido a PULGADAS es igual a",mul3)

elif opción==4:
    pul=int(input("Ingrese las PULGADAS que desea convertir:  "))
    mul4 = pul*2.54
    print(pul,"convertido a CENTÍMETROS es igual a",mul4)

elif opción==5:
    km=int(input("Ingrese los KILÓMETROS que desea convertir:  "))
    mul5 = km*0.621371
    print(km,"convertido a MILLAS es igual a",mul5)
    
elif opción==6:
    millas=int(input("Ingrese las MILLAS que desea convertir:  "))
    mul6 = millas*1.60934
    print(millas,"convertido a KILÓMETROS es igual a",mul6)

#Ejercicio 9
contador1 = 0
contador2 = 0
for i in range(1,1001):
    div3 = i%3
    div5 = i%5
    while div3==0:
        contador1 = contador1+i
        break
    while div5==0:
        contador2 = contador2+i
        break
    sumar = contador1 + contador2
    print(sumar)


#OBSERVACIÓN: Este documento reúne todos los ejercicios con el fin de facilitarle la tarea de revisarlos. Todos los ejercicios tienen los
#comentarios correspondientes a su funcionamiento.
