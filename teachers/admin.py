from django.contrib import admin

from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')

    class Meta:
        model = Teacher


admin.site.register(Teacher, TeacherAdmin)
