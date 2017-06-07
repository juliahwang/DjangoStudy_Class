# models 자체에서 불러오고 싶으므로 설정을 등록
from .car import Car,Manufacturer
from .person import Person
from .many_to_one_example import Reporter, Article
from .topping_and_pizza import Topping, Pizza
from .intermediate import Player, Club, TradeInfo
from .one_to_one_example import Restaurant, Place, Waiter