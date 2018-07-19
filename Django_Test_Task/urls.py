"""
Метод POST должен всегда использоваться,
если отправка данных приведет к внесению изменений в базе данных на сервере.
Применение данного метода должно повысить уровень защиты от CSRF.
Метод GET должен применяться только для форм,
действия с которыми не приводят к изменению базы данных (например для поисковых запросов).
Кроме того, данный метод рекумендуется применять для создания внешних ссылок на ресурсы сайта.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('teachers/', include('teachers.urls')),
    path('classes/', include('classes.urls')),
    path('users/', include('users.urls')),
    path('schedules/', include('schedules.urls')),
]
