# -*- coding: utf-8 -*-
"""
constante de conway

Ejemplo:

x_0 = 1  (un uno) =>
x_1 = 11 (dos uno) =>
x_2 = 21 (un dos y un uno) => 
x_3 = 1211 (un uno, un dos, y dos uno) =>
x_4 = 111221 (tres uno, dos dos, y un uno) =>
x_5 = 312211 ...

Ver más: https://es.wikipedia.org/wiki/Constante_de_Conway

"""

try:
	x_0 = int(raw_input('Input '))
	n = int(raw_input('Iterations '))
except ValueError:
	print ('{0:^40}'.format('Error: Is not a number'))

x_i = str(x_0)
list_x_i = []
previous_x = x_i[0]
count_x = 1
next_x = ''
print 'Cownway sequence:'
for i in xrange(0, n):
	for j in xrange(1, len(x_i)):
		if previous_x == x_i[j]:
			count_x += 1
		else:
			next_x = next_x + str(count_x) + str(previous_x)
			previous_x = x_i[j] 
			count_x = 1
	next_x = next_x + str(count_x) + str(previous_x)
	print next_x
	x_i = next_x
	previous_x = x_i[0]
	count_x = 1
	next_x = ''



	