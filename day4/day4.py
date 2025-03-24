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

SEARCH = "XMAS"

def	access_matrix(file:tuple, y:int, x:int) -> int:

	if (x < 0 or y < 0 or y >= len(file) or x >= len(file[y])):
		return -1
	else :
		return file[y][x]

def	find_xmas(y: int, x: int, i: int, dir: int, file:tuple) -> int:

	if (i == len(SEARCH)):
		return 1

	if (dir == 1 and access_matrix(file, y-1, x-1) == SEARCH[i]):
		return find_xmas(y-1, x-1, i+1, dir, file)
	if (dir == 2 and access_matrix(file, y-1, x) is SEARCH[i]):
		return find_xmas(y-1, x, i+1, dir, file)
	if (dir == 3 and access_matrix(file, y-1, x+1) is SEARCH[i]):
		return find_xmas(y-1, x+1, i+1, dir, file)
	if (dir == 4 and access_matrix(file, y, x-1) is SEARCH[i]):
		return find_xmas(y, x-1, i+1, dir, file)
	if (dir == 6 and access_matrix(file, y, x+1) is SEARCH[i]):
		return find_xmas(y, x+1, i+1, dir, file)
	if (dir == 7 and access_matrix(file, y+1, x-1) is SEARCH[i]):
		return find_xmas(y+1, x-1, i+1, dir, file)
	if (dir == 8 and access_matrix(file, y+1, x) is SEARCH[i]):
		return find_xmas(y+1, x, i+1, dir, file)
	if (dir == 9 and access_matrix(file, y+1, x+1) is SEARCH[i]):
		return find_xmas(y+1, x+1, i+1, dir, file)

	return 0

def	set_direction(y: int, x: int, file: tuple) ->int:

	result = 0

	if (access_matrix(file, y-1, x-1) is SEARCH[1]):
		result += find_xmas(y-1, x-1, 2, 1, file)
	if (access_matrix(file, y-1, x) is SEARCH[1]):
		result += find_xmas(y-1, x, 2, 2, file)
	if (access_matrix(file, y-1, x+1) is SEARCH[1]):
		result += find_xmas(y-1, x+1, 2, 3, file)
	if (access_matrix(file, y, x-1) is SEARCH[1]):
		result += find_xmas(y, x-1, 2, 4, file)
	if (access_matrix(file, y, x+1) is SEARCH[1]):
		result += find_xmas(y, x+1, 2, 6, file)
	if (access_matrix(file, y+1, x-1) is SEARCH[1]):
		result += find_xmas(y+1, x-1, 2, 7, file)
	if (access_matrix(file, y+1, x) is SEARCH[1]):
		result += find_xmas(y+1, x, 2, 8, file)
	if (access_matrix(file, y+1, x+1) is SEARCH[1]):
		result += find_xmas(y+1, x+1, 2, 9, file)

	return (result)
	
def	start_find(file:tuple) -> int:

	y = 0
	result = 0

	while (y < len(file)):
		x = 0
		while (x < len(file[y])):
			if file[y][x] is SEARCH[0]:
				result += set_direction(y, x, file)
			x += 1
		y += 1
	return result


def	main():

	with open("text.txt", "r") as file:
		print(start_find(tuple(file)))


if	__name__ == "__main__":
	main()

