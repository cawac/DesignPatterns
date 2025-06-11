# One class - one zone of responsibility

class Cooker:
    def cook(self):
        print("Cooking")

    def deliver_order(self):
        print("Delivering")

    def request_food(self):
        print("Requesting food")

# right variant

class RightCooker:
    def cook(self):
        print("Cooking")

