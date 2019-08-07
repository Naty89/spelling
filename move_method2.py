def move(str):
	l = []
	for i in str:
		if i == 'z' or i == 'Z':
	 		l.append(chr(int(ord(i)) - 25))
	 	else:
	 		l.append(chr(int(ord(i))+1))

	return "".join(l)

print(move("zebra"))	

