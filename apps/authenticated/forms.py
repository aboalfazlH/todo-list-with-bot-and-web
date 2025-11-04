from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields ="__all__"