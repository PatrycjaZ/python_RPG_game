import random
import json
from fictional_names import name_generator
from adventure import Task


def initialize_team(team_composition, available_races):
    team = []
    for profession_class, n_members in team_composition.items():
        for _ in range(n_members):
            name = name_generator.generate_name(style="tolkien", library=True)
            race_class = random.choice(available_races)
            race_object = race_class()
            team_member = profession_class(name, race_object)
            team.append(team_member)
    return team


def initialize_tasks(n_tasks):
    with open("data/tasks_db.json", "r") as f:
        tasks_json = json.load(f)

    tasks = random.sample(tasks_json, n_tasks)
    return [Task(**task) for task in tasks]
