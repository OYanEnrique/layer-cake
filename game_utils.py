import json
from attacks import get_random_attacks
from time import sleep


def show_status(p, e):
    sleep(2)
    print("================================")
    print(f'PLAYER')
    print("--------------------------------")
    print(p['name'])
    print(f"HP: {p['current_hp']} / {p['max_hp']}")
    print('\nVS\n')
    print(e['name'])
    print(f"HP: {e['current_hp']} / {e['max_hp']}")
    print("--------------------------------")
    print(f'1. {p['attacks'][0]['attack_name']} (Damage: {p['attacks'][0]['damage']})')
    print(f'2. {p['attacks'][1]['attack_name']} (Damage: {p['attacks'][1]['damage']})')
    print("================================")

def compare_candy(p, e):
    print(f'---------- {p['name'].upper()} ----------')
    print(f'HP: {p['current_hp']} / {p['max_hp']}')
    print(f'Attacks: {p['attacks'][0]['attack_name']} (Damage: {p['attacks'][0]['damage']}), {p['attacks'][1]['attack_name']} (Damage: {p['attacks'][1]['damage']})')
    sleep(2)
    print('\nVS\n')
    print(f'---------- {e['name'].upper()} ----------')
    print(f'HP: {e['current_hp']} / {e['max_hp']}')
    print(f'Attacks: {e['attacks'][0]['attack_name']} (Damage: {e['attacks'][0]['damage']}), {e['attacks'][1]['attack_name']} (Damage: {e['attacks'][1]['damage']})')
    print('--------------------------------')

def save_game(player_info, level_info):
    save_data = {
        "player": player_info,
        "level": level_info
    }
    with open('savegame.json', 'w') as save_file:
        json.dump(save_data, save_file, indent=4)
    print('Game saved successfully!')
    sleep(2)


def load_game():
    try:
        with open('savegame.json', 'r') as save_file:
            save_data = json.load(save_file)
            print('Game loaded successfully!')
            sleep(2)
            return save_data
    except FileNotFoundError:
        print('No saved game found. Starting a new game...')
        sleep(2)
        return None

def start_new_game(player_template):
    """Handles the creation of a new player character."""
    new_player = player_template.copy()
    player_name = input('Enter your candy character name:\n')
    
    player_attacks = get_random_attacks(2)
    for attack in player_attacks:
        # Give the starting player a small damage bonus
        attack['damage'] = attack['base_damage'] + 2
        
    new_player['attacks'] = player_attacks
    new_player['name'] = player_name
    print(f'Welcome, {player_name}! Starting a new sweet adventure.')
    sleep(2)
    return new_player, 1 # Returns player and starting level

def show_title_screen(player_template):
    """Displays the title screen and handles New Game/Load Game selection."""
    print('\n')
    print('---------- CANDY MAYHEM - THE SWEET ADVENTURE ----------\n')
    sleep(2)

    while True:
        print("\n1. New Game")
        print("2. Load Game")
        print("3. Quit Game")
        choice = input("> ").strip()

        if choice == '1':
            return start_new_game(player_template)
        elif choice == '2':
            saved_data = load_game()
            if saved_data:
                player = saved_data['player']
                level = saved_data['level']
                print(f"Welcome back, {player['name']}! Resuming at level {level}.")
                sleep(2)
                return player, level
        
            else:
                print("\nNo saved game found. Please start a new game.")
                sleep(2)
        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            sleep(2)
            exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")
            sleep(2)