# Remember views in Django acts like controllers in Larvavel

from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    """
    This is a class based view (cbv) that extends
    the generic Template view from django
    """
    template_name = "home.html"


class AboutPageView(TemplateView):
    """
    This is a class based view (cbv) that extends
    The generic Template view from django
    it would handle the about page template
    rendering
    """
    template_name = "about.html"
