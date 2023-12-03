import requests
import json


def get_starship_info(starship_name):
    response = requests.get(f"https://swapi.dev/api/starships/?search={starship_name}")

    data = response.json()
    if data['count'] == 0:
        print(f"Корабль {starship_name} не найден.")
        return None

    starship = data['results'][0]

    pilots_info = []
    for pilot_url in starship['pilots']:
        pilot_response = requests.get(pilot_url)
        if pilot_response.status_code == 200:
            pilot_data = pilot_response.json()

            pilot_info = {
                'name': pilot_data['name'],
                'height': pilot_data['height'],
                'weight': pilot_data['mass'],
                'homeworld': pilot_data['homeworld'],
                'homeworld_url': pilot_data['homeworld'],
            }
            pilots_info.append(pilot_info)

    result = {
        'ship_name': starship['name'],
        'starship_class': starship['starship_class'],
        'max_atmosphering_speed': starship['max_atmosphering_speed'],
        'pilots': pilots_info
    }

    print(json.dumps(result, indent=2))
    with open(f"{starship_name}_info.json", 'w') as file:
        json.dump(result, file, indent=2)


get_starship_info("Millennium Falcon")