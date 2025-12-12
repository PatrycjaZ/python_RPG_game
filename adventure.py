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

"""
Zadanie 9)
W pliku adventure.py napisz klasę Adventure, która będzie posiadała następujące atrybuty:

- team
- tasks

oraz następujące property:

- all_alive
- __lowest_hp_character

a także metodę publiczną run().

Utwórz instancję tej klasy w main.py i wywołaj run().
"""

"""
Zadanie 10

Zaimplementuj metodę run(). 
Powinna ona przeiterować po wszystkich zadaniach i dla każdego z nich wykonać następujące czynności:

- Sprawdzić czy wszyscy bohaterowie żyją. Jeśli nie to wychodzimy z pętli
- Wybrać najbardziej odpowiednią postać do wykonania zadania. 
Wybór tej postaci powinien być realizaowany przez osobną metodę __select_character_for_task()
- Obliczyć total_score jako wielkość kontrybucji wybranego bohatera oraz dodatkowo +1 od pozostałych postaci z drużyny
- Przypisać do zadania nazwę wybranej postaci (do atrybutu character_assigned)
- W zależności od relacji między total_score a trudnością zadania wywołać jedną z metod: 
__handle_victory(), __handle_defeat() lub __handle_draw(). Zdefiniuj te metody, ale na razie ich nie implementuj (pass)
- Jeśli hp bohatera spadło do 0 wyświetl odpowiedni komunikat i wyjdź z pętli. Oznacza to koniec gry i porażkę drużyny
- Wywołaj metodę __heal_allies(), ale na razie jej nie implementuj

Po zakończeniu pętli (wykonaniu wszystkich zadań) upewnij się, że wszyscy nadal żyją 
i jeśli tak to wyprintuj odpowiedni komunikat i ogłoś zwycięstwo.
"""


class Adventure:
    def __init__(self, team, tasks):
        self.team = team
        self.tasks = tasks

    def run(self):
        pass

    @property
    def all_alive(self):
        return True if all([team_member.is_alive
                            for team_member in self.team]) else False

    @property
    def __lowest_hp_character(self):
        hp_list = [team_member.hp for team_member in self.team]
        min_hp = min(hp_list)
        team_char_index = hp_list.index(min_hp)
        return self.team[team_char_index]
