a = []
la = 0
for i in range(3,10000000000000+10000,1):
	n = i
	while n > 1:
		# ~ if n < i:
			# ~ break
		if n in a:
			break
		a.append(n)
		if n%2 == 1:
			n =3 * n + 1
		if n%2 == 0:
			n = n //2
	b = input()
	# ~ if (i+1) % 40000 == 0:
		# ~ print (i, a, len(a))
	print()
	print(i, '-----', len(a), len(a) - la)
	la = len(a)
