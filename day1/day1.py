from collections import Counter
#input = open("./day1/input.txt", "r")

#print("----> %s" %(input.read()))
#Para leer el contenido de input.

list1 = []
list2 = []
num = 0

with open("./day1/input.txt", "r") as input:
	for line in input:
		temp = line.split()
		list1.append(int(temp[0]))
		list2.append(int(temp[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
	#num += max(list1[i], list2[i]) - min(list1[i], list2[i])
	num += abs(list1[i] - list2[i])
print(num)

num = 0
list2_counter = Counter(list2)
for i in range(len(list1)):
	num +=  list1[i] * list2_counter[list1[i]]

print(num)
