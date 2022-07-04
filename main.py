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

if __name__ == '__main__':
    """
    main()
    market = Market()

    order1 = BuyOrder(100, itemsList[0], "Ben")
    #order2 = BuyOrder(1000, "AMD", 1, "Jeff")
    #order3 = BuyOrder(1, "AMD", 1, "Greg")
    market.addBuyOrder(order1)
    #market.addBuyOrder(order2)
    #market.addBuyOrder(order3)

    order1 = SellOrder(75, itemsList[1], "Ben")
    #order2 = SellOrder(1000, "AMD", 1, "Jeff")
    #order3 = SellOrder(1, "AMD", 1, "Greg")
    market.addSellOrder(order1)
    #market.addSellOrder(order2)
    #market.addSellOrder(order3)

    market.print_orders()
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