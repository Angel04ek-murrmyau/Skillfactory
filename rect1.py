from rectangle import Rectangle, Circle, Triangle

rect1 = Rectangle(10,5)
rect2 = Rectangle(13,5)

circ1 = Circle(5)
circ2 = Circle(7)

tri1 = Triangle(1,5)
tri2 = Triangle(4,2)

figures = [rect1, rect2, circ1, circ2, tri1, tri2]
for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.getArea())
    elif isinstance(figure, Circle):
        print(figure.getAreaCircle())
    elif isinstance(figure, Triangle):
        print(figure.getAreaTriangle())