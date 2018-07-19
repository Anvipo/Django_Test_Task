from django.db import models

from teachers.models import Teacher


class Class(models.Model):
    title = models.CharField(primary_key=True, max_length=30, default='')
    description = models.CharField(max_length=500, default='')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['title']
