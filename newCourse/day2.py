
import sys
# constant defination how define a constant 

# first way
WIDTH= 300

# for access rate we use %timeit const.PI

# seconde way
def width():
    return 300


# using slots storage and comparing with none slots constants class
class Constant:
    __slots__ = ()
    PI=3.23
    
    
const = Constant()
print(const.PI) 
print(sys.getsizeof(const))
    
    
class Constan:
    PI=3.23    
    
constan = Constan()
print(constan.PI) 
print(sys.getsizeof(constan))    
    
    
# how to find out which file is the main file 


if __name__ == "__main__":
    print("it is true")
print(__name__)