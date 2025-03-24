import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
END = -1


def	find_square(y: int, x: int, game_map: tuple)-> int:
	aux_x = str(game_map[y]).find('#', x)
	if (aux_x == -1):
		return 0

	while(y < len(game_map)):
		print("y = %d, x = %d, aux = %d\n" %(y, x, aux_x))
		if (game_map[y][x] == '#' and game_map[y][aux_x]  == '#'):
			return 1
		y += 1
	return 0

def	start_movement(game_map: tuple):

	total_loops = 0
	y = 0

	while (y < len(game_map)):
		x = 0
		while (x < len(game_map[y]) - 1):
			if (game_map[y][x] != '#'):
				total_loops += find_square(y, x, game_map)
			x += 1
		y += 1
	print(total_loops)


def	main():

	with open("input.txt", "r") as file:
		start_movement(tuple(file))




if __name__ == "__main__":
	main()