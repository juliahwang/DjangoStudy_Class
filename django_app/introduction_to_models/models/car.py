from django.db import models


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
        Manufacturer,
        on_delete=models.CASCADE,
        related_name= 'cars',
        # m = Manufacturer.objects.first()
        # m.cars
        related_query_name='manufacturer_car',
        # Manufacturer.objects.filter(manufacturer_car__name='320')
    )

    def __str__(self):
        return self.name
