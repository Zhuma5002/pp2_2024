import math
from math import tan, pi
side=int(input("num of side:"))
length=int(input("num of length:"))
area=side * (length ** 2) / (4 * tan(pi / side))
print("area is:", area)