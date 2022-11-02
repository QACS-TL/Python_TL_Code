#! /bin/python
# Name:        demo_strings.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate the different ways of formatting str objects.
"""
    String formatting using concatenation, escape chars, str methods,
    format() method, f-strings and Python 2 syntax.
"""
import sys

def main():
    """ Display planetary objects and distance to Sun in Giga metres """
    planets = { 'Mercury': 57.91,
                'Venus': 108.2,
                'Earth': 149.597870,
                'Mars': 227.94
    }

    # Iterate through the keys in the planets to display distance to sun.
    # Format using str concatenation plus escape chars.  Argh :-(
    for planet in planets.keys():
        print("\t", planet + ": ", str(planets[planet]) + " Gm " + "\t" + str(hex(0xFF)))
    print("-" * 60)

    # Format using using str justification methods. okay :-)
    for planet in planets.keys():
        print(planet.rjust(10) + ": " + str(planets[planet]).rjust(10) + " Gm " + str(hex(0xFF)).center(10))
    print("-" * 60)

    # Format using str.format() method from Py3 onwards.  Better :-)
    for planet in planets.keys():
        print("{0:>10s}: {1:>10.4f} Gm {2:^#10X}".format(planet, planets[planet], 0xFF))
    print("-" * 60)

    # Format using f-strings. From Py3.6 onwards.  Great :-)
    for planet in planets.keys():
        print(f"{planet:>10s}: {planets[planet]:>10.4f} Gm {0xFF:^#10X}")
    print("-" * 60)

    # Format using Python 2 string formatting. Okay :-)
    for planet in planets.keys():
        print("%10s: %10.4f Gm  0x%10X" % (planet, planets[planet], 0xFF))

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)










