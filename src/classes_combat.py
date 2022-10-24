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
        self.url = url
        self.data = requests.get(self.url).json()
        self.name = self.data["name"]
        self.power = self.getPower()
    
    def getPower(self) -> int:
        return self.data["power"] if self.data["power"] is not None else 0
    
    def __str__(self) -> str:
        return f'MoveName : {self.name} \nPower {self.power}'

    def __eq__(self, moveB : object) -> bool:
        """
        Test the equality with another class Move
        """
        return self.name == moveB.name
    
    def __eq__(self, moveB : str) -> bool:
        """
        Test the equality only with the name of the move
        """
        return self.name == moveB

