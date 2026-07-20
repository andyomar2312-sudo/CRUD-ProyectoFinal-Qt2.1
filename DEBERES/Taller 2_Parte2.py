#CLASIFICACIÓN DE NUMERO
número = int(input("Ingrese un número:  "))
if número > 0:
    print("El número es positivo  ", número)
elif número < 0:
    print("El número es negativo", número)
else:
    print("El número es cero ", número)
if número != 0:
    if número%2 == 0:
        print("Además es par ")
    else:
        print ("Además es impar")
        
#DESCUENTO DE COMPRAS
compra = float(input("Ingrese el valor de su compra:  "))
if compra < 50:
  print("El valor total a pagar sin descuento es: ", compra )
elif compra >= 50 and compra <= 100:
  descuento = compra * 0.05
  total = compra - descuento
  print("El valor total a pagar con descuento del 5% es: ", total )
elif compra > 100 and compra <=200:
  descuento = compra * 0.10
  total = compra - descuento
  print("El valor total a pagar con descuento del 10% es: ", total)
elif compra > 200:
  descuento = compra * 0.15
  total = compra - descuento
  print("El valor total a pagar con descuento del 15% es: ", total)

#VERIFICACIÓN DEL SISTEMA
usuario = str(input("Ingrese su usuario:"))
contraseña = str(input("Ingrese su contraseña: "))
user = "admin"
pasw = "Python123"
if usuario == user and contraseña == pasw:
  print("Acceso totalmente exitoso ")
elif usuario != user or contraseña == pasw:
  print("Usuario incorrecto")
elif usuario == user or contraseña != pasw:
  print("Contraseña incorrecta ")
else:
  print("Usuario y contraseña incorrectos")

  #cálculo del bono
sueldo = int(input("Ingrese su sueldo:  "))
años = int(input("Ingrese sus años trabajando:  "))
if años < 2:
    bono = sueldo * 0.05
    print("Su bono por antigüedad es: ", bono)
elif años >= 2 and años < 5:
    bono = sueldo * 0.10
    print ("Su bono por antigüedad es: ", bono)
else:
    bono = sueldo * 0.15
    print("Su bono por antigüedad es: ", bono)
if sueldo >= 1000:
   bono_adicional = bono * 0.02
   total_del_bono = bono + bono_adicional
   print("El bono por los", años, "de antigüedad y su sueldo mayor que mil es: ", total_del_bono)
  
#APROBACIÓN DE CRÉDITO
print("## CREDITO ##")
edad = int(input("Ingrese su edad  "))
ingreso_mensual = float(input("Ingreso mensual "))
historial = input("Ingrese su historial crediticio Bueno/Malo/Regular   ")
if edad >= 21 and ingreso_mensual >=600 and (historial == "Bueno" or historial == "Regular"):
  print("Usted es apto para un crédito ")
else:
  print("Usted no es apto para crédito")

#CLASIFICACIÓN DE TRIANGULOS
lado1 = int(input("Ingrese un valor para un lado del triángulo: "))
lado2 = int(input("Ingrese un valor para otro lado del triángulo:"))
lado3 = int(input("Ingrese un valor para el último lado del triángulo: "))
if lado1 == lado2 ==lado3:
   print("El triángulo es equilatero") 
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
   print("El triángulo es isósceles")
else:    print("El triángulo es escaleno")

#TARIFA DE TRANSPORTE
edad = int(input ("Ingrese su edad: "))
tcompl = 0.35
if edad <5:
   print("El pasaje es gratis")
elif edad>=5 and edad <=12:
  total = tcompl * 0.5
  print ("El pasaje es de: ", total)
elif edad >13 and edad <=59:
  print("El pasaje es de: ", tcompl)
else:
   total =tcompl * 0.4
   print("El pasaje es de: ", total)
 
#EVALUACIÓN ACADEMICA COMPLETA •	Aprobado si el promedio es mayor o igual a 7.

nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))
promedio = (nota1 + nota2 +nota3)/3 
if promedio >=7:
   print("Usted aprobó")
elif promedio >5 and promedio <7:
  print ("Usted está en supletorios")
else: 
   print ("Usted reprobó")
if nota1 or nota2 or nota3 <4:
   print ("Usted tiene un bajo rendimiento")
   
#MAYOR DE TRES NÚMEROS
nm1 = float(input("Ingrese un número: "))
nm2 = float(input("Ingrese un segundo número: "))
nm3 = float(input("Ingrese un tercer número: "))
if nm1 > nm2 and nm1 > nm3: 
   print ("El primer número es mayor")
elif nm2 > nm1 and nm2 > nm3:
   print ("El segundo número es mayor")
else: 
   print ("El tercer número es mayor")
if nm1 == nm2 ==nm3:
   print ("Los tres números son iguales")
elif nm1 == nm2: 
   print ("Los dos primeros números son iguales")
elif nm1 == nm3:
   print ("El primer y tercer número son iguales")
else: 
   print ("El segundo número y el tercer número son iguales")

   #CALCULADORA CON MATCH
número1 = float(input("Ingrese un número  "))
número2 = float(input("Ingrese un número  "))

print("1. suma ")
print("2. resta ")
print("3. multiplicación")
print("4. división")

opcion = int(input("Seleccione una operación: ")) # Define 'opcion' from user input

match opcion:
    case 1:
        print("Usted ha elegido la suma ")
        suma = número1 + número2
        print("La respuesta de la suma es: ", suma)
    case 2:
        print("Usted ha elegido la resta")
        resta = número1 - número2
        print("La respuesta de la resta es: ", resta)
    case 3:
        print("Usted ha elegido la multiplicación")
        multiplicación = número1 * número2
        print("La respuesta de la multiplicación es: ", multiplicación)
    case 4:
        print("Usted ha elegido la división")
        if número2 == 0:
            print("No se puede dividir para cero, elija otro número por favor")
        else:
            división = número1 / número2
            print("La respuesta de la división es: ", división)
    case _:
        print("Opción inválida. Por favor, seleccione una opción entre 1 y 4.")

#MENÚ DE RESTAURANTE CON MATCH
print("# Menú de la \"Sazón\" #")
print("1. Desayuno $2,50")
print("2. Almuerzo $3,00 ")
print("3. Merienda $2,00 ")
print("4. Cena $3,50 ")
opcion = int(input("Ingrese la opción del menú: "))
bebida = 1.5

match opcion:
    case 1:
        print("Usted ha elegido el desayuno.")
        pregunta = input("Desea con bebida, el costo es $1,50. Si/No  ")
        desayuno = 2.50
        bebida_desayuno_costo = 1.5
        if pregunta == "Si" or pregunta == "si":
            valor_total = desayuno + bebida_desayuno_costo
            print("El valor total a pagar es: ", valor_total)
        else:
            print("El valor total a pagar es: ", desayuno)
    case 2:
        print("Usted ha elegido el almuerzo.")
        pregunta = input("Desea con bebida, el costo es $1,50. Si/No  ")
        almuerzo = 3.00
        bebida_almuerzo_costo = 1.5
        if pregunta == "Si" or pregunta == "si":
            valor_total = almuerzo + bebida_almuerzo_costo
            print("El valor total a pagar es: ", valor_total)
        else:
            print("El valor total a pagar es: ", almuerzo)
    case 3:
        print("Usted ha elegido la merienda.")
        pregunta = input("Desea con bebida, el costo es $1,50. Si/No  ")
        merienda = 2.00
        bebida_merienda_costo = 1.5
        if pregunta == "Si" or pregunta == "si":
            valor_total = merienda + bebida_merienda_costo
            print("El valor total a pagar es: ", valor_total)
        else:
            print("El valor total a pagar es: ", merienda)
    case 4:
        print("Usted ha elegido la cena.")
        pregunta = input("Desea con bebida, el costo es $1,50. Si/No  ")
        cena = 3.50
        bebida_cena_costo = 1.5
        if pregunta == "Si" or pregunta == "si":
            valor_total = cena + bebida_cena_costo
            print("El valor total a pagar es: ", valor_total)
        else:
            print("El valor total a pagar es: ", cena)
    case _:
        print("Ingrese una opción válida entre 1 y 4")