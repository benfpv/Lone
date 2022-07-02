class Market:
    def __init__(self, buyOrders = [], sellOrders = []) -> None:
        self.buyOrders = buyOrders
        self.sellOrders = sellOrders

    def print_orders(self):
        print("### BUY ORDERS ###")
        for buy in self.buyOrders:
            print('Buyer: {buyer}, Item: {item}, Value: {value}'
            .format(buyer=buy.buyer, item=buy.item, value=buy.value))

    def addBuyOrder(self, buy):
        self.buyOrders.append(buy)

    def addSellOrder(self, sell):
        self.sellOrders.append(sell)