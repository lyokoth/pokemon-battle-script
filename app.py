class Pokemon: 
    def __init__(self, name, type_, level=5, health=100, max_health=100):
        self.name = name
        self.type = type_
        self.level = level
        self.health = health
        self.max_health = max_health
        self.is_knocked_out = False


    def __repr__(self):
        return "{name} is a level {level} Pokemon with {health} health.".format(name=self.name, level=self.level, health=self.health)
        


    def lose_health(self, damage):
        self.health -= damage
        print(f"{self.name} now has {self.health} health.")
        if self.health <= 0:
            self.knock_out()

    def gain_health(self, amount):
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} now has {self.health} health.")

    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print(f"{self.name} is knocked out!")

    def revive(self):
        self.is_knocked_out = False
        self.health = 1
        print(f"{self.name} has been revived!".format(self.name))
        
    def attack(self, other_pokemon):
        if (self.type == "Fire" and other_pokemon.type == "Water") or \
           (self.type == "Water" and other_pokemon.type == "Grass") or \
           (self.type == "Grass" and other_pokemon.type == "Fire"):
            print(f"{self.name} attacked {other_pokemon.name} for {round(self.level * 0.5)} damage.")
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
        elif self.type == other_pokemon.type:
            print(f"{self.name} attacked {other_pokemon.name} for {self.level} damage.")
            other_pokemon.lose_health(self.level)
        # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
        elif (self.type == "Fire" and other_pokemon.type == "Grass") or \
             (self.type == "Water" and other_pokemon.type == "Fire") or \
             (self.type == "Grass" and other_pokemon.type == "Water"):
            print(f"{self.name} attacked {other_pokemon.name} for {self.level * 2} damage.")
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)


class Fennekin(Pokemon):
    def __init__(self, level=5):
        super().__init__("Fennekin", "Fire", level)


class Froakie(Pokemon):
    def __init__(self, level=5):
        super().__init__("Froakie", "Water", level)


class Chespin(Pokemon):
    def __init__(self, level=5):
        super().__init__("Chespin", "Grass", level)


class Trainer:
    def __init__(self, pokemons, potions, name):
        self.name = name
        self.potions = potions 
        self.pokemons = pokemons
        self.current_pokemon = 0

    def __repr__(self):
        print("The trainer {name} has the following Pokemon.".format(name=self.name))
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active Pokemon is {name}.".format(name=self.pokemons[self.current_pokemon].name)

    def switch_pokemon(self, active):
        if active < len(self.pokemons) and active >= 0:
            if self.pokemons[active].is_knocked_out:
                print("{self.name} has no energy left to battle!")
            elif active == self.current_pokemon:
                print(f"{self.name} is already in battle!")
            else:
                self.current_pokemon = active
                print(f"Go, {self.name}!")

    def use_potion(self):
        if self.potions > 0:
            print("Used a potion on {self.name}.")
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else: 
            print("You don't have any potions!")

    def battle_trainer(self, other_trainer):
        your_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        your_pokemon.attack(their_pokemon)


a = Fennekin(5)
b = Froakie(4)
c = Chespin(10)
d = Chespin(7)
e = Froakie(11)
f = Fennekin(3)
player_name = input("What's your name, trainer?")
print("Okay, {}!").input(player_name)
trainer_one = Trainer([a, b, c], 3, "Kieran")
trainer_two = Trainer([d, e, f], 5, "Lyn")
print(trainer_one)
print(trainer_two)

trainer_one.battle_trainer(trainer_two)
trainer_two.battle_trainer(trainer_one)
trainer_two.use_potion()
trainer_one.battle_trainer(trainer_two)
trainer_two.switch_pokemon(0)
trainer_two.switch_pokemon(1)


