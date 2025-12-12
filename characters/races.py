"""
ZADANIE 3)
Stwórz klasę Race, która będzie miała następujące atrybuty:

- name
- strength_mod (modyfikator siły)
- intelligence_mod (modyfikator inteligencji)
- faith_mod (modyfikator wiary)
- a także metodę modify_statistics(), która przyjmie słownik stats z kluczami: strength, intelligence i faith
    i nadpisze wartości tego słownika zgodnie z modyfikatorami będącymi w atrybutach klasy

Na koniec stwórz instancję tej klasy i przetestuj metodę modify_statistics().
"""


class Race:
    def __init__(self, name, strength_mod, intelligence_mod, faith_mod):
        self.name = name
        self.strength_mod = strength_mod
        self.intelligence_mod = intelligence_mod
        self.faith_mod = faith_mod

    def modify_statistics(self, character_stats):
        character_stats["strength"] += self.strength_mod
        character_stats["intelligence"] += self.intelligence_mod
        character_stats["faith"] += self.faith_mod
        return character_stats


"""
ZADANIE 4)
Stwórz klasy Human, Elf i Orc, które będą dziedziczyć po Race. 
W metodzie __init__ każda z tych klas powinna przekazywać do inita klasy bazowej stosowne argumenty. Przyjmij że:

- Human: siła +1, inteligencja +1, wiara +1
- Elf: siła -1, inteligencja +2
- Orc: siła +2, inteligencja -1, wiara -1

Na koniec przetestuj utworzone klasy.
"""


class Human(Race):
    def __init__(self):
        super().__init__("Human", 1, 1, 1)


class Elf(Race):
    def __init__(self):
        super().__init__("Elf", -1, 2, 0)


class Orc(Race):
    def __init__(self):
        super().__init__("Orc", 2, -1, -1)


# human = Human()
# print(human.__dict__)
# stats_base = {
#     "strength": 4,
#     "intelligence": 4,
#     "faith": 4
# }
# human = Human()
# print(human.__dict__)
# print(human.modify_statistics(stats_base.copy()))
