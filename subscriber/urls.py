from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('main/', views.show_main_page),
    path('main/validate/', views.validate, name='validate')
]