#
#     		 		Advent of Code 2017
# 					Day: 07 - Puzzle: 1
# 					  Giuseppe Luzzi
# 	https://github.com/GiuseppeLuzzi/advent-of-code-2017
#

import re

with open('input.txt', 'r') as input_file:
	disks_raw = input_file.read()

disks = []
parents = []
childs = []
for disk in disks_raw.split('\n'):
	match = re.match(r'([a-z]*) \(([0-9]*)\)( -> )?([a-z, ]*)?', disk)
	dep = []
	if match.group(3) is not None:
		dep = match.group(4).split(', ')
	disks.append({"id": match.group(1), "w": int(match.group(2)), "childs": dep})
	parents.append(match.group(1))
	childs.append(dep)

for child in childs:
	if len(child) > 0:
		for subchild in child:
			if subchild in parents:
				parents.remove(subchild)
print("Parent: %s" % (parents[0]))