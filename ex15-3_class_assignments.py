import copy

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
	new_rect = copy.deepcopy(rect)
	new_rect.corner.x += dx
	new_rect.corner.y +=dy
	return new_rect

print box.corner.x,box.corner.y

new_box = move_rectangle(box,4,9)

print new_box.corner.x,new_box.corner.y
print box == new_box
