from django.test import TestCase
from .models import Department, Employee

class EmployeeTestCase(TestCase):
    def test_employee_creation(self):
        department = Department.objects.create(name="IT")
        employee = Employee.objects.create(user=User.objects.create(username="testuser"), department=department)
        self.assertEqual(employee.user.username, "testuser")