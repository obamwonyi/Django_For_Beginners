from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    Model for the post
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        """
        Sets the default output of the blog in the
        admin panel to the title of the blog.
        """
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

