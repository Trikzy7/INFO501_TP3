'''
File: classes_combat.py
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

# ------------------------------------------------------------------------ #
# 4.5 : Faire la classe Move
# ------------------------------------------------------------------------ #
class Move():
    """
    Specific class for move data stockage
    """

    def __init__(self, url) -> None:
        """
        Initialization function
        @input url : url of the move
        """
        pass
    
    def getPower(self) -> int:
        pass
    
    def __str__(self) -> str:
        pass

    def __eq__(self, moveB : object) -> bool:
        """
        Test the equality with another class Move
        """
        pass
    
    def __eq__(self, moveB : str) -> bool:
        """
        Test the equality only with the name of the move
        """
        pass