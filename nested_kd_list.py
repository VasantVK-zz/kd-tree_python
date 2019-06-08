# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/07/19

from random import *
from math import *

def insertion(point, tree_node, trav): # Parameters: (Point, Tree, Current Depth)
	dim = trav % d

	if (point[dim] < tree_node[0][dim]):
		if (tree_node[1] == None):
			new_node = [point, None, None]
			tree_node[1] = new_node
		else:
			insertion(point, tree_node[1], trav + 1)
	if (point[dim] >= tree_node[0][dim]):
		if  (tree_node[2] == None):
			new_node = [point, None, None]
			tree_node[2] = new_node
		else: 
			insertion(point, tree_node[2], trav + 1) 

	return tree_node

def nested_kd_list(x):
	tree_node = [None, None, None] # Structure: [Point, Left Node, Right Node]
	
	i = 0
	while i < len(x):
		if i == 0:
			tree_node[0] = x[i]
		else:
			trav = 0
			#print(x[i])
			tree_node = insertion(x[i], tree_node, trav)
		#print(tree_node)
		
		i += 1

	return tree_node

def main():
	points1D = [(1,), (3,), (5,), (5,), (2,)]
	points2D = [(1,10), (3,5), (5,4), (5,3), (2,8)]
	points3D = [(1,10,7), (3,5,3), (5,4,0), (5,3,6), (2,8,9)]
	pointList = [points1D, points2D, points3D]
	#dimensions = 2
	for sample_points in pointList:
		dimensions = len(sample_points[0])
		global d
		d = dimensions
		nested_kd_list(sample_points)

main()