from django.db import models


class Post(models.Model):
    """
    Model for the post table
    """
    text = models.TextField()

    def __str__(self):
        """
        This will populate the preview of the data
        in the admin panel with the first 50 characters
        of the text filed declared above.
        """
        return self.text[:50]
