from django.db import models
from .article import Article
from django.urls import reverse
from django.conf import settings

class Comment(models.Model):
    """
    This is the model for the comments to be written
    by users as response to an article(hold article as an fk)
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        This would set the comment given as the
        default value to show after the comment is 
        created.
        """
        return self.comment
    

    def get_absolute_url(self):
        """
        This would return the absolute url 
        of the app
        """
        return reverse("article_list")