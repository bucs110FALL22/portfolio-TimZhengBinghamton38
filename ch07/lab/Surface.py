import Rectangle

class Surface:
    def __init__(self,filename,x,y,h,w) -> None:
        """
        Initializes the Surface object
        args: self, filename, x, y, h (height), w (width)
        return: None
        """
        self.rect = Rectangle.Rectangle(x,y,h,w)
        self.image = filename

    def getRect(self):
        """
        Returns the rectangle the Surface has
        args: self
        return : self.rect
        """
        return self.rect