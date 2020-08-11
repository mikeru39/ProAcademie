from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2')