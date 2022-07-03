from market_logic import Market
from order import BuyOrder, SellOrder
from class_items import Items

class User:
	def __init__(self, userID, name, inventory = {}, money = 1000, ) -> None:
		self.userID = userID
		self.name = name
		self.inventory = inventory
		self.money = money

	def buy(self, market: Market, value, item: Items):
		if value <= self.money:
			self.money -= value
			market.addBuyOrder(BuyOrder(value, item, self.name))
		else:
			print("You don't have have enough money!")

	def sell(self, market: Market, value, item: Items):
		if item.name in self.inventory:
			market.addSellOrder(SellOrder(value, item, self.name))
		else:
			print("You don't have that item to sell!")

	def buyOrderFulfilled(self, order):
		self.inventory[order.item.id] = order.item

	def sellOrderFulfilled(self, order):
		self.money += order.value
		self.inventory.pop(order.item.name)
