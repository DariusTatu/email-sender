from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import json

# Shows the main web page


def show_main_page(request):
    return render(request, "main.html")

# Sends the email to the defined list from settings.py


def send_email(request):
    title = "Bun venit la cafelutza DevOpsista"
    body = "In aceasta seara la ora 18:30 ne intalnim, prieteni!"

    send_mail(
        subject=title,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=settings.RECIPIENT_ADDRESS)
# Returns the email has been successfully sent message
    return render(request, 'success.html')
