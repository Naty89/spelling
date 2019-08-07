def move(str):
	c = []
	x = []
	l = []
	p = []
	for i in range(97,123):
		c.append(chr(i))
	for a in range(98,123):
		x.append(chr(a))
	x.append("a")
	for y in str:
		for e in range(len(c)):
			if y == c[e]:
				l.append(e)
	for o in range(len(l)):
		for  b in range(len(x)):
			if l[o] == b:
				p.append(x[b])
			else:
				pass
	return "".join(p)

print(move("zebra"))	

