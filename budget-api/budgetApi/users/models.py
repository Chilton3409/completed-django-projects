from email.policy import default
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.contrib.postgres.fields import JSONField
from django.db.models import JSONField
from django.db.models import Sum
from django.db.models.functions import Coalesce





from .managers import CustomUserManager #manager class we created in managers.py




# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= []

    objects = CustomUserManager()

    

    def __str__(self):
        return self.email



#models associated with the permissions tutorial

        

   
  


    