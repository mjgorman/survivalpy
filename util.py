__author__ = 'Leo'

from random import randint

def roll(cutoff):
    roll = randint(1, 100)
    return roll < cutoff