from random import choice
from attacks import get_random_attacks, get_boss_attacks
from time import sleep
from rich import print

def create_enemy(level):
	from rich import print
	
	enemy_hp = 15 + level
	
	names = list({
		"Gelatimon", "Chocobite", "Marshmunch", "Gummyfang", "Caramellow", "Fudgester", "Sprinkletooth", "Nougator", "Puffmallow", "Licoricepike",
		"Bonbonic", "Truffluff", "Sugaraptor", "Candicorn", "Mochibite", "Taffyjaw", "Jellifin", "Frostmallow", "Cinnasnarl", "Mallowtail",
		"Sourpuff", "Twizzlurk", "Crumblepaw", "Snickerdash", "Cocoaclaw", "Meringoon", "Gumdropper", "S'moregon", "Frostfang", "Pecanine",
		"Maplehorn", "Crispette", "Canelure", "Brittleback", "Fudgehog", "Mochitusk", "Puffernut", "Cinnabite", "Syrupine", "Glazebat",
		"Mallowmane", "Tartleap", "Crumbletail", "Jellypaw", "Nougathorn", "Sprinklepaw", "Sugarwing", "Marshclaw", "Frostbite", "Cocoapuff",
		"Gumblin", "Truffluffin", "Bonbunny", "Candysaur", "Mochicat", "Taffycoon", "Jellibear", "Frostcat", "Cinnadillo", "Mallowbug",
		"Sourling", "Twizzlizard", "Crumblebee", "Snickerbat", "Cocoamole", "Meringull", "Gumdrake", "S'morebat", "Frostowl", "Pecatoad",
		"Maplemouse", "Crispbat", "Canelizard", "Brittlebee", "Fudgebat", "Mochifin", "Pufferbat", "Cinnacorn", "Syrupbat", "Glazebee",
		"Mallowbat", "Tartbat", "Crumblefin", "Jellyfin", "Nougatcat", "Sprinklecat", "Sugarcat", "Marshbat", "Frostcat", "Cocoacat",
		"Gumcat", "Trufflecat", "Bonboncat", "Candycat", "Mochicat", "Taffycat", "Jellicat", "Frostcat", "Cinnacat", "Mallowcat",
		"Marshmouse", "Jellyhopper", "Nougathog", "Fudgefin", "Taffybug", "Chocoroo", "Sprinklebat", "Bonbonbunny", "Truffletail", "Frostfox",
		"Cinnacub", "Mallowmole", "Syrupbee", "Caramelpup", "Crunchycat", "Glazebird", "Jellysnail", "Mochifin", "Taffycrab", "Fudgelamb",
		"Licoriceowl", "Sugarfrog", "Gummysheep", "Bonbonrat", "Truffledeer", "Frostferret", "Cinnadillo", "Mallowlizard", "Syrupduck", "Carameltoad",
		"Crunchycoon", "Glazebee", "Jellyhog", "Mochifox", "Taffyfish", "Fudgefrog", "Licoricecat", "Sugarbug", "Gummygoat", "Bonbonmouse",
		"Trufflehare", "Frostmouse", "Cinnadog", "Mallowbee", "Syrupgoose", "Caramelmoth", "Crunchymouse", "Glazebat", "Jellycrab", "Gumdropper"
	})
	adjectives = list({
		"of Sugar", "Frosted", "Caramelized", "Filled", "from the Candyshop", "Glazed", "Crunchy", "Swirled", "Sticky", "Whipped",
		"Candied", "Toasted", "Iced", "Molten", "Syrupy", "Spiced", "Crisped", "Dusted", "Layered", "Fluffy",
		"Gooey", "Crumbly", "Nutty", "Zesty", "Tangy", "Buttery", "Jammed", "Honeyed", "Roasted", "Sprinkled",
		"Sugary", "Melted", "Puffed", "Brittle", "Chewy", "Chilled", "Spun", "Velvety", "Rich", "Light",
		"Deep-Fried", "Double-Dipped", "Triple-Layered", "Rainbow", "Golden", "Silvered", "Bronzed", "Crystalized", "Powdered", "Glittering",
		"Sparkling", "Glossy", "Shiny", "Dazzling", "Twisted", "Swirled", "Layered", "Frosty", "Creamy", "Dreamy",
		"Magic", "Mystic", "Enchanted", "Royal", "Epic", "Legendary", "Ancient", "Modern", "Classic", "Wild",
		"Mini", "Mega", "Ultra", "Hyper", "Super", "Max", "Prime", "Alpha", "Omega", "Beta",
		"Sweetest", "Sour", "Salty", "Spicy", "Mild", "Bold", "Gentle", "Fierce", "Brave", "Clever",
		"Sugary", "Frosty", "Caramel-Coated", "Glazed", "Crunch-Coated", "Swirled", "Sticky", "Whipped", "Candied", "Toasted",
		"Iced", "Molten", "Syrupy", "Spiced", "Crispy", "Dusted", "Layered", "Fluffy", "Gooey", "Crumbly",
		"Nutty", "Zesty", "Tangy", "Buttery", "Jammed", "Honeyed", "Roasted", "Sprinkled", "Melted", "Puffed",
		"Brittle", "Chewy", "Chilled", "Spun", "Velvety", "Rich", "Light", "Rainbow", "Golden", "Silvered",
		"Bronzed", "Crystalized", "Powdered", "Glittering", "Sparkling", "Glossy", "Shiny", "Dazzling", "Twisted", "Creamy"
	})
	boss_names = list({
		"Lord Licorice", "Queen Caramel", "Duke Doughnut", "Princess Praline", "Baroness Bonbon", "Count Candy", "Emperor Eclair", "King Kandy", "Sir Sugar", "Madame Meringue",
		"King Jawbreaker", "Baroness Bonbon", "Duke Nougat", "Emperor Eclair", "Count Candyfloss", "General Gumdrop", "Captain Caramel", "Sir Sugarcane", "Lady Lollipop", "Master Mochi",
		"Archduke Almond", "Supreme S'more", "Overlord Oreo", "Grandmaster Gummy", "Highlord Honeycomb", "Commander Cocoa", "Warlord Wafer", "Pharaoh Fudge", "Sultan Snickers", "Oracle Orangepeel",
		"Titan Toffee", "Vizier Velvet", "Magister Maple", "Chancellor Cherry", "Regent Raspberry", "Viceroy Vanilla", "Shogun Shortbread", "Paladin Peanut", "Sorcerer Sherbet", "Guardian Gum",
		"Sentinel Sprinkles", "Enchanter Espresso", "Prophet Pistachio", "Mystic Meringue", "Sage Strawberry", "Seer Sours", "Judge Jellybean", "Marshal Mint", "Admiral Apple", "Bishop Brownie",
		"Warden Walnut", "Keeper Kiwi", "Watcher Whitechoc", "Herald Hazelnut", "Champion Churro", "Defender Dulce", "Conqueror Crunch", "Queen Marshmallow", "Princess Praline", "Count Candy"
	})
	boss_adjectives = list({
		"The Sour", "The Sweet", "The Spicy", "The Creamy", "The Crunchy", "The Chewy", "The Fluffy", "The Gooey", "The Frosted", "The Glazed",
		"The Supreme Sweet", "The Infinite Sugar", "The Eternal Frost", "The Unyielding Caramel", "The Vicious Nougat", "The Colossal Marshmallow", "The Unbreakable Toffee", "The Legendary Licorice", "The Fearless Fudge", "The Unstoppable Gummy",
		"The Mighty Jawbreaker", "The Dreaded Bonbon", "The Glorious Praline", "The Ruthless Choco", "The Invincible S'more", "The Cursed Candyfloss", "The Blessed Maple", "The Ancient Almond", "The Timeless Honeycomb", "The Radiant Raspberry",
		"The Shadowed Sherbet", "The Blazing Brownie", "The Frozen Meringue", "The Electric Sherbet", "The Toxic Pistachio", "The Savage Shortbread", "The Noble Peanut", "The Fierce Sprinkles", "The Prime Espresso", "The Alpha Apple",
		"The Omega Oreo", "The Beta Berry", "The Sweetest Churro", "The Sour Sours", "The Salty Walnut", "The Spicy Hazelnut", "The Mild Kiwi", "The Bold Dulce", "The Gentle Whitechoc", "The Brave Crunch",
		"The Clever Jellybean", "The Wise Mint", "The Merciless Strawberry", "The Just Vanilla", "The Loyal Gum", "The Proud Wafer", "The Silent Judge", "The Loud Champion", "The Swift Keeper", "The Patient Watcher"
	})

	if level % 10 == 0:
		print(f'🎉🎉🎉 Candy Boss Level [bold magenta]{level}[/bold magenta] Reached! 🎉🎉🎉')
		enemy_name = f"[bold magenta]{choice(boss_names)} {choice(boss_adjectives)} Candy[/bold magenta]"
		enemy_hp += 20
		enemy_attacks = get_random_attacks(2)
		for attack in enemy_attacks:
			attack['damage'] = int(attack['base_damage'] + level)
		print(f'Whoa!{enemy_name} looks tough! Its attacks deal {enemy_attacks[0]['damage']} and {enemy_attacks[1]['damage']} damage respectively.')
		sleep(1)
	else:
		enemy_name = f"[bold green]{choice(names)} {choice(adjectives)}[/bold green]"
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