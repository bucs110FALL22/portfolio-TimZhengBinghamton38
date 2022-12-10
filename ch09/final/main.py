import Quotetrivianew
import sys

def main():
    game = Quotetrivianew.Quotetrivia()
    state = game.triviagameloop()
    while True:
        if state == "Fail":
            game.triviagameloop()
 
main()