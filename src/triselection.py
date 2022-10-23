'''
File: triselection.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
Ce fichier contient les classes et fonctions relatives au tri 
et à la sélection
'''

import pandas as pd

def print_liste(liste_pokemons):
    """Fonction qui affiche les noms des pokemons dans une liste de pokémons

    Parameters
    ----------
    liste_pokemons : list
        liste de pokémons
    """
    string = ""
    for pokemon in liste_pokemons:
        string += pokemon.name + " "
    print("-------------------------------------------------------------------------")
    print(string)


def print_liste_pandas(liste_pokemons, liste_attributs=["id", "name", "height", "weight"]):
    """Fonction qui affiche les informations sou forme de table d'une liste de pokémons

    Parameters
    ----------
    liste_pokemons : list
        liste de pokémons
    liste_attributs : list, optional
        liste d'attributs à afficher, by default ["id", "name", "height", "weight"]
    """    # Iterating through all the attributes and pokemons
    data = []
    for pokemon in liste_pokemons:
        data_pokemon = []
        for attribute in liste_attributs:
            pokemon.verify_attribute(attribute)
            data_pokemon.append( getattr(pokemon, attribute) )
        data.append(data_pokemon)

    # Constructing pandas dataframe to print the database
    data = pd.DataFrame(data)
    data.columns = liste_attributs
    print(data.to_string(index=False))


# ------------------------------------------------------------------------ #
# 3.2 : Réaliser le tri à bulle d'une liste
# ------------------------------------------------------------------------ #
def tri_bulle(tab) -> list:
    """Fonction qui implémente un tri à bulles

    Parameters
    ----------
    tab : list
        liste à trier

    Returns
    -------
    list
        liste triée
    """
    for i in range( len(tab)-1, 0, -1 ):
        for j in range(i):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp

    return tab


# ------------------------------------------------------------------------ #
# 3.3 : Réaliser la classe Tri
# ------------------------------------------------------------------------ #
class Tri():
    """Classe implémentant un tri sur attribut de Pokémons
    """
    def __init__(self, attr, type) -> None:
        self.attr = attr
        self.type = type

    # ------------------------------------------------------------------------ #
    # 3.4 : Réaliser la méthode run
    # ------------------------------------------------------------------------ #
    def run(self, list_pokemon) -> list:
        for pokemon in list_pokemon:
            pokemon.set_comparison_attribute(self.attr)
        list_sorted = tri_bulle(list_pokemon)

        if self.type == "descendant":
            list_sorted.reverse()

        return list_sorted

# ------------------------------------------------------------------------ #
# 3.5 : Réaliser la classe CompositionTri avec la méthode run
# ------------------------------------------------------------------------ #
class CompositionTri():
    """Classe permettant de faire une composition de plusieurs Tris.
    """
    def __init__(self, list_tri):
        self.list_tri = list_tri

    def run(self, list_pokemon) -> list:
        sorted_list = self.list_tri[0].run(list_pokemon)
        prev_attr = self.list_tri[0].attr

        print(len(self.list_tri)-1)

        for tri in self.list_tri[1:]:
            start, end = None, None
            for j in range(len(sorted_list) - 1):
                if getattr(sorted_list[j], prev_attr) == getattr(sorted_list[j + 1], prev_attr):
                    if start is None: start = j
                    end = j+1
                elif start != None:
                    sorted_list[start:end+1] = tri.run(sorted_list[start:end+1])
                    start = None

            prev_attr = tri.attr

        return sorted_list

# ------------------------------------------------------------------------ #
# 3.6 : Réaliser la classe Selection
# ------------------------------------------------------------------------ #
class Selection():
    """Classe implémentant un critère de sélection sur une liste de pokémons.
    """
    def __init__(self, function_critere):
        self.function_critere = function_critere

    # ------------------------------------------------------------------------ #
    # 3.7 : Réaliser la méthode run
    # ------------------------------------------------------------------------ #
    def run(self, list_pokemon) -> list:

        list_filtered = []
        for pokemon in list_pokemon:
            if self.function_critere(pokemon): list_filtered.append(pokemon)

        return list_filtered
# ------------------------------------------------------------------------ #
# 3.5 : Réaliser la classe CompositionTriSelection avec la méthode run
# ------------------------------------------------------------------------ #
class CompositionTriSelection():
    """Classe faisant la composition entre des critères de tri et de sélection.
    """
    def __init__(self, list_tri, list_selection):
        self.list_tri = list_tri
        self.list_selection = list_selection

    def run(self, list_pokemon) -> list:
        list_sorted_filtered = CompositionTri(self.list_tri).run(list_pokemon)

        for selection in self.list_selection:
            list_sorted_filtered = selection.run(list_sorted_filtered)

        return list_sorted_filtered

#
# list_test = [1,4,2,8,6]
# list_test.reverse()
# print( list_test)
#
# l = ["banane", "orange", "abricot"]
#
# print( tri_bulle(l) )

# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]

# reverse the order of list elements
prime_numbers.reverse()


print('Reversed List:', prime_numbers)