from django.contrib import admin

from .models import Class


class ClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Class._meta.fields
                    if (field.name != "description")]

    class Meta:
        model = Class


admin.site.register(Class, ClassAdmin)
