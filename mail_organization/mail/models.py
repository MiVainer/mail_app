from django.db import models
from employees.models import Employee

class Mail(models.Model):
    sender = models.ForeignKey(Employee, related_name='sent_mails', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Employee, related_name='received_mails', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject