from django.urls import path
from about import views as contentViews
urlpatterns = [
    path("",contentViews.about, name="about"),
]
