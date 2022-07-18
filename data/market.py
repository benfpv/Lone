from datetime import date, datetime

class Market:
    def __init__(self, buyOrders = [], sellOrders = [], users = {}, log = []) -> None:
        self.buyOrders = buyOrders
        self.sellOrders = sellOrders
        self.users = users
        self.log = log

    def print_orders(self):
        print('### MARKET.PRINT_ORDERS() ###');
        print("- BUY ORDERS: ")
        for buy in self.buyOrders:
            print('\tBuyer: {buyer}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(buyer=buy.buyer, item=buy.item.name, value=buy.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
        print("- SELL ORDERS: ")
        for sell in self.sellOrders:
            print('\tSeller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(seller=sell.seller, item=sell.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))

    def add_user(self, user):
        print('- User {username} has joined the market.'.format(username=user.name))
        self.users[user.name] = user
        self.log.append(['[Market][User Join] User: {username}, Date: {marketDate}, Time: {marketTime}'
            .format(username=user.name, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def addBuyOrder(self, buy):
        boughtOrder = self._buyFulfillment(buy)
        if not boughtOrder:
            i = 0
            while (i < len(self.buyOrders) and buy.value < self.buyOrders[i].value):
                i += 1
            self.buyOrders.insert(i, buy)
            self.log.append(['[Market][Create Buy Order] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(username=buy.buyer, item=buy.item.name, value=buy.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
            return
        else:
            self.users[boughtOrder.seller].sellOrderFulfilled(boughtOrder)
            return boughtOrder

    def addSellOrder(self, sell):
        soldOrder = self._sellFulfillment(sell)
        if not soldOrder:
            i = 0
            while (i < len(self.sellOrders) and sell.value > self.sellOrders[i].value):
                i += 1
            self.sellOrders.insert(i, sell)
            self.log.append(['[Market][Create Sell Order] User: {username}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                .format(username=sell.seller, item=sell.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
        else:
            return soldOrder

    def cancelBuyOrder(self, order):
        for i, o in enumerate(self.buyOrders):
            if o == order:
                self.buyOrders.pop(i)
                self.log.append(['[Market][Cancel Buy Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(user=o.buyer, item=o.item.name, value=o.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
                return True
        return False

    def cancelSellOrder(self, order):
        for i, o in enumerate(self.sellOrders):
            if o == order:
                self.sellOrders.pop(i)
                self.log.append(['[Market][Cancel Sell Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(user=o.seller, item=o.item.name, value=o.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
                return True
        return False

    def _buyFulfillment(self, buy):
        for index, sell in enumerate(self.sellOrders):
            if buy.item.name == sell.item.name and \
                buy.value > sell.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                self.log.append(['[Market][Fulfill Buy Order] Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
                return self.sellOrders.pop(index)
        return

    def _sellFulfillment(self, sell):
        for index, buy in enumerate(self.buyOrders):
            if sell.item.name == buy.item.name and \
                sell.value < buy.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller:{seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                self.log.append(['[Market][Fulfill Sell Order] Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
                return self.buyOrders.pop(index)
        return
    
    def printMarketHistory(self):
        print('### MARKET.PRINTMARKETHISTORY() ###');
        print("- Market History:")
        for i in self.marketHistory:
            print(i);