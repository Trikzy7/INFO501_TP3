'''
File: 5_pokemon_aleatoire.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 23 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

import requests
import random
from src.pokemon import Pokemon

if __name__ == "__main__":

        # ----------------------------------------------- #  
        # 4.1 : Liste de tous les pokémons
        # ----------------------------------------------- #   

        r = requests.get("https://pokeapi.co/api/v2/pokemon")

        data_names = r.json()
        list_names = [aPokemon["name"] for aPokemon in data_names["results"]]

        while data_names["next"] is not None:
                r = requests.get( data_names["next"] )
                data_names = r.json()

                for aPokemon in data_names["results"]:
                        list_names.append(aPokemon["name"])

        print(list_names)

        # ----------------------------------------------- #  
        # 4.2 : Tirer aléatoirement avec une proba uniforme
        # ----------------------------------------------- #  

        size_list_names = len(list_names) - 1
        pokemon_alea = list_names[ random.randint(0, size_list_names) ]
        print("Le pokemon choisi est :")
        print(pokemon_alea)


