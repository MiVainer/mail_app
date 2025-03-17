from django.db import models
from employees.models import Employee

class ChatMessage(models.Model):
    sender = models.ForeignKey(Employee, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Employee, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.message}"