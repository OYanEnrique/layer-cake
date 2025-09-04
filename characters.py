from random import choice
from attacks import get_random_attacks

def create_enemy(level):
	
	enemy_hp = 20 + (level * 5)
	
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
	enemy_name = f"{choice(names)} {choice(adjectives)}"

	# Get random attacks for the enemy
	enemy_attacks = get_random_attacks(2)

	# Adjust attack damage based on the enemy's level
	for attack in enemy_attacks:
		attack['damage'] = attack['base_damage'] + level

	new_enemy = {
		"name": enemy_name,
		"current_hp": enemy_hp,
		"max_hp": enemy_hp,
		"attacks": enemy_attacks
	}
	return new_enemy