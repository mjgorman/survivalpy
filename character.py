__author__ = 'Leo'

from random import randint
from util import roll
from event import (FoodHuntResult, BulletsUsed, VaccinesMade,
    CharacterSoothedResult, CharacterCureResult, CharacterDeath,
    CharacterInfected, BulletsMade, TherapyImpossible)

class Character(object):
    def __init__(self, name, game):
        self.game = game
        self.name = name
        self.insanity = 0
        self.days_infected = 0
        self.is_infected = False
        self.is_alive = True
        self.skills = {}

    def update(self):
        events = []
        if roll(self.game.insanity_rate):
            self.insanity += 1

        if self.is_infected:
            self.days_infected += 1
            if self.days_infected == 3:
                self.is_alive = False
        else:
            if (roll(self.game.infection_rate) and not 
                    self.game.infected_someone_today):
                self.is_infected = True
                self.days_infected = 0
                events.append(CharacterInfected(self))
                self.game.infected_someone_today = True

        if self.insanity == 5:
            self.is_alive = False

        if self.game.food_rations > 0:
            self.game.food_rations -= 1
        else:
            self.is_alive = False

        if self.is_alive:
            if not self.is_infected:
                self.game.turn_action_points += 1
        else:
            del self.game.skill_commands[self.skill_command]
            events.append(CharacterDeath(self))

        return events

    def soothe(self):
        self.game.turn_action_points -= 1
        if roll(90):
            self.insanity -= 1
            return (CharacterSoothedResult(self, True),)
        else:
            return (CharacterSoothedResult(self, False),)

    def cure(self):
        self.game.turn_action_points -= 1
        self.game.vaccines -= 1
        self.is_infected = False
        return (CharacterCureResult(self, True),)

class Soldier(Character):
    def __init__(self, game):
        super(Soldier, self).__init__("Soldier", game)
        self.game.bullets += 20
        self.skills['hunt'] = self.hunt
        self.skills['bullets'] = self.bullets

    def hunt(self):
        self.game.turn_action_points -= 1
        added_food = 0
        bullets_used = 0
        if roll(90) and self.game.bullets > 0:
            bullets_used = randint(1, min(6, self.game.bullets))
            added_food = randint(5, 10)
            self.game.food_rations += added_food
            self.game.bullets -= bullets_used
        return (FoodHuntResult(added_food), BulletsUsed(bullets_used))

    def bullets(self):
        self.game.turn_action_points -= 1
        added_bullets = 0
        if roll(75):
            added_bullets = randint(1, 10)
            self.game.bullets += added_bullets
        return (BulletsMade(added_bullets),)

class Dog(Character):
    def __init__(self, game):
        super(Dog, self).__init__("Fido", game)
        self.skills['scavenge'] = self.scavenge

    def scavenge(self):
        self.game.turn_action_points -= 1
        added_food = 0
        if roll(60):
            added_food = randint(5, 10)
            self.game.food_rations += added_food
        return (FoodHuntResult(added_food),)

class Psychiatrist(Character):
    def __init__(self, game):
        super(Psychiatrist, self).__init__("Psychiatrist", game)
        self.skills['therapy'] = self.therapy

    def therapy(self):
        if self.game.turn_action_points == self.game.characters:
            self.game.turn_action_points = 0
            for c in self.game.characters:
                c.insanity = 0
        else:
            return (TherapyImpossible(),)

class Scientist(Character):
    def __init__(self, game):
        super(Scientist, self).__init__("Scientist", game)
        self.skills['vaccines'] = self.vaccines

    def vaccines(self):
        self.game.turn_action_points -= 1
        vaccines_added = randint(1, 3)
        self.game.vaccines += vaccines_added
        return (VaccinesMade(vaccines_added),)