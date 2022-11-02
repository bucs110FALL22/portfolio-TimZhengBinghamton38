import time
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.identification = time.strftime("%d%m%M%S") #simplest approach proposed by classmates - very good too
        self.timeintake = time.strftime("%d/%m/%Y")
        self.adopttime = None

    def changetimeintake(self, intaketime = ""):
        self.timeintake = intaketime
    
    def set_adopted(self):
        self.adopttime = time.strftime("%d/%m/%Y")
    
    def __str__(self):
        result_str = f"{self.name}, the {self.type}"
        result_str += f"\nArrived {self.timeintake}"
        result_str += f"\nAdopted {self.adopttime}"
        return result_str

def main():
    jerry = Animal("Grendor", "Dog")
    print(jerry)
    jerry.set_adopted()
    print(jerry)

main()