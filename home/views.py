from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):
    projects=Project.objects.all()
    return render(request, "home/index.html", {'listProjects':projects})
def cart(request):
    return render(request, "core/cart.html")

