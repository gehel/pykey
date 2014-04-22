from evdev import ecodes as e

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

This mapping based on
http://homepage.ntlworld.com/itimpi/alphagrip.htm#DJW_MAPPING
"""

no_mods = {
    frozenset([e.KEY_G]): [e.KEY_G],
    frozenset([e.KEY_F]): [e.KEY_F],
    frozenset([e.KEY_T]): [e.KEY_T],
    frozenset([e.KEY_R]): [e.KEY_R],

    frozenset([e.KEY_D]): [e.KEY_D],
    frozenset([e.KEY_E]): [e.KEY_E],
    frozenset([e.KEY_W]): [e.KEY_W],
    frozenset([e.KEY_S]): [e.KEY_S],
    frozenset([e.KEY_Q]): [e.KEY_Q],
    frozenset([e.KEY_A]): [e.KEY_A],

    frozenset([e.KEY_M]): [e.KEY_M],
    frozenset([e.KEY_N]): [e.KEY_N],
    frozenset([e.KEY_U]): [e.KEY_U],
    frozenset([e.KEY_H]): [e.KEY_H],

    frozenset([e.KEY_I]): [e.KEY_I],
    frozenset([e.KEY_COMMA]): [e.KEY_L],
    frozenset([e.KEY_O]): [e.KEY_O],
    frozenset([e.KEY_DOT]): [e.KEY_C],
    frozenset([e.KEY_P]): [e.KEY_P],
    frozenset([e.KEY_B]): [e.KEY_B],

    frozenset([e.KEY_T, e.KEY_N]): [e.KEY_DOT],
    frozenset([e.KEY_T, e.KEY_E]): [e.KEY_J],
    frozenset([e.KEY_N, e.KEY_I]): [e.KEY_K],
    frozenset([e.KEY_E, e.KEY_I]): [e.KEY_COMMA],
    frozenset([e.KEY_E, e.KEY_S]): [e.KEY_V],
    frozenset([e.KEY_I, e.KEY_O]): [e.KEY_X],
    frozenset([e.KEY_S, e.KEY_O]): [e.KEY_LEFTSHIFT, e.KEY_SEMICOLON],
    frozenset([e.KEY_S, e.KEY_A]): [e.KEY_Y],
    frozenset([e.KEY_O, e.KEY_P]): [e.KEY_Z],
    frozenset([e.KEY_A, e.KEY_P]): [e.KEY_SEMICOLON]
}

orange_mod = {
    frozenset([e.KEY_N]): [e.KEY_F2],
}

key_combinations = {
    frozenset(): no_mods,
    frozenset([e.KEY_C]): orange_mod,
}

mod_mapping = dict()
mod_mapping[e.KEY_LEFTSHIFT] = e.KEY_LEFTSHIFT
mod_mapping[e.KEY_RIGHTSHIFT] = e.KEY_RIGHTSHIFT
