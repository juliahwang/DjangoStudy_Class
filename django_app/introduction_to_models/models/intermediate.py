from django.db import models
from datetime import timezone, date
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def current_club(self):
        """current_club프로퍼티에 현재 속하는 Club리턴"""
        return self.club_set.get(tradeinfo__date_left__isnull=True).name

    @property
    def current_tradeinfo(self):
        """current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴"""
        return TradeInfo.objects.get(
            player__exact=self,
            date_joined__lte=timezone.now()
        )


class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        # 아래에 정의했으므로 문자열로 적어준다.
        through='TradeInfo',
        through_fields=(
            ('club', 'player')
        ),
        related_name="%(app_label)s_%(class)s_related",
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        # squad 메서드에 현직 선수들만 리턴
        # 인수로 년도(2017, 2015,... 등)를 받아
        # 해당 년도의 현직 선수들을 리턴
        # 주어지지 않으면 현재를 기준으로 함
        if not year:
            return '{}'.format(self.players.filter(tradeinfo__date_joined__lte=date(year, 1, 1)))
        else:
            return '{}'.format(self.players.filter(tradeinfo__date_joined__lte=timezone.now()))


class TradeInfo(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE
    )
    # 추가 필드가 없으면 기본 many-to-many 모델을 구현한 것이 된다.
    date_joined = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    # 2. recommender와 prev_club을 활성화시키고 Club의 MTM 필드에 through_fields를 명시
    recommender = models.ForeignKey(
        Player,
        related_name='+',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    prev_club = models.ForeignKey(
        Club,
        related_name='+',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @property
    def is_current(self):
        """1. property로 is_current 속성이 TradeInfo가 현재 현직(left하지 않았는지) 여부 반환"""
        if self.date_left is None:
            return '{} didn\'t leave {}'.format(
                self.player.name,
                self.club.name,
            )
        else:
            return '{} left {}'.format(
                self.player.name,
                self.club.name,
            )

    def __str__(self):
        return '{} from {} joined on {}'.format(
            self.player,
            self.club,
            self.date_joined,
        )
