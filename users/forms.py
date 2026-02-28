# forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('avatar', 'phone_number', 'country')
