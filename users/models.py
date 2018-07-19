from django.db import models


class User(models.Model):
    course_number = models.CharField(max_length=50)
    faculty_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    graduation_year = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university_name = models.CharField(max_length=50)
    vk_ID = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.vk_ID)

    def save_dict_to_class(self, data):
        self.course_number = data['courseNumber']
        self.faculty_name = data['facultyName']
        self.first_name = data['firstName']
        self.graduation_year = data['graduationYear']
        self.last_name = data['lastName']
        self.university_name = data['universityName']
        self.vk_ID = data['vkId']

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'
