from django.shortcuts import render, redirect
from .forms import MailForm
from .models import Mail

def send_mail(request):
    if request.method == 'POST':
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            mail = form.save(commit=False)
            mail.sender = request.user.employee
            mail.save()
            return redirect('mail_list')
    else:
        form = MailForm()
    return render(request, 'mail/send_mail.html', {'form': form})

def mail_list(request):
    mails = Mail.objects.filter(recipient=request.user.employee)
    return render(request, 'mail/mail_list.html', {'mails': mails})