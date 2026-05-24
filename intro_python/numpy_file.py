import numpy as np

# height = [1.4,1.3,2.3]
# weight = [12,2.3,3.5]

# np_height= np.array(height)

# np_weight=np.array(weight)

# print(type(np_height))

# bmi= np_weight/ np_height ** 2

# print(bmi)

myArray= np.array([[22.3,43.4,3.4],[32.3,4.4,5.6]])

print(myArray[1,2]) # these are the same we can use both of them
print(myArray[1][2])



baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball= np.array(baseball)

# Print out the type of np_baseball
print(np_baseball)

# Print out the shape of np_baseball

print(np_baseball.shape)





np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball

print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])
