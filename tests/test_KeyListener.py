from pykey import metadata

__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright

import pytest
from mock import MagicMock

from pykey.KeyHandler import KeyHandler
from pykey.KeyListener import KeyListener
from evdev import InputEvent, KeyEvent
from evdev.ecodes import EV_KEY, KEY_LEFTSHIFT, KEY_A


class TestKeyListener:

    def single_key_is_detected(self):
        handler = KeyHandler
        handler.chord_event = MagicMock(name='chord_event')

        self.key_listener = KeyListener(
            device_name=None,
            handler=handler,
            mods=[KEY_LEFTSHIFT],
            virtual_mods=[])

        self.publish_key(KEY_A, 1)
        self.publish_key(KEY_A, 0)

        handler.chord_event.assert_called_once_with(
            set(),
            set(),
            set([KEY_A]), 1)
        handler.chord_event.assert_called_once_with(
            set(),
            set(),
            set([KEY_A]), 0)

    def single_key_with_shift_modifier_is_detected(self):
        handler = KeyHandler
        handler.chord_event = MagicMock(name='chord_event')

        self.key_listener = KeyListener(
            device_name=None,
            handler=handler,
            mods=[KEY_LEFTSHIFT],
            virtual_mods=[])

        self.publish_key(KEY_LEFTSHIFT, 1)
        self.publish_key(KEY_A, 1)

        self.publish_key(KEY_LEFTSHIFT, 0)
        self.publish_key(KEY_A, 0)

        handler.chord_event.assert_called_once_with(
            set([KEY_LEFTSHIFT]),
            set(),
            set([KEY_A]), 1)
        handler.chord_event.assert_called_once_with(
            set([KEY_LEFTSHIFT]),
            set(),
            set([KEY_A]), 0)

    def publish_key(self, key, value):
        self.key_listener.handle_key(KeyEvent(InputEvent(
            sec=0,
            usec=0,
            type=EV_KEY,
            code=key,
            value=value,
        )))
