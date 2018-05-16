class Cookies(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, flavor, topping):
        self.__cookie_flavor = flavor
        self.__cookie_topping = topping

    @property
    def baked_cookie(self):
        return self.__cookie_flavor + " " + self.__cookie_topping + " cookies have been made"

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
    print("Comfirm instance ID" + str(id(Cookies("Mattya", "Azuki"))))
    test_instance = id(Cookies("Mattya", "Azuki"))
    flavor = input("Input your flavor from  Chocolate or Vanilla")
    topping = input("Input your topping from Apple, Orange or Strawberry")
    result = Cookies(flavor, topping)

    print("Comfirm instance ID" + str(id(Cookies(flavor, topping))))
    current_instance =id(Cookies(flavor, topping))
    result.__set_name__(flavor, topping)
    print(result.baked_cookie)
    if current_instance==test_instance:
        print("Same instance")

