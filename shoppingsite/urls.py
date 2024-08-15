from shoppingsite import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mainpage/',views.mainpage, name='mainpage'),
    path('contactUs/',views.contactUs, name='contactUs'),
    path('aboutUs/',views.aboutUs, name='aboutUs'),
    path('signup/',views.signup,name='signup')

]