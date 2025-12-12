import random
import json
from fictional_names import name_generator
from adventure import Task


"""Zadanie 8)
W pliku initialization.py napisz funkcje initialize_team() oraz initialize_tasks().

Powinny one tworzyć listę postaci oraz listę zadań na podstawie informacji wejściowych utworzonych w poprzednim zadaniu. 
Do nadania postaciom imion wykorzystaj bibliotekę fictional_names. Rasa powinna być losowa.

Zadania wczytaj z pliku tasks_db.json a następnie wybierz losową próbkę tylu zadań ile wynika 
z wcześniej utworzonej zmiennej. Na podstawie listy słowników utwórz listę instancji klasy Task i zwróć ją.

Wywołaj obie funkcje w main.py i przechwyć ich output.
"""


def initialize_team(team_composition, available_races):
    team = []
    for profession, n_members in team_composition.items():
        for _ in range(n_members):
            name = name_generator.generate_name(style="tolkien", library=True)
            race = random.choice(available_races)()
            team_member = profession(name, race)
            team.append(team_member)
    return team


def initialize_tasks(n_tasks):
    with open("data/tasks_db.json", "r") as f:
        tasks_json = json.load(f)

    tasks = random.sample(tasks_json, n_tasks)
    return [Task(**task) for task in tasks]
