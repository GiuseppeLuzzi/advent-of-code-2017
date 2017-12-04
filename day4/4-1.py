#
#     		 		Advent of Code 2017
# 					Day: 04 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#


with open('input.txt', 'r') as input_file:
	rows = input_file.readlines()

counter = 0;
for row in rows:
	row = row.rstrip('\n')
	if len(set(row.split(' '))) == len(row.split(' ')):
		counter += 1
print("Valid passphares: %d" % (counter))
