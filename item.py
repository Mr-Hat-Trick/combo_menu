class Item:

    item_id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.item_id = Item.item_id
        Item.item_id += 1

    def __str__(self):
        return f"{self.item_id} --- {self.name} - ${self.price}"

    def get_price(self):
        return self.price


sandwich = [Item("Adam double", 2.50), Item("10 for 3 special", 3), Item("9 piece chicken tenders", 2)]
drink = [Item("Tiny", 0.75), Item("Average", 1.50), Item("Largo", 2)]
side = [Item("small", 0.50), Item("medium", 1.25), Item("large", 1.75)]
sauce = [Item("Adam sauce", 0.25)]