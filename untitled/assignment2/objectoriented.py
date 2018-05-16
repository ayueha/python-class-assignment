class Cookies:
    def __init__(self, flavor, topping):
        self.cookie_flavor = flavor
        self.cookie_topping = topping

    def get_cookie(self):
        return print("Cookie is " + self.cookie_flavor + " and " + self.cookie_topping)

    def __set_name__(self, flavor, topping):
        while True:
            if flavor != "Chocolate" and flavor != "Vanilla":
                print("Input Chocolate or Vanilla, program did not executed")
                flavor = input("Input your flavor from  Chocolate or Vanilla")
            elif topping != "Apple":
                if topping != "Orange":
                    if topping != "Strawberry":
                        print("Input Apple, Orange or Strawberry, program did not executed")
                        topping = input("Input your flavor from  Apple, Orange or Strawberry")
                    elif topping == "Strawberry":
                        break
                elif topping == "Orange":
                    break
            elif topping == "Apple":
                break


if __name__ == "__main__":
    print(id(Cookies("Mattya", "Azuki")))
    flavor = input("Input your flavor from  Chocolate or Vanilla")
    topping = input("Input your topping from Apple, Orange or Strawberry")
    cookie = Cookies(flavor, topping)
    print(id(Cookies(flavor, topping)))
    cookie.__set_name__(flavor, topping)
    cookie.get_cookie();
