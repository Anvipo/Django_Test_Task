from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import SignUpForm


class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
