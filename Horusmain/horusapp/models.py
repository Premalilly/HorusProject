# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings




# Create your models here.
class Userapi(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = PhoneNumberField()

    class Meta:
        db_table = 'tableuser'

    def __unicode__(self):
        return '%s %s %d' % (self.name, self.email, self.mobile)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

