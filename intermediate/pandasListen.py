# # Pre-defined lists
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]

import pandas as pd 
# # Create dictionary my_dict with three key:value pairs: my_dict
# my_dict= {"country":names, "drives_right":dr, "car_per_cap": cpc}

# # Build a DataFrame cars from my_dict: cars
# cars = pd.DataFrame(my_dict)

# Print car
# print(cars)

# Build cars DataFrame
# names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
# dr =  [True, False, False, False, True, True, True]
# cpc = [809, 731, 588, 18, 200, 70, 45]
# cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
# cars = pd.DataFrame(cars_dict)
# print(cars)

# # Definition of row_labels
# row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# # Specify row labels of cars
# cars.index= row_labels

# # Print cars again
# print(cars)



# Import cars data
# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# # Print out drives_right column as Series
# print(cars.loc[:,"drives_right"])

# # Print out drives_right column as DataFrame
# print(cars.loc[:,["drives_right"]])

# # Print out cars_per_cap and drives_right as DataFrame
# print(cars.loc[:,["cars_per_cap", "drives_right"]])





# two type of pandas the Series() and dataFrame();
# print(pd.__version__)
# Series 
# data = [200, 100,500,900]
# # series = pd.Series(data)
# series = pd.Series(data, index=["a", "b", "c", "d"])
# print(series)
# series.loc["a"]= 700
# print(series.loc["a"])
# print(series.iloc[1])
# print(series[series >=300])


# DataFrame object 

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict, index=["country 1", "country 2", "country 3","country 4", "country 5", "country 6","country 7"])
# adding new column 
cars["exp"]= [2000,3000,4000,5000,6000,7000, 9000]
# print(cars.loc["country 1"])

# adding new row 
# new_row= pd.DataFrame([{"country": "Afghan", "drivers_right":False, "cars_per_cap": 400, "exp": 400}], index=["country 8"])
# cars = pd.concat([cars, new_row])
# print(cars)


# reading csv and json file 

# csv_data= pd.read_csv("data.csv", index_col="country")
# json_data= pd.read_json("data.json")
# print(csv_data.to_string())




# Selection by column 
print(cars[["country", "drives_right","cars_per_cap"]])


# selecting by rows
# for searching by rows we can add index_col into csv file 
print(cars.loc["country 1": "country 3",["drives_right","country"]])
print(cars.iloc[1:4:2, 0:3]) # select the first three column 

# searchig for country by index 
# poke = input("Enter a country name: ")

# try:
#     print(cars.loc[poke])
# except KeyError:
#     print(f"the {poke} is not found:")    
    


# filtering
expence= cars[cars["exp"] > 3000]     
print(expence)   