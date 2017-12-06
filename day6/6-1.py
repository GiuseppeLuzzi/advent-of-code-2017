#
#     		 		Advent of Code 2017
# 					Day: 06 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#


with open('input.txt', 'r') as input_file:
	banks = input_file.read()

banks = banks.split('\t')
banks = list(map(int, banks))
current_i = 0
log = []
steps = 0

while True:
	current_i = banks.index(max(banks))
	val = banks[current_i]
	banks[current_i] = 0
	next_i = current_i + 1
	while (val > 0):
		if next_i >= len(banks):
			next_i = 0
		banks[next_i] += 1
		val -= 1
		next_i += 1
	steps += 1
	if '-'.join(str(x) for x in banks) in log:
		break
	log.append('-'.join(str(x) for x in banks))

print("Steps: %d" % (steps))
