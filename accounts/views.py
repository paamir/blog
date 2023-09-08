from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('blogs')