import requests
from colorama import Fore, Back, Style
from tabulate import tabulate
from time import sleep 
import os

def clear():
  # clearing the screen for Linux or mac
  if(os.name == 'posix'):
     os.system('clear')
  # screen will be cleared for windows
  else:
     os.system('cls')
     
     
def main():
     
    search = True
    intro = "**** WELCOME TO WORLD OF POKEMON ****"
    # new_intro = intro.center(20, '*')
    print(Fore.YELLOW + intro, "\n")

    while search:        
    
        user_input = input(Fore.CYAN + "Choose a pokemon: ").lower() # Get user input
        clear()
        print("\n")
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input}") # Create dynamic URL
        if req.status_code == 200: 
            # Fetch the data from the URL based on user input
            pokemons = req.json()
            p_type = ", ".join([p["type"]["name"] for p in pokemons["types"]])
            ability = ", ".join([a["ability"]["name"] for a in pokemons["abilities"]])
            
            # Print data into the columns 
            header = [Fore.YELLOW + "Name", "Height", "Weight", "Types", "Abilities"]
            data_info = [[Fore.YELLOW + pokemons["name"], pokemons["height"], pokemons["weight"], p_type, ability]]
            
            print(tabulate(data_info, headers=header, tablefmt='github'))
            print("\n")
            print(Style.RESET_ALL)
            
            user_choice = input(Fore.CYAN + "Would you like to search for another pokemon?(y/n) ").lower()
            if user_choice != "y":
                print("Buy!")
                search = False
            
        else:
            print(Fore.RED + "No pokemon found!\n")
            pok_names = input(Fore.CYAN + "Do you want to see pokemons list?(y/n) \n").lower()
            if pok_names == "y":
                
            # Waiting for data
                clear()
                print("Getting all names in 3")
                sleep(1)
                clear()
                print("Getting all names in 2")
                sleep(1)
                clear()
                print("Getting all names in 1")
                sleep(1)
                
                # Get all pokemon names and print it
                req = requests.get("https://pokeapi.co/api/v2/pokemon?offset=0&limit=1118")
                if req.status_code == 200:
                    pokemons = req.json()["results"]
                list_names = [pokemon["name"] for pokemon in pokemons]
                for a, b, c, d in zip(
                    list_names[::4], list_names[1::4], list_names[2::4], list_names[3::4]
                ):
                    print("{:<30}{:<30}{:<30}{:<30}\n".format(a, b, c, d))
            else:
                print("Buy!")
                search = False
                
if __name__ == "__main__":
    main()

