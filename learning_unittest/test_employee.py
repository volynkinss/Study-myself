import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_1 = Employee("Tim", "Birton", 50000)
        self.emp_2 = Employee("Kate", "Williams", 100000)

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Tim.Birton@email.com")
        self.assertEqual(self.emp_2.email, "Kate.Williams@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Ann"

        self.assertEqual(self.emp_1.email, "John.Birton@email.com")
        self.assertEqual(self.emp_2.email, "Ann.Williams@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Tim Birton")
        self.assertEqual(self.emp_2.fullname, "Kate Williams")

        self.emp_1.first = "John"
        self.emp_2.first = "Ann"

        self.assertEqual(self.emp_1.fullname, "John Birton")
        self.assertEqual(self.emp_2.fullname, "Ann Williams")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 105000)


if __name__ == "__main__":
    unittest.main()
