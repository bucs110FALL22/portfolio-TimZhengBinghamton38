

class Time:
    def __init__(self) -> None:
        """
        Initializes the time object


        """
        self.timeamount = 500 #initial amount of time given to complete the level
        self.timedownfast = False #determines if the timer decreases fast, updates based on when player completes the level
        self.addscorebasedontime = 500 - self.timeamount #determines points given based on speed of completeion of a level

class Questionblock:
    def __init__(self) -> None:
        """
        Initializes the Questionblock object

        """
        self.invisible = False #determines if the block is invisible, determined by level designer
        self.has = 12 #This stores the item that the block will release upon being hit by the player, 12 is a placeholder
        self.amount = 20 #determines how many of the item the block will release before becoming unsusable, i.e. 20 coins in one block

class Goomba:
    def __init__(self) -> None:
        """
        Initializes the goomba object

        """
        self.movedir = 0 #determines the direction the goomba will move in, i.e. 0 for left and 1 for right
        self.hasWings = 0 #determines if the goomba has wings
        self.lives = 1 #determines amount of "damage" the goomba can take - 1 to die upon being hit