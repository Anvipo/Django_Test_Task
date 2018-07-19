from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.ClassesListView.as_view(), name='classes'),
    path('', views.classes, name='classes'),
    url(r'ajax/$', views.ajax, name='ajax')
]
