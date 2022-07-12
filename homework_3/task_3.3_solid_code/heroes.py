from antagonistfinder import AntagonistFinder


class FireGunMixin:
    def fire_a_gun(self):
        print('PIU PIU')


class LasersMixin:
    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')


class RoundhouseKickMixin:
    def roundhouse_kick(self):
        print('Bump')


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        return "Kick"

    def ultimate(self):
        pass


class Superman(SuperHero, LasersMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = 'Clark Kent'

    def ultimate(self):
        return self.incinerate_with_lasers()


class ChackNorris(SuperHero, FireGunMixin, RoundhouseKickMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = 'Chack Norris'

    def attack(self):
        return self.fire_a_gun()

    def ultimate(self):
        return self.roundhouse_kick()
