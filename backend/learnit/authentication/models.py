from django.db import models

from datetime import datetime, time, timedelta
import jwt
from django.conf import settings

from course.models import Course
# Create your models here.


class AppUser(models.Model):
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):

        dt = datetime.now()+timedelta(days=60)
        timestamp = dt.timestamp()
        print(timestamp)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(timestamp)
        }, settings.SECRET_KEY, algorithm='HS256')
        return token
