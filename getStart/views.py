from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def index(request):
    return render(request, 'getStart/getStartIndex.html')

class ContactForm(forms.Form):
    name    = forms.CharField(max_length = 100)
    subject = forms.CharField()
    sender  = forms.CharField()
    message = forms.CharField()

    
def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = 'arbi.tularov1@yandex.ru' #form.cleaned_data['sender']
            message = "Name: {}, WeChat: {}, Email: {}".format(form.cleaned_data['name'], form.cleaned_data['message'], form.cleaned_data['sender'])

            recipients = ['arbi.tularov@yandex.ru', 'vizamv@qq.com']

            send_mail(subject, message, 'arbi.tularov1@yandex.ru', recipients)
            return render(request, 'getStart/thanks.html')
    else:
        form = ContactForm()
        return render(request, 'mainApp/index.html')
