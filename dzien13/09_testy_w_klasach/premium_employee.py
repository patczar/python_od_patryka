from employee import Employee

class PremiumEmployee(Employee):
    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        do_zaplaty = super().pay_salary() + self.bonus
        self.bonus = 0
        return do_zaplaty