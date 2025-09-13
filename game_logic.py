from random import choice
from game_utils import show_status
from time import sleep
from rich import print
from random import randint

def battle(p, e):
	sleep(2)
	print(f'[bold yellow]BATTLE START[/bold yellow]: [bold cyan]{p['name']}[/bold cyan] VS [bold magenta]{e['name']}[/bold magenta]')
	sleep(2)

	while True:
		show_status(p, e)
		print(f'[bold yellow]------ YOUR TURN ------[/bold yellow]')
		choice_input = input(f'Choose your attack (1 or 2)\n').strip()

		if choice_input == '1':
			if randint(1, 100) <= 15:
				print(f'[bold red]Your Attack missed![/bold red]')
			else:
				damage_dealt = p['attacks'][0]['damage']
				e['current_hp'] -= damage_dealt
				print(f'[bold blue]You used [/bold blue][bold red]{p['attacks'][0]['attack_name']}[/bold red] [bold blue]and dealt[/bold blue] [bold red]{damage_dealt}[/bold red] [bold blue]damage[/bold blue]')
				sleep(1)
		elif choice_input == '2':
			if randint(1, 100) <= 15:
				print(f'[bold red]Your Attack missed![/bold red]')
			else:
				damage_dealt = p['attacks'][1]['damage']
				e['current_hp'] -= damage_dealt
				print(f'[bold blue]You used[/bold blue] [bold red]{p['attacks'][1]['attack_name']}[/bold red] [bold blue]and dealt[/bold blue] [bold red]{damage_dealt}[/bold red] [bold blue]damage[/bold blue]')
				sleep(1)
		else:
			print(f'[bold red]Invalid option[/bold red]')
			continue

		if e['current_hp'] <= 0:
			e['current_hp'] = 0
			print(f"{e['name']} [bold green]has been defeated![/bold green]")
			sleep(2)
			return True
		else:
			if choice_input in ['1', '2']:
				if randint(1, 100) <= 15:
					print(f'{e['name']} [bold red]Attack missed![/bold red]')
				else:
					print(f"[bold yellow]------ {e['name']} TURN ------[/bold yellow]")
					enemy_attack = choice(e['attacks'])
					enemy_damage = enemy_attack['damage']
					p['current_hp'] -= enemy_damage
					print(f"{e['name']} [bold blue]used[/bold blue] [bold red]{enemy_attack['attack_name']}[/bold red] [bold blue]and dealt[/bold blue] [bold red]{enemy_damage}[/bold red] [bold blue]damage[/bold blue]")
					sleep(1)
				if p['current_hp'] <= 0:
					p['current_hp'] = 0
					return False
			else:
				print(f'[bold red]Please choose a valid attack next time [1 or 2]![/bold red]')
				sleep(1)