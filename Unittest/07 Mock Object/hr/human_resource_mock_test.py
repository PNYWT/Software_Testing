import unittest
from unittest.mock import Mock
from human_resource import Employee, HumanResourceService

class HumanResourceServiceTest(unittest.TestCase):

    def test_raise_salary_all(self):

        # create mock objects
        mock_employee1 = Mock()
        mock_employee2 = Mock()

        # create CUT and seting up
        hr = HumanResourceService()
        hr.add_employee(mock_employee1)
        hr.add_employee(mock_employee2)

        # call method under test
        hr.raise_salary_all(0.1)

        # ตรวจสอบที่ mock object
        mock_employee1.raise_salary.assert_called_with(0.1)
        mock_employee2.raise_salary.assert_called_with(0.1)
