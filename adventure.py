"""
Zadanie 6)
W pliku adventure.py napisz klasę Task, która będzie miała następujące atrybuty:
name, task_type, difficulty, success_damage, fail_damage, completed, character_assigned

Przetestuj tę klasę tworząc kilka zadań.
"""


class Task:
    def __init__(self, name, task_type, difficulty, success_damage, fail_damage):
        self.name = name
        self.task_type = task_type
        self.difficulty = difficulty
        self.success_damage = success_damage
        self.fail_damage = fail_damage
        self.completed = None
        self.character_assigned = None


# task1 = Task("Goblin attack", "combat", 10, 3, 6)
# print(task1.__dict__)
