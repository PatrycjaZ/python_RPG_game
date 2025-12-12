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


class Human(Race):
    def __init__(self):
        super().__init__("Human", 1, 1, 1)


class Elf(Race):
    def __init__(self):
        super().__init__("Elf", -1, 2, 0)


class Orc(Race):
    def __init__(self):
        super().__init__("Orc", 2, -1, -1)
