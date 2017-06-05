from django.contrib import admin
# from introduction_to_models.models import Person
from .models import Person
# 위처럼 상대경로로 작성하는 것을 권장.(추후 유지보수에 도움)

# Register your models here.
admin.site.register(Person)
