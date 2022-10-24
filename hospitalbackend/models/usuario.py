from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

def create_superuser(self, username, password):
    """
    Creates and saves a superuser with the given username and password.
    """
    user = self.create_user(
    username=username,
     password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

