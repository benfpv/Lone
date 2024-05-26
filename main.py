from import_items import * 
from data.market import Market
from data.order import BuyOrder, SellOrder
from data.user import User
import pygame as game
from ui.userInterface import *

class MainGame:
    def __init__(self):
        res = (720,720)                     # screen resolution
        self.screen = game.display.set_mode(res)# opens up a window
        self.screen.fill((60,25,60)) # fill background of screen
        self.exit = False
        # Init Items list
        self.itemsDict = import_objectify_itemsList()
        # Init Market
        self.market = Market()
        # Init Users
        self.users = []
        self.users.append(User(1, "Ben", 1000, {"apple", self.itemsDict["apple"]}))
        self.users.append(User(2, "Jeff Bezos", 1000000))
        player_index = 0
        len_users = len(self.users)
        # Init UI
        self.userInterface = UserInterface(game, self.screen, self.users, player_index)
        
        # Add users to market
        for i in range(len_users): 
            self.market.add_user(self.users[i])

    def printCommands(self):
        print("Commands:\n\t-help\n\t-select user\n\t-inventory\n\t-buy\n\t-sell")    

    """
    def gameLoop(self):
        command = input("What would you like to do\n")
        command = command.lower()
        if command == "help":
            self.printCommands()
        elif command == "select user":
            self.select_user()
        elif command == "buy":
            self.buy()
        elif command == "sell":
            self.sell()
        else:
            print("That's not a option. Available commands are:\n")
            self.printCommands()
    """
    def gameLoop(self):
        # stores the (x,y) coordinates into the variable as a tuple
        mouse = game.mouse.get_pos()

        # fills the screen with a color
        #self.screen.fill((60,25,60))
        self.userInterface.update_buttons_hover(mouse)

        # updates the frames of the game
        game.display.update()
        
        for ev in game.event.get():
            if ev.type == game.MOUSEBUTTONDOWN:
                self.userInterface.update_mouseclick(mouse) # check ui
            
            # to quit game, call self.quit_game() in this loop
            if ev.type == game.QUIT:
                game.quit()
                    
    def quit_game(self):
        self.exit = True
        #game.quit()

    def select_user(self):
        for user in self.market.users:
            print(user)
        name = input("Which user are you?\n")
        while not name in self.market.users:
            name = input("Not a valid name, which user are you?\n")
        self.currentUser = self.market.users[name]
        print("You are now " + name)

    def buy(self):
        if self.currentUser == None:
            print("Select a user first\n")
        else:
            buyitem = input("What do you want to buy?\n")
            itemNameList = [x for x in itemsDict.keys()]
            while not buyitem in itemNameList:
                print("That's not a valid item\n")
                print("Valid items are:\n {}".format(itemNameList))
                buyitem = input("What do you want to buy?\n")
            value = input("How much are you spending?\n")
            while not value.isnumeric():
                print("Not a valid number\n")
                value = input("How much are you spending?\n")
            while int(value) > self.currentUser.money:
                value = input("That's more money than you have. How much are you spending?\n")
            buyorder = BuyOrder(value, itemsDict[buyitem], self.currentUser)
            self.market.addBuyOrder(buyorder)

    def sell(self):
        if self.currentUser == None:
            print("Select a user first\n")
        else:
            sellItem = input("What do you want to sell?\n")
            inventoryList = [x for x in self.market.users[self.currentUser.name].inventory]
            while not sellItem in inventoryList:
                print("That's not a valid item\n")
                print("Valid items are:\n {}".format(inventoryList))
                sellItem = input("What do you want to sell?\n")
            value = input("How much are you selling it for?\n")
            sellorder = SellOrder(value, itemsDict[sellItem], self.currentUser)
            self.market.addSellOrder(sellorder)


if __name__ == '__main__':    

    game.init()                         # initializing the constructor
    mainGame = MainGame()
    
    while not mainGame.exit:
        mainGame.gameLoop()