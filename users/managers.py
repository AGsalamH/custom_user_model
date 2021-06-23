from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('staff', False)
        extra_fields.setdefault('admin', False)

        if extra_fields.get('staff') is True:
            raise ValueError(_('A user must have can NOT have staff=True'))
        if extra_fields.get('admin') is True:
            raise ValueError(_('A user can NOT have admin=True'))

        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password, **extra_fields):
        extra_fields.setdefault('staff', True)
        extra_fields.setdefault('admin', False)

        if extra_fields.get('staff') is not True:
            raise ValueError(_('A staffuser must have staff=True'))
        if extra_fields.get('admin') is True:
            raise ValueError(_('A staffuser can NOT have admin=True'))

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('staff', True)
        extra_fields.setdefault('admin', True)

        if extra_fields.get('staff') is not True:
            raise ValueError(_('A superuser must have staff=True'))
        if extra_fields.get('admin') is not True:
            raise ValueError(_('A superuser must have admin=True'))

        return self._create_user(email, password, **extra_fields)
