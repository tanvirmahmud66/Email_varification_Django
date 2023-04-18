from django.shortcuts import render, redirect
from django.core.mail import send_mail
import uuid
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from .models import Profile
from django.conf import settings
from django.contrib import messages
# Create your views here.


def registration_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        domain_name = get_current_site(request).domain
        token = str(uuid.uuid4())
        link = f"http//{domain_name}/varified_and_login/{username}/{token}"

        subject = "Email Varification"
        message = f"Please click this link {link} to varify your Registration process"
        recipient_list = [email]
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False
        )
        return render(request, 'login.html')
    return render(request, 'registration.html')


def login_view(request, username, token):
    user_model = User.objects.get(username=username)
    new_profile = Profile.objects.create(
        user=user_model,
        token=token,
        is_varified=True)
    new_profile.save()
    messages.info(request, 'Your email is verified please Login Again')
    return render(request, 'login.html')
