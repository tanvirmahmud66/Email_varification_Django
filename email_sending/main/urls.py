from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
    path('varified_and_login/<str:username>/<str:token>/',
         views.login_view, name='login'),
]
