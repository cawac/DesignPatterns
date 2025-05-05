from .payment_processor import PaymentProcessor
from .legacy_payment import LegacyPaymentSystem

class LegacyPaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_system: LegacyPaymentSystem):
        self.legacy_system = legacy_system

    def process_payment(self, amount: float) -> bool:
        result = self.legacy_system.make_payment(amount)
        return "Processed" in result 