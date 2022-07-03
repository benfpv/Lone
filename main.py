import numpy as np
import math
import random
import time

from import_items import * 

from market_logic import Market
from order import BuyOrder, SellOrder


def main():
    pass

if __name__ == '__main__':
    main()
    market = Market()

    #order2 = BuyOrder(1000, "AMD", 1, "Jeff")
    #order3 = BuyOrder(1, "AMD", 1, "Greg")
    market.addBuyOrder(BuyOrder(100, itemsList[0], "Ben"))
    #market.addBuyOrder(order2)
    #market.addBuyOrder(order3)

    #order2 = SellOrder(1000, "AMD", 1, "Jeff")
    #order3 = SellOrder(1, "AMD", 1, "Greg")
    market.addSellOrder(SellOrder(75, itemsList[0], "Ben"))
    #market.addSellOrder(order2)
    #market.addSellOrder(order3)

    market.addBuyOrder(BuyOrder(80, itemsList[0], "Ben"))

    market.print_orders()