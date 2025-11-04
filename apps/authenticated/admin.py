from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    readonly_fields = ("date_joined", "last_login")
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': (
                "username","email","password1","password2",
            ),
        }),
    )
    fieldsets = (
        (_('important fields'), {
            'classes':('wide'),
            'fields': (
                "username","email","password1","password2",
                "first_name","last_name",
            ),
        }),
        (_('advanced fields'), {
            'classes':('wide'),
            'fields': (
                "date_joined","last_login"
            ),
        }),
    )