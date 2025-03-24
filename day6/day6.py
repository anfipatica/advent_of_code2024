import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
END = -1

def	print_tuple(game_map: list):
	for line in game_map:
		print(line)

def	move_up(game_map: list, y: int, x: int):
	while (y > 0 and game_map[y][x] != '#'):
		game_map[y][x] = 'X'
		y -= 1
	if (y == 0 and game_map[y][x] != '#'):
		return (y, x, END)
	return (y + 1, x, RIGHT)

def	move_right(game_map: list, y: int, x: int):
	x_max = len(game_map[0])
	while (x < x_max and game_map[y][x] != '#'):
		game_map[y][x] = 'X'
		x += 1
	if (x == x_max):
		return (y, x, END)
	return (y, x - 1, DOWN)

def	move_down(game_map: list, y: int, x: int):
	y_max = len(game_map[0])

	while (y < y_max and game_map[y][x] != '#'):
		game_map[y][x] = 'X'
		y += 1
	if (y == y_max):
		return (y, x, END)
	return (y - 1, x, LEFT)

def	move_left(game_map: list, y: int, x: int):

	while (x > 0 and game_map[y][x] != '#'):
		game_map[y][x] = 'X'
		x -= 1
	if (x == 0 and game_map[y][x] != '#'):
		return (y, x, END)
	return (y, x + 1, UP)

def	move_character(game_map: list, y: int, x: int):
	dir = UP
	while True:
		if (dir == UP):
			y, x, dir = move_up(game_map, y, x)
		elif (dir == RIGHT):
			y, x, dir = move_right(game_map, y, x)
		elif (dir == DOWN):
			y, x, dir = move_down(game_map, y, x)
		elif (dir == LEFT):
			y, x, dir = move_left(game_map, y, x)
		elif (dir == END):
			break

def	start_movement(game_map: list):

	y = 0
	while (y < len(game_map)):
		x = 0
		while (x < len(game_map[y])):
			if (game_map[y][x] == '^'):
				dir = UP
				return move_character(game_map, y, x)
			x += 1
		y += 1



def	main():

	with open("input.txt", "r") as file:
		map = [list(linea.strip()) for linea in file] 
		'''
		The above line is: list comprehension
		A simpler way of writing this in just one line:

		map = list()
		for line in file:
			map.append(list(line.strip()))
		'''
		start_movement(map)
	print_tuple(map)
	total_x = 0
	for line in map:
		total_x += line.count('X')
	print(total_x)



if __name__ == "__main__":
	main()