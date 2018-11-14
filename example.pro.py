import rtmidi
import time


def light_up(port, position, color):
    port.send_message([
        240, 0, 32, 41, 2, 16, 10,
        position,
        color,
        247]
    )


def main():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
        port_name = mo.get_port_name(port_no)
        print("MIDI out:", port_name)
        if port_name.find('Launchpad Pro Standalone Port') > -1:
            # or 'Launchpad Pro Standalone Port'
            midi_port = mo.open_port(port_no)

    position = 22
    color = 3
    for pad_color in range(14):
        for pad_position in range(11, 19):
            light_up(midi_port, pad_position, pad_color)

            time.sleep(0.04)


if (__name__ == '__main__'):
    main()
