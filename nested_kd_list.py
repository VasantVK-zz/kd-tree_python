# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/07/19

import matplotlib.pyplot as plt
from random import *
from math import *


xy_size = 11 # Square plot

def insertion(point, tree_node, cur_dep): # Parameters: (Point, Tree, Current Depth)
	dim = cur_dep % d

	if (point[dim] < tree_node[0][dim]):
		if (tree_node[1] == None):
			new_node = [point, None, None]
			tree_node[1] = new_node
			l_or_r = 0
		else:
			insertion(point, tree_node[1], cur_dep + 1)
			
	if (point[dim] >= tree_node[0][dim]):
		if  (tree_node[2] == None):
			new_node = [point, None, None]
			tree_node[2] = new_node
			l_or_r = 1
		else: 
			insertion(point, tree_node[2], cur_dep + 1) 

	kd_plot(point, dim, l_or_r)

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


def kd_plot(point, dim, l_or_r): # (Point, Mod Dimension, Left/Right)
	plt.plot(point[0], point[1], color='black', marker='o') 

	if len(x_axis_list) == 0: # Will always start with x_axis_list
		x = [point[dim], point[dim]]
		y = [0, xy_size]
	else:
		if l_or_r == 0:
			if dim == 0:
				for a in x_axis_list:
			elif dim == 1:
				for b in y_axis_list:	

		elif l_or_r == 1:
			if dim == 0:
				for c in x_axis_list:
			elif dim == 1:
				for d in y_axis_list:

	plt.plot(x, y, color='black', marker='-')

	if dim == 0:
		x_axis_list.append(point)
	elif dim == 1:
		y_axis_list.append(point)




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
	global x_axis_list
	global y_axis_list
	x_axis_list = []
	y_axis_list = []

	d = dimensions
	node_list = nested_kd_list(points2D)



main()