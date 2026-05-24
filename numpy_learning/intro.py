import numpy as np

# sample_1 = np.random.normal() 
# print(f"Single sample: {sample_1}")

# samples_array = np.random.normal(loc=10.0, scale=2.0, size=5)
# print(f"Array samples: {samples_array}")


# samples_2d = np.random.normal(size=(2, 3))
# print(f"2D array samples:\n{samples_2d}")



# avg = np.mean(np_baseball[:,0])
# print("Average: " + str(avg))

# # Print median height
# med = np.median(np_baseball[:,0])
# print("Median: " + str(med))

# # Print out the standard deviation on height
# stddev = np.std(np_baseball[:,0])
# print("Standard Deviation: " + str(stddev))

# # Print out correlation between first and second column
# corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
# print("Correlation: " + str(corr))



array= np.array([[1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])


# row selection
# print((array[start:end:step]))
# print((array[0:4:2]))
# print((array[::2])) # select all rows but step is two 
# print((array[::-1])) # select all rows reversed 


# column selection
# print((array[:,2]))    # select all rows but the second index column
# print((array[:,0:3]))  # select all rows but from 0 to 3 column 
# print((array[:,::2]))  # select all rows and columns but the column select 2 step by step
# print((array[:,1::2])) # select all rows and columns can be different
# print((array[:,::-1])) # select all rows and columns but reverse


# print((array[0:2,0:2])) # select the first and second rows , select the first and second columns
# print((array[0:2,2:])) # select the first and second rows , select the 2 index of colunms and the last columns



# scaler opertion in numpy array

array= np.array([1,2,3])

# print(array + 1)
# print(array * 2)
# print(array / 3)
# print(array ** 4)


# vectorized math operation 

# print(np.sqrt(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.pi)



# EXERSIZE

# radii = np.array([1,2,3])   # A = pi * r2
# print(np.pi * radii ** 2)


# element wise operation 

# array1= np.array([1,2,3])
# array2= np.array([4,5,6])

# print(array1 * array2)
# print(array1 + array2)
# print(array1 - array2)
# print(array1 / array2)
# print(array1 ** array2)


# comparison array

scores = np.array([90,89,30,32,87,10])

# print(scores==100)
# print(scores>=55)
# print(scores <= 10)

print(np.logical_and(scores > 30, scores < 70))
print(np.logical_or(scores > 30, scores < 70))
print(np.logical_not(scores > 30, scores < 70))
print(scores[np.logical_not(scores > 30, scores < 70)])

# scores[scores <= 55] = 0
# print(scores)