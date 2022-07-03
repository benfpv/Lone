from re import M
import numpy as np
import math
import random
import time

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
	firstItem = itemsList[0]

	market = Market()

	user1 = User(1, "Ben", {firstItem.name: firstItem}, 1000)
	user2 = User(2, "Jeff Bezos", {firstItem.id: firstItem}, 1000000)


	market.add_user(user1)
	market.add_user(user2)

	user1.sell(market, 100, firstItem)
	
	market.print_orders()
	
	user2.buy(market, 200, firstItem)

	market.print_orders()
