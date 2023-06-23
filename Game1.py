#!/bin/python3

# Import library code
from p5 import *
from random import randint


def mouse_pressed():
    if hit_color == outer:
        print('You hit the outer circle, 50 points!')
    elif hit_color == inner:
        print('You hit the inner circle, 200 points!')
    elif hit_color == middle:
        print('You hit the middle, 500 points!')


def shoot_arrow():
    global hit_color
    arrow_x = randint(100, 300)  # Store a random number between 100 and 300
    arrow_y = randint(100, 300)  # Store a random number between 100 and 300
    hit_color = get(arrow_x, arrow_y)
    fill(wood)  # Set the arrow to fill colour to wood
    circle(arrow_x, arrow_y, 15)  # Draw a small circle at random coordinates


def setup():
    # Setup your game here
    size(400, 400)  # width and height
    frame_rate(2)
    no_stroke()


def draw():
    # Things to do in every frame
    global wood, outer, inner, middle
    sky = color(92, 204, 206)  # Red = 92, Green = 204, Blue = 206
    grass = color(149, 212, 122)
    wood = color(145, 96, 51)
    outer = color(0, 120, 180)
    inner = color(210, 60, 60)
    middle = color(220, 200, 0)

    fill(sky)
    rect(0, 0, 400, 250)
    fill(grass)
    rect(0, 250, 400, 150)
    fill(wood)
    triangle(150, 350, 200, 150, 250, 350)
    fill(outer)
    circle(200, 200, 170)
    fill(inner)
    circle(200, 200, 110)
    fill(middle)
    circle(200, 200, 30)

    shoot_arrow()


# Keep this to run your code
run()
