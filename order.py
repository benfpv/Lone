class Order:
    def __init__(self, value, itemName, itemID):
        self.value = value
        self.itemName = itemName
        self.itemID = itemID

class BuyOrder(Order):
    def __init__(self, value, itemName, itemID, buyer):
        super().__init__(value, itemName, itemID)
        self.buyer = buyer

class SellOrder(Order):
    def __init__(self, value, itemName, itemID, seller):
        super().__init__(value, itemName, itemID)
        self.seller = seller