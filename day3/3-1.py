#
#     		 		Advent of Code 2017
# 					Day: 04 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#

import numpy

to = 368078

def nextDirection(val):
	val += 1
	if val > 4:
		val = 1
	return val

matrix_size = int(numpy.ceil(numpy.sqrt(to)))
if (matrix_size % 2 == 0):
	matrix_size += 1

half = int(matrix_size/2)

grid = []
for _ in range(0, matrix_size):
	grid.append([0] * matrix_size)

x = half
y = half
last_x = half
last_y = half
c = 1

s = 1
max_step = 1
direction = 1
first = True
for item in range(0, to):
	grid[y][x] = c
	last_y = y
	last_x = x
	c += 1
	if s > 0:
		s -= 1
	else:
		direction = nextDirection(direction)
		if first == True:
			s = max_step - 1
			first = False
		else:
			s = max_step
			max_step += 1
			first = True

	if direction == 1:
		# Right
		x += 1
	elif direction == 2:
		# Up
		y -= 1
	elif direction == 3:
		# Left
		x -= 1
	elif direction == 4:
		# Down
		y += 1


distance = abs(last_x - half) + abs(last_y - half)
print("(%d;%d) Distance: %d" % (last_x,last_y, distance))
