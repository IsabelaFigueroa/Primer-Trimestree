# #1. Verifica si un numero es positivo,negativo o cero
# numero100= int(input("Ingrese un numero: "))
# if numero100 > 0:
#     print("El numero es positivo")
# elif numero100 <0:
#     print("El numero es negativo")
# else:
#     print("El numero es cero")

# #-----------------------------------------------------------------------------------------------------------
# #2. Calcular el mayor de dos numeros
# numero1= int(input("Ingrese el primer numero: "))
# numero2= int(input("Ingrese el segundo numero: "))
# if numero1 > numero2:
#     print("El mayor es: ",numero1)
# elif numero2 > numero1:
#     print("El mayor es: ",numero2)
# else:
#     print("Los numeros son iguales")


#------------------------------------------------------------------------------------------------------------
# #3. Determinar si un numero es par o impar
# num=int(input("Ingrese un numero: "))
# if num % 2 == 0:
#     print("El numero es par")
# else:
#     print("El numero es impar")
#-----------------------------------------------------------------------------------------------------------

# #4. Verificar si un numero esta entre 10 y 20
# num1=int(input("Ingrese un numero: "))
# if 10<= num1 <=20:
#     print("El numero si esta entre 10 y 20")

# else:
#     print("El numero no esta entre 10 y 20")
#---------------------------------------------------------------------------------------------------------

# #5. Encontrar el mayor de tres numeros.
# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el segundo numero: "))
# num3=int(input("Ingrese el tercer numero: "))
# if num1 <= num2:
#     if num1>=num3:
#         print("El mayor es: ",num1)
#     else:
#         print("El mayor es: ",num3)
# else:
#     if num2 >= num3:
#         print("El mayor es: ",num2)
#     else: 
#         print("El mayor es: ",num3)
#--------------------------------------------------------------------------------------------------------
# #6. Calcular precio final con 10% de descuento si el total es mayor $100
# precio= float(input("Ingrese el precio total de la compra: "))
# if precio >100:
#     descuento = precio * 0.10
#     precio = precio - descuento
# print("El precio final es: ", precio)
#--------------------------------------------------------------------------------------------------------

# #7. Verifica si una persona debe votar (mayor o igual a 18 años)
# Edad=int(input("edad: "))
# if Edad >=18:
#     print("Puede votar")
# else:
#     print("No puede votar")

#-------------------------------------------------------------------------------------------------------
# #8. Dado el precio y tipo de cliente vip o normal, aplica un descuento del 20% solo a vip
# precio=float(input("Precio: "))
# tipo=input("Tipo de cliente Vip o normal: ")
# if tipo == "VIP":
#     precio = precio * 0.8
# print("Precio final: ",precio)

#----------------------------------------------------------------------------------------------------------
# #9. Determina si un numero es multiplo de 5 y de 3 al mismo tiempo
# numero=int(input("Numero: "))
# if numero %3 == 0 and numero %5 == 0:
#     print("Multiplo de 3 y 5")
# else:
#     print("El numero no es multiplo de3 y 5")

#---------------------------------------------------------------------------------------------------------

# #10.Dado un numero ,verifica si es divisible entre dos numeros dados
# numero = int(input("Número: "))
# divisor1 = int(input("Divisor 1: "))
# divisor2 = int(input("Divisor 2: "))
# if numero  % divisor1 == 0 and numero % divisor2 == 0:
#     print("Es divisible entre ambos")
# else:
#     print("No es divisible entre ambos")

#------------------------------------------------------------------------------------------------------

# #Ejercicios con Listas (con condicionales)
# #11.Crea una lista con 5 numeros.Si el tercer numero es mayor que 10,muestra "Mayor a 10",y si no,muestra "Menor o igual a 10" 
# num1=int(input("Ingrese el numero uno de la lista: "))
# num2=int(input("Ingrese el numero dos de la lista: "))
# num3=int(input("Ingrese el numero tres de la lista: "))
# num4=int(input("Ingrese el numero cuatro de la lista: "))
# num5=int(input("Ingrese el numero cinco de la lista: "))
# lista=[num1, num2, num3, num4, num5, ]
# if lista[2] > 10:
#     print("Mayor a 10")
# else:
#     print("Menor o igual que 10")

#------------------------------------------------------------------------------------------------------

# #12.Verifica si el numero 7 esta en la lista [3, 5, 7, 9].Si esta muestra "Esta en la lista",si no,muestra "No esta en la lista"

# lista=[3, 5, 7, 9]
# print("Lista: ",lista)
# numero= int(input("ingresa un numero para verificar si esta en la lista: "))
# if numero in lista:
#     print("El numero si esta en la lista")
# else:
#     print("El numero no esta en la lista")

#------------------------------------------------------------------------------------------------------
# # 13.Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayorque 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”

# lista= [4, 6, 2, 8lis]
# suma= lista[0] + lista[1]
# if suma >10:
#     print("La suma es alta")
# else:
#     print("La suma es baja")
#------------------------------------------------------------------------------------------------------------
#  #14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.

# nombres= ["Ana", "Luis", "Pedro", "Marta"]
# print("Lista de nombres: ", nombres)
# ultimo_nombre=nombres[-1]
# print ("Ultimo nombre: ",ultimo_nombre)
# if ultimo_nombre == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre incorrecto")

# #------------------------------------------------------------------------------------------------------------

# # 15.Crea una lista con tres colores.Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada
# colores = ["rojo", "azul", "verde"]
# if colores[1] == "azul":
#     colores[1] = "amarillo"
# print("Lista actualizada:", colores)

#---------------------------------------------------------------------------------------------------------

# #Ejercicios con Tuplas (con condicionales)
# # 16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que último, muestra “Orden ascendente”, si no, “Orden 

# tupla = (5, 8, 12, 20)
# if tupla[0] < tupla[-1]:
#     print("Orden ascendente)")
# else:
#     print("Orden descendente")

#-----------------------------------------------------------------------------------------------------

# # 17.Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es,muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.

# tupla = (25, 32, 28)
# if tupla[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")

#---------------------------------------------------------------------------------------------------------

# # 18.Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.

# tupla = (1, 2, 3)
# lista = list(tupla)
# if lista[1] == 2:
#     lista[1] = 10
# tupla = tuple(lista)
# print("Tupla modificada:", tupla)

# #-----------------------------------------------------------------------------------------------------
# # 19.Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.

# tupla = (4, 9)
# valor = tupla[1]
# if valor > 5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

#----------------------------------------------------------------------------------------------------------

# # 20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”.

# tupla1 = (3, 4)
# tupla2 = (3, 5)

# if tupla1 == tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")
#----------------------------------------------------------------------------------------------------

# # Ejercicios con Diccionarios (con condicionales)
# #21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.

# persona = {"nombre": "Juan", "edad": 17}
# if persona["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

#-------------------------------------------------------------------------------------------------

# #22.Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario.

# persona = {"nombre": "Lucía", "edad": 20}
# if persona["edad"] > 18:
#     persona["edad"] = 21
# print(persona)

#------------------------------------------------------------------------------------------------

# # 23. Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe,agrégala con el valor “Bogotá” y muestra el diccionario.

# diccionario = {"nombre": "Carlos"}
# if "ciudad" not in diccionario:
# diccionario["ciudad"] = "Bogotá"
# print(diccionario)

#------------------------------------------------------------------------------------------

# # 24.Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave“precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.
# producto = {"producto": "pan", "precio": 1200}
# if "precio" in producto:
# print(producto["precio"])
# else:
# print("No hay precio")
# productos = {"pan": 1200, "leche": 2000}
 #---------------------------------------------------------------------------------------------

# # 25. Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”

# productos = {"pan": 1200, "leche": 2000}
# if "pan" in productos:
#     print(productos["pan"])
# else:
#     print("Producto no disponible")


