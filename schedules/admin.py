from django.contrib import admin

from .models import Schedule


class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'class_begin_time',
        'class_end_time',
        'class_name',
        'teacher_name',
    ]

    class Meta:
        model = Schedule


admin.site.register(Schedule, ScheduleAdmin)
