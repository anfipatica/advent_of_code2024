
FILE = "/home/anfi/Escritorio/adventofcode/day3/input.txt"

def	get_num(line: str, i: int) -> int:
	n = 0

	while (line[i].isdigit() == True):
		n *= 10
		n += int(line[i])
		i += 1
	if (n == 0):
		return -1, i
	return n, i

def	mul(line: str, i):
	
	j = i
	n1 = 0
	n2 = 0
	n1, i = get_num(line, i)
	if (line[i] == ',' and n1 != -1):
		i += 1
	else:
		return 0
	n2, i = get_num(line, i)
	if (line[i] == ')' and n2 != -1):
		return (n1 * n2)
	else:
		return 0

def	get_next_dont(line, i) -> int:

	next_do =  line.find("do()", i)
	next_dont = line.find("don't()", i)

	while (next_dont < next_do and next_dont != -1):
		next_dont = line.find("don't()", next_dont + 1)
	return (next_dont)

def	check_line(line) -> int:

	i = 0
	last_dont = False
	n = 0
	
	aux = line.find("don't()", i)
	while (i < len(line) and i != -1):
		i = line.find("mul(", i)
		if (i >= aux and last_dont == False):
			aux = get_next_dont(line, i)
			if (aux == -1 and last_dont == False):
				last_dont = True
				i = line.find("do()", i)
			else:
				i = line.find("do()", i)
			if i != -1:
				i = line.find("mul(", i)
		if (i == -1):
			break
		n += mul(line, i + 4)
		i += 1

	return n

def	main():

	n = 0
	new_line: str = ""

	with open(FILE, "r") as file:
		for line in file:
			new_line += line.strip()
		n = check_line(new_line)

	print("n === %d" %(n))

if __name__ == "__main__":
	main()