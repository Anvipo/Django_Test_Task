from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.teachers, name='teachers'),
    # path('', views.TeachersListView.as_view(), name='teachers'),
    url(r'ajax/$', views.ajax, name='ajax')
]
