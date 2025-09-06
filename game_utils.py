import json
from attacks import get_random_attacks
from time import sleep
from rich import print

def show_status(p, e):
    sleep(2)
    print("================================")
    print(f'[bold yellow]PLAYER:[/bold yellow] [bold cyan]{p['name']}[/bold cyan]')
    print(f"[bold yellow]HP:[/bold yellow] {p['current_hp']} / {p['max_hp']}")
    print(f'\n[bold red]VS[/bold red]\n')
    print(e['name'])
    print(f"[bold yellow]HP:[/bold yellow] {e['current_hp']} / {e['max_hp']}")
    print("--------------------------------")
    print(f'1. [bold cyan]{p['attacks'][0]['attack_name']} (Damage: {p['attacks'][0]['damage']})[/bold cyan]')
    print(f'2. [bold cyan]{p['attacks'][1]['attack_name']} (Damage: {p['attacks'][1]['damage']})[/bold cyan]')
    print("================================")

def compare_candy(p, e):
    print(f'---------- {p['name']} ----------')
    print(f'[bold yellow]HP:[/bold yellow] {p['current_hp']} / {p['max_hp']}')
    print(f'[bold cyan]Attacks: {p['attacks'][0]['attack_name']} (Damage: {p['attacks'][0]['damage']}), {p['attacks'][1]['attack_name']} (Damage: {p['attacks'][1]['damage']})[/bold cyan]')
    sleep(2)
    print(f'[bold yellow]\nVS\n[/bold yellow]')
    print(f'[bold blue]---------- {e['name']} ----------[/bold blue]')
    print(f'[bold yellow]HP:[/bold yellow] {e['current_hp']} / {e['max_hp']}')
    print(f'[bold cyan]Attacks: {e['attacks'][0]['attack_name']} (Damage: {e['attacks'][0]['damage']}), {e['attacks'][1]['attack_name']} (Damage: {e['attacks'][1]['damage']})[/bold cyan]')
    print('--------------------------------')

def save_game(player_info, level_info):
    save_data = {
        "player": player_info,
        "level": level_info
    }
    with open('savegame.json', 'w') as save_file:
        json.dump(save_data, save_file, indent=4)
    print(f'[bold green]Game saved successfully![/bold green]')
    sleep(2)


def load_game():
    try:
        with open('savegame.json', 'r') as save_file:
            save_data = json.load(save_file)
            print(f'[bold green]Game loaded successfully![/bold green]')
            sleep(2)
            return save_data
    except FileNotFoundError:
        print(f'[bold red]No saved game found. Starting a new game...[/bold red]')
        sleep(2)
        return None

def start_new_game(player_template):
    """Handles the creation of a new player character."""
    new_player = player_template.copy()
    player_name = input(f'Enter your candy character name:\n')
    player_name = f'[bold cyan]{player_name}[/bold cyan]'
    player_attacks = get_random_attacks(2)
    for attack in player_attacks:
        # Give the starting player a small damage bonus
        attack['damage'] = attack['base_damage'] + 2
        
    new_player['attacks'] = player_attacks
    new_player['name'] = player_name
    print(f'Welcome, [bold cyan]{player_name}[/bold cyan]! Starting a new sweet adventure.')
    sleep(2)
    return new_player, 1 # Returns player and starting level

def show_title_screen(player_template):
    """Displays the title screen and handles New Game/Load Game selection."""
    print('\n')
    print(f'[bold blue]---------- CANDY MAYHEM - THE SWEET ADVENTURE ----------\n[/bold blue]')
    sleep(2)

    while True:
        print("1. [bold yellow]New Game[/bold yellow]")
        print("2. [bold yellow]Load Game[/bold yellow]")
        print("3. [bold yellow]Quit Game[/bold yellow]")
        choice = input(f'>').strip()

        if choice == '1':
            return start_new_game(player_template)
        elif choice == '2':
            saved_data = load_game()
            if saved_data:
                player = saved_data['player']
                level = saved_data['level']
                print(f"Welcome back, [bold cyan]{player['name']}[/bold cyan]! Resuming at level {level}.")
                sleep(2)
                return player, level
        
            else:
                print(f"[bold red]\nNo saved game found. Please start a new game.[/bold red]")
                sleep(2)
        elif choice == '3':
            print(f"[bold green]Thanks for playing! Goodbye![/bold green]")
            sleep(2)
            exit()
        else:
            print(f"[bold red]Invalid choice. Please enter 1 or 2.[/bold red]")
            sleep(2)