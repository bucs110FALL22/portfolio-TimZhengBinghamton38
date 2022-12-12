import quoteproxy
import fakenameproxy
import random

class Quotetrivia:
    def __init__(self) -> None:
        """
        Initializes the quote api objects
        args: self
        return: None
        """ 
        self.randquoteapi = quoteproxy.Randquoteapi()
        self.fakeapi = fakenameproxy.Fakenameapi()
    
    def triviagameloop(self):
        """
        Controls the actual trivia game loop
        args: self
        return: "Fail" string if answer input does not match author
        or None
        """
        author, quote = self.randquoteapi.get()
        author2, _ = self.randquoteapi.get()
        name = self.fakeapi.get()
        name2 = self.fakeapi.get()
        namelist = [author,name,name2,author2]
        random.shuffle(namelist)
        print(quote,"\n")
        print("Who is the author of this quote? \n------------")
        for string in namelist:
            print(string)
        answer = input("You think the author is: ")
        if answer == author:
            print(f"\nPass! The author is indeed {author}")
            exit()
        elif answer != author:
            print(f"\nFail! The author was {author} \n")
            if answer not in namelist:
                print("That wasn't even a choice/A typo has been made \n Regardless, it is still a fail. \n")
            return "Fail"
