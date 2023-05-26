import requests
import json


def get_ship_info(ship_name):

    ship_url = f'https://swapi.dev/api/starships/?search={ship_name}'
    ship_response = requests.get(ship_url)
    ship_data = ship_response.json()

    ship_results = ship_data['results']
    if len(ship_results) > 0:
        ship = ship_results[0]
        ship_info = {
            'name': ship.get('name'),
            'max_speed': ship.get('max_atmosphering_speed'),
            'class': ship.get('starship_class'),
            'pilots': ship.get('pilots', [])
        }
        return ship_info
    else:
        return None


def get_pilot_info(pilot_url):
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    pilot_info = {
        'name': pilot_data.get('name'),
        'height': pilot_data.get('height'),
        'mass': pilot_data.get('mass'),
        'homeworld': pilot_data.get('homeworld')
    }
    return pilot_info


def get_homeworld_info(homeworld_url):

    homeworld_response = requests.get(homeworld_url)
    homeworld_data = homeworld_response.json()
    homeworld_info = {
        'name': homeworld_data.get('name'),
        'url': homeworld_data.get('url')
    }
    return homeworld_info


def fetch_millennium_falcon_info():

    ship_info = get_ship_info('Millennium Falcon')
    if ship_info is None:
        print("Millennium Falcon ship not found.")
        return

    pilots_info = []
    for pilot_url in ship_info['pilots']:
        pilot_info = get_pilot_info(pilot_url)
        if pilot_info:
            homeworld_info = get_homeworld_info(pilot_info['homeworld'])
            pilot_info['homeworld'] = homeworld_info
            pilots_info.append(pilot_info)

    print('Information about the Millennium Falcon ship:')
    print('Name:', ship_info['name'])
    print('Max Speed:', ship_info['max_speed'])
    print('Class:', ship_info['class'])
    print('List of pilots:')
    for pilot in pilots_info:
        print('---')
        for key, value in pilot.items():
            print(key + ':', value)

    output_data = {
        'name': ship_info['name'],
        'max_speed': ship_info['max_speed'],
        'class': ship_info['class'],
        'pilots': pilots_info
    }
    with open('millennium_falcon_info.json', 'w') as file:
        json.dump(output_data, file, indent=4)


fetch_millennium_falcon_info()
