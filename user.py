from market_logic import Market

class User:
	def __init__(self, userID, name, stocks = [], money = 1000) -> None:
		self.userID = userID
		self.name = name
		self.stocks = stocks
		self.money = money

	def buy(self, market: Market):
		#market.addBuyOrder()
		pass

	def sell(self, market: Market):
		#market.addSellOrder()
		pass

	def buyOrderFulfilled(self):
		pass

	def sellOrderFulfilled(self):
		pass