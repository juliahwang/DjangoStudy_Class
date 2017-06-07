from django.db import models
from datetime import timezone, date

from django.db.models import Q
from django.utils import timezone


class Player(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    @property
    def current_club(self):
        """current_club프로퍼티에 현재 속하는 Club리턴"""
        #return self.club_set.get(tradeinfo__date_left__isnull=True).name
        return self.current_tradeinfo.club

    @property
    def current_tradeinfo(self):
        """current_tradeinfo프로퍼티에 현재 자신의 TradeInfo리턴"""
        return TradeInfo.objects.get(
            player__exact=self,
            date_joined__lte=timezone.now()
        )
        # return self.tradeinfo_set.get(date_left__isnull=True)


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
        # 2015년에 현직이었던 = 2015년에 하루라도 뛰었던 선수
        # ex) 2015년에 현직으로 존재했던 선수의 경우
        #  떠난 날짜가 2015. 1. 1 보다는 커야한다
        #  들어온 날짜는 2016. 1. 1 보다는 작아야 한다.
        # if year:
        #
        #     return '{}'.format(self.players.filter(tradeinfo__date_joined__lte=date(year, 1, 1)))
        # else:
        #     return '{}'.format(self.players.filter(tradeinfo__date_joined__lte=timezone.now()))
        if year:
            """해당년도가 넘어가기 전에 영입했고 떠난 날이 해당년도를 넘어가거나 떠난 날짜가 없다면."""
            return self.players.filter(
                Q(tradeinfo__date_joined__lt=date(year + 1, 1, 1)) &
                (
                    Q(tradeinfo__date_left__gt=date(year, 1, 1)) |
                    Q(tradeinfo__date_left__isnull=True))
                )
        # 인수로 년도(2017, 2015,... 등)를 받아
        # 해당 년도의 현직 선수들을 리턴
        # 주어지지 않으면 현재를 기준으로 함


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
        related_name='tradeinfo_set_by_recommender',
        # 역참조 매니저의 이름을 오버라이드하여 지정, 사용가능
        # player.recommender_set.all() = player.tradeinfo_set_by_recommender.all()
        # related_name = '+'라고 적어주면 역참조할 필요가 없다는 설정임.
        on_delete=models.PROTECT,
        # 추천인을 삭제한다고 TradeInfo가 삭제(CASCADE)되면 안되므로 지우지 못하게 PROTECT 사용
        null=True,
        blank=True,
    )
    prev_club = models.ForeignKey(
        Club,
        related_name='player_prev_club',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return '{}, {} ({} ~ {})'.format(
            self.player,
            self.club,
            self.date_joined,
            self.date_left if self.date_left else '현직'
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

            # return self.date_left is None
            # return not self.date_left
