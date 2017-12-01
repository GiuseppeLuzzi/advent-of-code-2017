#
#     		 		Advent of Code 2017
# 					Day: 01 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#

with open('inputs/1.txt', 'r') as input_file:
	content = input_file.read()

result = 0
content = str(content)
half = int(len(content) / 2)

for i, digit in enumerate(content):
	index = i + half

	if (index >= len(content)):
		index = index - len(content)

	if (digit == content[index]):
		result = result + int(digit)

print("Result: ", result)
