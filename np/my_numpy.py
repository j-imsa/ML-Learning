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

# Update dimensions
arr = arr.reshape(2, 10)  # n * m ==TRUE== array_size
arr = arr.reshape(2, 5, 2)  # n * m * h ==TRUE== array_size
# arr = arr.reshape(len(arr),)

print(arr.ndim)
print(len(arr))
print(arr.size)
print(arr.shape)

a = arr.reshape(2, 5)
print(a.shape[0])
print(a.shape[1])

# List to Array
lst = [[1, 2, 3], [4, 5, 6]]
arr = np.asarray(lst)
print(arr)

# Array with default values
print(np.zeros((3, 4), dtype='int32'))
print(np.zeros((3, 4), dtype=np.float64))
print(np.ones((3, 4)))
print(np.eye(3))
print(np.linspace(1, 5, num=3))
print(np.linspace(1, 5, num=19))
print(np.random.random(5))
print(np.random.random(5) * 10)

# numpy\'s cool functions
arr = np.random.random(12).reshape(4, 3)
print(arr)
print(np.max(arr, axis=0))  # axis 0 means column
print(np.max(arr, axis=1))  # axis 1 means row
print(np.argmax(arr))
print(np.min(arr, axis=1))
print(np.mean(arr, axis=1))
print(np.median(arr))
print(np.sum(arr))

# index
arr = np.random.random(12).reshape(4, 3)
print(arr)
# arr[n,m] => n row , m column
print(arr[1, 2])
print(arr[1:, :2])
for item in arr.flat:
    print(item)
