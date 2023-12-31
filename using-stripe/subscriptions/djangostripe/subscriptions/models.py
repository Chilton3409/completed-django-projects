from django.db import models

# Create your models here.
from django.contrib.auth.models import User

#may have to chaneg things using a custom user model, easy enough though
class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    