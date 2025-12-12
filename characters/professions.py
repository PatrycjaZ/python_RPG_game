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

Na koniec stwórz kilka instancji tej klasy i przetestuj wszystki funkcjonalności.
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

    def to_json(self):
        return self.__dict__

    @property
    def is_alive(self):
        return self.hp > 0

    def __str__(self):  # to nie działa
        return self.name

    def __repr__(self):  # to nie działa
        return f"'{self.name}' - '{self.race}'"

    def take_damage(self, amount):
        return max(self.hp - max(amount, 0), 0)

    def heal(self, amount):
        return min(self.hp + amount, self.max_hp)


character = Character("Godfryd", "Human")

print(character.to_json())

print("Is character alive?", character.is_alive)

print([character.name])

print(character.name)

print("Character took damage, hp now is:", character.take_damage(8))
