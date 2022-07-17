from data.market import Market
from data.order import BuyOrder, SellOrder
from data.item import Item

from datetime import date, datetime

class User:
    def __init__(self, userID, name, money = 1000, inventory = {}) -> None:
        self.userID = userID
        self.name = name
        self.inventory = inventory
        self.money = money
        self.buyOrders = []
        self.sellOrders = []
        self.marketHistory = []

    def buy(self, market: Market, value, item: Item):
        if value <= self.money:
            self.money -= value
            buying = BuyOrder(value, item, self.name)
            self.buyOrders.append(buying)
            bought = market.addBuyOrder(buying)
            if bought:
                print("- User {name} bought {item} for {value}!" \
                .format(name=self.name, item=item.name, value=bought.value))
            else:
                print("- User {name} created buy order for {item} at {value}!" \
                .format(name=self.name, item=item.name, value=value))
        else:
            print("- User {name} doesn't have enough money to buy {item} for {value}!" \
                .format(name = self.name, item=item.name, value=value))

    def sell(self, market: Market, value, item: Item):
        if item.name in self.inventory:
            selling = SellOrder(value, item, self.name)
            self.sellOrders.append(selling)
            sold = market.addSellOrder(selling)
            if sold:
                print("- User {name} sold {item} for {value}!" \
                .format(name=self.name, item=item.name, value=sold.value))
            else:
                print("- User {name} created sell order for {item} at {value}!" \
                .format(name=self.name, item=item.name, value=value))
        else:
            print("- User {name} doesn't have that item {item} to sell!" \
                .format(name = self.name, item=item.name))

    def buyOrderFulfilled(self, order: BuyOrder):
        self.inventory[order.item.id] = order.item
        self.historyOrders.append(self.marketHistory.append(['[Buy Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(user=buy.buyer, item=buy.item.name, value=buy.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))]))
        print("- User {name} bought {item} for {value}!" \
                .format(name=self.name, item=order.item.name, value=order.value))

    def sellOrderFulfilled(self, order: SellOrder):
        self.money += order.value
        self.inventory.pop(order.item.name)
        
        print("- User {name} sold {item} for {value}!" \
                .format(name=self.name, item=order.item.name, value=order.value))

    def cancelBuy(self, market: Market, order):
        if order in self.buyOrders:
            market.cancelBuyOrder(order)
            print("- User {name} cancelled their buy order for {item}!" \
                .format(name=self.name, item=order.item.name))
        else:
            print("- User {name} doesn't have that buy order for {item}!" \
                .format(name = self.name, item=order.item.name))

    def cancelSell(self, market: Market, order):
        if order in self.sellOrders:
            market.cancelSellOrder(order)
            print("- User {name} is cancelled their sell order for {item}!" \
                .format(name=self.name, item=order.item.name))
        else:
            print("- User {name} doesn't have that sell order for {item}!" \
                .format(name = self.name, item=order.item.name))