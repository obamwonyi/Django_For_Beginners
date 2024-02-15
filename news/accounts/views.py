from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    """
    This class will handle the sign up view
    with a modified form implemented.
    """
    # Here we are adding the custom form class
    # We created earlier.
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
