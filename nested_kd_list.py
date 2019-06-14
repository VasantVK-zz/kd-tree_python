# Created by Vasant Kurvari
# Begun: 06/06/19
# Last Update: 06/07/19

import matplotlib.pyplot as plt
from random import *
from math import *


xy_size = 20 # Square plot

def insertion(point, tree_node, cur_dep): # Parameters: (Point, Tree, Current Depth)
	dim = cur_dep % d

	if (point[dim] < tree_node[0][dim]):
		if (tree_node[1] == None):
			new_node = [point, None, None]
			tree_node[1] = new_node
			l_or_r = 0
			kd_plot(point, dim, l_or_r)
		else:
			insertion(point, tree_node[1], cur_dep + 1)
			
	if (point[dim] >= tree_node[0][dim]):
		if  (tree_node[2] == None):
			new_node = [point, None, None]
			tree_node[2] = new_node
			l_or_r = 1
			kd_plot(point, dim, l_or_r)
		else: 
			insertion(point, tree_node[2], cur_dep + 1) 

	

	return tree_node


def nested_kd_list(x):
	tree_node = [None, None, None] # Structure: [Point, Left Node, Right Node]
	
	i = 0
	while i < len(x):
		if i == 0:
			tree_node[0] = x[i]
			kd_plot(x[i], 1, 0)
		else:
			cur_dep = 0
			tree_node = insertion(x[i], tree_node, cur_dep)
		# print(tree_node)
		
		i += 1

	return tree_node


def kd_plot(point, dim, l_or_r): # (Point, Mod Dimension, Left/Right)
	plt.plot(point[0], point[1], color='black', marker='o') 
	dim = 1 - dim
	max_list = []
	min_list = []

	if l_or_r == 0: # 'Left or Right' is only used to determine where the line should go if it falls exactly on another line
		if dim == 0:
			new_dim = 1 - dim
			for d in y_axis_list:
				if point[new_dim] <= d[0][new_dim] and d[1][new_dim] >= point[dim] and d[1][dim] <= point[dim]:
					max_list.append(d[0][new_dim] - point[new_dim])
				if point[new_dim] > d[0][new_dim] and d[1][new_dim] >= point[dim] and d[1][dim] <= point[dim]:
					min_list.append(d[0][new_dim] - point[new_dim])
			
			y_1 = max(min_list) + point[new_dim]
			y_2 = min(max_list) + point[new_dim]
			y = [y_1, y_2]
			x = [point[dim], point[dim]]

		elif dim == 1:
			new_dim = 1 - dim
			for d in x_axis_list:
				if point[new_dim] <= d[0][new_dim] and d[2][dim] >= point[dim] and d[2][new_dim] <= point[dim]:
					max_list.append(d[0][new_dim] - point[new_dim])
				if point[new_dim] > d[0][new_dim] and d[2][dim] >= point[dim] and d[2][new_dim] <= point[dim]:
					min_list.append(d[0][new_dim] - point[new_dim])
			
			x_1 = max(min_list) + point[new_dim]
			x_2 = min(max_list) + point[new_dim]
			x = [x_1, x_2]
			y = [point[dim], point[dim]]

	elif l_or_r == 1:
		if dim == 0:
			new_dim = 1 - dim
			for d in y_axis_list:
				if point[new_dim] < d[0][new_dim] and d[1][new_dim] >= point[dim] and d[1][dim] <= point[dim]:
					max_list.append(d[0][new_dim] - point[new_dim])
				if point[new_dim] >= d[0][new_dim] and d[1][new_dim] >= point[dim] and d[1][dim] <= point[dim]:
					min_list.append(d[0][new_dim] - point[new_dim])
			
			y_1 = max(min_list) + point[new_dim]
			y_2 = min(max_list) + point[new_dim]
			y = [y_1, y_2]
			x = [point[dim], point[dim]]

		elif dim == 1:
			new_dim = 1 - dim
			for d in x_axis_list:
				if point[new_dim] < d[0][new_dim] and d[2][dim] >= point[dim] and d[2][new_dim] <= point[dim]:
					max_list.append(d[0][new_dim] - point[new_dim])
				if point[new_dim] >= d[0][new_dim] and d[2][dim] >= point[dim] and d[2][new_dim] <= point[dim]:
					min_list.append(d[0][new_dim] - point[new_dim])
			
			x_1 = max(min_list) + point[new_dim]
			x_2 = min(max_list) + point[new_dim]
			x = [x_1, x_2]
			y = [point[dim], point[dim]]


	plt.plot(x, y, color='black')

	if dim == 0:
		x_axis_list.append([point,x,y])  # Goes Up-Down
	elif dim == 1:
		y_axis_list.append([point,x,y]) # Goes Left-Right




def main():
	# Non-Random Tests
	# points1D = [(1,), (3,), (5,), (5,), (2,)]
	# Alt test points 2D 
	# points2D = [(1,10), (3,5), (5,4), (5,3), (2,8), (3,2)]
	points2D = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
	# points3D = [(1,10,7), (3,5,3), (5,4,0), (5,3,6), (2,8,9)]
	# pointList = [points1D, points2D, points3D]
	dimensions = 2
	# for sample_points in pointList:
	# 	dimensions = len(sample_points[0])
	global d
	global x_axis_list
	global y_axis_list
	x_axis_list = [[(0,0),[0,xy_size],[0,xy_size]], [(xy_size, xy_size),[0,xy_size],[0,xy_size]]]
	y_axis_list = [[(0,0),[0,xy_size],[0,xy_size]], [(xy_size, xy_size),[0,xy_size],[0,xy_size]]]

	d = dimensions
	node_list = nested_kd_list(points2D)

	plt.title("KD Plot")
	plt.show()



main()