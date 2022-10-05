from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255, 255, 255)
O = (0, 0, 0)
P = (255, 105, 180)
c1 = (220, 220, 220)
o = (O)
c2 = (W)


def trinket_logo(G, Y, B, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, Y, Y, Y, B, G, O, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        Y, Y, Y, Y, Y, B, G, O,
        O, Y, Y, Y, B, G, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def raspi_logo(G, R, O):
    logo = [
        O, G, G, O, O, G, G, O,
        O, O, G, G, G, G, O, O,
        O, O, R, R, R, R, O, O,
        O, R, R, R, R, R, R, O,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R,
        O, R, R, R, R, R, R, O,
        O, O, R, R, R, R, O, O,
    ]
    return logo


def plus(W, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, W, W, O, O, O,
        O, O, O, W, W, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def equals(W, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, W, W, W, W, W, W, O,
        O, W, W, W, W, W, W, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def heart(P, O):
    logo = [
        O, O, O, O, O, O, O, O,
        O, P, P, O, P, P, O, O,
        P, P, P, P, P, P, P, O,
        P, P, P, P, P, P, P, O,
        O, P, P, P, P, P, O, O,
        O, O, P, P, P, O, O, O,
        O, O, O, P, O, O, O, O,
        O, O, O, O, O, O, O, O,
    ]
    return logo


def elephant(o, c1, c2):
    logo = [
        o, o, c1, c1, o, o, o, o,
        o, c1, c1, c1, c1, c1, c1, o,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, c1, c1, c1, c1, c1, c1, c1,
        c1, c2, c2, c1, c1, c1, c1, c1,
        c1, o, c1, c1, c1, c1, c1, c1,
        c1, o, c1, c1, o, c1, c1, o,
        c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo


images = [trinket_logo(G, Y, B, O), trinket_logo(G, Y, B, O), plus(W, O), raspi_logo(G, R, O), raspi_logo(G, R, O),
          equals(W, O), heart(P, O), heart(P, O), elephant(o, c1, c2), ]
count = 0
while True:
    s.set_pixels(images[count % len(images)])
    time.sleep(.75)
    count += 1

def guestUserChoice():
    while True:
        print("""Please select from menu.
        trinket_logo = 1
        plus = 2
        equals = 3
        raspi_logo = 4
        heart = 5
        elephant = 6 
        exit = 0 """)

        try:
        g = int(input('please select from menu: '))
        print(g)
        if 0 <= g and g > 6:
            guestUserChoice(g)
            break
        else:
            print('invalid integer,try again')
            break

BS
