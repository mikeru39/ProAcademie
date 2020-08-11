from django.shortcuts import render

from authapp.models import User
from mainapp.models import Course


def index(request):
    if request.user.is_authenticated:
        user = User.objects.get(uuid=request.user.pk)
        user_courses = []
        user_courses_pk = []
        for added in user.added_courses.all():
            user_courses.append(added.course)
            user_courses_pk.append(added.course.pk)
        courses = []
        for course in Course.objects.all():
            if course.pk not in user_courses_pk:
                courses.append(course)
        content = {'courses': courses,
                   'user_courses': user_courses
                   }
    else:
        courses = Course.objects.all()
        content = {'courses': courses }
    return render(request, 'mainapp/dashboard.html', content)
