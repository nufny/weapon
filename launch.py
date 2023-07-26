import sys

from readchar import readchar
from random import choice

from util import clear

hp = 5
block = False
enemy_hp = 5
enemy_attack = 1
enemy_actions = ["attack", "buff"]
while enemy_hp > 0 and hp > 0:
    clear()

    # Combat
    enemy_action = choice(enemy_actions)
    info = [
        f"HP: {hp}",
        f"Enemy HP: {enemy_hp}",
        f"Enemy Attack Strength: {enemy_attack}",
        f"Enemy next Action: {enemy_action}",
        "d: Attack Enemy",
        "a: Block",
        "q: Quit"
    ]
    print("\n".join(info))
    k = readchar()
    if k == "q":
        sys.exit(0)
    if k == "d":
        enemy_hp -= 1
    if k == "a":
        block = 1

    # Enemy Turn
    if enemy_action == "attack":
        if not block:
            hp -= enemy_attack
    if enemy_action == "buff":
        enemy_attack += 1

    # Player effects end
    if block:
        block = False

clear()
if hp > 0:
    print("You won!")
elif enemy_hp > 0:
    print("You lost!")
else:
    print("Pyrrhic Victory! But who will defend them next time?")
