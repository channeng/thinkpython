import math

class Point(object):
	"""Represents a point. attributes: x, y."""

class Rectangle(object):
	"""Represents a rectangle. attributes: width, height, corner."""

box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 3.0
box.corner.y = 4.0

def move_rectangle(rect,dx,dy):
	rect.corner.x += dx
	rect.corner.y +=dy

print box.corner.x,box.corner.y

move_rectangle(box,4,9)

print box.corner.x,box.corner.y
