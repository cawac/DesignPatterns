from .legacy_payment import LegacyPaymentSystem
from .legacy_adapter import LegacyPaymentAdapter
from .modern_payment import ModernPaymentSystem

def process_payment(payment_processor, amount: float):
    success = payment_processor.process_payment(amount)
    if success:
        print("Payment processed successfully!")
    else:
        print("Payment processing failed!")

if __name__ == "__main__":
    modern_system = ModernPaymentSystem()
    process_payment(modern_system, 100.0)

    legacy_system = LegacyPaymentSystem()
    legacy_adapter = LegacyPaymentAdapter(legacy_system)
    process_payment(legacy_adapter, 50.0)