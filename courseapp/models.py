from django.core.files.storage import FileSystemStorage
from django.db import models

from mainapp.models import Course


def user_dir_path(self, filename):
    return 'homework/{0}/{1}/{2}'.format(self.user, self.course_pk, filename)


class File(models.Model):
    user = models.CharField(max_length=50)
    course_pk = models.CharField(max_length=30)
    path = models.FileField(upload_to=user_dir_path)


class AddedCourse(models.Model):
    progress = models.IntegerField(default=0)
    course = models.OneToOneField(Course, models.CASCADE)
    homeworkFiles = models.ManyToManyField(File, related_name='homework')

    def __str__(self):
        return str(self.pk)
