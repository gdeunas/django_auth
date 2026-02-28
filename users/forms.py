# forms.py
from django.contrib.auth.forms import UserCreationForm
from catalog.forms import StyleFormMixin
# from users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm, StyleFormMixin):
    class Meta:
        model = User
        fields = ('email',)
