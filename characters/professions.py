from utils import dice_roll, expected_dice_roll
from races import Human, Elf, Orc


"""
ZADANIE 1)
W pliku professions.py stwórz klasę Character. Powinna ona posiadać:

- atrybut klasy max_hp równy 10.0
- atrybuty name i race przyjmowane przez argumenty
- atrybuty hp (8.0) oraz strength, intelligence i faith (4) z wartościami przypisanymi na sztywno
- metodę to_json(), która zwraca słownik z wszystkimi atrybutami obiektu.
    Klucze tego słownika powinny być stringami a wartości stringami lub liczbami
- property is_alive, które zwróci informację czy postać żyje (ma dodatnie hp)
- metody __str__ i __repr__.
    Pierwsza z nich powinna zwracać imię postaci a druga wartość w stylu: Boromir - Human Warrior
- metody take_damage(), która przyjmie ilość obrażeń i pomniejszy hp o tyle. hp nie może spaść poniżej 0
- metodę heal(), która przyjmie ilość punktów życia i powiększy hp o tyle. hp nie może przekroczyć max_hp

Na koniec stwórz kilka instancji tej klasy i przetestuj wszystkie funkcjonalności.
"""

"""
Zadanie 5)
Wróć do klasy Character i utwórz metodę _apply_race(), która zaaplikuje do postaci modyfikatory wynikające z rasy.
"""


class Character:
    max_hp = 10.0

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hp = 8.0
        self.strength = 4
        self.intelligence = 4
        self.faith = 4

        self._apply_race()

    def __str__(self):  # print(character)
        return self.name

    def __repr__(self):  # print([character])
        return f"{self.name} - {self.race} {self.__class__.__name__}"

    def _apply_race(self):
        stats_modified = self.race.modify_statistics(self.__dict__)

        self.strength = stats_modified["strength"]
        self.intelligence = stats_modified["intelligence"]
        self.faith = stats_modified["faith"]

    def take_damage(self, amount):
        self.hp = max(0, self.hp - max(amount, 0))

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)

    def to_json(self):
        return self.__dict__

    @property
    def is_alive(self):
        return self.hp > 0


# character = Character("Godfryd", "Human")
# print(character.to_json())
# print("Is character alive?", character.is_alive)
# print(character)
# print([character])
# character.take_damage(10)
# print("Character took damage, hp now is:", character.hp)
# character.heal(2)
# print("Character was healed, hp now is:", character.hp)

"""
ZADANIE 2)
Stwórz następujące klasy:

Warrior
- niech dziedziczy po Character
- powinien mieć bonus +2 do siły i -1 do inteligencji
- napisz metodę expected_contribution(), która na podstawie typu zadania obliczy oczekiwany wkład w zadanie. 
    Dla tasków typu combat powinna to być wartość siły + oczekiwany rzut kością,
    a dla innych typów 2 + oczekiwany rzut kością
- napisz metodę contribute(), która wyznaczy faktyczny wkład w wykonanie zadania uwzględniając rzut kością
"""


class Warrior(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength += 2
        self.intelligence -= 1

    def expected_contribution(self, task_type):
        return (self.strength + expected_dice_roll
                if task_type == "combat" else 2 + expected_dice_roll)

    def contribute(self, task_type):
        contribution = (self.strength + dice_roll()
                        if task_type == "combat" else 2 + dice_roll())
        return contribution


# warrior = Warrior("Godryf", "Human")
# print(warrior.__dict__)
# print(warrior.expected_contribution('combat'))
# print(warrior.contribute('combat'))

"""
Wizard
- niech dziedziczy po Character
- powinien mieć bonus -1 do siły, +2 do inteligencji i +1 do wiary a także atrybut mana równy 5
- napisz metodę expected_contribution(), która na podstawie typu zadania obliczy oczekiwany wkład w zadanie. 
    Dla tasków typu magic powinien być obliczany ze wzoru mana // 2 + intelligence + expected_dice_roll,
    a dla innych typów niech będzie równy 2 + rzut kością
- napisz metodę contribute(), która wyznaczy faktyczny wkład w wykonanie zadania uwzględniając rzut kością
- napisz metodę __spend_mana(), która odejmie 1 od many czarodzieja. Wywołaj ją w metodzie contribute()
"""


class Wizard(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 1
        self.intelligence += 2
        self.faith += 1

        self.mana = 5

    def expected_contribution(self, task_type):
        return (self.mana // 2 + self.intelligence + expected_dice_roll
                if task_type == "magic" else expected_dice_roll + 2)

    def contribute(self, task_type):
        if task_type == "magic":
            contribution = self.mana // 2 + self.intelligence + dice_roll()
            self.__spend_mana()
        else:
            contribution = 2 + dice_roll()
        return contribution

    def __spend_mana(self):
        self.mana = max(0, self.mana-1)


# wizard = Wizard("Godryf", "Human")
# print(wizard.__dict__)
# print(wizard.expected_contribution('magic'))
# print(wizard.contribute('magic'))

"""
Priest
- niech dziedziczy po Character
- powinien mieć bonus -2 do siły, +1 do inteligencji i +3 do wiary a także atrybut mana równy 5.0
- napisz metodę expected_contribution(), która na podstawie typu zadania obliczy oczekiwany wkład w zadanie. 
    Dla tasków typu holy oraz support powinna to być wartość wiary + oczekiwany rzut kością,
    a dla innych typów 1 + oczekiwany rzut kością
- napisz metodę contribute(), która wyznaczy faktyczny wkład w wykonanie zadania uwzględniając rzut kością
- napisz metodę heal_ally(), która przyjmie jako argument sojusznika należącego do drużyny 
    i jeżeli kapłan ma dodatnią ilość many to 
    (1) wyznaczy heal_amount równe faith / 5 
    (2) uleczy sojusznika tą ilością punktów życia i 
    (3) pomniejszy manę o 10% z heal_amount

Na koniec stwórz instancje tych klas i przetestuj wszystkie funkcjonalności.
"""


class Priest(Character):
    def __init__(self, name, race):
        super().__init__(name, race)

        self.strength -= 2
        self.intelligence += 1
        self.faith += 3

        self.mana = 5.0

    def expected_contribution(self, task_type):
        return (self.faith + expected_dice_roll
                if task_type in ("holy", "support") else expected_dice_roll + 1)

    def contribute(self, task_type):
        return (self.faith + dice_roll()
                if task_type in ("holy", "support") else dice_roll() + 1)

    def heal_ally(self, team_member):
        if self.mana > 0:
            heal_amount = self.faith / 5
            team_member.heal(heal_amount)
            self.mana = max([0, self.mana-(heal_amount / 10)])


# if __name__ == "__main__":
#     warrior = Warrior("Godfryd", Human())
#     print(warrior.__dict__)
# # print(warrior.hp, priest.mana)  # 8.0, 5.0
# print(priest.faith / 5)  # 1.4
# priest.heal_ally(warrior)
# print(warrior.hp, priest.mana)  # 9.4, 5.0 - 0.14 = 4.86
