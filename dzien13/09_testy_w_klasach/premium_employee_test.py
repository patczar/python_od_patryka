from employee_test import TestEmployee
from premium_employee import PremiumEmployee

# Teraz dla obiektu PremiumEmployee - jak go tworzymy w detup_method - zostaná wykonane także testy odziedziczone z TestEmployee
# - czyli testy zgodności z kontraktem klasy Employee
class TestPremiumEmployee(TestEmployee):
    def setup_method(self, method):
        """wykonywane przed każdym testem; to powinno nadpisać setup z nadklasy"""
        print("start testu ", method.__name__)
        self.emp = PremiumEmployee('Jan', 'Nowak', 100.0)


    def test_premium_employee(self):
        self.emp.register_time(5)
        self.emp.give_bonus(1000)
        assert 1500 == self.emp.pay_salary()

    def test_premium_employee_reset(self):
        self.emp.register_time(5)
        self.emp.give_bonus(1000)
        self.emp.pay_salary()
        assert 0 == self.emp.pay_salary()

    def test_premium_employee_no_bonus(self):
        self.emp.register_time(5)
        assert 500 == self.emp.pay_salary()

    def test_premium_employee_multi_bonus(self):
        self.emp.give_bonus(1000)
        self.emp.give_bonus(300)
        assert 1300 == self.emp.pay_salary()
