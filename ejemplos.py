x,y,z = 1,4,8
print(x)
print(y)
print(z)
a=b=c= 0
print(x,y,z)
print(a)
print(b)
print(c)
op="hola "
op+="que "
op+="tal "
print(op)
op = "hola"
op+= "mundo"
print(op)
op *= 2
print(op)
texto1="hola"
texto2="mundo"
resultado=texto1+texto2
print(resultado)
mensaje = "hola mundo"
buscar= mensaje.find("mundo")
print(buscar)
saludo = "hola mundo"
extraccion = saludo [0:5]
print(extraccion)
cadena1= "hola"
cadena2= "sheril"
print= cadena1==cadena2
mensaje= "el conocimiento es poder"
print(mensaje.find("conocimiento"))
print(mensaje.find("poder"))
mensaje= "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print(mensaje.find("Sabia"))
print(mensaje.find("Caminaba"))
print(mensaje.find("falanges"))
print(mensaje[459:647])
texto= "La sociedad francesa estaba dividida en estamentos dependiendo de su clase sociales, el poder mas alto lo tenía el rey, detrás estaban la nobleza y el clero y el nivel mas bajo de poder lo tenia el tercer estado que estaba constituido por la burguesía, los artesanos y los campesinos Los Estados Generales eran una asamblea, compuesta por tres ordenes separados: el clero, la nobleza y el grupo formado por burguesía y campesinado. Este último orden se conoce como el tercer estadeo, término que usaremos para referirnos a él en lo sucesivo. Dicha asamblea se había citado por ultima vez en 1614 y el dramatismo de la situación obligó al gobierno a convocarla nuevamente.Luis XVI cedió a las presiones de la reina María Antonieta y del conde de Artois y dio instrucciones para que varios regimientos extranjeros leales se concentraran en París y Versailles. Al mismo tiempo, Necker fue nuevamente destituido. El pueblo de París respondió con la insurrección ante estos actos de provocación; los disturbios comenzaron el 12 de julio, y las multitudes asaltaron y tomaron La Bastilla -una prisión real que simbolizaba el despotismo de los Borbones- el 14 de julio.El 5 de octubre de 1789, las mujeres parisinas partieron desde los barrios obreros hacia la residencia real de Versailles, este suceso dió comienzo a la revolución.A fines de 1792 comenzó el proceso de Convención contra Luis XVI, quien fue juzgado y condenado a la guillotina por mayoría de votos. El 21 de enero de 1793, Luis subió al cadalso, inconmovible hasta el último momento en el sentimiento de su inocencia. La noticia de la muerte del rey produjo indignación en Inglaterra, la que despidió al embajador o representante francés. Francia contestó declarando la guerra a Inglaterra y a Holanda, su aliada."
print(texto.find("pueblo"))
print(texto.find("comienzo"))
print(texto.find("aliada"))
print(texto[1303:1769])
nombre=input("ingrese su nombre:     ")
nota1:float(input("cual es la nota de quimica:   "))
nota2:float(input("cual es la nota de trigonometria:   "))
nota3:float(input("cual es la nota de fisica:     "))
notafinal= (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)
print("hola",nombre,  ", tu nota final es:   ", nota_final)
print("Taller en clase")
print("Ejercicio 1")
num1=int(input("ingrese el primer numero a sumar:  "))
num2=int(input("ingrese el segundo numero a sumar:  "))
op=num1+num2
result=op
print("el resultado de la operacion es:  ",result)
print("Ejercicio 2")
num1=int(input("ingrese un numero:  "))
num2=int(input("ingrese el numero a restar:   "))
op=num1-num2
result=op
print("el resultado de la operacion es:  ",result)
print("Ejercicio 3")
num1=int(input("ingrese un numero:    "))
num2=int(input("ingrese el numero a multiplicar:  "))
op=num1*num2
result=op
print("el resultado de la multiplicacion es:      ",result)
print("Ejercicio 4")
num1=int(input("ingrese un numero:   "))
num2=int(input("ingrese el numero por el cual dividir:   "))
op=num1/num2
result=op
print("el resultado de la division es:       ",result)
print("Ejercicio 5")
nombre=(input("ingrese su nombre: "))
apellido=(input("ingrese su apellido:  "))
print("Hola" , nombre + " " + apellido)
print("Ejercicio 6")
nombre=(input("ingresa tu nombre:   "))
primera=nombre[0:1]
print("la primera letra de su nombre es: ",primera)
print("Ejercicio 7")
palabra1=input("ingrese una palabra:  ")
print("la ultima letra de la palabra es:  ",palabra1[-1])
print("Ejercicio 9")
dato=int(input("ingrese su fecha de nacimiento:  "))
dato1=int(input("ingrese el año actual:  "))
op2=dato-dato1
print("su edad es:  ",op2)
print("Ejercicio 10")
dato=input("ingrese su usuario:  ")
dato1=input("ingrese su dominio:   ")
print("Su correo es ",dato + "@" + dato1)
print("Ejercicio 11")
nombre=input("Ingrese su nombre: ")
print("Tu nombre tiene",  len(nombre), "letras")
print("Ejercicio 12")
nombre=input("ingrese nombre:  ")
print("Tu nombre tiene",len(nombre),"letras")
palabra1=input("ingrese una palabra:  ")
palabra2=input("ingrese una segunda palabra:   ")
print("La union de sus palabras es:  ",palabra1 + " " + palabra2)
print("Ejercicio 13")
palabra=input("ingrese una palabra: ")
print("La segunda letra de la palabra es: ",palabra[1])
print("Ejercicio 14")
palabra=input("ingrese una palabra:  ")
print("Las primeras 3 letras de su palabra es:  ",palabra[0:3])
print("Ejercicio 15")
palabra=input("ingrese una palabra: ")
print("Las letras de su palabra en orden inverso es:  ",palabra[::-1])
print("Sistema de evaluacion")
print("Si tu nota es 2.9 o menos pierdes la materia  y si es 3.0 o mas ganas")
nombre=input("Ingresar el nombre del estudiante: ")
Nota=input("Ingrese el grado que cursa el estudiante: ")
Materia1="Matematicas"
Materia2="Castellano"
Materia3="Ingles"
Materia4="Fisica"
Materia5="Quimica"
print(f"Las notas finales del estudiante son:   ")