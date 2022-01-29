def text_scroll(text, color=1, loop=1, speed=15, color_mode=0):

    text_ascii = list(map(ord, list(text)))
    return [ 240, 0, 32, 41, 2, 13, 7, 
            loop, speed, color_mode, color, 
            *text_ascii,
            247]

def light_up(colourspec):
    if type(colourspec) == int:
        colourspec = [colourspec]
    return   [240, 0, 32, 41, 2, 13, 3, *colourspec, 247]