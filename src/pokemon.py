'''
File: pokemon.py
Created Date: Wed Sep 14 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
Ce fichier contient la définition de la classe Pokemon
'''

import requests
import random

from .classes_combat import Move
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib.image import imread

class Pokemon():
    """
    Class for a specific pokemon
    """

    base_url = "https://pokeapi.co/api/v2/pokemon/"
    # ------------------------------------------------------------------------ #
    # 2.1 : Faire la méthode init
    # ------------------------------------------------------------------------ #
    def __init__(self, name) -> None:
        """
        Initialization function

        @input name :           Name of the pokemon to generate
        @input base_url :       URL where to find all data (not specific to the list of pokemons)
        """
        self.name = name
        self.data = (requests.get(Pokemon.base_url + name)).json()
        self.id = self.data['id']
        self.weight = self.data['weight']
        self.height = self.data['height']
        self.get_color()
        self.reset_comparison_attribute()

    # ------------------------------------------------------------------------ #
    # 2.2 : Faire la méthode __str__
    # ------------------------------------------------------------------------ #
    def __str__(self) -> str:
        text = f'Name : {self.name} \n' + f'Height : {self.height} \n' + f'Weight : {self.weight}'

        text += f'\nColor : {self.color}' if hasattr(self, "color") else ""
        return text
    # ------------------------------------------------------------------------ #
    # 2.3 : Faire la méthode get_color
    # ------------------------------------------------------------------------ #
    def get_color(self) -> None:
        url_species = self.data['species']['url']
        data_species = (requests.get(url_species)).json()

        self.color = data_species['color']['name']

    # ------------------------------------------------------------------------ #
    # 2.4 : Faire la méthode plot_sprite
    # ------------------------------------------------------------------------ #
    def plot_sprite(self) -> None:
        image_url = self.data['sprites']['front_default']
        response = requests.get(image_url, stream=True)
        img = imread(BytesIO(response.content))

        plt.figure()
        plt.imshow(img, aspect='auto')
        plt.xticks([], [])
        plt.yticks([], [])
        plt.show()

    # ------------------------------------------------------------------------ #
    # 2.5 : Faire les méthodes reset_comparison_attribute et 
    #       set_comparison_attribute
    # ------------------------------------------------------------------------ #

    def set_comparison_attribute(self, attribute):
        self.comparaison_attribute = attribute

    def reset_comparison_attribute(self):
        self.comparaison_attribute = None


    # A LAISSER, utile pour afficher le tableau de plusieurs pokémons
    def verify_attribute(self, attribute=None):
        if attribute == None:
            attribute = self.comparison_attribute

        if attribute is  None:
            raise AttributeError(
                f"No comparison attribute set"
            )
        else:
            if attribute not in self.__dict__.keys():
                raise AttributeError(
                    f"Attribute {attribute} does not exist !"
                )
    # ------------------------------------------------------------------------ #
    # 2.6 : Faire les méthodes pour surcharger les comparaisons
    # ------------------------------------------------------------------------ #

    def __eq__(self, other):
        if self.comparaison_attribute is None: raise AttributeError("Pas d'attribut de comparaison ")
        return getattr(self, self.comparaison_attribute) == getattr(other, self.comparaison_attribute)

    def __ge__(self, other):
        if self.comparaison_attribute is None: raise AttributeError("Pas d'attribut de comparaison ")
        return getattr(self, self.comparaison_attribute) >= getattr(other, self.comparaison_attribute)

    def __le__(self, other):
        if self.comparaison_attribute is None: raise AttributeError("Pas d'attribut de comparaison ")
        return getattr(self, self.comparaison_attribute) <= getattr(other, self.comparaison_attribute)

    def __gt__(self, other):
        if self.comparaison_attribute is None: raise AttributeError("Pas d'attribut de comparaison ")
        return getattr(self, self.comparaison_attribute) > getattr(other, self.comparaison_attribute)

    def __lt__(self, other):
        if self.comparaison_attribute is None: raise AttributeError("Pas d'attribut de comparaison ")
        return getattr(self, self.comparaison_attribute) < getattr(other, self.comparaison_attribute)

    # ------------------------------------------------------------------------ #
    # 4.3 : Infos nécéssaires pour les combats
    # ------------------------------------------------------------------------ #
    def get_stats(self) -> None:
        """
        Collect stats usefull for the fight
        """


        pass

    # ------------------------------------------------------------------------ #
    # 4.6 : Afficher la santé
    # ------------------------------------------------------------------------ #
    def choose_moves(self) -> None:
        """
        Select the 4 moves which the pokemon can use in battle
        """
        pass
    
    # ------------------------------------------------------------------------ #
    # 4.4 : Afficher la santé et la perdre au besoin
    # ------------------------------------------------------------------------ #
    def display_health(self):
        """
        Used to display the actual health level of the pokemon
        """
        pass
    
    def get_HP(self):
        pass
    
    def take_damage(self, HP):
        pass

    def get_def(self):
        pass
    
    def attackMove(self):
        """
        Select a move to use during the battle round

        @return :   Attacking power : move power * pokemon attack
        """
        #Move selection
        pass

