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

        pass
        
    def choose_random_pokemon(self):
        """
        Random pokemon selection

        @return :   Pokemon object of the random selected pokemon
        """
        pass

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
        pass
    


    # ------------------------------------------------------------------------ #
    # 4.9 : Gérer le combat
    # ------------------------------------------------------------------------ #
    def run_fight(self, latent_time = 2):
        """
        Battle progressing

        @input latent time :    Number of seconds between each display
        """

        pass