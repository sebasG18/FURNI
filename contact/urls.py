from django.urls import path
from  . import views as coreViews
urlpatterns = [
    path("", coreViews.contact, name="contact"),
]
