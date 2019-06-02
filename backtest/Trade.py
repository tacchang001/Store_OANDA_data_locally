
class Trade:

    def __init__(self):
        self.orders = []

    def add_orders(self, orders):
        self.orders += orders

    def remove_orders(self, orders):
        for order in orders:
            try:
                self.orders.remove(order)
            except ValueError:
                pass

    def get_orders(self):
        return self.orders

    def __str__(self):
        return "<{}>".format(len(self.orders))
