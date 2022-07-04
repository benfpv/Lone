from market_logic import Market
from order import BuyOrder, SellOrder
from class_items import Item

class User:
	def __init__(self, userID, name, inventory = {}, money = 1000, ) -> None:
		self.userID = userID
		self.name = name
		self.inventory = inventory
		self.money = money
		self.buyOrders = []
		self.sellOrders = []

	def buy(self, market: Market, value, item: Item):
		if value <= self.money:
			self.money -= value
			buying = BuyOrder(value, item, self.name)
			self.buyOrders.append(buying)
			bought = market.addBuyOrder(buying)
			if bought:
				print("{name} bought {item} for {value}" \
				.format(name=self.name, item=item.name, value=bought.value))
			else:
				print("{name} is buying {item} for {value}" \
				.format(name=self.name, item=item.name, value=value))
		else:
			print("You don't have have enough money!")

	def sell(self, market: Market, value, item: Item):
		if item.name in self.inventory:
			selling = SellOrder(value, item, self.name)
			self.sellOrders.append(selling)
			sold = market.addSellOrder(selling)
			if sold:
				print("{name} sold {item} for {value}" \
				.format(name=self.name, item=item.name, value=sold.value))
			else:
				print("{name} is selling {item} for {value}" \
				.format(name=self.name, item=item.name, value=value))
		else:
			print("You don't have that item to sell!")

	def buyOrderFulfilled(self, order: BuyOrder):
		self.inventory[order.item.id] = order.item
		print("{name} bought {item} for {value}!" \
				.format(name=self.name, item=order.item.name, value=order.value))

	def sellOrderFulfilled(self, order: SellOrder):
		self.money += order.value
		self.inventory.pop(order.item.name)
		print("{name} sold {item} for {value}!" \
				.format(name=self.name, item=order.item.name, value=order.value))

	def cancelBuy(self, market: Market, order):
		if order in self.buyOrders:
			market.cancelBuyOrder(order)
			print("{name} cancelled their buy order for {item}" \
				.format(name=self.name, item=order.item.name))
		else:
			print("You don't have that buy order")

	def cancelSell(self, market: Market, order):
		if order in self.sellOrders:
			market.cancelSellOrder(order)
			print("{name} is cancelled their sell order for {item}" \
				.format(name=self.name, item=order.item.name))
		else:
			print("You don't have that sell order")