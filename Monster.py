#!/usr/bin/env python3


class Monster:
    pass


monster = Monster()

print(monster)
print(isinstance(monster, Monster))
print(isinstance(monster, object))


class WalkingMonster(Monster):
    pass


class FlyingMonster(Monster):
    pass


walking_monster = WalkingMonster()
flying_monster = FlyingMonster()

print(walking_monster)
print(isinstance(walking_monster, WalkingMonster))
print(isinstance(walking_monster, Monster))
print(isinstance(walking_monster, object))

print(flying_monster)
print(isinstance(flying_monster, FlyingMonster))
print(isinstance(flying_monster, Monster))
print(isinstance(flying_monster, object))

print(isinstance(walking_monster, FlyingMonster))
print(isinstance(flying_monster, WalkingMonster))
