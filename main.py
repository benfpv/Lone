from re import M
from traceback import print_exc
import numpy as np
import math
import random
import time
from datetime import date, datetime

from import_items import * 

from market_logic import Market
from order import BuyOrder, SellOrder
from user import User

class Game:
    def __init__(self):
        self.exit = False
        self.market = Market()

        user1 = User(1, "Ben", 1000, {"apple", itemsDict["apple"]})
        user2 = User(2, "Jeff Bezos", 1000000)

        self.market.add_user(user1)
        self.market.add_user(user2)
        
        self.currentUser = user1

    def printCommands(self):
        print("Commands:\n\t-help\n\t-select user\n\t-inventory\n\t-buy\n\t-sell")    

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
            while value > self.currentUser.money:
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
            value = input("How much are you spending?\n")
            sellorder = SellOrder(value, itemsDict[sellItem], self.currentUser)
            self.market.addSellOrder(sellorder)


if __name__ == '__main__':    

    itemsListCsv = import_itemsList() 
    itemsDict = objectify_itemsList(itemsListCsv)
    game = Game()
    
    while not game.exit:
        game.gameLoop()