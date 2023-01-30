import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Sediqa', 'Hadid')
        self.assertEqual(student.full_name, 'Sediqa Hadid')


if __name__ == "__main__":
    unittest.main()
