#! /bin/python
# Name:        instances.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This is an ultra realistic computer game with Tanks!
"""
    Game of Tanks!
"""

import sys
import tank2

def main():
    """ Main game """
    # Instantiate 3 new Tank objects.
    lancelot_tank = tank2.Tank("German", "Tiger")
    arthur_tank = tank2.Tank("British", "Churchill")
    robin_tank = tank2.Tank("American", "Sherman")

    # .. and the game begins.
    lancelot_tank.accel(41)
    arthur_tank.accel(33)

    robin_tank.rotate_left(385)
    robin_tank.accel(15)
    robin_tank.shoot()

    # ..and success!
    lancelot_tank.take_damage(40)
    arthur_tank.take_damage(62)

    print(lancelot_tank.get_health())
    lancelot_tank.set_health(5000)
    lancelot_tank._health = 5000

    arthur_tank.tank_health2 = 30000
    print(type(arthur_tank))
    print(arthur_tank.tank_health1)

    lancelot_tank.tank_health = -1
    # And now for some game visuals! Well at least a print statement!
    print(f"Health of Lancelot's Tank = {lancelot_tank.tank_health}") # Why is this POOR Code?

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)