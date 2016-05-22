import random


class Combat:
    attack_limit = 6
    dodge_limit = 6

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 4

    def hit(self, damage):
        self.hit_points -= damage
