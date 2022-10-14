Personnage en ligne is a work in progress right now. The main idea is
to handle table top RPG characters caracteristics crunching. You
should provide some basics unmodified caracteristics and it will
crunch the rest.

It does not check for errors or inconsistency, it is you who should
know the rules and fill the params properly.

I’m working on a first module to manage Old-School Essentials
characters. Only stuff from the
[SRD](https://oldschoolessentials.necroticgnome.com/srd/index.php/Main_Page),
so most of this code fall under the
[OGL](https://oldschoolessentials.necroticgnome.com/srd/index.php/⧼Open_Game_License⧽)
I guess.

You should’nt use this module. I don’t know if I’ll do something
production ready on day.

Test
====
```import json
f = open("examples/ose/fighter_character.json", "r", encoding="utf-8")
caracs = json.load(f)
import ose
fighter = ose.Character(caracs)
fighter.attack_value_matrix
{-3: 20, -2: 20, -1: 20, 0: 19, 1: 18, 2: 17, 3: 16, 4: 15, 5: 14, 6: 13, 7: 12, 8: 11, 9: 10}
fighter.opendoors
'3-in-6'
dir(fighter)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ac', 'attack_value_matrix', 'cha', 'con', 'dex', 'hp', 'initiative', 'int', 'languages', 'literacy', 'magicsave', 'maxretainers', 'melee', 'missile', 'npcreactions', 'opendoors', 'saving', 'str', 'thac0', 'wis', 'xp']
```