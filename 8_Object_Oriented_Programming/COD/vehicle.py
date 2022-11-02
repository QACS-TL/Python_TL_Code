#! /bin/python
# Name:        vehicle.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This module describes a generic Vehicle class.
"""
    BASE class of Vehicle
"""

class Vehicle:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0

    def accel(self, increase):
        self._speed += increase
        return None

    def decel(self, decrease):
        self._speed -= decrease
        return None
