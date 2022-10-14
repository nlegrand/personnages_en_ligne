# Copyright (c) 2022 Nicolas Legrand <nicolas.legrand@gmail.com>
  
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
  
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS 

import json

class Character:
    """Create a character with the minimum numbers needed"""
    def __init__(self, data):
        self.xp = data['XP']
        self.hp = data['HP']
        str = data['abilities']['STR']
        self.str = str
        if (str == 3):
            meleemod = -3
            opendoors = "1-in-6"
        elif (str >= 4 and str <= 5):
            meleemod = -2
            opendoors = "1-in-6"
        elif (str >= 6 and str <= 8):
            meleemod = -1
            opendoors = "1-in-6"
        elif (str >= 9 and str <= 12): 
            meleemod = 0
            opendoors = "2-in-6"
        elif (str >= 13 and str <= 15): 
            meleemod = 1
            opendoors = "3-in-6"
        elif (str >= 16 and str <= 17): 
            meleemod = 2
            opendoors = "4-in-6"
        elif (str == 18):
            meleemod = 3
            opendoors = "5-in-6"
        self.opendoors = opendoors
        self.meleemod = meleemod

        int = data['abilities']['INT']
        self.int = int
        if (int == 3):
            languages = "Native (broken speech)"
            literacy = "Illeterate"
        elif (int >= 4 and int <= 5):
            languages = "Native"
            literacy = "Illiterate"
        elif (int >= 6 and int <= 8):
            languages = "Native"
            literacy = "Basic"
        elif (int >= 9 and int <= 12): 
            languages = "Native"
            literacy = "Literate"
        elif (int >= 13 and int <= 15): 
            languages = "Native + 1 additional"
            literacy = "Literate"
        elif (int >= 16 and int <= 17): 
            languages = "Native + 2 additional"
            literacy = "Literate"
        elif (int == 18):
            languages = "Native + 3 additional"
            literacy = "Literate"
        self.languages = languages
        self.literacy = literacy

        wis =  data['abilities']['WIS']
        self.wis = wis
        if (wis == 3):
            magicsave = -3
        elif (wis >= 4 and wis <= 5):
            magicsave = -2
        elif (wis >= 6 and wis <= 8):
            magicsave = -1
        elif (wis >= 9 and wis <= 12): 
            magicsave = 0
        elif (wis >= 13 and wis <= 15): 
            magicsave = 1
        elif (wis >= 16 and wis <= 17): 
            magicsave = 2
        elif (wis == 18):
            magicsave = 3
        self.magicsave = magicsave

        dex = data['abilities']['DEX']
        self.dex = dex
        if (dex == 3):
            bonus = -3
            initiative = -2
        elif (dex >= 4 and dex <= 5):
            bonus = -2
            initiative = -1
        elif (dex >= 6 and dex <= 8):
            bonus = -1
            initiative = -1
        elif (dex >= 9 and dex <= 12): 
            bonus = 0
            initiative = 0
        elif (dex >= 13 and dex <= 15): 
            bonus = 1
            initiative = 1
        elif (dex >= 16 and dex <= 17): 
            bonus = 2
            initiative = 1
        elif (dex == 18):
            bonus = 3
            initiative = 2
        self.acmod = bonus
        self.missilemod = bonus
        self.initiative = initiative

        con = data['abilities']['CON']
        self.con = con
        if (con == 3):
            hpmod = -3
        elif (con >= 4 and con <= 5):
            hpmod = -2
        elif (con >= 6 and con <= 8):
            hpmod = -1
        elif (con >= 9 and con <= 12): 
            hpmod = 0
        elif (con >= 13 and con <= 15): 
            hpmod = 1
        elif (con >= 16 and con <= 17): 
            hpmod = 2
        elif (con == 18):
            hpmod = 3
        self.hpmod = hpmod

        cha = data['abilities']['CHA']
        self.cha = cha
        if (int == 3):
            maxretainers = 1
            retainersloyalty = 4
            npcreactions = -2
        elif (int >= 4 and int <= 5):
            maxretainers = 2
            retainersloyalty = 5
            npcreactions = -1
        elif (int >= 6 and int <= 8):
            maxretainers = 3
            retainersloyalty = 6
            npcreactions = -1
        elif (int >= 9 and int <= 12): 
            maxretainers = 4
            retainersloyalty = 7
            npcreactions = 0
        elif (int >= 13 and int <= 15): 
            maxretainers = 5
            retainersloyalty = 8
            npcreactions = 1
        elif (int >= 16 and int <= 17): 
            maxretainers = 6
            retainersloyalty = 9
            npcreactions = 1
        elif (int == 18):
            maxretainers = 7
            retainersloyalty = 10
            npcreactions = 2
        self.maxretainers = maxretainers
        self.npcreactions = npcreactions

        classname = data['class']
        f = open("data/ose/" + classname + ".json", "r", encoding="utf-8")
        classparams = json.load(f)
        for level in classparams['level_progression']:
            if (self.xp >= classparams['level_progression'][level]['XP']):
                mylevel = level
            else:
                break
        self.level = mylevel
        self.thac0 = classparams['level_progression'][mylevel]['THAC0']
        self.saving = {}
        saving = ['D','W','P','B','S']
        for s in saving:
            self.saving[s] = classparams['level_progression'][mylevel]['Saving'][s]
        if "Spells" in classparams['level_progression'][mylevel]:
            self.spells = classparams['level_progression'][mylevel]['Spells']
        matrix = {}
        for i in range(-3, 10):
            tohit = self.thac0 + 1 * -i
            if tohit > 20:
                tohit = 20
            matrix[i] = tohit
        self.attack_value_matrix = matrix
