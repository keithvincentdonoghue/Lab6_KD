# Computational Methods Lab 6
# 07th November 2023
# Name: Keith Donoghue
# This Program Computes the Mean Square Error
import numpy as np 

array_1 = np.array([1,2,3,4,5,]) 
array_3 = np.array([6,7,8,9,10]) 

def mean_square_error(array_1,array_2):
    
    answer = (np.square(array_1 - array_2))
    mean_square = np.mean(answer)
    return mean_square

print(mean_square_error(array_1,array_2))