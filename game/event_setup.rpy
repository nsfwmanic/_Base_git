init -1 python:
    ## ==== Start of Setup
########################################
########################################
    ##  Stats defaults
    ##  Prevents stat related issues
    bwn         = 1
    brn         = 1
    bty         = 1
    stats       = [bwn, brn, bty]
    sta         = 50
    apo         = 0
    con         = 25
    tol         = 100
    #npc(ba, b2, b3, tol, con, aff_lvl, att_lvl)

    ##  Temp dmg
    dmg         = 0

    ##  Places, People, and Activities
    acom        = "Acommon"
    aloc        = "Alocation"
    aper        = "Aperson"
    period      = acom
    act         = "room"

########################################
########################################
    ## Gallery
    g = Gallery()
   # Step 2. Add buttons and images to the gallery.
    g.locked_background = "lock"
    g.locked_button = "lock" ##make one for this
    g.hover_border = "hov" ##optional, you can just set it to None
    g.idle_border = "idle" ##optional, you can just set it to None

   # A button that contains an image that automatically unlocks.
    #g.button("cg1unlock") ##preview icon
    #g.unlock_image ("cg1")
    g.button("cg1")
    g.image("cg1")
########################################
########################################

########################################
########################################
    ##  Temp talking things maybe
    rand1       = renpy.random.choice(['rand1'])
    rand2       = renpy.random.choice(['rand2'])
    rand3       = renpy.random.choice(['rand3'])
    rand4       = renpy.random.choice(['rand4'])
    rand5       = renpy.random.choice(['rand5'])
    rand0       = renpy.random.choice(['rand0'])
########################################
########################################
    ##  Classes
    ##  Class for People, Places, Events
    ##  Methods to change a person's stats
    ## Method to change player stats
##Inventory
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost
    class Inventory:
        def __init__(self, money=10):
            self.money = money
            self.items = []
        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False
        def earn(self, amount):
            self.money += amount
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
    inven = Inventory()
## Person
    class npc:
        def __init__(self, name, stats = [5,5,5]):
            self.name       = name
            self.stats       = stats
        def change_stat(self,p):
            for s in p:
                x   = 0
                self.stat[x] += s
                x   += 1
## Place
    class Place:
        def __init__(self, name, lab, bg, people = [], acts = [], room = 5):
            self.name = name
            self.lab = lab
            self.bg = bg
            self.room = room
            self.people = people
            self.activities = acts
        def add(self, person):
            if room > 0:
                self.people.append(person)
                self.room -= 1
                return True
            else:
                return False
        def remove(self, person):
            self.people.remove(person)
            self.room += 1
        def has_Person(self, person):
            if person in self.people:
                return True
            else:
                return False
        def has_Activity(self, activity):
            if activity in self.activities:
                return True
            else:
                return False
## Event
    class Activ:
        def __init__(self, name):
            self.name = name
        def Run(self):
            Call("events_run_period")

########################################
########################################
        ## ==== End of Setup
init python:
    config.name = _("_Base")
    config.version = "0.0.0"
    build.name = "Classic Edition"
    config.window_icon = "gui/window_icon.png"
    #config.main_menu_music = Mmain
    #config.game_menu_music = space

    _game_menu_screen = "preferences"
    title_image = "gui/overlay/main_menu.png"
    gmenu_image = "gui/overlay/game_menu.png"
    #quick_menu = False
########################################
########################################
    ##  Register Stats
    # example register_stat("Brawn", "bwn", 5, 100)
    register_stat("Brawn", "bwn", 5, 100)
    register_stat("Brain", "brn", 5, 100)
    register_stat("Beauty", "bty", 5, 100)
    stats = [bwn, brn, bty]
    register_stat("Stamina", "sta", 50, 600)
    register_stat("AP", "apo", 0)
    register_stat("Confidence", "con", 100, 500)
    register_stat("Tolerance", "tol", 0, 100)
