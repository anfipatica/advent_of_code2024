#ASCEND = 0 1 2 3 4
#DESCEND = 4 3 2 1 0

def	check_line(arr):
	i = 0
	error = 0
	if (1 < len(arr) and int(arr[0]) < int(arr[1])):
		ascend = True
	else:
		ascend = False
	while i + 1 < len(arr):
		n = int(arr[i]) - int(arr[i + 1])
		if (n == 0):
			return i
		elif (ascend is True and not (n <= 0 and n >= -3)):
			return i
		elif (ascend is False and not (n >= 0 and n <= 3)):
			return i
		i += 1
	return -1
def intermediate(arr):

	i = 0
	if (check_line(arr) == -1):
		return 1
	while (i < len(arr)):
		copy = arr.copy()
		del copy[i]
		if (check_line(copy) == -1):
			return 1
		i += 1
	return 0


def main():
	ok = 0
	with open("/home/anfi/Escritorio/adventofcode/day2/input.txt","r") as file:
		for line in file:
			arr = line.split()
			ok += intermediate(arr)
	print(ok)



if __name__ == "__main__":
	main()