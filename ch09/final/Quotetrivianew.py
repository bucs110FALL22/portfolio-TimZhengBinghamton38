import quoteproxy
import fakenameproxy
import random

class Quotetrivia:
    def __init__(self) -> None:        
        self.randquoteapi = quoteproxy.Randquoteapi()
        self.fakeapi = fakenameproxy.Fakenameapi()
    
    def triviagameloop(self):
        author, quote = self.randquoteapi.get()
        name = self.fakeapi.get()
        name2 = self.fakeapi.get()
        namelist = [author,name,name2]
        random.shuffle(namelist)
        print(quote,"\n")
        print("Who is the author of this quote? \n------------")
        for string in namelist:
            print(string)
        answer = input("The author is: ")
        print("Your input was:",answer,"\n")
        if answer != author:
            print(f"Fail! The author was {author} \n")
            return "Fail"
        elif answer == author:
            print(f"Pass! The author is indeed {author}")
            exit()