"""Feature	How Dictionaries Help
Character Stats	Store health, attack, mana dynamically.
- will use dictionaries for stats and spells/skills

Combat Log	Track who attacked who & how much damage was dealt.
-Every action will be put into the log so that everyone can get a play by play on what happend so far. atleast for the batttle with each battle that log getting rewrote with the current battle
Skills & Spells	Store spell names as keys, damage functions as values.
Inventory	Track items and their durability using comprehensions.
-I will need to make an inventroy menu i suppose that would probably be a list of dictionaries with item name being the key and the inventory and the ability effect being the values 
Enemy AI	Define enemy behavior dynamically.
-idk maybe a random or a percent base on using certain skills or maybe conditionals like if hp less than half more likely to use this skill or more likely to have a critical hit or something

    """

1️⃣ Character Class (Base Class)

This is the base template for all RPG characters. 
-base class for monsters and playable characters every subclass will inherit this.  Will also use overright methods but unsure on how to use them.
Every Warrior and Mage will inherit from it.
-after inheriting the character class the subclassess will get some benefit and maybe some detriment for the class.

-attributes will be a name attribute and a stats dictionary so far hp =100 mp=0 attack_power equals something and a skill dictionary that will be changed if subclass needs it or maybe just have a different list item added to it.  Maybe have skills be used with a limit like 1 or two times until you rest. like a mage might have skills and spells while a warrior might only have skills.
Attributes:
	•	name: The name of the character.
    -name will be an attribute
    -stats will be in dictionary
    will use dictionary comprehension for
	•	health: Starts at 100 and decreases when taking damage.
	•	attack_power: Determines how strong an attack is.

Methods:
-metho attack attack and a target attack would have attack - what ever else such as armor which would include a bonus for warriors as everyone should be able to wear armor.  The attack would be a random number from the attack minimum plus whatever bonuses up to the max plus whatever bonuses.
- str Im sure is an overwrite method that gives you a hint or just some basic knowledge when looking at a person maybe an examine option that costs a turn that may or may not help you out but if you have examined that type of monster before you wont have to use it again for the battle atleast. maybe a class or an item later that allows you to remember things you have examined.


is alive will be a status that is checked after every action because you never know maybe poision or something else killed them.  If is_alive = false they will be unavaialble until that becomes true again.  Either item spell or rest.
	1.	attack(target) → Asks the player if they want to attack.
	•	If Yes, it generates random damage between 1 and attack_power.
	•	Reduces the target’s health by that damage.
	•	Calls is_alive() on the target after attack.
	2.	is_alive() → Returns True if health is above 0, otherwise False.
	3.	str() → Used to display character details when print(object) is called.

2️⃣ Warrior Class (Subclass of Character)
	•	Warriors inherit from Character and have extra armor to reduce damage.

New Attribute:
	•	armor: The amount of damage reduction applied when taking a hit.

New Method:
	1.	take_damage(amount) → Handles how a warrior receives damage.
	•	Damage is reduced by the armor value.
	•	If damage is lower than armor, set it to 0 (Warrior takes no damage).
	•	Subtracts final damage from the Warrior’s health.

	Example:
		•	If an enemy attacks with 15 damage, and the Warrior has 5 armor, the Warrior only takes 10 damage.

3️⃣ Mage Class (Subclass of Character)

Mages inherit from Character but use mana to cast spells.

New Attributes:
	•	mana → The current mana pool.
	•	max_mana → The maximum mana a Mage can have.

New Methods:
	1.	cast_fireball(target)
	•	Checks if the Mage has at least 10 mana.
	•	If True, it deals attack_power × 1.5 damage.
	•	Subtracts 10 mana from the Mage’s mana pool.
	•	Prints “Mage casts Fireball!”.
	•	Calls is_alive() on the target after attack.
	•	If not enough mana, prints "Not enough mana!".
	2.	regenerate_mana(amount)
	•	Restores mana by a given amount.
	•	If mana goes over max_mana, it is capped at max_mana.

	Example:
		•	A Mage with 20 mana casts Fireball twice.
	•	After two casts, mana drops to 0.
	•	If regenerate_mana(15) is called, the new mana is 15.
	•	If max_mana = 25, the Mage cannot exceed 25 mana.



4️⃣ Core Game Logic

-so from my understanding a game is just like a movie with dynamically appearing code.  So this would be a while loop that checks the status of the logic over each loop and each loop going back and forth until a party dies or escapes or some sort of other conditional.


	•	The player takes turns selecting an action.
	•	If the enemy’s is_alive() is False, the player wins.
	•	If the player’s is_alive() is False, they lose.
	•	Later, additional menus and mechanics can be added:
	•	Skills for Warriors
	•	Healing items
	•	Running from battle
	•	Enemy AI behavior

    What to Research & Work On
	•	How to inherit from a class in Python.
	•	How to override methods from a base class.
	•	How to use super() to reference the parent class.
	•	How to generate random numbers (random.randint).
	•	How to use conditionals (if health <= 0).
