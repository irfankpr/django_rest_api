from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class MyAccountManager(BaseUserManager):
    def create_user(self, name, phone, email, password=None):
        if not email:
            raise ValueError('email required')
        if not name:
            raise ValueError('name required')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password, ):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            name=name,
            phone=None
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save()
        return user


# Create your models here.
class users(AbstractBaseUser):
    username = None
    first_name = None
    last_name = None
    date_joined = None
    last_login = None
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(('phone number'), max_length=15, unique=True)
    email = models.EmailField(blank=False, unique=True, max_length=100)
    DOB = models.DateField(null=True)
    propic = models.ImageField(upload_to="propic", default=None)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, add_label):
        return True
