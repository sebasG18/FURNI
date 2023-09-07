from django.shortcuts import render
from .models import Content
# Create your views here.

def about(request):
    contents=Content.objects.all()
    return render(request, "about/about.html", {'listContents':contents})