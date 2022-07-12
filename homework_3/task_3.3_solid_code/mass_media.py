from places import Place


class NewsPaper:
    name = 'The New York Times'

    def create_news(self, name_hero: str, place: Place):
        print(f'{self.name}: "{name_hero} saved the {place.name}!"')
