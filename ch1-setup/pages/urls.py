from django.urls import path
from .views import homePageView

urlpatterns = [
    # "" : the url to look out for
    # homePageView : the function to handle the route
    # name : the name to be given to the route for future reference.
    path("", homePageView, name="home"),
]