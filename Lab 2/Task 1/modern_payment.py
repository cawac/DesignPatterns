from .payment_processor import PaymentProcessor

class ModernPaymentSystem(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing payment of ${amount} using modern system")
        return True 