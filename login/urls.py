from django.urls import path

from login import views

urlpatterns = [
    path('', views.index, name="index"),  #
    path('login/', views.login, name="login"),  #
    path('register/', views.reginter, name="register"),  #
    path('pswd_update/', views.pswd_update, name="pswd_update"),  #
    path('logout/', views.logout, name="logout"),  #

]
