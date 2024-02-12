from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    """
    This class would be responsible for
    adding the generic view for the base.html template
    for the blog post home route , which would
    make use of the model, Post as object resource
    to generate list from .
    """
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    """
    This class would be responsible for adding the generic
    view for loading our various post in details, like
    dedicating a particular view to one post
    """
    model = Post
    template_name = "post_detail.html"
