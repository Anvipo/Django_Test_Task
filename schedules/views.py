# from django.shortcuts import render
import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import Schedule

successResponseText = "УСПЕШНО: Ваше расписание было сохранено на сервере"
failResponseText = "ОШИБКА: Вы ничего не прислали"


def get_json_list(query_set):
    list_objects = []
    for obj in query_set:
        dict_obj = {}
        # noinspection PyProtectedMember
        for field in obj._meta.get_fields():
            try:
                if field.many_to_many:
                    dict_obj[field.name] = get_json_list(getattr(obj, field.name).all())
                    continue
                dict_obj[field.name] = getattr(obj, field.name)
            except AttributeError:
                continue
        list_objects.append(dict_obj)
    return list_objects


# сюда приходит информация из мобильного приложения Seffectle
def schedules(request):
    if request.method == 'GET':
        if not request.GET:
            schedule_list = Schedule.objects.all()
            return render(request, 'schedules/schedule_list.html', locals())

        schedule_data = request.GET['data']

        schedule_data = json.loads(schedule_data)

        try:
            var = schedule_data['id']
            need_to_give_schedule_to_user = True
        except TypeError:
            need_to_give_schedule_to_user = False

        if need_to_give_schedule_to_user:
            user_id = schedule_data['id']
            schedule = Schedule.objects.filter(user_ID=user_id)

            schedule_list = get_json_list(schedule)
            schedule_json = json.dumps(schedule_list, ensure_ascii=False)

            return HttpResponse(schedule_json)
        else:
            print('Пришло такое расписание от юзера:')
            for item in schedule_data:
                print('\t', item)

            user_id = schedule_data[0]['user_ID']

            prev_schedule = Schedule.objects.filter(user_ID=user_id)

            prev_schedule.delete()

            new_schedule = Schedule()

            for item in schedule_data:
                new_schedule.save_dict_to_class(item)

            return HttpResponse(json.dumps(successResponseText, ensure_ascii=False))
    else:
        return HttpResponse("???")

# def teachers(request):
#     teacher_list = Teacher.objects.all()
#
#     form = TeacherForm(request.POST or None)
#
#     return render(request, 'teachers/teacher_list.html', locals())

# class SchedulesListView(ListView):
#     model = Schedule
#     paginate_by = 2
#     template_name = 'schedules/schedule_list.html'
