from random import choice
from game_utils import show_status
from time import sleep

def battle(p, e):
	sleep(2)
	print(f'BATTLE START: {p['name']} VS {e['name']}')
	sleep(2)

	while True:
		show_status(p, e)
		print('------ YOUR TURN ------')
		choice_input = input('Choose your attack (1 or 2)\n').strip()

		if choice_input == '1':
			damage_dealt = p['attacks'][0]['damage']
			e['current_hp'] -= damage_dealt
			print(f'You used {p['attacks'][0]['attack_name']} and dealt {damage_dealt} damage')
			sleep(1)
		elif choice_input == '2':
			damage_dealt = p['attacks'][1]['damage']
			e['current_hp'] -= damage_dealt
			print(f'You used {p['attacks'][1]['attack_name']} and dealt {damage_dealt} damage')
			sleep(1)
		else:
			print('Invalid option')
			continue

		if e['current_hp'] <= 0:
			e['current_hp'] = 0
			print(f'{e['name']} has been defeated!')
			sleep(2)
			return True
		else:
			if choice_input in ['1', '2']:
				print(f'------ {e['name'].upper()} TURN ------')
				enemy_attack = choice(e['attacks'])
				enemy_damage = enemy_attack['damage']
				p['current_hp'] -= enemy_damage
				print(f'{e['name']} used {enemy_attack['attack_name']} and dealt {enemy_damage} damage')
				sleep(1)
				if p['current_hp'] <= 0:
					p['current_hp'] = 0
					return False
			else:
				print('Please choose a valid attack next time [1 or 2]!')
				sleep(1)