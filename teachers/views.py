# from django.shortcuts import render
import json

from django.http import HttpResponse
from django.shortcuts import render

from teachers.forms import TeacherForm
from .models import Teacher


def teachers(request):
    teacher_list = Teacher.objects.all()

    form = TeacherForm(request.POST or None)

    return render(request, 'teachers/teacher_list.html', locals())


def ajax(request):
    if request.method == "GET":
        if 'delete_data' in request.GET:
            response = []
            teacher_id = request.GET['delete_data']

            deleted_user = Teacher.objects.get(id=teacher_id)

            deleted_user.delete()
        else:
            response = []
            teacher_last_name = request.GET['teacher_last_name']
            teacher_first_name = request.GET['teacher_first_name']
            teacher_patronymic = request.GET['teacher_patronymic']
            teacher_full_name = (str(teacher_last_name) + ' ' +
                                 str(teacher_first_name) + ' ' +
                                 str(teacher_patronymic))

            try:
                teacher = Teacher.objects.get(full_name=teacher_full_name)
            except Teacher.DoesNotExist:
                teacher = Teacher()

            teacher.last_name = teacher_last_name
            teacher.first_name = teacher_first_name
            teacher.patronymic = teacher_patronymic
            teacher.full_name = teacher_full_name

            teacher.save()

        teachers_data = Teacher.objects.all()

        for teacher in teachers_data:
            response.append(str(teacher) + ' ' + str(teacher.id))

        return HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/javascript")
    else:
        return HttpResponse('Error', content_type='text/html')

# class TeachersListView(ListView):
#     model = Teacher
#     paginate_by = 5
#     template_name = 'teachers/teacher_list.html'
