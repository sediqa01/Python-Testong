import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Sediqa', 'Hadid')
        self.assertEqual(student.full_name, 'Sediqa Hadid')

    def test_alert_santa(self):
        student = Student('Sediqa', 'Hadid')
        student.alert_santa()

        self.assertTrue(student.naughty_list)

    def test_email_address(self):
        student = Student('Sediqa', 'Hadid')
        self.assertEqual(student.email_address, 'Sediqa.Hadid@email.com')


if __name__ == "__main__":
    unittest.main()
