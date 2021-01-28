from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.

class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Користувачі повинні мати email адресу!')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    f_name = models.CharField(
        verbose_name="Ім'я",
        max_length=50,
    )

    l_name = models.CharField(
        verbose_name='Прізвище',
        max_length=50,
    )

    phone_number = models.CharField(
        max_length=12,
        verbose_name="Номер телефону",
        null=True,
        blank=True,
        unique=True)

    email = models.EmailField(
        verbose_name='Email-адреса',
        max_length=50,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'



    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin