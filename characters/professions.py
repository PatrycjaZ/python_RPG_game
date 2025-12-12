"""
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


class Character:
    max_hp = 10.0

    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.hp = 8.0
        self.strength = 4
        self.intelligence = 4
        self.faith = 4

    def __str__(self):  # print(character)
        return self.name

    def __repr__(self):  # print([character])
        return f"{self.name} - {self.race} {self.__class__.__name__}"

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
# # print(character.to_json())
# print("Is character alive?", character.is_alive)
# print(character)
# print([character])
# character.take_damage(10)
# print("Character took damage, hp now is:", character.hp)
# character.heal(2)
# print("Character was healed, hp now is:", character.hp)
