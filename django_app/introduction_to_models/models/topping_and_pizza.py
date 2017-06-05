from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        # 자신이 가지고있는 토핑이름도 출력
        # cheese pizza (cheese, tomato sauce)
        return '{} ({})'.format(self.name, ','.join([topping.name for topping in self.toppings.all()]))

    # toppings_string = ''
    # for topping in self.toppings.all():
    #     toppings_string += topping.name
    #     toppings_string += ', '
    # toppings_string = toppings_string[:-2]
    # return '{} ({})'.format(
    #     self.name,
    #     toppings_string
    # )

    class Meta:
        ordering = ('name',)
