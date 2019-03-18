# launchpad-mini-starter

This is a starter project containing necessary information to display graphics on Novation Launchpad.

## Intro
Launchpad is a USB powered MIDI pad controller. It can be used to control music instruments and make funky lightshows.
You can light up the pads and also get a message when the pad is pressed.
MIDI is a standard for interacting with musical devices. The functions which talk to MIDI devices are provided by your operating system and are accessible from Python, Javascript or any other language

### Setup (Python)
install optional packages required for python-rtmidi:
````bash
sudo apt-get install libasound2-dev
sudo apt-get install libjack-dev
````

Create a virtual environment and install python-rtmidi module. `virtualenv` is used to isolate python modules so they don't pollute your system. `python-rtmidi` is a library for interacting with the system  in order to access MIDI devices.   
````bash
virtualenv XXX
source XXX/bin/activate
pip install python-rtmidi
````

### Basic operation
To light up a button you need to:
1. Connect to the device
2. Send a MIDI message with the position and color


### Example
````python
import rtmidi

mo = rtmidi.MidiOut()
for port_no in range(mo.get_port_count()):
        port_name = mo.get_port_name(port_no)
        print("MIDI out:", port_name)
        if port_name.find('Launchpad Mini') > -1: 
            # or 'Launchpad Pro Standalone Port'
            midi_port = mo.open_port(port_no)
            
# light up the top-right pad with green color 
midi_port.send_message([0x90, 7, 28]) # 7 and 28 are position and color, taken from the docs

# docs: https://global.novationmusic.com/support/downloads/launchpad-programmers-reference-guide
````

further information can be found in the [documentation](https://global.novationmusic.com/support/downloads/launchpad-programmers-reference-guide)

[Launchpad mini pdf](https://github.com/Granjow/launchpad-mini/blob/master/doc/launchpad-programmers-reference.pdf)
