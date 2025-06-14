#SENTENCIA WHILE
contador=1

while contador <= 100:
     print("Contador: ", contador)
contador += 1

contador=1

while contador <= 200:
    print("Contador: ", contador)
    contador += 1

#Tema nuevo en clase
#WHILE
Contador= int(input("Ingresar un numero: "))
while contador > 0:
     print(f"Contador: ,{contador}")
     contador -=1
     print('termino el contador')

#Ejemplo practico:salir cuando el usuario escriba "salir"
while True:
     texto=input("Escribe algo(o escribe 'salir'para terminar):")
     if texto == "salir":
          break
     print("Escribiste: ",texto)