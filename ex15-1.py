import math

class point(object):
	"""Represents a point in 2-D space."""

point1 = point()
point1.x = 3.0
point1.y = 2.0

point2 = point()
point2.x = 9.0
point2.y = 7.0

print math.sqrt(abs(point2.x-point1.x)**2+abs(point2.y-point1.y)**2)