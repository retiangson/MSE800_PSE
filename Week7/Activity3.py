# Singleton Pattern Ensures all payments are processed in one place, no confusion, no duplicates. PaymentGateway()
# Factory Pattern Decides which payment method to use. create_payment()
#The Factory pattern is applied to dynamically create the appropriate payment method object without requiring the client code to know 
# the exact implementation. This improves flexibility and makes the system easy to extend; for example, adding a new payment method requires 
# only creating a new class and registering it with the factory. process_payment()

from abc import ABC, abstractmethod

class IPaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class CreditCardPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Credit Card"


class PayPalPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via PayPal"


class BankTransferPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Bank Transfer"


class CryptoPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via Cryptocurrency"


class GooglePayPayment(IPaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Processing ${amount:.2f} via GooglePay"

class PaymentFactory:
    @staticmethod
    def create_payment(method: str) -> IPaymentMethod:
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
            cls._instance = super(PaymentGateway, cls).__new__(cls)
        return cls._instance

    def process(self, method: str, amount: float):
        payment_processor = PaymentFactory.create_payment(method)
        return payment_processor.process_payment(amount)


if __name__ == "__main__":
    gateway = PaymentGateway()

    print(gateway.process("CreditCard", 250.75))
    print(gateway.process("PayPal", 99.99))
    print(gateway.process("BankTransfer", 500.00))
    print(gateway.process("Crypto", 1200.50))
    print(gateway.process("GooglePay", 75.20))
