#battle turns
########################################
########################################
init python:
    class char:
        def __init__(self, name = "Name", y = 20, x = 5):
            self.name = name
            self.hp = bars(y)
            self.atk = x
            self.lvl = skill()
            self.skills = []
        def check(self):
            self.lvl.check()
        def rest(self):
            self.hp.reset()

    enemy01 = char(y=100)
    enemy02 = char()
    enemy03 = char(y=10, x=20)
    wchar = char("Will")
    ichar = char("Irma")
    tchar = char("Taranee")
    cchar = char("Cornelia")
    hchar = char("Hay Lin")
########################################
########################################
        ### Lola test

default Obj_lola = npc('Lola')
image I_lola = 'lola1.png'

########################################
########################################
