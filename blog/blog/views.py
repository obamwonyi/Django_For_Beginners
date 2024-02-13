from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Post

from django.urls import reverse_lazy

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


class BlogCreateView(CreateView):
    """
    This class base view would be used
    to set up the view for creating (inserting)
    Post into the blog.
    """
    model = Post
    template_name = "post_new.html"

    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    """
    This class base view would be used to set up
    the view for updating the post that have
    been created from the BlogCreateView class template
    (post_new.html)
    """
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "author", "body"]


class BlogDeleteView(DeleteView):
    """
    This class base view would be used to set up the view
    for deleting blog post
    """
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
