from django.db import models


class Schedule(models.Model):
    class_begin_time = models.CharField(max_length=50)
    class_end_time = models.CharField(max_length=50)
    class_name = models.CharField(primary_key=True, max_length=50)
    class_serial_number = models.CharField(max_length=50)
    class_type = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=50)
    room_name = models.CharField(max_length=50)
    schedule_creation_time = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=50)
    user_ID = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.class_name)

    def save_dict_to_class(self, data):
        try:
            self.class_begin_time = data['class_begin_time']
            self.class_end_time = data['class_end_time']
            self.class_name = data['class_name']
            self.class_serial_number = data['class_serial_number']
            self.class_type = data['class_type']
            self.day_of_week = data['day_of_week']
            self.room_name = data['room_name']
            self.schedule_creation_time = data['schedule_creation_time']
            self.teacher_name = data['teacher_name']
            self.user_ID = data['user_ID']
            self.save()
        except KeyError:
            raise KeyError("Поля входных данных не соответствуют формату")

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'Расписания'
