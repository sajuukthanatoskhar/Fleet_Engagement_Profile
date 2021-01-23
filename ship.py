import weapon

class Ship:
    def __init__(self, json_rec: dict):
        for k, v in json_rec.items():
            setattr(self, k, v)

        if self.weapons:
            self.weapons = None
        self.weapon = self.get_weapon(json_rec)

    def get_weapon(self, json_rec: dict) -> list:
        dict_weapons = []
        for weapon_system in json_rec["weapons"]:
            weapon_weapon = weapon.Weapon(weapon_system)
            dict_weapons.append(weapon_weapon)
        return dict_weapons
