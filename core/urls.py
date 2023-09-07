from django.urls import path
from . import views as coreViews
urlpatterns = [
    path("shop/",coreViews.shop, name="shop" ),
    path("cart/",coreViews.cart, name="cart" ),
]
