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

        user1 = User(1, "Ben", {itemsList[0].name: itemsList[0]}, 1000)
        user2 = User(2, "Jeff Bezos", {itemsList[2].id: itemsList[2]}, 1000000)

        self.market.add_user(user1)
        self.market.add_user(user2)

    def printCommands(self):
        print("Commands:\n\t-help\n\t-select user\n\t-inventory\n\t-buy [stock] [value]\n\t-sell [stock] [value]")    

    def gameLoop(self):
        command = input("What would you like to do\n")
        command = command.lower()
        if command == "help":
            self.printCommands()
        elif command == "select user":
            self.select_user()
        else:
            print("That's not a option. Available commands are:\n")
            self.printCommands()
    

    def select_user(self):
        for user in self.market.users:
            print(user)
        name = input("Which user are you?\n")
        while not name in self.market.users:
            if name in self.market.users:
                self.market.currentUser = self.market.users[name]
            else:
                name = input("Not a valid name, which user are you?\n")

if __name__ == '__main__':    

    game = Game()
    
    while not game.exit:
        game.gameLoop()