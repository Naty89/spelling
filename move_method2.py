def move(str):
	# l = []

	return ''.join([ chr(int(ord(x)) - 25) if x=='z' or x == 'Z' else chr(int(ord(x) + 1)) for x in str])


	# for i in str:
	# 	if i == 'z' or i == 'Z':
	# 		l.append(chr(int(ord(i)) - 25))
	# 	else:
	# 		l.append(chr(int(ord(i))+1))

	# return "".join(l)

print(move("zebra"))	

