from enums import Hero_Menu
from hero import Hero


def print_hero_menu():
    for key in Hero_Menu:
        print(int(key), '--', key.fullname)


class Service:

    @staticmethod
    def fight_squads(squad1, squad2):
        squad1_power = squad1.get_totalPower()
        squad2_power = squad2.get_totalPower()
        if squad1_power > squad2_power:
            print("The winning squad is: " + squad1.get_name())
        elif squad2_power > squad1_power:
            print("The winning squad is: " + squad2.get_name())
        else:
            print("There's a Tie! ")

    @staticmethod
    def compare_heroes(h1, h2):
        h1_power = h1.get_power()
        h2_power = h2.get_power()
        if h1_power > h2_power:
            print("The Stronger Hero is: " + h1.get_name())
        elif h2_power > h1_power:
            print("The Stronger Hero is: " + h2.get_name())
        else:
            print("There's a Tie!")

    @staticmethod
    def search_hero(given_hero, squads_list):
        for squad in squads_list:
            for hero in squad.heroes:
                if given_hero == hero.get_name():
                    return hero

    @staticmethod
    def search_squad(given_squad, squads_list):
        for squad in squads_list:
            if given_squad == squad.get_name():
                return squad

    @staticmethod
    def edit_hero(hero):
        print_hero_menu()
        option = int(input('Enter your choice: '))
        if option == int(Hero_Menu.Status):
            new_status = str(input('Please enter a new status, (Alive, Dead or Injured): '))
            hero.set_status(new_status)
            print(hero.name + " new status is: " + str(new_status))
        elif option == int(Hero_Menu.Nature):
            new_nature = str(input('Please enter his nature, (Good or Evil):'))
            hero.set_nature(new_nature)
            print(hero.name + " new nature is: " + str(new_nature))
        elif option == int(Hero_Menu.Power):
            new_power = int(input('Please enter a new power value (0-100): '))
            hero.set_power(new_power)
            print(hero.name + " New power value is: " + str(new_power))

    @staticmethod
    def edit_squad(squad):
        resting_mode = str(input('Is the Squad Resting?(True or False): '))
        if resting_mode == 'True':
            squad.set_resting(True)
            print(squad.name + " are now resting...")
        else:
            squad.set_resting(False)
            print(squad.name + " are now fighting!")

    @staticmethod
    def add_hero():
        hero_name = str(input('Please enter a name: '))
        hero_nature = str(input('Please enter his nature, (Good or Evil): '))
        hero_power = int(input('Please enter a power value (0-100): '))
        new_hero = Hero(hero_name, "Alive", hero_nature, hero_power)
        return new_hero
