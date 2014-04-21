from cli import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


from evdev import UInput
from evdev.ecodes import EV_KEY


class KeyHandler:

    def __init__(self, mod_mapping, key_mapping):
        self._ui = UInput()
        self._mod_mapping = mod_mapping
        self._key_mapping = key_mapping

    def chord_event(self, mods, virtual_mods, chord, value):
        for key in self.map_chord(virtual_mods, chord):
            self._ui.write(EV_KEY, key, value)
        self._ui.syn()

    def map_chord(self, virtual_mods, chord):
        frozen_vmods = frozenset(virtual_mods)
        if frozen_vmods not in self._key_mapping:
            return []
        current_mapping = self._key_mapping[frozen_vmods]
        frozen_chord = frozenset(chord)
        if frozen_chord not in current_mapping:
            return []
        return current_mapping[frozen_chord]

    def close(self):
        self._ui.close()
