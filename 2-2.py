#
#     		 		Advent of Code 2017
# 					Day: 02 - Puzzle: 2
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#


def find(row):
	row2 = row
	for element in row:
		for element2 in row:
			if (element != element2) and ((int(element) % int(element2)) == 0):
				return (int(element) / int(element2))


checksum = 0
with open('inputs/2.txt', 'r') as input_file:
	rows = input_file.readlines()

for row in rows:
	row = row.split('\t')
	checksum = checksum + find(row)

print("Checksum: ", int(checksum))
