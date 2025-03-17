from django.test import TestCase
from .models import ChatMessage

class ChatMessageTestCase(TestCase):
    def test_chat_message_creation(self):
        message = ChatMessage.objects.create(message="Hello")
        self.assertEqual(message.message, "Hello")