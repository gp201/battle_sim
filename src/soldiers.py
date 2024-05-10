class Soldiers:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank
        self.health = 100
        self.alive = True

    def attack(self):
        """Attack the enemy."""
        pass

    def defend(self):
        """Defend against the enemy."""
        pass

    def move(self):
        """Move to a new position."""
        pass

    def die(self):
        """Die and remove from the army."""
        pass
