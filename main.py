from enums import Menu
from hero import Hero
from service import Service
from squad import Squad


def option1(squads_list):
    hero_name = str(input('Please enter hero name: '))
    hero_found = Service.search_hero(hero_name, squads_list)
    hero_found.printname()


def option2(squads_list):
    print('Edit Hero:')
    hero_name = str(input('Please enter hero name: '))
    hero_found = Service.search_hero(hero_name, squads_list)
    hero_found.printname()
    Service.edit_hero(hero_found)


def option3(squads_list):
    new_hero = Service.add_hero()
    squad_name = str(input('Please enter Squad name: '))
    squad = Service.search_squad(squad_name, squads_list)
    squad.heroes.append(new_hero)
    print(new_hero.name + " has joined " + squad.name + "!")


def option4(squads_list):
    hero_name = str(input('Please enter a Hero name: '))
    found_hero = Service.search_hero(hero_name, squads_list)
    squad_name = str(input('Please enter The Hero Squad: '))
    squad = Service.search_squad(squad_name, squads_list)
    squad.heroes.remove(found_hero)


def option5(squads_list):
    hero_name1 = str(input('Please enter Opponent #1: '))
    hero_name2 = str(input('Please enter Opponent #2: '))
    print('Fight!')
    hero_found1 = Service.search_hero(hero_name1, squads_list)
    hero_found2 = Service.search_hero(hero_name2, squads_list)
    Service.compare_heroes(hero_found1, hero_found2)


def option6(squads_list):
    print('The Squads:')
    for heroes in squads_list:
        heroes.printname()
        print('')


def option7(squads_list):
    print('Edit Squad:')
    squad_name = str(input('Please enter Squad name: '))
    squad_found = Service.search_squad(squad_name, squads_list)
    squad_found.printname()
    Service.edit_squad(squad_found)


def option8(squads_list):
    squad_name1 = str(input('Please enter Squad #1: '))
    squad_name2 = str(input('Please enter Squad #2: '))
    squad_found1 = Service.search_squad(squad_name1, squads_list)
    squad_found2 = Service.search_squad(squad_name2, squads_list)
    Service.fight_squads(squad_found1, squad_found2)


def print_menu():
    print('\n***Welcome to the Squads fight***')
    for key in Menu:
        print(int(key), '--', key.fullname)
    print(' ')


def init_data():
    squad1 = Squad("The Avengers", [Hero("Loki", "Alive", "Evil", 50),
                                    Hero("Thor", "Alive", "Good", 90)], True)
    squad2 = Squad("Axis", [Hero("Thanos", "Alive", "Evil", 100), Hero("Troll", "Alive", "Evil", 30)],
                   True)
    return [squad1, squad2]


def main():
    squads_list = init_data()
    while True:
        print_menu()
        option = int(input('Enter your choice: '))
        if option == int(Menu.Show_Hero):
            option1(squads_list)
        elif option == int(Menu.Edit_Hero):
            option2(squads_list)
        elif option == int(Menu.Add):
            option3(squads_list)
        elif option == int(Menu.Remove):
            option4(squads_list)
        elif option == int(Menu.Compare):
            option5(squads_list)
        elif option == int(Menu.Show_Squads):
            option6(squads_list)
        elif option == int(Menu.Edit_Squad):
            option7(squads_list)
        elif option == int(Menu.Fight):
            option8(squads_list)
        elif option == int(Menu.Exit):
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


if __name__ == "__main__":
    main()
