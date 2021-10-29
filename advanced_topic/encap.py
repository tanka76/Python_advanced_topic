class Computer:

    def __init__(self):
        self.__maxprice = 900
        self.maxprice=9000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
        print("Selling Price: {}".format(self.maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
        self.maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.maxprice=10000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()