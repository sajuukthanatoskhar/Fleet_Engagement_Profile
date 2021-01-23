from uu import Error


# noinspection PyUnresolvedReferences


# noinspection PyUnresolvedReferences
class Weapon:
    def __init__(self, json):
        self.name = str
        for k, v in json.items():
            setattr(self, k, v)
        try:
            self.weapon_name = self.name.split(sep=', ', maxsplit=1)[0]
            self.ammo_name = self.name.split(sep=', ', maxsplit=1)[1]
        except AttributeError as e:
            print("{} doesn't exist".format(e))

        print(self.ammo_name)

    def weapon_calculate_distance_damage(self, distance):
        return self.distance_mod_calc(distance) * self.dps

    def distance_mod_calc(self, distance):

        if distance == 0:
            return 1
        result = 0.5 ** (((distance - self.optimal) / self.falloff)**2)
        return result
