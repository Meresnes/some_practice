class Restarant():

    def __init__(self, number, foodType, name ,price ,money):
        self.number = number
        self.foodType = foodType
        self.name = name
        self.price = price
        self.money = money
        
    def buy_food(self, n):
        if ((self.number - n) > 0):
            self.money += self.price * n
            print("Some one bought {} {} , now {} have {}$".format(n, self.foodType, self.name , self.money))
        else :
            print('Not enougth ' + self.foodType)
class IceCreamStand(Restarant):

    def __init__(self, number, foodType, name ,price ,money):
        super().__init__(number, foodType, name ,price ,money)

icecream_shop = IceCreamStand(10, 'icecream', 'Robins shop', 10, 0)
icecream_shop.buy_food(9)
