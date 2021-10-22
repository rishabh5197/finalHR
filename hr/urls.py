from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hr/results', views.results, name="results"),
    path('hr/gotoadduser', views.gotoadduser, name="gotoadduser"),
    path('hr/viewprofile', views.viewprofile, name="viewprofile"),
    path('hr/editprofile', views.editprofile, name="editprofile"),
    path('hr/deleteprofile', views.deleteprofile, name="deleteprofile"),
    path('hr/attendancereport', views.attendancereport, name="attendancereport"),
    path('hr/salary', views.salary, name="salary"),
    path('hr/editconfiguration', views.editconfiguration, name="editconfiguration"),
]
