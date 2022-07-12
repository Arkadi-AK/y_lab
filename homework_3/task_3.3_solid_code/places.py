from abc import abstractmethod


class Place:
    @abstractmethod
    def get_villain(self):
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_villain(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_villain(self):
        print('Godzilla stands near a skyscraper')
