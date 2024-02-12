from django.views.generic import ListView
from .models import Post
# Create your views here.


class HomePageView(ListView):
    """
    This class extends the generic ListView
    that is used to simply display list of
    objects (could be model objects)
    """
    # the model we will display its objects
    model = Post
    # the template to populate this list of data in
    template_name = "home.html"
