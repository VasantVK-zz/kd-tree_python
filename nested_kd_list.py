# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/06/19

from random import *
from math import *

def insertion(point, tree_node, d, trav):
	dim = trav % d
	if (point[dim] < tree_node[0][dim]) and (tree_node[1] == None):
		new_node = [point, None, None, trav]
		tree_node[1] = new_node
	if (point[dim] >= tree_node[0][dim]) and (tree_node[2] == None): 
		new_node = [point, None, None, trav]
		tree_node[2] = new_node
	else if (point[dim] >= tree_node[0][dim]) and (tree_node[1] != None): 
		return insertion(point, tree_node[1], d, trav + 1)
	else if (point[dim] >= tree_node[0][dim]) and (tree_node[2] != None):  
		return insertion(point, tree_node[2], d, trav + 1) 

def nested_kd_list(x, d):
	tree_node = [None, None, None, 0] # Structured as [Point, Left Node, Right Node, Current Depth]
	
	i = 0
	while i < len(x):
		if i = 0:
			tree_node[0] = x[i]
		else:
			trav = 0
			tree_node = insertion(x[i], tree_node, d, trav)
		
		i += 1


def main():
	example = [(1,10), (3,5), (5,4), (5,3), (2,8)]
	d = 2
	nested_kd_list(example, d)

main()