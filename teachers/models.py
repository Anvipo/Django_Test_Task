from django.db import models


class Teacher(models.Model):
    last_name = models.CharField(max_length=20, default='')
    first_name = models.CharField(max_length=20, default='')
    patronymic = models.CharField(max_length=20, default='')
    full_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return "{0} {1} {2}".format(self.last_name, self.first_name, self.patronymic)

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'Преподаватели'
        ordering = ['full_name']
