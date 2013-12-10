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

class CharacterSoothedResult(Event):
    def __init__(self, character, success):
        super(CharacterSoothedResult, self).__init__(8, 'character soothed')
        self.character = character
        self.success = success

    def __repr__(self):
        if self.success:
            return "%s has calmed down." % self.character.name
        else:
            return "%s refuses to calm down." % self.character.name

class CharacterCureResult(Event):
    def __init__(self, character, success):
        super(CharacterCureResult, self).__init__(9, 'character cured')
        self.character = character
        self.success = success

    def __repr__(self):
        if self.success:
            return "%s has been cured." % self.character.name
        else:
            return "The cure didn't work on %s" % self.character.name

class MonsterAttack(Event):
    def __init__(self, food_stolen):
        super(MonsterAttack, self).__init__(10, 'monster attack')
        self.food_stolen = food_stolen

    def __repr__(self):
        return ("You were attacked by monsters. You lost %d food rations" %
               self.food_stolen)

class RadioRepairProgress(Event):
    def __init__(self):
        super(RadioRepairProgress, self).__init__(11, 'radio repair progress')

    def __repr__(self):
        return "Radio repair in progress..."

class RadioRepairResult(Event):
    def __init__(self, result):
        super(RadioRepairResult, self).__init__(12, 'radio repair result')
        self.result = result

    def __repr__(self):
        return "Radio repaired: %s" % self.result

class BulletsMade(Event):
    def __init__(self, amount):
        super(BulletsMade, self).__init__(13, 'bullets made')
        self.amount = amount

    def __repr__(self):
        return "Made %d bullets." % self.amount

class TherapyImpossible(Event):
    def __init__(self):
        super(TherapyImpossible, self).__init__(14, 'therapy impossible')

    def __repr__(self):
        return "Therapy not possible. Need all action points."