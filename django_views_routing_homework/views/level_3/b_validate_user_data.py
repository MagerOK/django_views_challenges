"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json
import re

from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views import View


class ValidateUserDataView(View):

    def validate_full_name(self, full_name: str) -> bool:
        return 5 <= len(full_name) <= 256

    def validate_email(self, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True
        return False
    
    def validate_registered_from(self, registered_from: str) -> bool:
        return registered_from in ["website", "mobile_app"]
    
    def validate_age(self, age: int) -> bool:
        try:
            int(age)
            return True
        except TypeError and ValueError:
            return False

    def validate_all_data(self, data: dict) -> dict:
        is_valid = (
            self.validate_email(data.get('email', False)) and
            self.validate_full_name(data.get('full_name', False)) and
            self.validate_registered_from(data.get('registered_from', False))
        )
        age = data.get('age', None)
        if self.validate_age(age):
            data['age'] = age
        elif age is not None:
            is_valid = False
        return {"is_valid": is_valid}
    
    def post(self, request: HttpRequest) -> HttpResponse:
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return HttpResponse(status=400)
        return JsonResponse(self.validate_all_data(data))
        