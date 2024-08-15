# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.students, name='students'),
# ] 
from django.urls import path
from . import views
from django.http import HttpResponse
from django.template import loader

urlpatterns = [
    path('students/', views.students, name='students'),
    path('createstudent/', views.createStudent, name='createStudent'),
    path('view/', views.viewStudent, name='view'),
]

# def members(request):
#   template = loader.get_template('myfirst.html')
#   return HttpResponse(template.render())