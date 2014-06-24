class Bottle():
    """docstring for Bottle"""
    def __init__(self, material, color, capacity):
        super(Bottle, self).__init__()
        self.material = material
        self.color = color
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def fill_in(self, capacity):
        if self.capacity < 1 and self.capacity > 0:
            self.capacity += capacity
            return self.capacity
        elif self.capacity == 1:
            return self.capacity

    def fil_out(self, capacity):
        self.capacity -= capacity
        return self.capacity

def main():

    new_bottle = Bottle("plastic", "blue", 1)
    print(new_bottle.get_capacity())
    print(new_bottle.fill_in(0.3))
    print(new_bottle.fil_out(0.5))

if __name__ == '__main__':
    main()
