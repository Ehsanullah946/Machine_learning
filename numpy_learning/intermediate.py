import numpy as np

# broad_casting 

array1= np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1 * array2)


# aggragate functions = summarize the data and typically return a single value 

# array= np.array([[1,2,3,4],
#                  [6,7,8,9]])

# print(np.sum(array))
# print(np.sum(array, axis=0))
# print(np.sum(array, axis=1))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))



# filtering functions in numpy array


# ages = np.array([[12,33,15,70,40,56],
#                  [40,70,20,40,50,60]])

# tengers= ages[(ages < 18) & (ages < 60)] 
# adult= np.where(ages >= 18, ages, 0)
# print(tengers)
# print(adult)


rng= np.random.default_rng()

print(rng.integers(low=1, high=100, size=(2,3)))



