class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.money = 0
        self.house = None

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Money:", self.money)
        print("House:", self.house)

    @staticmethod
    def default_info():
        print("Default Name:", Human.default_name)
        print("Default Age:", Human.default_age)

    def make_deal(self, house, price):
        if self.money >= price:
            self.money -= price
            self.house = house
            print("House purchased successfully!")
        else:
            print("Not enough money to buy the house.")

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        self.make_deal(house, final_price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self):
        super().__init__(40, 100000)


Human.default_info()

human = Human()
human.info()

small_house = SmallHouse()

human.buy_house(small_house, 0.1)
human.info()

human.earn_money(120000)
human.buy_house(small_house, 0.1)
human.info()
