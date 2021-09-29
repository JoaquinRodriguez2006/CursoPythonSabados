#CLASE 2: Ejercicios del Power Point
#OBSERVACIÓN: Los ejercicios tienen sus respectivos comentarios de acuerdo a su funcionamiento en sus respectivos documentos
#OBSERVACIÓN: Reuno todos los códigos en este programa para facilitarle la tarea de corregirlos.

#Ejercicio 1: Números Pares e Impares
entrada = int(input("Ingrese un número:     "))
if (entrada % 2 == 0):
    print("Es par")
else:
    print("Es impar")

#Ejercicio 2: Ciclo WHILE infinito
suma = (10-8)
while suma:
    print("El resultado es DOS")

#Ejercicio 3: Edades y grupos sociales
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

#Ejercicio 4: Números del 1 al 100
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
#OBSERVACIÓN: Cuando quise poner "print(/F1)" para que imprima todo en filas diferentes, me tiró error.

#Ejercicio 5: Último dígito
entrada=int(input("Ingrese un número:   "))
resto=entrada%10
print(resto)

#Ejercicio 6: Dígitos del número, del menos significativo al más significativo
entrada = int(input("Ingrese un número:     "))
número1=entrada//10
número2=número1%10
número4=número1//10
número3=entrada%10

if número1>número3:
    print(número3)
    print(número1)
    if número1<número3:
        print(número1)
        print(número3)

if número2>número3 and número4:
    if número4>número3:
        print(número3)
        print(número4)
        print(número2)
    elif número4<número3:
        print(número4)
        print(número3)
        print(número2)

elif número3>número2 and número4:
    if número4>número2:
        print(número2)
        print(número4)
        print(número3)
    elif número4<número2:
        print(número4)
        print(número2)
        print(número3)

elif número4>número2 and número3:
    if número3>número2:
        print(número2)
        print(número3)
        print(número4)
    elif número3<número2:
        print(número2)
        print(número3)
        print(número4)

#Ejercicio 7: Contar cifras de un número
ne = int(input("Ingrese un número:     "))
aux=ne
contador=1
while ne!=0:   
    contador
    ne = ne//10
    contador=contador+1
    if ne==0:
        break
    print("El número",aux,"tiene",contador,"dígitos")
    if ne!=0:
        continue

#Ejercicio 8: Contar cifras pares e impares
ne = int(input("Ingrese un número:     "))
aux=ne
contador=0
contador2=0

while ne!=0:   
    ne1 = ne//10
    ne2=ne%10
    ne = ne//10
    if ne%2==0:
        contador=contador+1
    if ne2%2!=0:
        contador2=contador2+1 
    print("El número tiene",contador,"dígitos pares")
    print("El número tiene",contador2,"dígitos impares")
    if ne==0:
        break
    if ne!=0:
        continue

#Ejercicio 9: Suma de los dígitos de un número
ne = int(input("Ingrese un número:     "))
aux=ne
ne1 = ne//10
contador=0
contador2=0

while ne1>0:   
    ne1 = ne//10
    ne2=ne%10
    ne = ne//10
    sumar=ne1+ne2
    print("La suma de los dígitos del número",aux,"es igual a",sumar)

#Ejercicio 10: 3 números del mayor al menor
entrada=int(input("INGRESE UN NÚMERO:  "))
entrada2=int(input("INGRESE UN NÚMERO:  "))
entrada3=int(input("INGRESE UN NÚMERO:  "))

if entrada>entrada2 and entrada3:
    if entrada2>entrada3:
        print(entrada)
        print(entrada2)
        print(entrada3)
    elif entrada3>entrada2:
        print(entrada)
        print(entrada3)
        print(entrada2)

if entrada2>entrada and entrada3:
    if entrada>entrada3:
        print(entrada2)
        print(entrada)
        print(entrada3)
    elif entrada3>entrada:
        print(entrada2)
        print(entrada3)
        print(entrada)

if entrada3>entrada and entrada2:
    if entrada>entrada2:
        print(entrada3)
        print(entrada)
        print(entrada2)
    elif entrada2>entrada:
        print(entrada3)
        print(entrada2)
        print(entrada)
        
#Ejercicio 11: ¿Es perfecto?
ne = int(input("Ingrese un número:     "))

for i in range(1,ne):
    div=ne//i
    aux1=ne//i
    if ne%i==0:
        suma=div
    if suma==ne:
        print("Es perfecto")
    
#Ejercicio 12: Números perfectos entre 1 y n
entrada = int(input("Ingrese un número: "))
for a in range(1,entrada):  #toma los números entre el número ingresado
    for b in range(1,a):    #selecciona uno de los números de A y los divide por los números que se encuentran entre el 1 y ese mismo número
        div=a//b    #divide el número con los números entre medio del 1 y el mismo
        if div%1==0:  #si esa división no da resto, entonces el número por el que se lo dividió sí es un divisor
            suma = div #suma todos sus divisotrs
        if suma==b  :#si la suma de sus divisores es igual al número, entonces es perfecto
            print(suma)

#OBSERVACIÓN: No llegué a terminar los ejercicios opcionales para el sábado, por lo que los terminaré para el otro. Disculpe