from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('main/', views.show_main_page),
    path('main/send/', views.validate, name='send')
]