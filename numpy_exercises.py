# Exercises
# In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.

import numpy as np

# Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?

len(a[a<0])
# 4 negative numbes in the list

# How many positive numbers are there?
len(a[a>0])
# 5 positive numbers

# How many even positive numbers are there?
pos = a[a>0]
pos

pos_even = pos[pos % 2 == 0]
pos_even

pos_even_count = len(pos_even)
pos_even_count
# 3 positive evens in the array

# If you were to add 3 to each data point, how many positive numbers would there be?
plus_three = a + 3
plus_three

p_t_pos = plus_three[plus_three > 0]
p_t_pos

p_t_pos_count = len(p_t_pos)
p_t_pos_count
# 10 postive integers if 3 added to each
# If you squared each number, what would the new mean and standard deviation be?
import statistics

squared = a**2
squared

sq_avg = statistics.mean(squared)
sq_avg
# mean of list is now 74

sq_stddev = statistics.stdev(squared)
sq_stddev
# stdev of new list is now 150.42606157179014

# A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. 
# See this link for more on centering.

centered = a - statistics.mean(a)
centered

# centered array array([  1,   7,   9,  20,  -5,  -4,  -3,  -3,  -3,  -9,   0, -10])
# Calculate the z-score for each data point. Recall that the z-score is given by:

original_avg = np.mean(a)
original_avg
# original_avg = 3.0

original_std = np.std(a)
original_std
# original_std = 8.06225774829855

original_z = (a - original_avg) / original_std
original_z
# original_z = array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
    #    -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
        # 0.        , -1.24034735])

# Copy the setup and exercise directions from More Numpy Practice into your 
# numpy_exercises.py and add your solutions.

import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = np.sum(a)
sum_of_a
# 55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = np.min(a)
min_of_a
# 1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = np.max(a)
max_of_a
# 10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = np.mean(a)
mean_of_a
# 5.5

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = np.product(a)
product_of_a
# 3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
squares_of_a
# array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]
odds_in_a
# array([ 1,  9, 25, 49, 81])
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a[a % 2 == 0]
evens_in_a
# array([  4,  16,  36,  64, 100])