import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


from KeyHandler import KeyHandler
from KeyListener import KeyListener
from evdev import InputDevice, list_devices


class PyKey(object):
    """Keyboard handler for AlphaGripp"""

    def __init__(self, device_name, mod_mapping, key_mapping, print_keys=False):

        self._handler = KeyHandler(mod_mapping, key_mapping)
        virtual_mods = set()

        for v_mods in key_mapping.keys():
            virtual_mods.update(v_mods)

        self._key_listener = KeyListener(
            device_name=device_name,
            handler=self._handler,
            mods=mod_mapping.keys(),
            virtual_mods=frozenset(virtual_mods),
            print_keys=print_keys)

    def start(self):
        self._key_listener.start()

    def close(self):
        self._key_listener.close()
        self._handler.close()


def print_devices():
    devices = map(InputDevice, list_devices())
    for dev in devices:
        print('%-20s %-32s %s' % (dev.fn, dev.name, dev.phys))
