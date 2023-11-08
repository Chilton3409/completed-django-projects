from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.contrib.auth.models import Permission


class CustomUserManager(BaseUserManager):
    """
    Customer user model manager where email is the uniq identtifier for auth instead of usernames
    """
    def create_user(self, email,password, **extra_fields):
        #create and save a user with the given email and password
        if not email:
            raise ValueError(_('The Email must be set'))
        
        email = self.normalize_email(email)
        
        
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        
       
       
        


        
        user.save()
        
        
        return user
        
    
   

            
        
            


        

    
    def create_superuser(self, email, password, **extra_fields):
        #create and save a Superuser with the gicen email and password
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
       
        


        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must not have is_staff=True.'))
       
        return self.create_user(email, password, **extra_fields)
