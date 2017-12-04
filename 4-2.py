#
#     		 		Advent of Code 2017
# 					Day: 04 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#


with open('inputs/4.txt', 'r') as input_file:
	rows = input_file.readlines()

counter = 0;
for row in rows:
	row = row.rstrip('\n')
	if len(set(row.split(' '))) == len(row.split(' ')):

		words = []
		for word in row.split(' '):
			word = list(word)
			word.sort()
			words.append(''.join(word))
		if (len(set(words)) == len(words)):
			counter += 1

print("Valid passphares: ", counter)
