from django.db import models

from pricecompare.helper.models import TrackingModel
from django.contrib.auth.models import(PermissionsMixin,BaseUserManager, AbstractBaseUser)

# Create your models here.
#add new properties access_token, is_email _verified
#Use emailand password instead of username/password

class User(AbstractBaseUser, TrackingModel, PermissionsMixin ):
    pass
