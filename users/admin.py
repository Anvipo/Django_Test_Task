from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'vk_ID',
        'last_name',
        'first_name',
    ]

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
