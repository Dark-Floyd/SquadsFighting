

class Squad:
    def __init__(self, name, heroes, resting):
        self.name = name
        self.heroes = heroes
        self.resting = resting

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_heroes(self):
        return self.heroes

    def set_heroes(self, heroes):
        self.heroes = heroes

    def get_resting(self):
        return self.resting

    def set_resting(self, resting):
        self.resting = resting

    def printname(self):
        print("Name: " + self.name)
        print("Heroes: " )
        for hero in self.heroes:
            print(hero.name+', ', sep=' ', end='', flush=True)
        print("\nResting: " + str(self.resting))


    def print_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def get_totalPower(self):
        total_power = 0
        for hero in self.heroes:
            total_power += hero.power
        return total_power

