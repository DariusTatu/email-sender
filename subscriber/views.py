from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import json


def show_main_page(request):
    return render(request, "main.html")


def send_email(request):
    title = "Get the chance to win 1 million $ by clicking this link"
    body = "Hello dear followers, you can follow me on my social media for a chance to win 1 million $."

    send_mail(
        subject=title,
        message=body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=settings.RECIPIENT_ADDRESS)

    return render(request, 'success.html')
