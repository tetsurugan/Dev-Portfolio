
""" 
Create a Character class with attributes and methods that define an RPG character. Then, extend it to specific Warrior and Mage subclasses.

1️⃣ Character Class (Base Class)
	•	Attributes:
	•	name → Character’s name (string)
	•	health → Health points (integer, starts at 100)
	•	attack_power → Attack strength (integer)
	•	Methods:
	•	attack(target) → Reduces the target’s health by the character’s attack_power.
	•	is_alive() → Returns True if health > 0, otherwise False.
 -would is alive be a method on every character that is checked after every action where if is_alive is false make character unavailable?
 
	•	__str__() → Returns a description of the character.
 -would __str__() is a private method would it like show up if somebody used like alook function or something like that to be implemented?
 
-Create Class Character(self): #Will have the attributes and will be inherited to the subclass
	__init__  #we need to initiate the class 
	self.name = name
	self.health = health
	self.attack_power = attack_power
	
	def attack(target):
-select target but for this prototype only one target
-confirm if they want to attack that attarget
-if yes go on to next option
	-subtract attack_power with a random from 1 to attack power
 -end turn
	-if no break and return to menu
 
	def is_alive():
is a method that is private that is checked after every action.  If it is not true that character is made unavailable or in this case the battle is over because it is one vs one
	__str__():
 is a private method that provides a description for an enemy.  That may give hints for special attacks.  You would be able to see it with a look command or something
 


Warrior (Subclass of Character)
-create a class Warrior
-It would have an attribute called armor that can go up by level or maybe equipment in the future.

when taking damage a method will be checked called take_damage(amount) that method would subtract method which would be the armor attribute from the damage and if it was below 0 it would just take 0 damage
	•	Has extra defense (armor).
	•	When taking damage, reduces incoming damage by armor value.

Additional Methods:
	•	take_damage(amount) → Reduces health based on armor.
 
 3️⃣ Mage (Subclass of Character)
	•	Has mana for casting spells.
	•	Can cast fireball, which deals extra damage but consumes mana.
-Would have an attribute in its class called mana and mana would be displayed somewhere in an area that would be appropriate to be figured out in a visual command line situation. mana would be an interger it would need a current mana value and  a max mana value and mana current mana can't go below 0 or past max mana.

an additional method would be made probably a method in a folder of methods for available spells or something. it would cost 10 mana so it would subtract from the current mana value


Additional Methods:
	•	cast_fireball(target) → Deals attack_power * 1.5 damage but consumes 10 mana.
	•	regenerate_mana(amount) → Restores mana. """