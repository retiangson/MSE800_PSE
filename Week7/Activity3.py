# Singleton Pattern Ensures all payments are processed in one place, no confusion, no duplicates.
# Factory Pattern Decides which payment method to use.
#The Factory pattern is applied to dynamically create the appropriate payment method object without requiring the client code to know 
# the exact implementation. This improves flexibility and makes the system easy to extend; for example, adding a new payment method requires 
# only creating a new class and registering it with the factory.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Credit Card"


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via PayPal"


class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Bank Transfer"


class CryptoPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Cryptocurrency"


class GooglePayPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via GooglePay"

class PaymentFactory:
    @staticmethod
    def create_payment(method: str) -> PaymentMethod:
        methods = {
            "creditcard": CreditCardPayment,
            "paypal": PayPalPayment,
            "banktransfer": BankTransferPayment,
            "crypto": CryptoPayment,
            "googlepay": GooglePayPayment
        }
        if method.lower() not in methods:
            raise ValueError(f"Unknown payment method: {method}")
        return methods[method.lower()]()

class PaymentGateway:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Initializing Payment Gateway Singleton...")
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process(self, method: str, amount: float):
        payment_processor = PaymentFactory.create_payment(method)
        return payment_processor.process_payment(amount)


if __name__ == "__main__":
    gateway1 = PaymentGateway()
    gateway2 = PaymentGateway()

    print("Are both gateways the same?", gateway1 is gateway2)  # Singleton check

    # Sample transactions
    print(gateway1.process("CreditCard", 250.75))
    print(gateway1.process("PayPal", 99.99))
    print(gateway1.process("BankTransfer", 500.00))
    print(gateway1.process("Crypto", 1200.50))
    print(gateway1.process("GooglePay", 75.20))
