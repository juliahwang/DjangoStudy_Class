from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
        # 아래에 정의했으므로 문자열로 적어준다.
    )

    def __str__(self):
        return self.name


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    # 추가 필드가 없으면 기본 many-to-many 모델을 구현한 것이 된다.
    date_joined = models.DateField()
    date_left = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} from {} joined on {}, left on {}'.format(
            self.player,
            self.club,
            self.date_joined,
            self.date_left,
        )
