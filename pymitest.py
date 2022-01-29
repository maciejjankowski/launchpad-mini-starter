
import rtmidi
import time

midiout = rtmidi.MidiOut()

midiout.get_ports()

port = midiout.open_port(1)

i = 0

port.send_message([144, i, 0x010])

heart = [12, 13, 15, 16, 21, 22, 23, 24, 25, 26, 27, 31, 32,
         33, 34, 35, 36, 37, 42, 43, 44, 45, 46, 53, 54, 55, 64]
heart_mini = [0x12, 0x13,     0x15, 0x16,
              0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27,
              0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37,
              0x42, 0x43, 0x44, 0x45, 0x46,
              0x53, 0x54, 0x55,
              0x64]

for i in heart_mini:
    port.send_message([144, i, 0x010])
    time.sleep(0.05)


for i in range(0x80):
    port.send_message([144, i, 0x010])
    time.sleep(0.05)


def get_lightup_msg_pro(position, color=1):
    return [240, 0, 32, 41, 2, 16, 10, position, color, 247]


def get_lightup_msg_mini(position, color=1):
    return [144, position, color]


# midi_port.send_message([0x90, 8, 16])
