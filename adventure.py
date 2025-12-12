"""
Zadanie 6)
W pliku adventure.py napisz klasę Task, która będzie miała następujące atrybuty:

- name
- task_type
- difficulty
- success_damage
- fail_damage
- completed
- character_assigned

Przetestuj tę klasę tworząc kilka zadań.
"""


class Task:
    def __init__(self, name, task_type, difficulty, success_damage, fail_damage, completed, character_assigned):
        self.name = name
        self.task_type = task_type
        self.difficulty = difficulty
        self.success_damage = success_damage
        self.fail_damage = fail_damage
        self.completed = completed
        self.character_assigned = character_assigned
