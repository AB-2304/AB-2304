from random import randint
from random import choice
import sys


class Pokemon:
    """
    This is a class for creating Pokemon objects.

    Attributes:
        name (str): The name of the Pokemon.
        attack (int): The attack power of the Pokemon.
        defense (int): The defense power of the Pokemon.
        max_health (int): The maximum health of the Pokemon.
        current_health (int): The current health of the Pokemon.
        """    

    def __init__(self, name, attack, defense, max_health, current_health):
        # I,me, my, mine-English Python - self  Java - this
        # self.radius -  radius becomes the property of the object that self is bound to
        # Assign radius_p1 to this property
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

        
    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        return f'{self.name} (health: {self.current_health}/{self.max_health})'
    
    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        1.If amount is less than the current health, the current health of the Pokemon should decrease by the amount
        2.If amount is greater or equal than the current health, the current health of the Pokemon should decrease to 0
        3.If amount is negative, nothing should happen
        """
        if amount >= 0:
            if amount < self.current_health:
                self.current_health -= amount
            else:
                self.current_health = 0
        return self.current_health
            
    
    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        return self.current_health > 0
    
    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")
        
    def attempt_attack(self, other: "Pokemon") -> bool:
            """
            Attempt an attack on another Pokemon.
            
            1. First, the coefficient of luck is calculated. It is a random value in a range of 0.7 to 1.3 with a step of 0.1.
            
            2. Damage is calculated as the attacking Pokemon’s attack level multiplied by the coefficient of luck. It’s rounded to the nearest integer.
            
            3. If the damage is greater than the defending Pokemon’s defense level, then the attack attempt is successful, and the defending Pokemon’s health loss is equal to the difference between the damage and their defense level. 
            
            4. If the damage is equal to or less than the defending Pokemon’s defense level, then the attack is blocked, and the defending Pokemon does not lose any health.

            """
            luck = choice([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]) 
            damage = round(self.attack*luck)
            print(f"{self.name} attacks {other.name} for {damage} damage!")
            if damage > other.defense:
                attack_attempt = True
                health_loss = damage - other.defense
                other.lose_health(health_loss) 
                print(f"Attack is successful! {other.name} has {other.current_health} health remaining!")
            else:
                print("Attack is blocked")
                attack_attempt = False
            return attack_attempt
        

    def attack_method(self, other: "Pokemon"):
        """
        Game loop for 1 round of battle between two pokemon
        """
        rounds = 1
        while self.is_alive() and other.is_alive() and rounds <= 10:
            print(f"\nRound {rounds} begins! {self} and {other}")
            if self.attempt_attack(other):
                if not other.is_alive():
                    revival_chance = choice([True,False])        
                    if revival_chance == True:
                        other.revive()
                    else:
                        print(f"{self} has won in {rounds} rounds")
                        sys.exit()  # End the function when the battle is over
            if other.attempt_attack(self):
                if not self.is_alive():
                    revival_chance = choice([True,False])        
                    if revival_chance == True:
                        self.revive()
                        continue  # loop back to the beggining 
                    else:
                        print(f"{other} has won in {rounds} rounds")
                        sys.exit()  # End the function when the battle is over
            rounds += 1
              

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines
    

def main():
    """
    Battle of two Pokemon
    """
    pokemon_list = read_pokemon_from_file("C:\\Users\\abhir\\Downloads\\all_pokemon.txt") 
    # Choose a two random pokemon from file
    character1 = pokemon_list[randint(1,801)].strip().split("|")
    character2 = pokemon_list[randint(1,801)].strip().split("|")
    # if the two pokemon chosen are the same, choose another pokemon
    while character1 == character2:  
        character2 = pokemon_list[randint(1,801)].strip().split("|")
    pokemon1 = Pokemon(character1[0], int(character1[1]), int(character1[2]), int(character1[3]), int(character1[3]))
    pokemon2 = Pokemon(character2[0], int(character2[1]), int(character2[2]), int(character2[3]), int(character2[3]))
    print(f"Welcome, {pokemon1} and {pokemon2}!\n")
    pokemon1.attack_method(pokemon2)
    if pokemon1.is_alive() and pokemon2.is_alive():
        print(f"\nIt's a tie between {pokemon1} and {pokemon2}!\n")
        
        
if __name__ == '__main__':
    main()