import binascii
import os

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from apps.account.models import Contacts,User,Business

@python_2_unicode_compatible
class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        User, related_name='auth_token_user',
        on_delete=models.CASCADE, verbose_name=_("User"),blank=True,null=True
    )
    business = models.OneToOneField(
        Business, related_name='auth_token_business',
        on_delete=models.CASCADE, verbose_name=_("Business"),blank=True,null=True
    )
    contact = models.OneToOneField(
        Contacts, related_name='auth_token_contact',
        on_delete=models.CASCADE, verbose_name=_("Contact"),blank=True,null=True
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = 'rest_framework.authtoken' not in settings.INSTALLED_APPS
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

