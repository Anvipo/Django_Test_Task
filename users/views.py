import json

from django.http import HttpResponse

from users.models import User

successResponseText = "УСПЕШНО: информация о Вас была сохранена на сервере"
failResponseText = "ОШИБКА: Вы ничего не прислали"


# сюда приходит информация из мобильного приложения Seffectle
def users(request):
    if request.method == 'GET':
        if not request.GET:
            # Если в Get запросе ничего не было прислано
            return HttpResponse(json.dumps(failResponseText, ensure_ascii=False))

        user_data = request.GET['data']

        user_data_dict = json.loads(user_data)
        print('Пришла такая инфа о юзере:')
        for key, value in user_data_dict.items():
            print('\t', key, ':', value)

        user_info = User()
        user_info.save_dict_to_class(user_data_dict)

        try:
            user_info = User.objects.get(vk_ID=user_info.vk_ID)
        except User.DoesNotExist:
            # если такого пользователя не было, то добавить в БД
            user_info.save()

        return HttpResponse(json.dumps(successResponseText, ensure_ascii=False))
    else:
        return HttpResponse("???")
