import unittest
from student import Student
from datetime import date, timedelta


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setup")
        self.student = Student("Sediqa", "Hadid")

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

    def tearDown(self):
        print("tear down")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "Sediqa Hadid")

    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email_address(self):
        print("test_email_address")
        self.assertEqual(self.student.email_address, 'sediqa.hadid@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

if __name__ == "__main__":
    unittest.main()
