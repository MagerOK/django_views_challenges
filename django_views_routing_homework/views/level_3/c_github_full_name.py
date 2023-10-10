"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""

from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
import requests


class FetchNameFromGithubView(View):
    def get(self, request: HttpRequest, github_username: str) -> HttpResponse:
        response = requests.get(f"https://api.github.com/users/{github_username}")
        if response.status_code == 404:
            return HttpResponse(status=404)
        
        user_data = response.json()
        name = user_data.get("name", None)
        return JsonResponse({"name": name})
    