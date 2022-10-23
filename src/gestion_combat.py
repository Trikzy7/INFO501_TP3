'''
File: gestion_combat.py
Created Date: Thu Sep 22 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 23 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''
from pokemon import Pokemon
import random
import time
import requests

class FightManager():
    """
    Class used to manage the battle between two given (or random) pokemons
    """

    r = requests.get("https://pokeapi.co/api/v2/pokemon")

    data_pokemons = r.json()
    list_pokemons = [Pokemon(aPokemon["name"]) for aPokemon in data_pokemons["results"]]

    while data_pokemons["next"] is not None:
        r = requests.get(data_pokemons["next"])
        data_pokemons = r.json()

        for aPokemon in data_pokemons["results"]:
            list_pokemons.append(Pokemon(aPokemon["name"]))

    # ------------------------------------------------------------------------ #
    # 4.7 : Faire le constructeur
    # ------------------------------------------------------------------------ #
    def __init__(self, pok1 = None, pok2 = None, base_url = "https://pokeapi.co/api/v2/") -> None:
        """
        Initialization

        @input pok1 :           Player 1 pokemon (if None, random pokemon is selected) - default : None
        @input pok2 :           Player 2 pokemon (if None, random pokemon is selected) - default : None
        @input base_url :       URL where to find all data (not specific to the list of pokemons)
        """
        
        self.base_url = base_url
        if pok1 is None: self.pok1 = self.choose_random_pokemon()
        if pok2 is None: self.pok2 = self.choose_random_pokemon()

        
    def choose_random_pokemon(self):
        """
        Random pokemon selection

        @return :   Pokemon object of the random selected pokemon
        """
        size_list_pokemons = len(FightManager.list_pokemons) - 1
        return FightManager.list_pokemons[random.randint(0, size_list_pokemons)]

    # ------------------------------------------------------------------------ #
    # 4.8 : Formule de calcul de dégats
    # ------------------------------------------------------------------------ #
    def calculate_damage(self, attack, defense):
        """
        Simplified function for damage calculation

        @input attack :             Attacking power : attacking pokemon attack stat * move power
        @input defense :            Defensive pokemon defense stat

        @return :                   Damage points
        """
        return (3*attack / 50*defense) + 2
    


    # ------------------------------------------------------------------------ #
    # 4.9 : Gérer le combat
    # ------------------------------------------------------------------------ #
    def run_fight(self, latent_time = 2):
        """
        Battle progressing

        @input latent time :    Number of seconds between each display
        """

        nb_alea = random.randint(1, 2)
        first_pokemon_attacking = self.pok1 if nb_alea == 1 else self.pok2
        first_pokemon_attacked = self.pok2 if nb_alea == 1 else self.pok1

        attack_random = first_pokemon_attacking.list_move[
            random.randint(0, len(first_pokemon_attacking.list_move))
        ]
        damage = self.calculate_damage(attack_random.power, first_pokemon_attacked.defense)
        first_pokemon_attacked.take_damage(damage)

        cpt = 0
        print(f'-----------STEP {cpt} \n')
        print(f'--Pokemon en attaque : {first_pokemon_attacking.name}\n')
        first_pokemon_attacking.display_health()
        print(f'Attaque/Puissance: {attack_random.name}/{attack_random.power}')

        print(f'--Pokemon en defense : {first_pokemon_attacked.name}\n')
        first_pokemon_attacked.display_health()

        while first_pokemon_attacking.health != 0 or first_pokemon_attacking.health != 0:
            if cpt%2 == 0:
                attack_random = first_pokemon_attacked.list_move[
                    random.randint(0, len(first_pokemon_attacked.list_move))
                ]
                damage = self.calculate_damage(attack_random.power, first_pokemon_attacking.defense)
                first_pokemon_attacking.take_damage(damage)

                print(f'-----------STEP {cpt} \n')
                print(f'--Pokemon en attaque : {first_pokemon_attacked.name}\n')
                first_pokemon_attacked.display_health()
                print(f'Attaque/Puissance: {attack_random.name}/{attack_random.power}')

                print(f'--Pokemon en defense : {first_pokemon_attacking.name}\n')
                first_pokemon_attacking.display_health()

            else:
                attack_random = first_pokemon_attacking.list_move[
                    random.randint(0, len(first_pokemon_attacking.list_move))]
                damage = self.calculate_damage(attack_random.power, first_pokemon_attacked.defense)
                first_pokemon_attacked.take_damage(damage)

                print(f'-----------STEP {cpt} \n')
                print(f'--Pokemon en attaque : {first_pokemon_attacking.name}\n')
                first_pokemon_attacking.display_health()
                print(f'Attaque/Puissance: {attack_random.name}/{attack_random.power}')

                print(f'--Pokemon en defense : {first_pokemon_attacked.name}\n')
                first_pokemon_attacked.display_health()

            cpt += 1