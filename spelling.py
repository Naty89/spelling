def spelling(str):
    x = []
    for i in range(len(str)+1):
    	x.append(str[0:i])
    return(x)

print(spelling("important"))