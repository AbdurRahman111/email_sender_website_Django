from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method=="POST":
        subject=request.POST['subject']
        email_mass=request.POST['email_mass']
        mass=request.POST['mass']

        send_mail(
            subject,#subject
            mass,#massage
            '',#from email
            [email_mass],#to email

            fail_silently=False

        )



        return render(request, 'index.html')

    else:
        return render(request, 'index.html')
