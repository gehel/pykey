import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


from evdev import InputDevice, KeyEvent
from evdev.ecodes import EV_KEY, KEY_ESC


def should_stop(key_event):
    return key_event.keycode == KEY_ESC


class KeyListener:
    """
    Listen to all key strokes and detect when an actual key event should be
    sent
    """
    def __init__(self, handler, mods, virtual_mods, device_name=None):
        if device_name is not None:
            self._device = InputDevice(device_name)
        self._handler = handler
        self._pressed_keys = set()
        self._pressed_count = 0
        self._virtual_mods = frozenset(virtual_mods)
        self._pressed_virtual_mods = set()
        self._mods = frozenset(mods)
        self._pressed_mods = set()
        self._chord_mods = set()

    def print_capabilities(self):
        print self._device.capabilities(verbose=True)

    def start(self):
        self._device.grab()
        for event in self._device.read_loop():
            if event.type == EV_KEY:
                key_event = KeyEvent(event)
                if should_stop(key_event):
                    break
                self.handle_key(key_event)

    def handle_key(self, key_event):
        if key_event.keystate == KeyEvent.key_down:
            if key_event.scancode in self._virtual_mods:
                self._pressed_virtual_mods.add(key_event.scancode)
            elif key_event.scancode in self._mods:
                self._pressed_mods.add(key_event.scancode)
                self._chord_mods.add(key_event.scancode)
            else:
                self._pressed_keys.add(key_event.scancode)
                self._pressed_count += 1
        elif key_event.keystate == KeyEvent.key_up:
            if key_event.scancode in self._virtual_mods:
                self._pressed_virtual_mods.remove(key_event.scancode)
            elif key_event.scancode in self._mods:
                self._pressed_mods.remove(key_event.scancode)
            else:
                self._pressed_count -= 1
                if self._pressed_count == 0:
                    mods = self._chord_mods
                    virtual_mods = self._pressed_virtual_mods
                    chord = self._pressed_keys
                    self._pressed_keys = set()
                    self._chord_mods = set(self._pressed_mods)
                    self._handler.chord_event(
                        mods=mods,
                        virtual_mods=virtual_mods,
                        chord=chord,
                        value=KeyEvent.key_down)
                    self._handler.chord_event(
                        mods=mods,
                        virtual_mods=virtual_mods,
                        chord=chord,
                        value=KeyEvent.key_up)

    def close(self):
        self._device.ungrab()
