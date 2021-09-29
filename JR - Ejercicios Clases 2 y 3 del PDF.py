#CLASES 2 Y 3
#EJERCICIOS DEL PDF

#Ejercicio 1: Determinar si el número es par o impar
entrada = int(input("Ingrese un número:     "))
if (entrada % 2 == 0):
    print("Es par")
else:
    print("Es impar")

#Ejercicio 2: Ingresar edad y determinar etapa de vida
edad = int(input("Ingrese su edad actual:   "))
if (edad<2):
    print("Es un bebé")
elif (edad>=2) and (edad<4):
    print("Es un infante")
elif (edad>=4) and (edad<12):
    print("Es un niño")
elif (edad>=13) and (edad<20):
    print("Es un adolescente")
elif (edad>=20) and (edad<65):
    print("Es un adulto")
elif (edad>=65):
    print("Es un anciano")
elif (edad>=130):
    print("Es un fantasma. BOOO")

#Ejercicio 3: Ciclo infinito
suma = (10-8)
while suma:
    print("El resultado es DOS")

#Ejercicio 4: Números de 1 al 100 con dos While
i = 0
j = 0
bandera = 1
linea = ""

while i < 10:
    while j < 10:
        linea += " " + str(bandera)
        bandera += 1
        j += 1
    print(linea)
    j = 0
    linea = ""
    i += 1

#Ejercicio 5: Números del 1 al 100 con un While
while True:
    for F1 in range(1,11):
        print(F1)
    for F2 in range(11,21):
        print(F2)
    for F3 in range(21,31):
        print(F3)
    for F4 in range(31,41):
        print(F4)
    for F5 in range(41,51):
        print(F5)
    for F6 in range(51,61):
        print(F6)
    for F7 in range(61,71):
        print(F7)
    for F8 in range(71,81):
        print(F8)
    for F9 in range(81,91):
        print(F9)
    for F10 in range(91,101):
        print(F10)
    break

#Ejercicio 6: Números primos entre el 1 y n
n = int(input("Ingrese un número:    "))
print("Voy a mostrarle todos los números primos entre el 1 y su número")
for i in range (1,n+1):
    resto = i%2
    resto2  = i%3
    resto3 = i%5
    resto4 = i%7
    resto5 = i%9
    while resto!=0 and resto2!=0 and resto3!=0:
        print(i)
        break

#Ejercicio 7: Condimentos de un Sandwich
def Preparaciòn():
    entrada=str(input("Ingrese un condimento:    "))
    while entrada != "salir":
        print("El condimento",entrada,"ha sido agregado")
        entrada=str(input("Ingrese un condimento o salir:    "))

Preparaciòn()

#Ejercicio 8a: Remera
def hacer_remera(talle,mensaje=""):
    print("Se va a crear una remera de talle",talle,"que diga",mensaje)

talle=str(input("Ingrese un talle:  "))
mensaje=str(input("Ingrese un mensaje que le gustarìa que contenga la remera:   "))
hacer_remera(talle,mensaje)

#Ejercicio 8b: Remera grande
def hacer_remera(talle='L',mensaje='Me gusta Python'):
    talle=str(input("Ingrese un talle:  "))
    mensaje=str(input("Ingrese un mensaje que le gustarìa que contenga la remera:   "))
    if talle=="": 
        talle="L"
    if mensaje=="":
        mensaje="Me gusta Python"
    print("Se va a crear una remera de talle",talle,"que diga",mensaje)

#Ejercicio 9: Serie de Fibonacci
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

#Ejercicio 10: Calculadora inteligente
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

#Ejercicio 11: Conversor de medidas
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

#Ejercicio 12a: Determinar si el año ingresado es bisiesto
print("Este programa determina si el año ingesado es bisiesto o no")
año=int(input("Ingrese un año:  "))
div1=año%4
div2=año%100
div3=año%400
if div1==0 and div2==0 and div3==0:
    print("El año es bisiesto")
else:
    print("El año NO es bisiesto")

#Ejercicio 12b: Determinar los años bisiestos entre 2021 y n
print("Este programa determina si el año ingesado es bisiesto o no")
año=int(input("Ingrese un año:  "))
for i in range(2021,año):
    div1=i%4
    div2=i%100
    div3=i%400
    if div1==0 and div2==0 and div3==0:
        print("El año",i, "es bisiesto")

#Ejercicio 13: Sumar múltiplos de 3 y 5 menores a 1000
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