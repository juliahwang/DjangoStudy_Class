from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PERSON_TYPES = (
        ('student', '학생'),
        ('teacher', '선생'),
    )
    person_type = models.CharField(
        max_length=10,
        choices=PERSON_TYPES,
        default=PERSON_TYPES[0][0]
    )
    # teacher 속성 지정 (ForeignKey, 'self'를 이용해 자기 자신을 가리킴, null=True허용)
    teacher_attrs = models.ForeignKey(
        'self',
        verbose_name='선생님',
        null=True,
        blank=True,  # 해당속성이 있어야 필수 입력필드가 아니게된다.
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZE,
        help_text="L for men"
    )

    def __str__(self):
        return self.name


# 일대다, one-to-many
class Manufacturer(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(
        # 아직 정의되지 않은 모델을 불러올 경우에는 문자열로 <앱이름>.<모델명>을 사용
        # (Manufacturer가 Car모델 아래에 있거나 아직 정의되지 않았을 경우)
        # 'introduction_to_models.Manufacturer', on_delete=...
        Manufacturer, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
