import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.models import User, AddedCourse
from courseapp.models import File
from mainapp.models import Course


@login_required
def lessons(request, pk):
    course = Course.objects.get(pk=pk)
    content = {
        'course': course
    }
    if request.method == 'POST':
        for item in request.FILES.getlist('file'):
            file = File()
            file.user = request.user.pk
            file.course_pk = pk
            file.path = item
            file.save()
    return render(request, 'courseapp/course-lesson-3.html', content)


def course_intro(request, pk):
    user = User.objects.get(uuid=request.user.pk)
    user_courses = user.added_courses.all()
    user_courses_pk = user.added_courses.all().values_list('pk', flat=True)
    course = Course.objects.get(pk=pk)
    content = {
        'is_new_user_course': True,
        'course': course
    }
    return render(request, 'courseapp/course-intro.html', content)


@login_required
def proceed_course(request, pk):
    course = Course.objects.get(pk=pk)
    content = {
        'course': course
    }
    return render(request, 'courseapp/course-lesson-3.html', content)


@login_required
def payment_for_the_course(request, pk):
    course = Course.objects.get(pk=pk)
    user = User.objects.get(uuid=request.user.pk)
    add_course(course, user)
    print(user.added_courses.all())
    user_dir = settings.MEDIA_ROOT + '\\homework\\' + str(user.uuid) + '\\' + str(pk) + '\\'
    if not os.path.exists(user_dir):
        os.mkdir(user_dir)
    return HttpResponseRedirect(reverse('course:lessons', kwargs={'pk': pk}))

# def cpuc (user, course_pk): #checking purchased user courses
#     return course_pk in us


def add_course(course, user):
    user_course = AddedCourse()
    user_course.user = user
    user_course.course = course
    user_course.save()
    user.added_courses.add(user_course)
