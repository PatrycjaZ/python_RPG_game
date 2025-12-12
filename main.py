from characters.professions import Warrior, Wizard, Priest
from characters.races import Human, Elf, Orc
from initialization import initialize_team, initialize_tasks

"""
Zadanie 7)
W pliku main.py stwórz zmienną team_composition, która będzie określała strukturę drużyny.
Powinien to być słownik, którego klucze to klasy postaci (profesje),
a jego wartości to liczebność poszczególnych profesji.

Na początek spróbuj następującej struktury:
2 wojowników, 2 czarodziejów, 1 kapłan

Stwórz też zmienną available_races, która będzie przechowywać wszystkie rasy, jakie mamy w grze.
Określ również liczbe zadań do wykonani (np. 5).
"""

team_composition = {
    Warrior: 2,
    Wizard: 2,
    Priest: 1
}

available_races = [Human, Elf, Orc]

n_tasks = 5

team = initialize_team(team_composition, available_races)

tasks = initialize_tasks(n_tasks)

print(team)
print(tasks)
