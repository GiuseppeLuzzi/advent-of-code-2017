#
#     		 		Advent of Code 2017
# 					Day: 02 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#

checksum = 0

with open('input.txt', 'r') as input_file:
	rows = input_file.readlines()

for row in rows:
	row = row.split('\t')
	row_min = int(row[0])
	row_max = int(row[0])
	for element in row:
		if int(element) < row_min:
			row_min = int(element)
		if int(element) > row_max:
			row_max = int(element)
	checksum = checksum + (row_max-row_min)

print("Checksum: %d" % (checksum))
