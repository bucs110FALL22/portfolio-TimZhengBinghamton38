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


class Num:
  def __init__(self, n):
    self.num = n

num_obj = Num(5) 
print(num_obj.num) #the instance variable values are self.num=5
#the State of the object is self.num = 5
num_obj.num = 7 #changing the state
print(num_obj) #not changing the state

num_obj.num = (num_obj.num * 2) #result changes state

