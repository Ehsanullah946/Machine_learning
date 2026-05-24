# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger = countries.index("germany")
# print(ind_ger)



# Definition of dictionary
# europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
# # Print out the keys in europe
# europe.keys()
# # Print out value that belongs to key 'norway'
# print(europe["norway"])


# dictionary part 2 

# world = {'spain':30.55, 'france':2.81, 'germany':39.4, 'norway':2.7 }
# world["norway"]= 2.8
# del(world["norway"])
# print(world)


# Definition of dictionary
# europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# # Add italy to europe
# europe['italy']= "rome"
# # Print out italy in europe
# print('italy' in europe)
# # Add poland to europe
# europe['poland']= "warsaw"
# # Print europe
# print(europe)


europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe["france"].get("population"))

print(europe["france"]["capital"])

# Create sub-dictionary data
data= {"capital": "rome", "population":59.83}

# Add data to europe under key 'italy'
europe["italy"]= data

# Print europe
print(europe)


