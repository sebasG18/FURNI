from django.shortcuts import render

# Create your views here.

def shop(request):
    return render(request, "core/shop.html")
def cart(request):
    return render(request, "core/cart.html")




