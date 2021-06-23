import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models
from .models import User


class Profile(models.Model):
    id = models.UUIDField(_('ID'), auto_created=True,
                          primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(_('city'), max_length=80, blank=True)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)
    bio = models.CharField(_('About me'), max_length=120, blank=True)
    image = models.ImageField(_('Profile image'), upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.email
