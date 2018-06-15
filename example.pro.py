import rtmidi

mo = rtmidi.MidiOut()
for port_no in range(mo.get_port_count()):
        port_name = mo.get_port_name(port_no)
        print("MIDI out:", port_name)
        if port_name.find('Launchpad Pro Standalone Port') > -1: 
            # or 'Launchpad Pro Standalone Port'
            midi_port = mo.open_port(port_no)
            
position = 22
color = 1
midi_port.send_message([240, 0, 32, 41, 2, 16, 10, position, color, 247])