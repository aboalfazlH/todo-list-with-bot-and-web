from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(verbose_name=_("email"),unique=True)
    bale_id = models.CharField(max_length=110,verbose_name="شناسه بله",null=True)