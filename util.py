__author__ = 'Leo'

from random import randint

def roll(cutoff):
    roll = randint(1, 100)
    return roll < cutoff

def has_instance(collection, cls):
    for i in collection:
        if instanceof(i, cls):
            return True
    return False