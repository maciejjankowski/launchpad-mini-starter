import rtmidi

def main():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find('Launchpad Mini') > -1: 
                # or 'Launchpad Pro Standalone Port'
                midi_port = mo.open_port(port_no)
                
    color = 28
    position = 7
    midi_port.send_message([0x90, 7, 28])

if (__name__ == '__main__'):
    main();
else:
    print("wat?", __name__)