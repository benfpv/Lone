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
        self.log = []

    def buy(self, market: Market, value, item: Item):
        if value <= self.money:
            self.money -= value
            buying = BuyOrder(value, item, self.name)
            self.buyOrders.append(buying)
            bought = market.addBuyOrder(buying)
            if bought:
                print("- User {name} bought {item} for {value}!" \
                    .format(name=self.name, item=item.name, value=bought.value))
                self.log.append(['[User][Fulfill Buy Order] User: {buyer}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
            else:
                print("- User {name} created buy order for {item} at {value}!" \
                    .format(name=self.name, item=item.name, value=value))
                self.log.append(['[User][Create Buy Order] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(username=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
        else:
            print("- User {name} doesn't have enough money to buy {item} for {value}!" \
                .format(name = self.name, item=item.name, value=value))
            self.log.append(['[User][Unable to Create Buy Order: Insufficient Funds] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(username=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def sell(self, market: Market, value, item: Item):
        if item.name in self.inventory:
            selling = SellOrder(value, item, self.name)
            self.sellOrders.append(selling)
            sold = market.addSellOrder(selling)
            if sold:
                print("- User {name} sold {item} for {value}!" \
                    .format(name=self.name, item=item.name, value=sold.value))
                self.log.append(['[User][Fulfill Sell Order] User: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(seller=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
            else:
                print("- User {name} created sell order for {item} at {value}!" \
                    .format(name=self.name, item=item.name, value=value))
                self.log.append(['[User][Create Sell Order] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(username=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
        else:
            print("- User {name} doesn't have that item {item} to sell!" \
                    .format(name = self.name, item=item.name))
            self.log.append(['[User][Unable to Create Sell Order: Insufficient Funds] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(username=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def buyOrderFulfilled(self, order: BuyOrder):
        self.inventory[order.item.id] = order.item
        print("- User {name} bought {item} for {value}!" \
            .format(name=self.name, item=order.item.name, value=order.value))
        self.log.append(['[User][Fulfill Buy Order] User: {buyer}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(buyer=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def sellOrderFulfilled(self, order: SellOrder):
        self.money += order.value
        self.inventory.pop(order.item.name)
        print("- User {name} sold {item} for {value}!" \
            .format(name=self.name, item=order.item.name, value=order.value))
        self.log.append(['[User][Fulfill Sell Order] User: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(seller=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def cancelBuy(self, market: Market, order):
        if order in self.buyOrders:
            market.cancelBuyOrder(order)
            self.log.append(['[User][Cancel Buy Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(user=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
        else:
            print("- User {name} doesn't have that buy order for {item}!" \
                .format(name = self.name, item=order.item.name))
            self.log.append(['[User][Unable to Cancel Buy Order: Buy Order Does Not Exist] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(user=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def cancelSell(self, market: Market, order):
        if order in self.sellOrders:
            market.cancelSellOrder(order)
            print("- User {name} is cancelled their sell order for {item}!" \
                .format(name=self.name, item=order.item.name))
            self.log.append(['[User][Cancel Sell Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(user=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
        else:
            print("- User {name} doesn't have that sell order for {item}!" \
                .format(name = self.name, item=order.item.name))
            self.log.append(['[User][Unable to Cancel Sell Order: Sell Order Does Not Exist] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(user=self.name, item=item.name, value=value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])