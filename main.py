from random import randint
from characters import create_enemy
from game_logic import battle
from game_utils import save_game, compare_candy, show_title_screen
from time import sleep


# --- Global Game State ---
player_alive = True
player_template = {
		"name": "user",
		"current_hp": 50,
		"max_hp": 50,
		"attacks": []
	}

# --- Game Start ---
player, level = show_title_screen(player_template)

while player_alive:
	print(f'🍬🍭🍫🍩🍪 Level {level} of the Sweet Journey 🍬🍭🍫🍩🍪')
	sleep(2)
	print("You explore the layer cake even deeper...")
	sleep(2)
	enemy = create_enemy(level)
	print(f"A candy creature named {enemy['name']} appeared!")
	sleep(2)
	battle_result = battle(player, enemy)

	if battle_result:
		print(f'You survived level {level} of the sweet adventure!')
		sleep(2)
		level += 1
		player['current_hp'] = player['max_hp']
		if level >=2:
			# Increase base damage of player's attacks by 10% each level after level 1
			for attack in player['attacks']:
				attack['damage'] = int(attack['damage'] + level // 2)
			print(f'Your candy character {player['name']} feels stronger! Base damage increased to {player['attacks'][0]['damage']} and {player['attacks'][1]['damage']} respectively.')
			sleep(1)

		# Ask to save game after winning a level
		save_choice = input('Do you want to save the game? (y/n)\n').lower().strip()[0]
		if save_choice == 'y':
			save_game(player, level)
		else:
			print('Continuing without saving...')
			sleep(2)

		# Friendship chance after winning
		level_check = level - 1
		friendship = randint(1,4)
		if level_check % 10 == 0:
			friendship = randint(1,20) # Lower chance on boss levels
		if friendship == 4:
			enemy['current_hp'] = enemy['max_hp']
			print(f"You and {enemy['name']} share a moment of friendship!")
			print('Comparing candy stats...')
			sleep(2)
			compare_candy(player, enemy)
			accept = input(f"{enemy['name']} looks sweet and friendly. Do you want to swap your {player['name'].upper()} for it? (y/n)\n").lower().strip()
			if accept == 'y':
				print(f"{enemy['name']} has joined your confectionery team!")
				sleep(2)
				player = enemy.copy()
				player['current_hp'] = player['max_hp']
			else:
				print(f"You refused the friendship of {enemy['name']}. It dissolves into the air like sugar.")
				sleep(2)
	else: # Player was defeated
		print('Your sweet adventure ends here!')
		sleep(2)
		player_alive = False

print('Game Over - Thanks for sweetening the world!')
sleep(2)