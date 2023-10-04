"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from django.http import HttpResponse, HttpRequest
from django.views import View
from faker import Faker


class GenerateFileWithTextView(View):
    
    def generate_text(self, length: int) -> str:
        fake = Faker()
        text = ''
        while len(text) < length:
            text += fake.word() + ' '
        text_cut = text[:length]
        return text_cut
    
    def validate_length(self, length: int) -> bool:
        try:
            int(length)
        except ValueError or TypeError:
            return False
        if 0 <= int(length) <= 10000:
            return True
        return False
    
    def get(self, request: HttpRequest) -> HttpResponse:
      length = request.GET.get("length", None)
      if not self.validate_length(length):
          return HttpResponse(status=403)
      response = HttpResponse(
          content_type="text/txt",
          headers={"Content-Disposition": 'attachment; filename="generated_file.txt"'},
      )
      text = self.generate_text(int(length))
      response.write(text)
      return response
    