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

    growth = 75
    base_stats = {"Wisdom": 15,
    "Charisma": 14,
    "Strength": 10,
    "Dexterity": 12,
    "Constitution": 13,
    "Intelligence": 8}
    ab_score = [15, 14, 13, 12, 10, 8]
    cleric = {"Wisdom": 15,
    "Charisma": 14,
    "Constitution": 13,
    "Strength": 12,
    "Dexterity": 10,
    "Intelligence": 8}
    fighter = {"Strength": 15,
    "Constitution": 14,
    "Dexterity": 13,
    "Intelligence": 12,
    "Wisdom": 10,
    "Charisma": 8}
    rogue = {"Dexterity": 15,
    "Intelligence": 14,
    "Constitution": 13,
    "Strength": 12,
    "Wisdom": 10,
    "Charisma": 8}
    wizard = {"Intelligence": 15,
    "Wisdom": 14,
    "Constitution": 13,
    "Strength": 12,
    "Dexterity": 10,
    "Charisma": 8}
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
## Inventory
    class item:
        def __init__(self, name, cost = 1, sellcost = 1, mount = 1, tags = []):
            self.name = name
            self.cost = cost
            self.sellcost = sellcost
            self.mount = mount # will use later
            self.tags = tags #will use later
    class Inventory:
        def __init__(self, money=0):
            self.cash = money
            self.items = []
            self.list = {}
        def check(self):
            self.list = {}
            for x in self.items:
                if x.name in self.list:
                    self.list[x.name] = 0
                    for y in self.items:
                        if y == x:
                            self.list[x.name] += 1
                else:
                    self.list[x.name] = 1
            return self.list

        def buy(self, item):
            if self.cash >= item.cost:
                self.cash -= item.cost
                self.items.append(item)
                self.check()
                return True
            else:
                return False
        def add(self, item):
            self.items.append(item)
            self.check()
        def remove(self, item):
            self.items.remove(item)
            self.check()
        def sell(self, item):
            self.cash += item.sellcost
            self.items.remove(item)
            self.check()
        def earn(self, amount):
            self.cash += amount
        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False
    bag = Inventory()
## Items
    food = item("food", 10)
## Person
    class npc:
        def __init__(self, name = 'person', stats = base_stats, growth = 0.75):
            self.name       = name
            self.tags = []
            self.lvl = 0
            self.stats       = stats
            self.growth = growth
            self.body = skill()
            self.mind = skill()
            self.charm = skill()
            self.hp = bars(100)
            self.stamina = bars( 4+ (self.growth * self.body.lvl))
            self.willpower = bars( 4+ (self.growth * self.mind.lvl))
        def check(self):
            self.mind.check()
            self.body.check()
            self.stamina.max = self.growth * self.body.lvl
            self.willpower.max = self.growth * self.mind.lvl
            self.lvl = self.mind.lvl + self.body.lvl
        def rest(self):
            self.stamina.reset()
            self.willpower.reset()
## Place
    class Place:
        def __init__(self, name, lab, bg, people = [], acts = [], room = 5):
            self.name = name
            self.tags = []
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
## Leveling skill
    class skill:
        def __init__(self):
            self.cur = 0
            self.max = 100
            self.lvl = 1
        def check(self):
            while self.cur >= self.max:
                self.lvl += 1
                self.cur -= self.max
                self.max = growth * self.lvl
        def plus(self, x):
            self.cur += x
            self.check()
            return self.lvl
    class bars:
        def __init__(self, x = 100):
            self.cur = 0
            self.max = x
            self.reset()
        def reset(self):
            self.cur = self.max



########################################
########################################
        ## ==== End of Setup
init python:
    config.name = _("_Base")
    config.version = "0.0.0"
    build.name = "Test_Edition"
    config.window_icon = "gui/window_icon.png"
    #config.main_menu_music = Mmain
    #config.game_menu_music = space

    _game_menu_screen = "preferences"
    title_image = "gui/overlay/main_menu.png"
    gmenu_image = "gui/overlay/game_menu.png"
    quick_menu = False
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
