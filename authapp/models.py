import uuid as uuid

from django.conf import settings

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from courseapp.models import AddedCourse
from mainapp.models import Course


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False,
                            verbose_name='ID')
    added_courses = models.ManyToManyField(AddedCourse, related_name='courses')

    def __str__(self):
        return str(self.first_name or self.username)
