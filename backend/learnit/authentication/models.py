from django.db import models
from django.contrib.auth.models import (
    BaseUserManager
)
from datetime import datetime, timedelta
import jwt
from django.conf import settings

# Create your models here.


class AppUser(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):

        dt = datetime.now()+timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token
