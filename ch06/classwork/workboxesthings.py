class Point:
    def __init__(self, x=0, y=0, color="red") -> None:
        self.x = x
        self.y = y
        self.color = color

p1 = Point()
p1.x = 2
p1.y = 4
p1.color = "greer"
print(p1.x, p1.y, p1.color, type(p1))