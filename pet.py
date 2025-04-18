class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5         # Midpoint to start from
        self.energy = 5
        self.happiness = 5
        self.tricks = []        # For storing learned tricks

    def eat(self):
        print(f"{self.name} is eating...")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = min(10, self.energy + 5)

    def play(self):
        if self.energy < 2:
            print(f"{self.name} is too tired to play! ")
            return
        print(f"{self.name} is playing...")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def get_status(self):
        print(f"\n {self.name}'s Current Status:")
        print(f"Hunger: {self.hunger} (0 = Full, 10 = Starving)")
        print(f"Energy: {self.energy} (0 = Exhausted, 10 = Rested)")
        print(f"Happiness: {self.happiness} (0 = Sad, 10 = Ecstatic)")
        if self.tricks:
            print(f"Tricks: {', '.join(self.tricks)} 👌")
        else:
            print("Tricks: None yet")
        print()

    
    def train(self, trick):
        print(f"{self.name} is learning the trick: '{trick}'! 👌")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}  '🙌")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
    