__author__ = 'Leo'

from time import sleep

from event import GameEnd, FireWentOut, CharacterDeath
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

        events = []
        for character in self.characters:
            cevt = character.update()
            if cevt is not None:
                for e in cevt:
                    events.append(e)

        self.characters = [c for c in self.characters if c.is_alive]
        if len(self.characters) == 0:
            events.append(GameEnd(False))

        return events

def recount_events(events):
    if events is not None:
        for e in events:
            print e
            if isinstance(e, GameEnd):
                exit(0)
            sleep(0.5)

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
        print ("============================================")
        for character in game.characters:
            print ("%s (INS: %d, INF: %s) ['%s']" % (character.name,
                                              character.insanity,
                                              character.is_infected,
                                              character.skill_command))
        print ("")
        print ("Fire strength: %d" % game.fire)
        print ("You have %d food rations" % game.food_rations)
        print ("You have %d bullets" % game.bullets)
        print ("You have %d vaccines" % game.vaccines)
        print ("You have %d action points" % game.turn_action_points)

        print ("")
        if game.turn_action_points > 0:
            cmd = raw_input('What would you like to do? ').lower().split(' ')
            print ("")
            sleep(0.5)
            if cmd[0] in game.skill_commands and game.turn_action_points > 0:
                events = game.skill_commands[cmd[0]]()
                recount_events(events)
            elif cmd[0] == 'fire' and game.turn_action_points > 0:
                game.fire = 3
                game.turn_action_points -= 1
                print ("You put some wood in the fire.")
            elif (cmd[0] == 'soothe' and len(cmd[1]) > 0 and
                          game.turn_action_points > 0):
                for c in game.characters:
                    if c.name.lower() == cmd[1]:
                        events = c.soothe()
                        recount_events(events)
                        break
            elif (cmd[0] == 'cure' and len(cmd[1]) > 0 and
                          game.turn_action_points > 0 and game.vaccines > 0):
                for c in game.characters:
                    if c.name.lower() == cmd[1]:
                        events = c.cure()
                        recount_events(events)
                        break
            else:
                print ("You may use character skills, 'fire', "
                       "'soothe <name>', 'cure <name>'")

        sleep(1)

        if game.turn_action_points == 0:
            events = game.update()
            recount_events(events)

if __name__ == '__main__':
    main()