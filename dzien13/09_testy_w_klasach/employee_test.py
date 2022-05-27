from employee import Employee

class TestEmployee:
    @classmethod
    def setup_class(cls):
        """ wykonywane raz przed wszystkimi testami z tej klasy"""
        print('przed testami z klasy ' + cls.__name__)

    @classmethod
    def teardown_class(cls):
        """ wykonywane raz po wszystkich testach z tej klasy"""
        print('po testach z klasy ' + cls.__name__)

    def setup_method(self, method):
        """wykonywane przed każdym testem"""
        print("start testu ", method.__name__)
        self.emp = Employee('Jan', 'Nowak', 100.0)

    def teardown_method(self, method):
        """wykonywane po każdym teście"""
        print("koniec testu ", method.__name__)

    def test_zwykly(self):
        self.emp.register_time(5)
        assert 500 == self.emp.pay_salary()

    def test_employee_initial(self):
        print('Typ testowanego obiektu:', type(self.emp))
        assert 0 == self.emp.pay_salary()

    def test_employee_reset(self):
        self.emp.register_time(5)
        pierwsza_wyplata = self.emp.pay_salary()
        druga_wyplata = self.emp.pay_salary()
        assert 0 == druga_wyplata

    def test_employee_overtime(self):
        self.emp.register_time(10)
        assert 1200 == self.emp.pay_salary()

    def test_employee_cumulate(self):
        self.emp.register_time(5)
        self.emp.register_time(5)
        assert 1000 == self.emp.pay_salary()
