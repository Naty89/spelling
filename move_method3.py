def move(str):


	return ''.join([ chr(int(ord(x)) - 25) if x=='z' or x == 'Z' else chr(int(ord(x) + 1)) for x in str])

print(move("zebra"))	

