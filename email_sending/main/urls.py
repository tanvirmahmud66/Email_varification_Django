from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
    path('varify/<str:username>/<str:token>/', views.varify, name='varify'),
]
