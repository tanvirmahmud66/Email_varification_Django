from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def home(request):
    if request.method == "POST":
        subject = "Testing"
        email = request.POST['email']
        recipient_list = [email,]
        message = request.POST["email_body"]
        email_from = "tanvirmahmudfahim1313@gmail.com"
        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)
    return render(request, 'home.html')
