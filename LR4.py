from LR3_3 import Department

import unittest
import pickle


class DepartmentTest(unittest.TestCase):
    def setUp(self):
        self.department = Department()

    def tearDown(self):
        with open(self.department.department_name, 'wb') as f:
            pickle.dump([], f)

    def test_add_department(self):
        initial_count = len(self.department.levels)
        self.department.add_department(1000)
        self.assertEqual(len(self.department.levels), initial_count + 1)

    def test_demolish_department(self):
        self.department.add_department(1000)
        initial_count = len(self.department.levels)

        self.department.demolish_department(initial_count)
        self.assertEqual(len(self.department.levels), initial_count - 1)

    def test_change_balance(self):
        self.department.add_department(1000)
        department_level = self.department.levels[-1]
        new_balance = 2000

        self.department.change_balance(department_level.number, new_balance)
        self.assertEqual(department_level.balance, new_balance)


if __name__ == '__main__':
    unittest.main()
