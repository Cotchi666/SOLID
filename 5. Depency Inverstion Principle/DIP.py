class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of {amount}")
    pass

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self,order_id, items,payment_getway):
        self.order_id = order_id
        self.items = items
        self.payment_getway = payment_getway
    def calculate_item(self):
        total = sum(item.price for item in self.items)
        return total
    def place_order(self):
        total = self.calculate_item()
        self.payment_getway.process_payment(total)

class OrderManager:
    def __init__(self,order):
        self.order = order
    def place_order(self):
        total = order.place_order()

payment_gateway = PaymentGateway()
order_items={
    Item("Item 1", 100),
    Item("Item 2", 200),
}
order= Order(123,order_items,payment_gateway)
order_manager = OrderManager(order)
order_manager.place_order()