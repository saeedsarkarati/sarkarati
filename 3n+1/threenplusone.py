a = []
for i in range(3,131801,2):
	n = i
	while n > 1:
		if n in a:
			break
		if n%2 == 1:
			print (n, end = ' ')
			a.append(n)
		if n%2 == 0:
			n = n //2
		else: 
			n =3 * n + 1
	# ~ if (i+1) % 40000 == 0:
		# ~ print (i, a, len(a))
	print(n)
