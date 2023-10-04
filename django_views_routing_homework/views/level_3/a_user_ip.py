"""
В этом задании вам нужно реализовать вьюху, которая возвращает IP входящего запроса в виде строки.

Вот тут есть информация о том, как узнать IP:
https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.META
"""

from django.views import View
from django.http import HttpResponse, HttpRequest


class Show_User_IP_View(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(request.META["REMOTE_ADDR"])