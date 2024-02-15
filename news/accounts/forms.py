from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Modifies the extended UserCreationForm , so as to
    add additional form fields and model to be used for
    the data insertion
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username", 
            "email", 
            "age",
            )


class CustomUserChangeForm(UserChangeForm):
    """
    Modifies the extended UserChangForm, so as to 
    add fields and set model to use for data update.
    """
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "age",
        )
