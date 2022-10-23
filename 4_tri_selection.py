'''
File: 4_tri_selection.py
Created Date: Fri Sep 23 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

from src.pokemon import Pokemon
from src.triselection import Tri, Selection, CompositionTriSelection, print_liste_pandas
import time
from tqdm import tqdm


if __name__ == "__main__":
    # ------------------------------------------------------------------------------------------------------------------------- #
    # Lecture de pokémons dans une liste.
    # ------------------------------------------------------------------------------------------------------------------------- #
    pokemon_names = ["charizard", "charmeleon", "charmander", "bulbasaur", "squirtle",
                     "wartortle", "blastoise", "pikachu", "raichu", "pichu", "eevee",
                     "vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon",
                     "ninetales", "lugia", "mewtwo", "mew"]
    print("Lecture des pokméons :")
    print(pokemon_names)
    t_beginning = time.time()
    list_pokemon = [Pokemon(name) for name in tqdm(pokemon_names)]
    print("Lecture effectuee en ", time.time()-t_beginning, " s.\n")

    # Affichage de la liste sans tri
    print("Liste de base :")
    print_liste_pandas(list_pokemon, liste_attributs=["id", "name", "height", "weight", "color"])
    print("\n\n\n")

    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.7 : Crière de sélection simple sur la taille.
    # ------------------------------------------------------------------------------------------------------------------------- #
    def critere_taille(pokemon):
        return pokemon.height > 15
    selection = Selection(critere_taille)
    liste_filtree = selection.run(list_pokemon)
    print("Liste filtree de pokemon de taile > 15m :")
    print_liste_pandas(liste_filtree, liste_attributs=["id", "name", "height", "weight", "color"])
    print("\n\n\n")
    # ------------------------------------------------------------------------------------------------------------------------- #
    # /\ Appeler le prof pour valider une fois que ça marche. On vous demandera alors un autre critère de Sélection.
    # ------------------------------------------------------------------------------------------------------------------------- #



    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.8 : Composition Tri/Sélection : À FAIRE SI VOUS ÊTES EN AVANCE.
    # ------------------------------------------------------------------------------------------------------------------------- #
    def critere_couleur(pokemon):
        return pokemon.color == "red" or pokemon.color == "yellow"
    liste_selection = [Selection(critere_taille), Selection(critere_couleur)]
    liste_tri = [Tri("weight", "ascendant")]
    liste_filtree_triee = CompositionTriSelection(liste_tri, liste_selection).run(list_pokemon)
    print("Liste filtree de pokemon de taile > 0.7m, de couleur jaune ou rouge et triee par poids ascendant :")
    print_liste_pandas(liste_filtree_triee, liste_attributs=["id", "name", "height", "weight", "color"])
    print("\n\n\n")
    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # Appeler le prof pour valider.
    # # ------------------------------------------------------------------------------------------------------------------------- #
