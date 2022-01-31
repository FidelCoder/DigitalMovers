#from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
#from . models import Contact
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    return render(request, "moversapp/index.html")

def getquote(request):
    return render(request, 'moversapp/getquote.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        movingfrom = request.POST.get('movingfrom')
        movingto = request.POST.get('movingto')
        message = request.POST.get('message')
        email = request.POST.get('email')
        
        data = {
            'name':name,
            'subject':subject,
            'movingfrom':movingfrom,
            'movingto':movingto,
            'message':message,
            'email':email,
        }
        message = '''
        New message: {}
        From: {}
        '''.format(data['name'], data['subject'], data['movingfrom'], data['movingto'], data['message'], data['email'])
        send_mail(data['subject'], name, movingfrom, movingto, message, '', ['griffinesonyango@gmail.com'])
    return render(request, 'moversapp/index.html', {})
    
        

