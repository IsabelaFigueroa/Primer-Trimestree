#credito bancario
nombre=input("ingrese su nombre completo: ")
edad=int(input("ingrese su edad: "))
print(f"cliente:{nombre},edad:{edad} años")
if edad>18:
    print("credito aprobado")
else:
    print("credito rechazado: Edad invalida")
print("----Fin del proceso----")

#---------------------------------------------------------------------------------------------------

#Programa empresa de juegos para todas las edades
edad=int(input("ingrese se edad: "))
if edad <0:
    print("Error edad invalida")
elif edad <4:
    print("Entrada gratis")
elif edad <=18:
    print("Debe pagar 5 euros")
else:
    print("Debe pagar 18 euros")

#----------------------------------------------------------------------------------------------

#Simulacion calculadora
print("Operaciones disponibles: ")
print("s:Suma")
print("r: Resta")
print("m: multipliacion")
print("d: Division")
operacion= input("Seleccione la operacion(s/r/m/d): ")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
if operacion == 's':
    print("Resultado: ",num1+num2)
elif operacion == 'r':
    print("Resultado: ",num1-num2)
elif operacion == 'm':
    print("Resultado: ",num1*num2)
elif operacion == 'd':
    if num2 == 0:
        print("Resultado: ",num1/num2)
    else:
        print("No se puede dividir por 0")
else:
    print("Operacion no valida")



