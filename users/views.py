# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.views.generic.edit import CreateView, UpdateView
from .forms import UserRegisterForm, User, UserProfileForm
import os
from dotenv import load_dotenv

load_dotenv(override=True)


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе'
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('catalog:products_list')

    def get_object(self, queryset=None):
        return self.request.user
