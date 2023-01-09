from django.urls import path
from . import views

urlpatterns = [
    path('',views.form.as_view()),
    path('register', views.register.as_view()),
    path('login', views.LogIn.as_view()),
    path('profile', views.profile.as_view()),
    path('logout', views.logout.as_view())
]
