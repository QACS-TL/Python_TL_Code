#! /bin/python
# Name:        tank.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This module describes a class of Tank for
# an online game.
"""
    Derived class of Tank
"""

class Tank:

    __game_version = "1.0.42" # Global class variable.

    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._shells = 20
        self._health = 100
        # Implicitly called so we do not return.

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None

    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, amount):
        self._health -= amount
        return None

    #### EXTRA CODE for SPECIAL METHODS ####

    # Example of Operator overloading.
    def __add__(self, other):
        return self._health + other._health

    # Example of Duck Typing, Quack like a str object.
    def __str__(self):
        return f"Health={self._health}, speed={self._speed}, shells={self._shells}"

    # Example of a GETTER method.
    def get_health(self):
        return self._health

    # Example of a SETTER method.
    def set_health(self, newhealth):
        if newhealth > 100 or newhealth < 0:
            newhealth = 100
        self._health = newhealth
        return None

    #### EXTRA CODE for special PROPERTIES. ####

    # Property function is wrapping the two methods with one name/interface!
    tank_health1 = property(get_health, set_health)

    #### EXTRA CODE for DECORATORS. ####

    # Wrapping the Identical Named Methods with a DECORATOR to indicate when
    # they should be used. DECORATORS = PYTHONIC!
    @property
    def tank_health2(self):
        return self._health

    # Example of a SETTER method.
    @tank_health2.setter
    def tank_health2(self, newhealth):
        if newhealth > 100 or newhealth < 0:
            newhealth = 100
        self._health = newhealth
        return None

    @classmethod
    def get_version(cls):
        return f"Game version {cls.__game_version}"


