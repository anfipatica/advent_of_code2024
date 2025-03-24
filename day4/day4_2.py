'''
123
456
789

1 -> x-1, y-1
2 -> x  , y-1
3 -> x+1, y-1
4 -> x-1, y
5 -> x  , y
6 -> x+1, y
7 -> x-1, y+1
8 -> x  , y+1
9 -> x+1, y+1
'''

def	access_matrix(file:tuple, y:int, x:int) -> int:

	if (x < 0 or y < 0 or y >= len(file) or x >= len(file[y])):
		return -1
	else :
		return file[y][x]

#/
def	find_mas_x2(y: int, x: int, file: tuple) -> int:

	if (access_matrix(file, y-1, x+1) == 'M'):
		if (access_matrix(file, y+1, x-1) == 'S'):
			return 1
		else:
			return 0
	elif (access_matrix(file, y-1, x+1) == 'S'):
		if (access_matrix(file, y+1, x-1) == 'M'):
			return 1
		else:
			return 0
	return 0


#\
def	find_mas_x1(y: int, x: int, file: tuple) -> int:

	if (access_matrix(file, y-1, x-1) == 'M'):
		if (access_matrix(file, y+1, x+1) == 'S'):
			return (find_mas_x2(y, x, file))
		else:
			return 0
	elif (access_matrix(file, y-1, x-1) == 'S'):
		if (access_matrix(file, y+1, x+1) == 'M'):
			return (find_mas_x2(y, x, file))
		else:
			return 0
	return 0
	
	
def	start_find(file:tuple) -> int:

	y = 0
	result = 0

	while (y < len(file)):
		x = 0
		while (x < len(file[y])):
			if file[y][x] == 'A':
				result += find_mas_x1(y, x, file)
			x += 1
		y += 1
	return result


def	main():

	with open("text.txt", "r") as file:
		print(start_find(tuple(file)))


if	__name__ == "__main__":
	main()

