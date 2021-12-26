from enum import Enum


class Menu(Enum):
    Show_Hero = 1, 'Show a Hero'
    Edit_Hero = 2, 'Edit a Hero'
    Add = 3, 'Add a Hero to a Squad'
    Remove = 4, 'Remove a Hero from a Squad'
    Compare = 5, 'Compare between 2 Heroes'
    Show_Squads = 6, 'Show Squads'
    Edit_Squad = 7, 'Edit a Squad',
    Fight = 8, 'Fight between 2 Squads',
    Exit = 9, 'Exit'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value


class Hero_Menu(Enum):
    Status = 1, 'Status'
    Nature = 2, 'Nature'
    Power = 3, 'Power'

    def __new__(cls, value, name):
        member = object.__new__(cls)
        member._value_ = value
        member.fullname = name
        return member

    def __int__(self):
        return self.value
