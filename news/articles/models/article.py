from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """
    This is the model that would be used to 
    create migrations for the article data 
    storage. 
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """
        This would set the default value to
        display in the admin panel.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        This method is used to retrieve the 
        absolute url of the app
        """
        return reverse("article_detail", kwargs={"pk": self.pk})