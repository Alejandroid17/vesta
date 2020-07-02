from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.models import TimeStampedModel
from core.models import UUIDModel
from user.managers import UserManager


class User(AbstractBaseUser, UUIDModel, TimeStampedModel, PermissionsMixin):
    first_name = models.CharField(_("First name"), max_length=120, blank=True)
    last_name = models.CharField(_("Last name"), max_length=120, blank=True)
    email = models.EmailField(_("Email"), unique=True, db_index=True)
    is_staff = models.BooleanField(_('Staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. Unselect '
                                                'this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('Date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # Field to identify the user.

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('user')
        ordering = ['-date_joined']
        app_label = 'user'

    def __str__(self):
        return str(self.email)

    def get_full_name(self) -> str:
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        """
        Returns the short name for the user.
        """
        return self.first_name.strip()
