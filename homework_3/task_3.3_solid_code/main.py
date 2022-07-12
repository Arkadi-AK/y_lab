from typing import Union

from heroes import SuperHero, Superman, ChackNorris
from mass_media import NewsPaper
from places import Kostroma, Tokyo


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo], news: NewsPaper):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(hero.name, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), NewsPaper())
    print('-' * 20)
    save_the_place(ChackNorris(can_use_ultimate_attack=False), Tokyo(), NewsPaper())
