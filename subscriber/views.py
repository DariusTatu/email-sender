from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import json

def show_main_page(request):
    return render(request, "main.html")


def validate(request):
    if request.method == 'POST': 
        send_email()
    return render(request, 'success.html')


def send_email():
    title = "Email for my followers"
    body = "Hello dear followers, this is my first email."

    send_mail(
        subject=title,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])