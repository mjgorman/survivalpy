__author__ = 'Leo'

from time import sleep

from event import GameEnd, FireWentOut
from character import Soldier, Dog, Psychiatrist, Scientist

class Game(object):
    def __init__(self):
        self.days = 30
        self.bullets = 0
        self.food_rations = 0
        self.vaccines = 0
        self.characters = []
        self.skill_commands = {}
        self.turn_action_points = 0
        self.fire = 0

    def update(self):
        self.days -= 1
        if self.days == 0:
            return (GameEnd(True),)

        self.fire -= 1
        if self.fire <= 0:
            return (FireWentOut(), GameEnd(False))

        for character in self.characters:
            character.update()
            if character.is_alive:
                if not character.is_infected:
                    self.turn_action_points += 1
                self.food_rations -= 1
            else:
                del self.skill_commands[character.skill_command]
        self.characters = [c for c in self.characters if c.is_alive]

def main():
    game = Game()
    soldier = Soldier(game)
    dog = Dog(game)
    shrink = Psychiatrist(game)
    spook = Scientist(game)

    while True:
        print ("")
        print ("============================================")
        print ("Day %d" % game.days)
        for character in game.characters:
            print ("%s (INS: %d, INF: %s)" % (character.name,
                                              character.insanity,
                                              character.is_infected))
            print ("\tSkill: %s" % character.skill_command)
        print ("")
        print ("Fire strength: %d" % game.fire)
        print ("You have %d food rations" % game.food_rations)
        print ("You have %d bullets" % game.bullets)
        print ("You have %d action points" % game.turn_action_points)

        cmd = raw_input('What would you like to do? ').lower().split(' ')
        print ("")
        sleep(1)
        if cmd[0] in game.skill_commands and game.turn_action_points > 0:
            events = game.skill_commands[cmd[0]]()
            if events is not None:
                for e in events:
                    print e
        elif cmd[0] == 'fire' and game.turn_action_points > 0:
            game.fire = 3
            print ("You put some wood in the fire.")
        elif (cmd[0] == 'soothe' and len(cmd[1]) > 0 and
                game.turn_action_points > 0):
            for c in game.characters:
                if c.name.lower() == cmd[1]:
                    c.soothe()
                    break
        else:
            print ("You may use character skills, 'fire', or 'soothe <name>'")

        sleep(1)

        if game.turn_action_points == 0:
            events = game.update()
            if events is not None:
                for e in events:
                    print e
                    if isinstance(e, GameEnd):
                        exit(0)

if __name__ == '__main__':
    main()