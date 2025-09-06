from random import randint
from characters import create_enemy
from game_logic import battle
from game_utils import save_game, compare_candy, show_title_screen
from time import sleep
from rich import print

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
	print(f'🍬🍭🍫🍩🍪 Level [bold green]{level}[/bold green] of the Sweet Journey 🍬🍭🍫🍩🍪')
	sleep(2)
	print(f"[bold yellow]You explore the layer cake even deeper...[/bold yellow]")
	sleep(2)
	enemy = create_enemy(level)
	print(f"A candy creature named {enemy['name']} appeared!")
	sleep(2)
	battle_result = battle(player, enemy)

	if battle_result:
		print(f'You survived level [bold green]{level}[/bold green] of the sweet adventure!')
		sleep(2)
		level += 1
		player['current_hp'] = player['max_hp']
		if level >=2:
			# Increase base damage of player's attacks by 10% each level after level 1
			for attack in player['attacks']:
				attack['damage'] = int(attack['damage'] + level // 2)
			print(f'Your candy character [bold cyan]{player['name']}[/bold cyan] feels stronger! Base damage increased to {player['attacks'][0]['damage']} and {player['attacks'][1]['damage']} respectively.')
			sleep(1)

		# Ask to save game after winning a level
		save_choice = input(f'Do you want to save the game? (y/n)\n').lower().strip()[0]
		if save_choice == 'y':
			save_game(player, level)
		else:
			print(f'[bold yellow]Continuing without saving...[/bold yellow]')
			sleep(2)

		# Friendship chance after winning
		level_check = level - 1
		friendship = randint(1,4)
		if level_check % 10 == 0:
			friendship = randint(1,20) # Lower chance on boss levels
		if friendship == 4:
			enemy['current_hp'] = enemy['max_hp']
			print(f"You and {enemy['name']} share a moment of friendship!")
			print(f'[bold yellow]Comparing candy stats...[/bold yellow]')
			sleep(2)
			compare_candy(player, enemy)
			print(f"{enemy['name']}", end = '')
			accept = input(f" looks sweet and friendly. Do you want to swap your CANDY for it? (y/n)\n")
			if accept == 'y':
				print(f"{enemy['name']} has joined your confectionery team!")
				sleep(2)
				player = enemy.copy()
				player['current_hp'] = player['max_hp']
			else:
				print(f"[bold red]You refused the friendship of[/bold red] {enemy['name']}. [bold red]It dissolves into the air like sugar.[/bold red]")
				sleep(2)
	else: # Player was defeated
		print(f'[bold red]Your sweet adventure ends here![/bold red]')
		sleep(2)
		player_alive = False

print(f'[bold red]Game Over[/bold red] [bold green]- Thanks for sweetening the world![/bold green]')
sleep(2)