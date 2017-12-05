#
#     		 		Advent of Code 2017
# 					Day: 05 - Puzzle: 2
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#


with open('input.txt', 'r') as input_file:
	rows = input_file.read()

rows = rows.split('\n')
index = 0
steps = 0

while (index >= 0) and (index < len(rows)):
	old_index = index
	index = index + int(rows[index])
	if int(rows[old_index]) >= 3:
		rows[old_index] = int(rows[old_index]) - 1
	else:
		rows[old_index] = int(rows[old_index]) + 1
	steps += 1

print("Steps: %d" % (steps))
