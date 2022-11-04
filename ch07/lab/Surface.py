import Rectangle

class Surface:
    """
    Initializes the Surface object
    args: self, filename, x, y, h (height), w (width)
    return: None
    """
    def __init__(self,filename,x,y,h,w) -> None:
        self.rect = Rectangle.Rectangle(x,y,h,w)
        self.image = filename

    """
    Returns the rectangle the Surface has
    args: self
    return : self.rect
    """

    def getRect(self):
        return self.rect