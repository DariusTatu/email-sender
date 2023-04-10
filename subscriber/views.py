from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

def say_hello(request):
    return render(request, "hello.html", {'name': "Darius"})

def show_main_page(request):
    return render(request, "main.html")

def validate(request):
    if request.method == 'POST':
        email= request.POST["email"]
        dict = {
            'email_body': email,
        }
        send_email(dict)
    return render(request, 'success.html', dict)


def send_email(dict):
    email_body = dict["email_body"]
    print(email_body)
    
    send_mail(
        subject='Email test',
        message='Email test from yahoo',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.RECIPIENT_ADDRESS])