class HousePlan:
    def __init__(self, name, houseprice, savingrate, salary):
        self.name = name
        self.housePrice = houseprice
        self.rate = savingrate
        self.salary = salary

    @houseprice.setter
    def houseprice(self,houseprice):


if __name__ == "__main__":
    salary = input("Input your Salary")
    savingrate = input('Saving Rate')
    houseprice = input("house price")
    plan = HousePlan("Alice", houseprice, savingrate, salary)



"""
    def add_price(self, price):
        self.price.append(price)

x = HousePlan("Alice")
print(x.name)
x.add_price(200)
"""
