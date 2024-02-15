from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    """
    This is the class that creates the form
    for adding comment to a particular article
    """
    class Meta:
        model = Comment
        fields = ("comment", "author")