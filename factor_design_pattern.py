from abc import ABC, abstractmethod

class Coffee(ABC):
    def prepare(self):
        pass

class Expresso(Coffee):
    def prepare(self):
        return "Preparing a rich and strong expresso"

class Latte(Coffee):
    def prepare(self):
        return "preparing creamy and sweet latte"

class Cappucino(Coffee):
    def prepare(self):
        return "preparing delicious cappicono"

class Coffeemachi:
    def make_coffee(self, coffee_type):
        if coffee_type == "Expresso":
            return Expresso().prepare()
        elif coffee_type == "Latte":
            return Latte().prepare()
        elif coffee_type == "Cappucino":
            return Cappucino().prepare()
        else:
            return "Unknown coffee type!"


if __name__ == "__main__":
    machine = Coffeemachi()

    coffee =machine.make_coffee("Expresso")
    print(coffee)
    coffee =machine.make_coffee("Latte")
    print(coffee)
    coffee =machine.make_coffee("Cappucino")
    print(coffee)
