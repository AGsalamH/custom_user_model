import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(_("ID"), auto_created=True,
                          primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        _("Email Address"),
        max_length=255,
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    first_name = models.CharField(_('first name'), max_length=80, blank=True)
    last_name = models.CharField(_('last name'), max_length=80, blank=True)

    active = models.BooleanField(
        _('active status'), default=True)  # can login ?
    staff = models.BooleanField(
        _('staff status'), default=False)  # Staff member ?
    admin = models.BooleanField(
        _('superuser status'), default=False)  # superuser ?

    USERNAME_FIELD = 'email'

    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = []

    # My custom User manager
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.full_name or self.email

    ''' 
        - is_staff & is_superuser properties:
            Need to be overriden since i'm using different names `staff` & `admin` 
            to be able to manage permissions and groups    
    '''

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email
