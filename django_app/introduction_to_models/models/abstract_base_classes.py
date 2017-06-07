from django.db import models

from introduction_to_models.models import Car


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # cars 필드에 MTM으로 related_name, related_query_name을 설정 후 migrate
    cars = models.ManyToManyField(
        Car,
        related_name='%(app_label)s_%(class)s_related',
        # 역참조 c.teacher_set이 더이상 동작하지 않는다.
        # c.introduction_to_models_teacher_related
        related_query_name='%(app_label)s_%(class)ss'
        # 역방향 쿼리 필터시 모델명을 사용하면 동작하지 않는다.
        # >>> Teacher.objects.filter(cars__name__contains="d")
        # <QuerySet [<Teacher: Class wps's teacher (julia, 20)>]>
        # Car.objects.filter(introduction_to_models_teachers__name='julia')
        # <QuerySet [<Car: 520d>]>
    )

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return 'HomeGroup {}\'s student({}, {})'.format(
            self.home_group,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_student'


class Teacher(CommonInfo):
    cls = models.CharField(max_length=20)

    def __str__(self):
        return 'Class {}\'s teacher ({}, {})'.format(
            self.cls,
            self.name,
            self.age,
        )

    class Meta:
        db_table = 'introduction_to_models_abc_teacher'
