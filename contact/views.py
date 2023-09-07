from django.shortcuts import render, redirect
from . forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def contact(request):
    contactForm=ContactForm()
    if request.method=="POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name', '')
            lastname=request.POST.get('lastname', '')
            email=request.POST.get('email', '')
            message=request.POST.get('message', '')
            emailContact=EmailMessage(
                "FURNI nueva mensaje",
                "De {} <{}>\n\nMensaje:n\n\{}".format(name,email, message),
                "parami@gmail.com",
                ["correo-prueba@inbox.mailtrap.io"],
                reply_to=[email]
            )
            try:
                emailContact.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
            
    return render(request, "contact/contact.html", {'contactForm': contactForm})
