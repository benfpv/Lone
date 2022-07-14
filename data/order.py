class Order:
    def __init__(self, value, item):
        self.value = value
        self.item = item

class BuyOrder(Order):
    def __init__(self, value, item, buyer):
        super().__init__(value, item)
        self.buyer = buyer

class SellOrder(Order):
    def __init__(self, value, item, seller):
        super().__init__(value, item)
        self.seller = seller