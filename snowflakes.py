#!/usr/bin/env python3
from unicornhatmini import UnicornHATMini
import time
import random
import random

SLEEP_TIME = 0.2
TOTAL_SNOWFLAKES = 8

def move_snowflakes():
    # count snowflakes
    count = count_snowflakes()
    if count <= 0:
        set_random_snowflakes()

    # display current snowflakes
    for y in range(height):
        for x in range(width):
            if snowflake_display[y][x] == 1:
                unicornhatmini.set_pixel(x, y, 255, 255, 255)
            else:
                unicornhatmini.set_pixel(x, y, 0, 0, 50)

    # move snowflakes down
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if snowflake_display[y][x] == 1:
                if y == height - 1:
                    snowflake_display[y][x] = 0
                else:
                    snowflake_display[y][x] = 0
                    snowflake_display[y + 1][x] = 1
            
    unicornhatmini.show()

# count snwoflakes
def count_snowflakes():
    count = 0
    for y in range(height):
        for x in range(width):
            if snowflake_display[y][x] == 1:
                count += 1
    return count

# Imposta 5 pixel casualmente colorati di bianco
# Genera 5 posizioni casuali
def set_random_snowflakes():
    positions = random.sample(range(width * height), TOTAL_SNOWFLAKES)

    # Imposta i pixel alle posizioni casuali a 1
    for position in positions:
        x = position % width
        y = position // width
        snowflake_display[y][x] = 1

# Inizializza il display
unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(0.1)
unicornhatmini.set_rotation(0)
width, height = unicornhatmini.get_shape()

# Pulisce il display
unicornhatmini.clear()

snowflake_display = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


# Imposta tutti i pixel di colore blu scuro
unicornhatmini.set_all(0, 0, 50)


set_random_snowflakes()

# Mostra i pixel
while True:
    move_snowflakes()
    unicornhatmini.show()
    time.sleep(SLEEP_TIME)
    
