import requests
import json

# Request to SWAPI API to get information about the Millennium Falcon ship
ship_url = 'https://swapi.dev/api/starships/?search=Millennium Falcon'
ship_response = requests.get(ship_url)
ship_data = ship_response.json()

# Checking the availability of data for the Millennium Falcon ship
ship_results = ship_data['results']
if len(ship_results) > 0:
    ship = ship_results[0]
    ship_name = ship.get('name')
    ship_max_speed = ship.get('max_atmosphering_speed')
    ship_class = ship.get('starship_class')
    ship_pilots = ship.get('pilots', [])
else:
    print("Millennium Falcon ship not found.")
    exit()

# Getting information about the pilots
pilots_info = []
for pilot_url in ship_pilots:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    pilot_name = pilot_data.get('name')
    pilot_height = pilot_data.get('height')
    pilot_mass = pilot_data.get('mass')
    pilot_homeworld = pilot_data.get('homeworld')

    # Getting information about the pilot's homeworld
    homeworld_response = requests.get(pilot_homeworld)
    homeworld_data = homeworld_response.json()
    homeworld_name = homeworld_data.get('name')
    homeworld_url = homeworld_data.get('url')

    pilot_info = {
        'name': pilot_name,
        'height': pilot_height,
        'weight': pilot_mass,
        'homeworld': homeworld_name,
        'homeworld_info_url': homeworld_url
    }
    pilots_info.append(pilot_info)

# Checking the availability of ship and pilots data
if ship_name and ship_max_speed and ship_class and pilots_info:
    # Displaying the information on the screen
    print('Information about the Millennium Falcon ship:')
    print('Name:', ship_name)
    print('Max Speed:', ship_max_speed)
    print('Class:', ship_class)
    print('List of pilots:')
    for pilot in pilots_info:
        print('---')
        for key, value in pilot.items():
            print(key + ':', value)

    # Writing the information to a JSON file
    output_data = {
        'name': ship_name,
        'max_speed': ship_max_speed,
        'class': ship_class,
        'pilots': pilots_info
    }
    with open('millennium_falcon_info.json', 'w') as file:
        json.dump(output_data, file, indent=4)
else:
    print("An error occurred while retrieving information about the Millennium Falcon ship or its pilots.")
