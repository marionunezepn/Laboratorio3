import math
def triangulo():
	print("Area y perimtro del triangulo")
	lado1 = float(input('ingrese lado 1: '))
	lado2 = float(input('ingrese lado 2: '))
	lado3 = float(input('ingrese lado 3: '))
	if((lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado2+lado3>lado1)):
		s = (lado1+lado2+lado3)/2
		v = s*(s-lado1)*(s-lado2)*(s-lado3)
		area = math.sqrt(v)
		print ('Area: '+str(round(area,2))+'Perimetro: '+str(round(s,2)))
	else:
		print('El triangulo no existe!!!!111')
def cuadrado():
	print("Area y perimtro del cuadrado: ")
	lado = float(input('Ingrese el lado del cuadrado: '))
	if(lado>0):
		area = lado*lado
		perimetro = lado*4
		print('Perimetro es: '+str(round(perimetro,2))+'Area: '+str(round(area,2)))
	else:
		print('Datos incorrectos!!')
	
def rectangulo():
	print("Area y perimtro del rectangulo")
	base = float(input('Ingrese la base del rectangulo: '))
	altura = float(input('Ingrese la altura del rectangulo: '))
	if(base>0 and altura>0):
		area = base* altura
		perimetro = 2*(base+altura)
		print('Perimetro es: '+str(round(perimetro,2))+'Area: '+str(round(area,2)))
	else:
		print('Datos incorrectos!!')
		
def pentagono():
	print("Area y perimtro del Pentagono")
	radio = float(input('Ingrese el radio del poligono: '))
	longitud = float(input('Ingrese la longitud del lado: ')) 
	if(radio>0 and longitud>0):
		apotema = math.sqrt(radio**2-(longitud/2)**2)
		perimetro = longitud*5
		print('Perimetro= '+str(perimetro))
		print('Area=: '+str((perimetro*apotema)/2))
	else:
		print('Datos incorrectos!!!')

continuar ='s'
while (continuar=='s'):

	print('-----------------Menu-------------')
	print('1.- Area y perimetro del triangulo')
	print('2.- Area y perimetro del cuadrado')
	print('3.- Area y perimetro del rectangulo')
	print('4.- Area y perimetro del pentagono')
	print('5.- Salir')
	opcion=str(input('ingrese la opcion: '))

	if(opcion=='1'):
		triangulo()
	elif(opcion=='2'):
		cuadrado()
	elif(opcion=='3'):
		rectangulo()
	elif(opcion=='4'):
		pentagono()
	elif(opcion=='5'):
		continuar='n'
	else:
		print('Ingrese la opcion correcta!!') 

