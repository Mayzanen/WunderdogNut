from PIL import Image
im = Image.open("wunderdog.png").convert("RGB")
pix = im.load()


# piirtämisen suorittava funktio
# y = ylös, v = vasen, a = alas, o = oikea
def piirra(x, y, suunta):
    # Tarkistetaan lopetetaanko piirtäminen
    if pix[x, y] != (51, 69, 169):
        pix[x, y] = (0, 0, 0)
        # suunnan perusteella valitaan seuraava pikseli
        if suunta == "y":
            y -= 1
        elif suunta == "v":
            x -= 1
        elif suunta == "a":
            y += 1
        elif suunta == "o":
            x += 1
        # Tarkistetaan muuttuuko viivan piirtämisen suunta
        if pix[x, y] == (182, 149, 72):
            if suunta == "y":
                suunta = "o"
            elif suunta == "o":
                suunta = "a"
            elif suunta == "a":
                suunta = "v"
            elif suunta == "v":
                suunta = "y"
        elif pix[x, y] == (123, 131, 154):
            if suunta == "y":
                suunta = "v"
            elif suunta == "o":
                suunta = "y"
            elif suunta == "a":
                suunta = "o"
            elif suunta == "v":
                suunta = "a"
        piirra(x, y, suunta)
    else:
        pix[x, y] = (0, 0, 0)


# Loopataan alkuperäinen kuva oikealta alakulmasta alkaen, koska piirtämisien lähtösuunnat ovat vasemmalle ja ylös
# Tarkistetaan jos pikselin kohdalla aloitetaan piirtäminen ja sen suunta
i = 179
j = 59
while j >= 0:
    while i >= 0:
        if pix[i, j] == (7, 84, 19):
            direction = "y"
            piirra(i, j, direction)
        elif pix[i, j] == (139, 57, 137):
            direction = "v"
            piirra(i, j, direction)
        # Jos ei ole itse piirretty tai ohjevärien mukainen pikseli, värjätään se valkoiseksi
        elif (pix[i, j] != (51, 69, 169)) & (pix[i, j] != (182, 149, 72)) & (pix[i, j] != (123, 131, 154)) & (pix[i, j] != (0, 0, 0)):
            pix[i, j] = (255, 255, 255)
        i -= 1
    j -= 1
    i = 179
im.show()
