# -*- coding: utf-8 -*-
from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

    next = input(">")
    try:
        how_much = int(next)
    except:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print ("""
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    """)
    bear_moved = False


    while True:
        next = input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print ("The baer has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            break
        else:
            print ("I got no idea what that means.")

    gold_room()

def cthulhu_room():
    print ("""
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?
    """)

    next = input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print (why, "Good job!")
    exit(0)

def start():
    print ("""
    You are in a dark room.
    There is a door to your right and left.
    Which one do you take?
    """)

    next = input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
