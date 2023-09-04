class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
class OrderItem:
    def __init__(self, items, orderId):
        self.items = items
        self.orderId = orderId
    def calculate_item(self):
        total = sum(item.price for item in self.items)
        return total

class OrderManager:
    def place_order(self, order):
        total = order.calculate_item()
        print(f"Total: {total}")

item = Item("Item 1", 100)
item2 = Item("Item 2", 200)

order_item = OrderItem([item, item2], 1)

order_manager = OrderManager()
order_manager.place_order(order_item)
    
    