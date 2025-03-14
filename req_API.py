import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)    #gives response code (200 means ok)
    # print(response)
    if response.status_code == 200:
        # print("Success")
        pokemon_data = response.json()  #JSON object
        return pokemon_data

    else:
        print(f"Failed to retrieve, status {response.status_code}")

pokemon_name = "Pikachu"

pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"]}")
    print(f"Id: {pokemon_info["id"]}")
