from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    # note reverse_lazy was used cause all
    # urls might have not been loaded at the
    # time of user creation .
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


