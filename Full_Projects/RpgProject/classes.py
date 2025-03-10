class Character:
    def __init__(self,name):
        self.name = name
        self.stats = {
                    "health" : 100,
                    "mana" : 0,
                    "attack_power" : 5,
                    }
    def attack(self, target):
        import random
        hit_chance = random.randint(1,10)
        
        if hit_chance > 2:
            damage = self.stats["attack_power"]
            target.stats["health"] -= damage
            print(f"{self.name} attacks {target.name} for {damage} damage")
            
            if target.stats["health"] <= 0:
                print(f"{target.name} has been defeated!")
        else:
            print(f"{self.name} has missed the attack!")
player = Character("Hero")
enemy = Character("Goblin")

player.attack(enemy)  # Hero attacks Goblin for X damage!

enemy.attack(player)    

""" CLASS Character:
    INIT(name, attack_power):
        SET self.name = name
        SET self.health = 100
        SET self.attack_power = attack_power

    METHOD attack(target):
        PRINT "Do you want to attack?" (Yes/No)
        IF Yes:
            GENERATE random_damage BETWEEN 1 and self.attack_power
            REDUCE target.health BY random_damage
            PRINT attack message
        ENDIF
        CHECK target.is_alive()

    METHOD is_alive():
        RETURN self.health > 0

    METHOD __str__():
        RETURN "Description of character (name, health, etc.)" """
        
"""         
CLASS Warrior EXTENDS Character:
    INIT(name, attack_power, armor):
        CALL Superclass(Character) INIT with name, attack_power
        SET self.armor = armor

    METHOD take_damage(amount):
        SET reduced_damage = amount - self.armor
        IF reduced_damage < 0:
            SET reduced_damage = 0
        ENDIF
        REDUCE self.health BY reduced_damage
        PRINT "Warrior takes reduced damage!" """
        
""" CLASS Mage EXTENDS Character:
    INIT(name, attack_power, mana, max_mana):
        CALL Superclass(Character) INIT with name, attack_power
        SET self.mana = mana
        SET self.max_mana = max_mana

    METHOD cast_fireball(target):
        IF self.mana >= 10:
            SET damage = attack_power * 1.5
            REDUCE target.health BY damage
            REDUCE self.mana BY 10
            PRINT "Mage casts Fireball!"
        ELSE:
            PRINT "Not enough mana!"
        ENDIF
        CHECK target.is_alive()

    METHOD regenerate_mana(amount):
        INCREASE self.mana BY amount
        IF self.mana > self.max_mana:
            SET self.mana = self.max_mana """
            
inventory = {
    "Potion": {"quantity": 5, "description": "Heals 50 Hp"},
    "Bomb":{"quantity": 2, "description": "Deals 100 damage to enemies"},
    "Elixir": {"quantity": 1, "description": "Restores full HP & MP"}
}

def show_inventory():
    """Displays the inventory with item names and their attributes."""
    if not inventory:
        print("Your inventory is empty")
        return
    
    print("Inventory: ")
    
    for item_name, item_data in inventory.items():
        quantity = item_data["quantity"]
        description = item_data["description"]
        print(f"- {item_name}: ({quantity}) {description}")
        
show_inventory()        




test_dic = {
    "Bomb": {"Quantity": 5, "effect": "Deals 100 damage to enemies"},
    "Potion": {"Quantity": 5, "effect": "Heals 100 damage."}
}

def show_inventory(inv):
    for items, details in inv.items():
        print(inv.items())