from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileDetailView(DetailView):
    model = User
    template_name = 'account_profile/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user





