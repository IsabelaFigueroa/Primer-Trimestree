print("Sistema de evaluacion")
print("Si tu nota es 2.9 o menos pierdes la materia  y si es 3.0 o mas la")
nombre=input("Ingresar el nombre del estudiante: ")
Nota=input("Ingrese el grado que cursa el estudiante: ")
Materia1="Matematicas"
Materia2="Artistica"
Materia3="Ingles"
Materia4="Fisica"
Materia5="Quimica"

print("Ingrese 3 notas de", Materia1)
Mat1=float(input("nota1: "))
Mat2=float(input("nota2: "))
Mat3=float(input("nota3: "))
Op1=Mat1+Mat2+Mat3
promedio= Op1/3
print("Suma de las notas",Op1)
print(f"promedio de",{Materia1},"es",{promedio})

print("Ingrese 3 notas de",Materia2)
Mate1=float(input("nota1: "))
Mate2=float(input("nota2: "))
Mate3=float(input("nota3: "))
Op2=Mate1+Mate2+Mate3
promedio=Op2/3
print("Suma de notas", Op2)
print("promedio de", {Materia2}, "es", promedio)

print("Ingrese 3 notas de",Materia3)
Matee1=float(input("nota1: "))
Matee2=float(input("nota2: "))
Matee3=float(input("nota3: "))
Op3=Matee1+Matee2+Matee3
promedio=Op2/3
print("Suma de notas", Op3)
print("promedio de", {Materia3}, "es", promedio)

print("Ingrese 3 notas de",Materia4)
Mateee1=float(input("nota1: "))
Mateee2=float(input("nota2: "))
Mateee3=float(input("nota3: "))
Op4=Mateee1+Mateee2+Mateee3
promedio=Op4/3
print("Suma de notas", Op2)
print("promedio de", {Materia4}, "es", promedio)




Mateeee1=float(input("nota1: "))
Mateeee2=float(input("nota2: "))
Mateeee3=float(input("nota3: "))
Op5=Mateeee1+Mateeee2+Mateeee3
promedio=Op5/3
print("Suma de notas", Op2)
print("promedio de", {Materia5}, "es", promedio)

print("PRODUCTOS")
productos=[     ]
producto1=input("ingrese el primer producto: ")
productos.append(producto1)
producto2=input("Ingrese el segundo producto: ")
productos.append(producto2)
producto3=input("Ingrese el tercer producto: ")
productos.append(producto3)
print("Lista completa de productos:  ",productos)


print("PRECIOS")
precios=[     ]
precio1=float(input("precio del primer articulo: "))
precios.append(precio1)

precio2=float(input("precio del segundo articulo: "))
precios.append(precio2)

precio3=float(input("precio del tercer articulo: "))
precios.append(precio3)

total=sum(precios)
print("suma total de los precios:  ", total)



print("NUMEROS")
numeros=[    ]
num1=int(input("ingresa el primer numero: "))
numeros.append(num1)
num2=int(input("ingresa el segundo numero:  "))
numeros.append(num2)
num3=int(input("ingresa el tercer numero:  "))
numeros.append(num3)
num4=int(input("ingresa el cuarto numero:  "))
numeros.append(num4)
print("El numero mayor es: ",max(numeros))
print("El numero menor es: ",min(numeros))

#Ejercicios de clase


