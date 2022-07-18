import numpy as np

# np.random.normal(loc=0.0, scale=1.0, size=(3,3))

# from numpy.random import normal

# normal (size=(3,3))

# m = np.random.rand(3,3)
# print(m)
# print(m.mean())

# Create a 3x3 matrix with values ranging from 0 to 8
# Create a 4x4 array with random values and find the minimum and maximum values
# Create a 5x5 matrix and fill it with a checkerboard pattern
# Create random vector of size 6 and replace the maximum value by 0
# Generate n evenly spaced intervals between 0. and 1.

# my_list = [[10,20,30,40,50],[1,2,3,4,5]]
# print(my_list, type(my_list))

# array = np.array(my_list)
# print(array, type(array))

# print(np.zeros((4,3)))
# print(np.ones((6,2)))

# print(np.random.random((3, 3)))

# my_list = [1,2,3,4,5]

# new_list = np.array(my_list) + np.array(my_list)

# print(new_list)

# rand_num = np.random.random((3, 3))
# # print(rand_num)

# mask = (0.2 < rand_num) * (rand_num < 0.6)
# print(rand_num[mask])

my_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

sorted_array = np.array(my_array)
print(sorted_array.reshape((3, 3)))