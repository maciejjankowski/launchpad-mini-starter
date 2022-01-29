import rtmidi
import lpminimk3 as lp
from time import sleep
import random

def main():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find('LPMini') > -1: 
                # or 'Launchpad Pro Standalone Port'
                midi_port = mo.open_port(port_no)
                break
                
    color = 44
    position = 7
    speed = 22
    loop = 1
    print('should light up')
    # midi_port.send_message([0x90, 7, 22])
    # midi_port.send_message(lp.text_scroll('Tobiasz', color=color))

    while True:
        for c in range(1, 4):
            surface = list();
            r = random.randint(64, 127)
            r2 = random.randint(1, 63)
            for i in range(9):
                for j in range(11, 101, 10):
                    # if c | 0x04 | 0x08 | 0x10
                    c = random.randint(r, r + 4)
                    c2 = random.randint(max(r2 - 4, 0), r2)
                    r3 = random.randint(1, 10)
                    if r3 < 3:
                        surface = surface + [1, i+j, c, c2]
                    elif r3 < 5:
                        surface = surface + [2, i+j, c2]
                    else:
                        surface = surface + [0, i+j, c2]
            # print(surface)
            midi_port.send_message(lp.light_up(surface))
            sleep(3)

    # midi_port.send_message(lp.light_up([0, 11, 22, 
    #     0, 23, 24,
    #     0, 25, 40,
    #     0, 57, 50,
    #     ]))

    # midi_port.send_message([145, 81, 19])
    # midi_port.send_message([146, 18, 45])
    sleep(10)




if (__name__ == '__main__'):
    main()