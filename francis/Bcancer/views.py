
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
    return render(request, 'Bcancer/home.html')



def send_to_org(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', 'N/A')
        comment = request.POST.get('comment', 'No message provided')

        subject = "New message from website"
        message = f"Name: {name or 'N/A'}\nEmail: {email or 'N/A'}\nPhone: {phone}\nMessage: {comment}"
        sender_email = settings.DEFAULT_FROM_EMAIL
        receiver_email = 'francisdugbe967@gmail.com'
        
        try:
            send_mail(subject, message, sender_email, [receiver_email])
            return render(request, 'Bcancer/status.html', {'status': 'success'})
        except BadHeaderError:
            return render(request, 'Bcancer/status.html', {'status': 'failure'})
        except Exception as e:
            return render(request, 'Bcancer/status.html', {'status': 'failure'})

    return render(request, 'Bcancer/home.html')