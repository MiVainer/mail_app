from django.test import TestCase
from .models import Mail

class MailTestCase(TestCase):
    def test_mail_creation(self):
        mail = Mail.objects.create(subject="Test", body="Test body")
        self.assertEqual(mail.subject, "Test")