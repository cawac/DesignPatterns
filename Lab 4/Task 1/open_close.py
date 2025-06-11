# open to extension, close to changes

class DiscountCalculator:
    @staticmethod
    def calculate(customer_type: str, amount: float) -> float:
        match customer_type:
            case 'regular':
                return amount * 0.9
            case 'vip':
                return amount * 0.8
            case 'senior':
                return amount * 0.7

        return 0.0

# right variant

class RightCustomer:
    def __init__(self):
        self.discount: float = 0.0

class ConcreteRegular(RightCustomer):
    def __init__(self):
        super().__init__()
        self.discount = 0.1

class ConcreteVip(RightCustomer):
    def __init__(self):
        super().__init__()
        self.discount = 0.2

class ConcreteSenior(RightCustomer):
    def __init__(self):
        super().__init__()
        self.discount = 0.3

class RightDiscountCalculator:
    @staticmethod
    def calculate(customer: RightCustomer, amount: float) -> float:
        if customer is None:
            return 0.0

        return (1 - customer.discount) * amount