class Rectangle:
    def __init__(self,x = 0,y = 0,height = 0,width = 0) -> None:
        """
        This initializes the Rectangle object (x,y,height,width) set to zero if not defined, also sets to 0 if a negative is entered
        args: self, x, y, height, width
        return: None
        """
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        #this is actually the easiest way to check for negatives, though I would much like it to be shorter
        if self.x <0:
            self.x = 0
            print("A negative x value was set to 0")
        if self.y <0:
            self.y = 0
            print("A negative y value was set to 0")
        if self.height <0:
            self.height = 0
            print("A negative height value was set to 0")
        if self.width < 0:
            self.width = 0
            print("A negative width value was set to 0")

    def __str__(self) -> str:
        """
        This function changes the return type of the Rectangle object to a set of attributes describing the Rectangle
        args: self
        return: str, a set of coordinates and the height and width of the rectangle
        """
        return f"Coordinates(x:{self.x},y:{self.y}),\nHeight:{self.height}, Width:{self.width}"
