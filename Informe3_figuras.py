import math
import os
import sys
def triangulo():
	print("Area y perimtro del triangulo")
	lado1 = float(input('ingrese lado 1: '))
	lado2 = float(input('ingrese lado 2: '))
	lado3 = float(input('ingrese lado 3: '))
	s = (lado1+lado2+lado3)/2
	v = s*(s-lado1)*(s-lado2)*(s-lado3)
	area = math.sqrt(v)
	print ('Area: '+str(round(area,2))+'Perimetro: '+str(round(s,2)))
def cuadrado():
	print("Area y perimtro del cuadrado")
	lado = float(input('Ingrese el lado del cuadrado: '))
	area = lado*lado
	perimetro = lado*4
	print('Perimetro es: '+str(round(perimetro,2))+'Area: '+str(round(area,2)))
def rectangulo():
	print("Area y perimtro del rectangulo")
	base = float(input('Ingrese la base del rectangulo: '))
	altura = float(input('Ingrese la altura del rectangulo: '))
	area = base* altura
	perimetro = 2*(base+altura)
	print('Perimetro es: '+str(round(perimetro,2))+'Area: '+str(round(area,2)))
def pentagono():
	print("Area y perimtro del pentagono")
	lado=float(input('Ingrse el lado:'))
	n=(lado**2)-((lado/2)**2)
	apotema=math.sqrt(n)
	perimetro=5*lado
	area=(perimetro*apotema)/2
	print('Perimetro es:'+str(round(perimetro,2))+'Area:'+str(round(area,2)))
def exagono():
	print("Area y perimtro del exagono")
	lado=float(input('Ingrse el lado:'))
	n=(lado**2)-((lado/2)**2)
	apotema=math.sqrt(n)
	perimetro=6*lado
	area=(perimetro*apotema)/2
	print('Perimetro es:'+str(round(perimetro,2))+'Area:'+str(round(area,2)))
def eptagono():
	print("Area y perimtro del eptagono")
	lado=float(input('Ingrse el lado:'))
	n=(lado**2)-((lado/2)**2)
	apotema=math.sqrt(n)
	perimetro=7*lado
	area=(perimetro*apotema)/2
	print('Perimetro es:'+str(round(perimetro,2))+'Area:'+str(round(area,2)))
def octagono():
	print("Area y perimtro del octagono")
	lado=float(input('Ingrse el lado:'))
	n=(lado**2)-((lado/2)**2)
	apotema=math.sqrt(n)
	perimetro=7*lado
	area=(perimetro*apotema)/2
	print('Perimetro es:'+str(round(perimetro,2))+'Area:'+str(round(area,2)))
while True:
	os.system('cls')
	print("Ingrese el numero de lados, de acuardo con la figura deseada:")
	try:
		opcion=int(input('Ingrese el numero de lados: '))
	except:
		print("opcion no valida")
		input()
		continue
	if opcion == 3:
		triangulo()	
		input()
		continue		
	elif opcion == 4:
		cuadrado()
		input()
		continue		
	elif opcion == 5:
		pentagono()
		input()
		continue		
	elif opcion == 6:
		exagono()
		input()
		continue		
	elif opcion == 7:
		eptagono()
		input()
		continue	
	elif opcion == 8:
		octagono()
		input()
		continue	
	else:
		print("opcion no valida")
	continue		
	#input()



