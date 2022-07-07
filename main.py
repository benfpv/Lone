from re import M
import numpy as np
import math
import random
import time
from datetime import date, datetime

from import_items import * 

from market_logic import Market
from order import BuyOrder, SellOrder
from user import User


def main():
    pass

def gameLoop(market):
    command = input("What would you like to do\n")
    command = command.lower()
    if command.lower() == "help":
        pass
    elif command.lower() == "select user":
        pass
    elif command.lower() == "open inventory":
        pass
    elif command.lower() == "Buy":
        pass

    switch = {
        "h" : lambda switch: print([k for k in switch.keys()]),
        "select user": select_user(market)
    }

    switch[command](switch)

def select_user(market):
    for user in market.users:
        print(user)
    name = input("Which user are you?\n")
    while not name in market.users:
        if name in market.users:
            market.currentUser = market.users[name]
        else:
            name = input("Not a valid name, which user are you?\n")

if __name__ == '__main__':
    market = Market()    

    user1 = User(1, "Ben", {itemsList[0].name: itemsList[0]}, 1000)
    user2 = User(2, "Jeff Bezos", {itemsList[2].id: itemsList[2]}, 1000000)

    market.add_user(user1)
    market.add_user(user2)

    gameLoop(market)
    """
    itemsListCsv = import_itemsList() 
    itemsList = objectify_itemsList(itemsListCsv) 

    print('----- debug market -----');
    market = Market()

    user1 = User(1, "Ben", {itemsList[0].name: itemsList[0]}, 1000)
    user2 = User(2, "Jeff Bezos", {itemsList[2].id: itemsList[2]}, 1000000)

    market.add_user(user1)
    market.add_user(user2)

    user1.sell(market, 100, itemsList[0])
    market.print_orders()
    user2.buy(market, 200, itemsList[2])
    market.print_orders()
    user2.buy(market, 200, itemsList[0])
    market.print_orders()
    user2.cancelBuy(market, user2.buyOrders[0])
    market.print_orders()
    print('----- debug marketHistory -----');
    market.print_marketHistory();
    """