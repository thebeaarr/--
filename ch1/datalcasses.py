from dataclasses import dataclass, field 
from typing import List


@dataclass
class Point:
	x: float
	y: float

	def distance_orginie(self):
		return (self.x**2 + self.y**2) ** 0.5


#python gener automatiquement __init__ , __repr__ , __eq__


p1 = Point(3, 4)
p2 = Point(3, 4)

print(p1)
print(p1 == p2)
print(p1.distance_orginie())

