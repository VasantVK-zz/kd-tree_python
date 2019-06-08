# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/07/19

import matplotlib.pyplot as plt
from random import *
from math import *


def insertion(point, tree_node, cur_dep): # Parameters: (Point, Tree, Current Depth)
	dim = cur_dep % d

	if (point[dim] < tree_node[0][dim]):
		if (tree_node[1] == None):
			new_node = [point, None, None]
			tree_node[1] = new_node
		else:
			insertion(point, tree_node[1], cur_dep + 1)
			
	if (point[dim] >= tree_node[0][dim]):
		if  (tree_node[2] == None):
			new_node = [point, None, None]
			tree_node[2] = new_node
		else: 
			insertion(point, tree_node[2], cur_dep + 1) 

	return tree_node

def nested_kd_list(x):
	tree_node = [None, None, None] # Structure: [Point, Left Node, Right Node]
	
	i = 0
	while i < len(x):
		if i == 0:
			tree_node[0] = x[i]
		else:
			cur_dep = 0
			tree_node = insertion(x[i], tree_node, cur_dep)
		print(tree_node)
		
		i += 1

	return tree_node

# Attempting to create a recursive-like structure to create a plot
def kd_plot(node_list):
	dep = 0
	dep_list = []
	i_list = []

	for i in range(0, len(node_list)-1):
		if isinstance(node_list[i], int):
			# plot
		else:
			dep_list.append(dep)
			i_list.append(i)
		if len(i_list) == 0 and i_list[len(i_list)-1] != 2:



def main():
	# Non-Random Tests
	# points1D = [(1,), (3,), (5,), (5,), (2,)]
	points2D = [(1,10), (3,5), (5,4), (5,3), (2,8)]
	# points3D = [(1,10,7), (3,5,3), (5,4,0), (5,3,6), (2,8,9)]
	# pointList = [points1D, points2D, points3D]
	dimensions = 2
	# for sample_points in pointList:
	# 	dimensions = len(sample_points[0])
	global d
	d = dimensions
	node_list = nested_kd_list(points2D)

	if d == 2:
		kd_plot(node_list)



main()