import numpy as np
import math
import random
import time

from market_logic import Market
from order import BuyOrder

def main():
	# test pr
	pass

if __name__ == '__main__':
	main()
	market = Market()
	order1 = BuyOrder(100, "AMD", 1, "Ben")
	order2 = BuyOrder(1000, "AMD", 1, "Jeff")
	order3 = BuyOrder(1, "AMD", 1, "Greg")
	market.addBuyOrder(order1)
	market.addBuyOrder(order2)
	market.addBuyOrder(order3)
	market.print_orders()

	#itemsList = []
	#itemsList.append(Item("apple", "fruit", "2/2/2222"))