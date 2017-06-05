from django.contrib import admin
# from introduction_to_models.models import Person
from .models import Person
# 위처럼 상대경로로 작성하는 것을 권장.(추후 유지보수에 도움)
# models/ 패키지를 만들었을 때 .models로 적어놓으면 추가수정이 필요없다.

# Register your models here.
admin.site.register(Person)
