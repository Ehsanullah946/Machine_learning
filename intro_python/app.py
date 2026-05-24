from pathlib import Path

from zipfile import ZipFile


# path = Path("foundimentals/file_directory/file1.py")

# path.unlink()

# with ZipFile("files.zip", "w") as zip:
#         for path in Path("foundimentals").rglob("*.py"):
#             zip.write(path)
            
            
# with ZipFile("files.zip") as zip:
#     zipInfo= zip.getinfo(zip.namelist()[0])
#     print(zipInfo.file_size)
            
            
# with ZipFile("files.zip") as zip:
#      zip.extractall("extractFiles")


# import sys

# if len(sys.argv) == 1:
#     print("please enter you password")
# else:
#     password= sys.argv[1]
#     print("you password is :",password)    

# import subprocess
# subprocess.run(["python", "copy.py"])

# areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# print(areas[6:10])
# house = [["hallway", 11.25],
#          ["kitchen", 18.0],
#          ["living room", 20.0],
#          ["bedroom", 10.75],
#          ["bathroom", 9.50]]
# print(house[4])


# areas = ["hallway", 11.25, "kitchen", 18.0,
#         "chill zone", 20.0, "bedroom", 10.75,
#          "bathroom", 10.50, "poolhouse", 24.5,
#          "garage", 15.45]

# del (areas[10])
# del (areas[11])

# print(areas)

# sorted method sort all numbers 

# first = [11.25, 18.0, 20.0]
# second = [10.75, 9.50]
# full = first + second
# full_sorted = sorted(full,reverse=True)
# print(full_sorted)


# everythig is object 
# index and count method 
# index method  return the index of specific member of that list
# count() method is counting the number of repeating index in the list

# areas = ["hallway", 11.25, "kitchen", 20.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
# print(areas.count(20.0))


# # string to experiment with: place
# place = "poolhouse"

# # Use upper() on place
# place_up = place.upper()

# # Print out place and place_up
# print(place)
# print(place_up)

# # Print out the number of o's in place
# print(place.count("o"))



# # Create list areas
# areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# ste=str(areas)
# print(type(ste))
# # Use append twice to add poolhouse and garage size

# areas.append(24.5)
# areas.append(15.45)

# # Print out areas
# print(areas)

# # Reverse the orders of the elements in areas
# areas.reverse()

# # Print out areas
# print(areas)




# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))