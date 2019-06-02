
class Trade:

    def __init__(self):
        self.orders = []

    def add_orders(self, orders):
        self.orders += orders

    def remove_orders(self, orders):
        for order in orders:
            try:
                if order in self.orders:
                    self.orders.remove(order)
            except ValueError:
                pass

    def get_orders(self):
        return self.orders

    def __str__(self):
        return "<{}>".format([str(i) for i in self.orders])


if __name__ == "__main__":
    from backtest.order import Order
    o1 = Order()
    o2 = Order()
    o3 = Order()
    ol = [o1, o2, o3]
    print(ol)
    ol.remove(o1)
    print(ol)
