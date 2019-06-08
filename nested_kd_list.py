# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/06/19

from random import *
from math import *

def insertion(point, tree_node, d, trav): # Parameters: (Point, Tree, Dimension, Current Depth)
	dim = trav % d
	if (point[dim] < tree_node[0][dim]) and (tree_node[1] == None):
		new_node = [point, None, None, trav]
		tree_node[1] = new_node
	elif (point[dim] < tree_node[0][dim]) and (tree_node[1] != None): 
		insertion(point, tree_node[1], d, trav + 1)
	if (point[dim] >= tree_node[0][dim]) and (tree_node[2] == None): 
		new_node = [point, None, None, trav]
		tree_node[2] = new_node
	elif (point[dim] >= tree_node[0][dim]) and (tree_node[2] != None):  
		insertion(point, tree_node[2], d, trav + 1) 

	return tree_node

def nested_kd_list(x, d):
	tree_node = [None, None, None, -1] # Structure: [Point, Left Node, Right Node, Current Depth]
	
	i = 0
	while i < len(x):
		if i == 0:
			tree_node[0] = x[i]
		else:
			trav = 0
			print(x[i])
			tree_node = insertion(x[i], tree_node, d, trav)
		print(tree_node)
		
		i += 1

	return tree_node

def main():
	points1 = [(1,10), (3,5), (5,4), (5,3), (2,8)]
	dimensions = 2
	nested_kd_list(points1, dimensions)

main()