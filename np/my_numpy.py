import numpy as np

# Array Creation
arr = np.array([1, 2, 3])
print(arr)
print(np.array([
    [1, 2, 3],
    ['a', 'b', 'c'],
    ['الف', 'ب']
]))
print(np.array([
    [1, 2, 3],
    [10, 20, 30],
    [11, 21, ]
]))
print(np.array([1, 0, 0, 1], bool))

# [start, end) , step
print(np.arange(10))
print(np.arange(2, 10))
print(np.arange(2, 17, 3))

print(np.arange(2, 18, 3).reshape(3, 2))
print(np.arange(2, 18, 3).reshape(2, 3))
# print(np.arange(2, 17, 3).reshape(2, 3)) #  ValueError: cannot reshape array of size 6 into shape (2,2)
print(np.arange(2, 18, 3).reshape(2, 3, 1))

# Update values
arr[1] = 20
print(arr)
arr = np.arange(1, 21)
arr[5:10] = -1
print(arr)
