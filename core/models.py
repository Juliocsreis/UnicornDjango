import uuid
import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
from django.conf import settings
from rest_framework.authtoken.models import Token



def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('upload/', filename)


USER_CATEGORIES = (
    ('S','Startup'),
    ('I', 'Investidor'),
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new user """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True, error_messages={
        'unique': ("A user with that email already exists."),
    })
    name = models.CharField(max_length=255)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    user_category = models.CharField(max_length=1, choices=USER_CATEGORIES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    facebook_id = models.CharField(null=True, max_length=200, unique=True)
    profile_image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    gender = models.CharField(max_length=10, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'user_info_login'
