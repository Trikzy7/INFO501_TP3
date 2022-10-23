'''
File: 2_classe_pokemon.py
Created Date: Wed Sep 28 2022
Author: Ammar Mian
-----
Last Modified: Fri Sep 30 2022
Modified By: Ammar Mian
-----
Copyright (c) 2022 Université Savoie Mont-Blanc
-----
'''

from src.pokemon import Pokemon


if __name__ == "__main__":

    # 2.1 : Création d'un objet de type pokémon
    # Création du pokémon et affichage des infos de base
    # pokemon_name = input("Entrez un pokemon:\n")
    # pokemon = Pokemon(pokemon_name)

    # 2.2 : Afficher les informations avec print
    # print(f'Les informations sur {pokemon_name} sont:')
    # print(pokemon)


    # # 2.3 : Affichage d'informations plus complexes :
    # pokemon.get_color()
    # print(f'Sa couleur est {pokemon.color}')

    # # Appeler le prof (on demandera une requête plus compliquée)

    # # 2.4 : Affichage de l'image du pokémon
    # print("Affichage du sprite :")
    # pokemon.plot_sprite()

    # ------------------------------------------------------------------------------------------------------------------------- #
    # 2.6 : Surcharge des opérateurs : Tester ici des comparaisons entre pokémons sur des attributs différents.
    # ------------------------------------------------------------------------------------------------------------------------- #

    pikachu = Pokemon("pikachu")
    tortank = Pokemon("blastoise")

    pikachu.set_comparison_attribute("height")

    print(f'Pikachu est plus grand que Tortank : {pikachu > tortank}')
    print(f'Pikachu est plus petit que Tortank : {pikachu < tortank}')
    print(f'Pikachu fait la même taille que Tortank : {pikachu == tortank}')

    # ------------------------------------------------------------------------------------------------------------------------- #
    # /\ Appeler le prof pour valider une fois que ça marche. On vous demandera alors de faire une comparaison en plus.
    # ------------------------------------------------------------------------------------------------------------------------- #
