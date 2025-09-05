from random import choice
from attacks import get_random_attacks, get_boss_attacks
from time import sleep

def create_enemy(level):
	
	enemy_hp = 15 + level
	
	names = [
		"Gelatimon", "Chocobite", "Marshmunch", "Gummyfang", "Caramellow", "Fudgester", "Sprinkletooth", "Nougator", "Puffmallow", "Licoricepike",
		"Bonbonic", "Truffluff", "Sugaraptor", "Candicorn", "Mochibite", "Taffyjaw", "Jellifin", "Frostmallow", "Cinnasnarl", "Mallowtail",
		"Sourpuff", "Twizzlurk", "Crumblepaw", "Snickerdash", "Cocoaclaw", "Meringoon", "Gumdropper", "S'moregon", "Frostfang", "Pecanine",
		"Maplehorn", "Crispette", "Canelure", "Brittleback", "Fudgehog", "Mochitusk", "Puffernut", "Cinnabite", "Syrupine", "Glazebat",
		"Mallowmane", "Tartleap", "Crumbletail", "Jellypaw", "Nougathorn", "Sprinklepaw", "Sugarwing", "Marshclaw", "Frostbite", "Cocoapuff",
		"Gumblin", "Truffluffin", "Bonbunny", "Candysaur", "Mochicat", "Taffycoon", "Jellibear", "Frostcat", "Cinnadillo", "Mallowbug",
		"Sourling", "Twizzlizard", "Crumblebee", "Snickerbat", "Cocoamole", "Meringull", "Gumdrake", "S'morebat", "Frostowl", "Pecatoad",
		"Maplemouse", "Crispbat", "Canelizard", "Brittlebee", "Fudgebat", "Mochifin", "Pufferbat", "Cinnacorn", "Syrupbat", "Glazebee",
		"Mallowbat", "Tartbat", "Crumblefin", "Jellyfin", "Nougatcat", "Sprinklecat", "Sugarcat", "Marshbat", "Frostcat", "Cocoacat",
		"Gumcat", "Trufflecat", "Bonboncat", "Candycat", "Mochicat", "Taffycat", "Jellicat", "Frostcat", "Cinnacat", "Mallowcat"
	]
	adjectives = [
		"of Sugar", "Frosted", "Caramelized", "Filled", "from the Candyshop", "Glazed", "Crunchy", "Swirled", "Sticky", "Whipped",
		"Candied", "Toasted", "Iced", "Molten", "Syrupy", "Spiced", "Crisped", "Dusted", "Layered", "Fluffy",
		"Gooey", "Crumbly", "Nutty", "Zesty", "Tangy", "Buttery", "Jammed", "Honeyed", "Roasted", "Sprinkled",
		"Sugary", "Melted", "Puffed", "Brittle", "Chewy", "Chilled", "Spun", "Velvety", "Rich", "Light",
		"Deep-Fried", "Double-Dipped", "Triple-Layered", "Rainbow", "Golden", "Silvered", "Bronzed", "Crystalized", "Powdered", "Glittering",
		"Sparkling", "Glossy", "Shiny", "Dazzling", "Twisted", "Swirled", "Layered", "Frosty", "Creamy", "Dreamy",
		"Magic", "Mystic", "Enchanted", "Royal", "Epic", "Legendary", "Ancient", "Modern", "Classic", "Wild",
		"Mini", "Mega", "Ultra", "Hyper", "Super", "Max", "Prime", "Alpha", "Omega", "Beta",
		"Sweetest", "Sour", "Salty", "Spicy", "Mild", "Bold", "Gentle", "Fierce", "Brave", "Clever"
	]
	boss_names = [
		"Lord Licorice", "Queen Caramel", "Duke Doughnut", "Princess Praline", "Baroness Bonbon", "Count Candy", "Emperor Eclair", "King Kandy", "Sir Sugar", "Madame Meringue"
	]
	boss_adjectives = [ "The Sour", "The Sweet", "The Spicy", "The Creamy", "The Crunchy", "The Chewy", "The Fluffy", "The Gooey", "The Frosted", "The Glazed"]

	if level % 10 == 0:
		print(f'🎉🎉🎉 Candy Boss Level {level} Reached! 🎉🎉🎉')
		enemy_name = f"{choice(boss_names)} {choice(boss_adjectives)} Candy"
		enemy_hp += 20
		enemy_attacks = get_random_attacks(2)
		for attack in enemy_attacks:
			attack['damage'] = int(attack['base_damage'] + level)
		print(f'Whoa! {enemy_name} looks tough! Its attacks deal {enemy_attacks[0]['damage']} and {enemy_attacks[1]['damage']} damage respectively.')
		sleep(1)
	else:
		enemy_name = f"{choice(names)} {choice(adjectives)}"
		enemy_attacks = get_random_attacks(2)
		for attack in enemy_attacks:
			attack['damage'] = attack['base_damage'] * (level // 2)

	new_enemy = {
		"name": enemy_name,
		"current_hp": enemy_hp,
		"max_hp": enemy_hp,
		"attacks": enemy_attacks
	}
	return new_enemy