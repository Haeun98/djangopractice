from django.urls import path

from . import views

urlpatterns = [
    path('<age>/', views.index, name='index'),
]
