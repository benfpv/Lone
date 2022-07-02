import numpy as np
import math
import random
import time

from market_logic import Market
from order import BuyOrder

def main():
	# test pr
	pass;

if __name__ == '__main__':
	main();
	market = Market()
	order1 = BuyOrder(100, "AMD", "Ben")
	market.addBuyOrder(order1)
	market.print_orders()