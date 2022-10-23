'''
File: 3_tri.py
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
from src.triselection import Tri, CompositionTri, print_liste_pandas
import time
from tqdm import tqdm


if __name__ == "__main__":

    # ------------------------------------------------------------------------------------------------------------------------- #
    # 3.1 : Lecture de pokémons dans une liste.
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

    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # 3.4 : Tris simples.
    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # Tri simple ascendant
    # print("Liste triee par nom ascendant :")
    # liste_triee_nom = Tri("name", "ascendant").run(list_pokemon)
    # print_liste_pandas(liste_triee_nom, liste_attributs=["id", "name", "height", "weight", "color"])
    # print("\n\n\n")

    # print(liste_triee_nom)

    # # Tri simple descendant
    # print("Liste triee par taille descendant :")
    # liste_triee_taille = Tri("height", "descendant").run(list_pokemon)
    # print_liste_pandas(liste_triee_taille, liste_attributs=["id", "name", "height", "weight", "color"])
    # print("\n\n\n")

    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # /\ Appeler le prof pour valider une fois que ça marche. On vous demandera alors un autre crière de Tri.
    # # ------------------------------------------------------------------------------------------------------------------------- #



    # # ------------------------------------------------------------------------------------------------------------------------- #
    # #  3.5 : Tri complexes : À FAIRE SI VOUS ÊTES EN AVANCE.
    # # ------------------------------------------------------------------------------------------------------------------------- #
    # print("Liste triee par taille déscendant et poids ascendant")
    # TriTaillePoids = CompositionTri([Tri("height", "descendant"), Tri("weight", "ascendant")])
    # print_liste_pandas(TriTaillePoids.run(list_pokemon), liste_attributs=["id", "name", "height", "weight", "color"])
    # print("\n\n\n")
    # TriTaillePoids.run(list_pokemon)


    print("Liste triee par taille déscendant, poids ascendant et coleur ascendant")
    TriTaillePoidsId = CompositionTri([Tri("height", "descendant"),
                                    Tri("weight", "ascendant"),
                                    Tri("color", "ascendant")])
    print_liste_pandas(TriTaillePoidsId.run(list_pokemon), liste_attributs=["id", "name", "height", "weight", "color"])
    print("\n\n\n")
    # # ------------------------------------------------------------------------------------------------------------------------- #
    # # Appeler le prof si on y arrive pas (on y a passé plus de 1h) ou pour valider.
    # # ------------------------------------------------------------------------------------------------------------------------- #