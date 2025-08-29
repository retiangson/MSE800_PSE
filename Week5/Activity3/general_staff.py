from person import Person

class GeneralStaff(Person):
    def __init__(self, name, address, age, ID, tax_code, pay_rate):
        super().__init__(name, address, age, ID)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        return super().display_info() + f", Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}"