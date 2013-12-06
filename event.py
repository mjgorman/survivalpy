__author__ = 'Leo'

class Event(object):
    def __init__(self, id, description):
        self.id = id
        self.description = description

class FoodHuntResult(Event):
    def __init__(self, amount):
        super(FoodHuntResult, self).__init__(1, 'food hunt result')
        self.amount = amount

    def __repr__(self):
        return "Found %d food rations." % self.amount

class BulletsUsed(Event):
    def __init__(self, amount):
        super(BulletsUsed, self).__init__(2, 'bullets used')
        self.amount = amount

    def __repr__(self):
        return "Used %d bullets." % self.amount

class VaccinesMade(Event):
    def __init__(self, amount):
        super(VaccinesMade, self).__init__(3, 'vaccines made')
        self.amount = amount

    def __repr__(self):
        return "Made %d vaccines." % self.amount

class GameEnd(Event):
    def __init__(self, survived):
        super(GameEnd, self).__init__(4, 'game end')
        self.survived = survived

    def __repr__(self):
        if self.survived:
            return "You have survived!"
        else:
            return "You did not survive..."

class FireWentOut(Event):
    def __init__(self):
        super(FireWentOut, self).__init__(5, 'fire went out')

    def __repr__(self):
        return "The fire went out."

class CharacterInfected(Event):
    def __init__(self, character):
        super(CharacterInfected, self).__init__(6, 'character infected')
        self.character = character

    def __repr__(self):
        return "%s has been infected." % self.character.name

class CharacterDeath(Event):
    def __init__(self, character):
        super(CharacterDeath, self).__init__(7, 'character dead')
        self.character = character

    def __repr__(self):
        return "%s has died." % self.character.name