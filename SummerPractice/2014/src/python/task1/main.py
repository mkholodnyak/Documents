# -*- coding: utf8 -*-
import math, random

#Algoritm Evklida
def NOD(x, y):
	if (type(x) != int)or(type(y) != int):
		print 'Not int'
		return

	x,y = max(x,y), min (x,y)
	while x != y:
		if y == 0:
			break
		x,y = y, x % y
	
	return int(x)


#Proverka na prostotu
def IsSimple(n):
    i = 2
    j = 0 # flag
    while i**2 <= n and j != 1:
        if n%i == 0:
            j = 1
        i += 1
    if j == 1:
        return False
    else:
        return True


#Vyvesti na jekran vse natural'nye chisla iz diapazona ot A do V v zapisi kotoryh cifra 7 vstrechaetsja N raz. 
#Pri otsutstvii chisel s ukazannymi svojstvami vydat' na jekran soobshhenie "Trebuemyh chisel net". 
#Granicy diapazona A i V i znachenie N vyvesti s klaviatury. (Rekomenduetsja ispol'zovat' metody raboty so strokami)
def Task1():
	A = int(raw_input('Input A: '))
	B = int(raw_input('Input B: '))
	N = int(raw_input('Input N: '))


	if (type(A) != int)or(type(B) != int):
		print 'Not int'
		return

	if A > B:
		A,B = B,A

	number = '7' # Iskomaja cifra
	for currentNumber in range(A,B+1):
		if str(currentNumber).count(number) == N:
			print currentNumber


#Vvesti natural'noe trehznachnoe chislo. 
#Vychislit' i vyvesti na jekran chislo, poluchennoe putem "perevorota" (123 -> 321). 
#Ne ispol'zovat' metody dlja raboty so strokami.
def Task2(number):
	if (type(number) != int)or(len(str(number)) != 3):
		print 'Invalid argument'
		return

	result_number = 0;
	while number>0:
		result_number = result_number*10 + number % 10
		number = number / 10
	
	print result_number 


#Vvesti natural'noe chetyrehznachnoe desjatichnoe chislo, 
#sformirovat' i vyvesti na jekran priznak "schastlivogo chisla" 
#(summa pervyh dvuh cifr ravne summe poslednih dvuh).
#Ne ispol'zovat' metody dlja raboty so strokami.
def Task3(number):
	if (type(number) != int)or(len(str(number)) != 4):
		print 'Invalid argument'
		return

	first_part = ((number / 100)% 10) + (number / 1000)
	second_part = (number % 10) + ((number / 10) % 10)
	if  first_part != second_part:
		print 'Obychnoe chislo'
	else:
		print 'Schastlivoe chislo'


#Realizovat' metod vychislenija faktoriala.
def Task4(n):
	if type(n) != int:
		print 'Not int'
		return 0

	if n == 1:
		return 1

	return n * Task4(n-1)


#Vychislit' znachenie funkcii Y=F(X), zadannoj grafikom
def Task5(x):
	if type(x) != int and type(x)!= float:
		print 'NaN'
		return

	if x <= -0.5:
		return 0.5
	elif x <= 0:
		return x+1
	elif x <= 1:
		return x*x -1
	else:
		return x-1

#Vychislit' znachenie funkcii Y=F(X), zadannoj grafikom
def Task6(x):
	if type(x) != int and type(x)!= float:
		print 'NaN'
		return

	if x <= 0.5:
		return math.sin(math.pi / 2)
	else:
		return math.sin((x-1)* (math.pi / 2))


#Sokratit' vvedennuju obyknovennuju drob'. 
#Drob' vvoditsja s klaviatury  v vide chislitelja i znamenatelja. 
#Kak vspomogatel'nuju funkciju opredelit' i ispol'zovat' metod dlja vychislenija naibol'shego obshhego delitelja dvuh celyh chisel.
def Task8():
	A = int(raw_input('Input A: '))
	B = int(raw_input('Input B: '))

	result = NOD(A, B)

	return str(A / result) + '/' + str(B / result)


#Najti i raspechatat' vse natural'nye trehznachnye chisla, ravnye summe kubov svoih cifr.
def Task9():
	for i in range(100, 1000):
		first_number = i / 100
		second_number = (i / 10) % 10
		third_number = i % 10

		result = first_number**3 + second_number**3 + third_number**3
		if result == i:
			print i


#Dany natural'nye chisla n i k. Opredelit' k-ju sprava cifru chisla n.
def Task10(n,k):
	return str(n)[-k]
 
#Vychislit' k-oe chislo Fibonachchi
def Task11(k):
	previous, current = 0, 1
	while k > 0:
		previous, current = current, previous + current
		k -= 1
	return previous

#Vvesti natural'noe chislo N. Odnomernyj massiv razmerom N zapolnit' sluchajnymi chislami. 
#Vyvesti na jekran kolichestvo prostyh chisel v massive 
#(Dlja udobstva proverki dopolnitel'no vyvesti sgenerirovannyj massiv).
def Task12():
	N = int(raw_input('Input N: '))
	array = [
		random.randint(0, 100) for i in xrange(N)
	]

	for element in array:
		if IsSimple(element):
			print element


#Dan celochislennyj massiv A. Najti v nem dva naimen'shih jelementa.
def Task13():
	N = int(raw_input('Input N: '))
	array = [
		random.randint(0, 5) for i in xrange(N)
	]

	print array
	min1 = min(array)
	array.remove(min1)
	min2 = min(array)

	return	min1, min2

#Sgenerirovat' (i vyvesti) dvumernuju matricu razmerom N*N (N<20). 
#Najti summu ee jelementov, nahodjashhihsja na diagonali, 
#i summu jelementov na diagonali, "ortogonal'noj" glavnoj.
def Task14():
	N = int(raw_input('Input N: '))
	array = [
	[random.randint(0, 100) for x in xrange(N)] for x in xrange(N)
	] 

	summ1 = 0
	summ2 = 0
	for number in xrange(N):
		summ1 += array[number][number]
		summ2 += array[number][N-(number+1)]
	print array

	return summ1, summ2

#Sformirovat' celochislennyj massiv A(75), 
#jelementami kotorogo javljajutsja sluchajnye chisla iz diapazona [-5, 20].
#Najti sredi ego jelementov dva, raznost' kotoryh imeet naibol'shee znachenie.
def Task15():
	array = [
	random.randint(-5,21) for i in range(0, 75)
	]

	maximum = -5 - 20
	k = l = 0
	for i in array:
		for j in array:
			if i - j > maximum:
				maximum = i - j
				k, l = i, j
	return k, l

#Najti naibol'shij obshhij delitel' (NOD) dvuh vvedennyh natural'nyh chisel, 
#ispol'zuja algoritm Evklida. Algoritm Evklida: 
#vychitaem iz bol'shego chisla men'shee do teh por, 
#poka oni ne sravnjajutsja; poluchennoe v rezul'tate chislo i est' NOD
def Task16(x, y):
	return NOD(x, y)
