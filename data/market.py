from datetime import date, datetime

class Market:
    def __init__(self, buyOrders = [], sellOrders = [], users = {}, marketHistory = []) -> None:
        self.buyOrders = buyOrders
        self.sellOrders = sellOrders
        self.users = users
        self.marketHistory = marketHistory

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
        self.addUserJoinToMarketHistory(self.marketHistory, user)
    
    def addUserJoinToMarketHistory(self, history, user):
        history.append(['[Market] Username: {username}, Action: {action}, Date: {marketDate}, Time: {marketTime}'
            .format(username=user.name, action='Joined the market', marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def addBuyOrder(self, buy):
        boughtOrder = self._buyFulfillment(buy)
        if not boughtOrder:
            i = 0
            while (i < len(self.buyOrders) and buy.value < self.buyOrders[i].value):
                i += 1
            self.buyOrders.insert(i, buy)
            self.addBuyOrderToHistory(self.marketHistory, buy)
            return
        else:
            self.users[boughtOrder.seller].sellOrderFulfilled(boughtOrder)
            return boughtOrder

    def addBuyOrderToHistory(self, history, buy):
        history.append(['[Market][Create Buy Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(user=buy.buyer, item=buy.item.name, value=buy.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def addSellOrder(self, sell):
        soldOrder = self._sellFulfillment(sell)
        if not soldOrder:
            i = 0
            while (i < len(self.sellOrders) and sell.value > self.sellOrders[i].value):
                i += 1
            self.sellOrders.insert(i, sell)
            self.addSellOrderToHistory(self.marketHistory, sell)
        else:
            return soldOrder

    def addSellOrderToHistory(self, history, sell):
        history.append(['[Market][Create Sell Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(user=sell.seller, item=sell.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def cancelBuyOrder(self, order):
        for i, o in enumerate(self.buyOrders):
            if o == order:
                self.buyOrders.pop(i)
                self.addCancelBuyOrderToHistory(self.marketHistory, o)
                return True
        return False

    def addCancelBuyOrderToMarketHistory(self, history, order):
        history.append(['[Market][Cancel Buy Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(user=order.buyer, item=order.item.name, value=order.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def cancelSellOrder(self, order):
        for i, o in enumerate(self.sellOrders):
            if o == order:
                self.sellOrders.pop(i)
                self.addCancelSellOrderToHistory(self.marketHistory, o)
                return True
        return False

    def addCancelSellOrderToMarketHistory(self, history, order):
        history.append(['[Market][Cancel Sell Order] User: {user}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(user=order.seller, item=order.item.name, value=order.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])

    def _buyFulfillment(self, buy):
        for index, sell in enumerate(self.sellOrders):
            if buy.item.name == sell.item.name and \
                buy.value > sell.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                self.addBuyFulfillmentToHistory(self.marketHistory, buy, sell)
                return self.sellOrders.pop(index)
        return

    def addBuyFulfillmentToHistory(self, history, buy, sell):
        history.append(['[Market][Fulfill Buy Order] Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
    
    def _sellFulfillment(self, sell):
        for index, buy in enumerate(self.buyOrders):
            if sell.item.name == buy.item.name and \
                sell.value < buy.value:
                print("- ORDER FULFILLED:")
                print('\tBuyer: {buyer}, Seller:{seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
                    .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S")))
                self.addSellFulfillmentToHistory(self.marketHistory, buy, sell)
                return self.buyOrders.pop(index)
        return
    
    def addSellFulfillmentToHistory(self, history, buy, sell):
        history.append(['[Market][Fulfill Sell Order] Buyer: {buyer}, Seller: {seller}, Item: {item}, Value: {value}, Date: {marketDate}, Time: {marketTime}'
            .format(buyer=buy.buyer, seller=sell.seller, item=buy.item.name, value=sell.value, marketDate=date.today().strftime("%d %m %Y"), marketTime=datetime.now().strftime("%H %M %S"))])
    
    def printMarketHistory(self):
        print('### MARKET.PRINTMARKETHISTORY() ###');
        print("- Market History:")
        for i in self.marketHistory:
            print(i);