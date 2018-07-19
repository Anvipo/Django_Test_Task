# from django.shortcuts import render
import json

from django.http import HttpResponse
from django.shortcuts import render

from classes.forms import ClassForm
from teachers.models import Teacher
from .models import Class


def classes(request):
    class_list = Class.objects.all()
    teacher_list = Teacher.objects.all()

    form = ClassForm(request.POST or None)

    return render(request, 'classes/class_list.html', locals())


def ajax(request):
    if request.method == "GET":
        if 'delete_data' in request.GET:
            response = []
            class_title = request.GET['delete_data']

            deleted_class = Class.objects.get(title=class_title)

            deleted_class.delete()
        else:
            response = []
            class_title = request.GET['class_title']
            class_description = request.GET['class_description']
            teacher = Teacher.objects.get(full_name=request.GET['class_teacher'])
            class_teacher = teacher

            try:
                new_class = Class.objects.get(title=class_title)
            except Class.DoesNotExist:
                new_class = Class()

            new_class.title = class_title
            new_class.description = class_description
            new_class.teacher = class_teacher

            new_class.save()

        classes_data = Class.objects.all()

        for _class in classes_data:
            response.append(str(_class.title) + ', ' + str(_class.description) + ', ' + str(_class.teacher))

        return HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/javascript")
    else:
        return HttpResponse('Error', content_type='text/html')

# class ClassesListView(ListView):
#     model = Class
#     paginate_by = 10
#     template_name = 'classes/class_list.html'
