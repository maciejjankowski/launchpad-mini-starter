import rtmidi
import time

# from documentation :)
CLEAR_MESSAGE = [176, 0, 0]
COLOR_OFF = 0x0C
COLOR_RED_LOW = 0x0D
COLOR_RED_FULL = 0x0F
COLOR_AMBER_LOW = 0x1D
COLOR_AMBER_FULL = 0x3F
COLOR_YELLOW_FULL = 0x3E
COLOR_GREEN_LOW = 0x1C
COLOR_GREEN_FULL = 0x3C

heart_mini = [0x12, 0x13, 0x15, 0x16, 0x21, 0x22, 0x23,
              0x24, 0x25, 0x26, 0x27, 0x31,
              0x32, 0x33, 0x34, 0x35, 0x36,
              0x37, 0x42, 0x43, 0x44, 0x45,
              0x46, 0x53, 0x54, 0x55, 0x64]


def open_port():
    midi = rtmidi.MidiOut()
    midi_port = None
    for port_no in range(midi.get_port_count()):
        port_name = midi.get_port_name(port_no)
        if port_name.find('Launchpad Pro Standalone Port') > -1:
            midi_port = rtmidi.MidiOut().open_port(port_no)
        elif port_name.find('Launchpad Mini') > -1:
            midi_port = rtmidi.MidiOut().open_port(port_no)

    return midi_port


port = open_port()


def createLightUpMessage(position, color):
    return [144, position, color]


def clear_launchpad():
    port.send_message(CLEAR_MESSAGE)


def light_up(port, position, color):
    message = createLightUpMessage(position, color)
    port.send_message(message)


for position in heart_mini:
    light_up(port, position, COLOR_AMBER_FULL)
