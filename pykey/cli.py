from pykey import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright

"""
SHIFT J     V       X     Z    SHIFT
      C     Y       ENT   BKSP
      K     L       SPACE TAB
      Green Red     Red   Green


         G             M
      F     T       N     U
         R             H
      D     E       I     ,
      W     S       O     .
      Q     A       P     B
"""

from evdev.ecodes import *
from pykey.PyKey import PyKey

if __name__ == "__main__":
    no_mods = {
        frozenset([KEY_G]): [KEY_G],
        frozenset([KEY_F]): [KEY_F],
        frozenset([KEY_T]): [KEY_T],
        frozenset([KEY_R]): [KEY_R],

        frozenset([KEY_D]): [KEY_D],
        frozenset([KEY_E]): [KEY_E],
        frozenset([KEY_W]): [KEY_W],
        frozenset([KEY_S]): [KEY_S],
        frozenset([KEY_Q]): [KEY_Q],
        frozenset([KEY_A]): [KEY_A],

        frozenset([KEY_M]): [KEY_M],
        frozenset([KEY_N]): [KEY_N],
        frozenset([KEY_U]): [KEY_U],
        frozenset([KEY_H]): [KEY_H],

        frozenset([KEY_I]): [KEY_I],
        frozenset([KEY_COMMA]): [KEY_L],
        frozenset([KEY_O]): [KEY_O],
        frozenset([KEY_DOT]): [KEY_C],
        frozenset([KEY_P]): [KEY_P],
        frozenset([KEY_B]): [KEY_B],

        frozenset([KEY_T, KEY_N]): [KEY_DOT],
        frozenset([KEY_T, KEY_E]): [KEY_J],
        frozenset([KEY_N, KEY_I]): [KEY_K],
        frozenset([KEY_E, KEY_I]): [KEY_COMMA],
        frozenset([KEY_E, KEY_S]): [KEY_V],
        frozenset([KEY_I, KEY_O]): [KEY_X],
        frozenset([KEY_S, KEY_O]): [KEY_LEFTSHIFT, KEY_SEMICOLON],
        frozenset([KEY_S, KEY_A]): [KEY_Y],
        frozenset([KEY_O, KEY_P]): [KEY_Z],
        frozenset([KEY_A, KEY_P]): [KEY_SEMICOLON]
    }

    orange_mod = {
        frozenset([KEY_N]): [KEY_F2],
    }

    key_combinations = {
        frozenset(): no_mods,
        frozenset([KEY_C]): orange_mod,
    }

    PyKey.print_devices()

    pyKey = PyKey(
        device_name='/dev/input/event8',
        mod_mapping={
            KEY_LEFTSHIFT: KEY_LEFTSHIFT,
            KEY_RIGHTSHIFT: KEY_RIGHTSHIFT,
        },
        key_mapping=key_combinations)
    #pyKey.print_capabilities()
    pyKey.start()
    pyKey.close()
