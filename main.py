"""
from re import M
from traceback import print_exc
import numpy as np
import math
import random
import time
from datetime import date, datetime
"""
from import_items import * 
from data.market import Market
from data.order import BuyOrder, SellOrder
from data.user import User
import pygame as game
from ui.homeScreen import HomeScreen

class MainGame:
    def __init__(self):
        res = (720,720)                     # screen resolution
        self.screen = game.display.set_mode(res) # opens up a window

        self.home = HomeScreen(game, self.screen)

        self.exit = False
        self.market = Market()

        user1 = User(1, "Ben", 1000, {"apple", itemsDict["apple"]})
        user2 = User(2, "Jeff Bezos", 1000000)

        self.market.add_user(user1)
        self.market.add_user(user2)
        
        self.currentUser = user1

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
        self.screen.fill((60,25,60))

        # if mouse is hovered on a button it
        # changes to lighter shade 
        self.home.draw(mouse)

        # updates the frames of the game
        game.display.update()
        
        for ev in game.event.get():
                
            #checks if a mouse is clicked
            if ev.type == game.MOUSEBUTTONDOWN:
                
                #if the mouse is clicked on the
                # button the game is terminated
                if self.home.click(mouse):
                    self.quit_game()
            
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
    itemsListCsv = import_itemsList() 
    itemsDict = objectify_itemsList(itemsListCsv)
    mainGame = MainGame()
    
    while not mainGame.exit:
        mainGame.gameLoop()