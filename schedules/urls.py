from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.schedules, name='schedules'),
    # path('', views.SchedulesListView.as_view(), name='schedules'),
]
