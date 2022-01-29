import rtmidi

plansza = ['x', 'x', 'o', 'o', 'o', 'o', ' ', 'x', 'o']


def midi_acces():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
        port_name = mo.get_port_name(port_no)
        print("MIDI out:", port_name)
        if port_name.find('Launchpad Mini') > -1:
            midi_port = mo.open_port(port_no)
    return midi_port


def reset():
    midi_acces().send_message([0xB0, 00, 00])  # reset


def get_loc(num):
    pos_dict = {
        1: 96,
        2: 99,
        3: 102,
        4: 48,
        5: 51,
        6: 54,
        7: 0,
        8: 3,
        9: 6, }
    loc = pos_dict.get(num)
    return loc


def display_box(loc, color, hex=0x90):
    light_box = midi_acces().send_message
    loc1 = loc + 1
    loc2 = loc + 16
    loc3 = loc + 17
    light_box([hex, loc, color])
    light_box([hex, loc1, color])
    light_box([hex, loc2, color])
    light_box([hex, loc3, color])


def znaczek_na_kolor(znaczek):
    KOLOR_X = 20
    KOLOR_O = 25
    KOLOR_PUSTAKA = 0
    if znaczek == "x":
        kolor = KOLOR_X
    elif znaczek == 'o':
        kolor = KOLOR_O
    else:
        kolor = KOLOR_PUSTAKA
    return kolor


""" przelatuje po liście dostając pozycję i wartość pola z listy (o,x,_ ) """


def wyswietl_plansze(mylist):
    for i, znaczek in enumerate(mylist, 1):
        """ mamy tu: indeks, wartość """
        kolor_pola = znaczek_na_kolor(znaczek)
        pozycja = get_loc(i)
        display_box(pozycja, kolor_pola)
    return


wyswietl_plansze(plansza)




ask_user = ["A1", "A2", "A3", B1, B2, B3, C1, C2, C3]
design_a_grid()
coin_toss()

ask_user("grid location")

where = 'B2'

if there_is_an_error(where):
    print("try again karol, use google")
    exit()


position = translate_from_text_to_position(where)

put_a_symbol(symbol, position)
