# python3
# coding: utf-8

class Warrior():
    ranks = ("Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master",
             "Greatest")

    def __init__(self):
        self.experience = 101
        self.achivments = []

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return self.ranks[self.level // 10]

    def training(self, training_name, new_exp, new_lvl):
        if self.level < new_lvl:
            return "Not strong enough"
        else:
            self.experience += new_exp
            self.achivments.append(training_name)
            return training_name

    def battle(self, boss_level):
        if 100 < boss_level < 1:
            return "Invalid level"
        elif self.level == boss_level:
            self.experience += 10
            return "A good fight"
        elif self.level - boss_level == 1:
            self.experience += 5
            return "A good fight"
        elif self.level - boss_level > 1:
            return "Easy fight"
        elif 1 <= boss_level - self.level < 5:
            self.experience += 20 * (boss_level - self.level) * (boss_level - self.level)
            return "An intense fight"
        elif boss_level - self.level >= 5:
            return "You've been defeated"


if __name__ == '__main__':
    Mike = Warrior()
    print(Mike.level)
    print(Mike.achivments)
    print(Mike.training("Defeated Witcher", 1000, 1))
    print(Mike.experience)
    print(Mike.level)
    print(Mike.rank)
    print(Mike.battle(13))
    print(Mike.experience)
    print(Mike.achivments)
