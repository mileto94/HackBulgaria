class OrderPizza():
    """docstring for OrderPizza"""
    def __init__(self, order):
        self.order = order

    def take_order(self, name, price):
        new_price = price
        for index in range(len(self.order)):
            if name in self.order[index]:
                new_price += self.order[index][1]
                del self.order[index]
        self.order.append((name, new_price))
        return self.order

    def status_order(self):
        return self.order

    def print_status(self):
        result = ""
        for index in range(len(self.order)):
            result += "%s - %s" % (self.order[index][0], self.order[index][1])
            if index != len(self.order) - 1:
                result += "\n"
        return result
