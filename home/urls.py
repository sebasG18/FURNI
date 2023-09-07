from django.urls import path
from home import views as homeViews
from core import views
urlpatterns = [
    path("",homeViews.index, name="home"),
    path("", views.cart, name="carrito"),
]
