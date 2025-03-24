import item as i

class Order:

    order_id = 1

    def __init__(self, sandwich, drink, side, sauce):
        self.sandwich = sandwich
        self.drink = drink
        self.side = side
        self.sauce = sauce
        self.total = 0
        self.order_id = Order.order_id
        Order.order_id += 1

    def __str__(self):
        return f"Order {self.order_id} \n-------\n{self.sandwich}\n{self.drink}\n{self.side}\n{self.sauce}\n-----\n${self.total}"

    def set_sandwich(self, sandwich):
        self.sandwich = sandwich

    def set_drink(self, drink):
        self.drink = drink

    def set_side(self, side):
        self.side = side

    def set_sauce(self, sauce):
        self.sauce = sauce

    def add_to_total_cost(self, amount):
        self.total += amount

    def set_order_id(self, order_id):
        self.order_id = random_number