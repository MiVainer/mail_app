from django import forms
from .models import Mail

class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['recipient', 'subject', 'body', 'attachment']