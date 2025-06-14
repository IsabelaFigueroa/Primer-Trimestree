#ASIGNACION, CONCATENACION Y EXTRACCIÓN.
 #1.suma de dos numeros
numero=int(input("ingresa el primer numero "))
numero2=int(input("ingresa el segundo numero "))
print("la suma es:",numero+numero2)

print("------------------------------------")

#2.Resta de primer numero menos el segundo
num1=int(input("ingrese el primer numero "))
num2=int(input("ingresar el segundo numero "))
print("la resta es:",num1-num2)

print("------------------------------------")

#3.multiplicación de dos numeros
numero1=int(input("ingrese el primer numero "))
numero2=int(input("ingresar el segundo numero "))
print("la multiplicación es:",numero1*numero2)

print("------------------------------------")

#4. división de dos numeros
c=int(input("ingrese el primer numero "))
d=int(input("ingresar el segundo numero "))
print("la división es:",c/d)

print("------------------------------------")

#5. saludo con nombre completo
nombre=(input("ingresa tu nombre "))
apellido=(input("ingresa tu apellido "))
print("Hola", nombre +" " + apellido)

print("------------------------------------")

#6.Primera letra del nombre
nombree=(input("ingresa tu nombre "))
primera=nombree[0]
print("la primera letra de su nombre es:", primera)

print("------------------------------------")

#7. Ultima letra de la palabra
palabra=(input("ingrese una palabra"))
ultima=palabra[-1]
print("la ultima letra de su palabra es:", ultima)

print("------------------------------------")

#8. Area de un rectangulo
base=int(input("ingresa la base del rectangulo "))
altura=int(input("ingresa la altura del rectangulo "))
print("El area del rectangulo es", base*altura)

print("------------------------------------")

#9. edad calculada
nacimiento=int(input("ingrese su año de nacimiento"))
print("tu edad es", 2025- nacimiento)

print("------------------------------------")

#10. correo electonico
usuario=input("ingresa tu nombre de usuario")
dominio=input("ingresa el dominio")
print("correo hecho:", usuario + "@" + dominio)
 
print("------------------------------------")

#11. numero de letras del nombre
usuarioo=input("ingresa su nombre")
print("su nombre tiene", len (usuarioo ),"letras")
      #DATO: len se usa para saber cuantas letras tiene una palabra o cuantas cosas hay en una lista
print("------------------------------------")
      
#12. Combinación de dos palabras
palabra1=input("ingrese una palabra")
palabra2=input("ingrese la segunda palabra")
print("combinacion de las palabras", palabra1+palabra2)

print("------------------------------------")

#13. segunda letra de una palabra
palabraaa=input("ingrese una palabra ")
print("la segunda letra es:", palabraaa[1])

print("------------------------------------")

#14. Las tres primeras letras de una palabra
palabraaaa=input("ingrese una palabra ")
print("las tres primeras letras son", palabraaaa[0]+ palabraaaa[1]+palabraaaa[2])


print("------------------------------------")
#15.Palabra invertida
palabre=input("ingresa una palabra: ")
print("palabra invertida:", palabre[::-1])

print("------------------------------------")


#16. Suma,resta, multiplicacion y division
numeroo1=int(input("ingresa el primer numero"))
numeroo2 =int(input("ingresa el primer numero"))
print("suma", numeroo1+ numeroo2)
print("resta", numeroo1-numeroo2)
print("multiplicacion", numeroo1* numeroo2)
print("division", numeroo1/ numeroo2)

print("------------------------------------")

#17. Doble del numero
nu=int(input("ingresar un numero "))
print("su numero doblado es", nu*2)

print("------------------------------------")

#18.Mitd de un numero
n=int(input("ingresa un numero "))
print("la mitad es:", n/2)
print("------------------------------------")
#19. contar caracteres de una frase
frase=input("ingrese una frase")
print("la frase tiene", len (frase),"caracteres")

print("------------------------------------")
#20. contar caracteres de una frase
palabraa=input("ingrese una palabra: ")
resultado=palabraa+palabraa+palabraa
print("repeticion", resultado)
print("------------------------------------")

#21. dos primeras y dos ultimas letras
nombre300=input("ingresa tu nombre ")
print("primera dos: ", nombre300[:2])
print("ultimas dos: " , nombre300[-2:])
print("------------------------------------")
# 22. Pide una palabra y muestra la letra del medio 
palabra = input("Escribe una palabra: ")
if len(palabra) % 2 == 1:
    medio = len(palabra) // 2
    print("Letra del medio:", palabra[medio])
else:
    print("La palabra no tiene número impar de letras.")
# 23. Mostrar solo los primeros 10 caracteres de una frase
frase = input("Escribe una frase: ")
print(frase[:10])

# 24. Elevar un número al cuadrado 
num = int(input("Escribe un número: "))
print(num * num)

# 25. Mostrar el mayor de dos números 
a = int(input("Escribe el primer número: "))
b = int(input("Escribe el segundo número: "))
mayor = (a + b + abs(a - b)) // 2
print("El mayor es:", mayor)

# 26. Mostrar cuántos días ha vivido 
edad = int(input("¿Cuántos años tienes? "))
print("Has vivido aproximadamente", edad * 365, "días.")

# 27. Mostrar cada letra de una palabra en una línea
palabra = input("Escribe una palabra: ")
for letra in palabra:
    print(letra)

# 28. Mostrar si la palabra tiene más de 5 letras
palabra = input("Escribe una palabra: ")
print("Tiene más de 5 letras:", len(palabra) > 5)

# 29. Multiplicar un número por 10
num = int(input("Escribe un número: "))
print("Multiplicado por 10 es:", num * 10)

# 30. Mostrar palabra en mayúsculas y minúsculas 
palabra = input("Escribe una palabra: ")
print(palabra.upper())
print(palabra.lower())