from django.urls import path

from courseapp import views

app_name = 'courseapp'

urlpatterns = [
    path('user/<int:pk>/', views.course_intro, name='user'),
    path('add/<int:pk>/', views.payment_for_the_course, name='add'),
    path('lessons/<int:pk>/', views.lessons, name='lessons'),
    path('intro/<int:pk>/', views.course_intro, name='intro')

]
