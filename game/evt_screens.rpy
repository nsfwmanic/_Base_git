##############################
############################## Testing some junk
## 'texter/tab1.png'
## outerbox, scroll_bar, tab1, tab2, scroller
screen testtext:
    add 'gui/texter/outerbox.png' pos 88,258
    use tabs
    label '[dlabel]' pos dpos
    viewport:
        label 'Coin: [bag.cash]' xalign 0.95
        pos 126, 298
        xysize 730,487
        scrollbars 'vertical'
        mousewheel True
        vbox:
            pass
            if tab == 1:
                use main_action
            if tab == 2:
                pass
            if tab == 3:
                pass
            if tab == 4:
                use testinven
            if tab == 5:
                hbox:
                    textbutton "Buy" action SetVariable("shoptab", 1)
                    null width 50
                    textbutton "Sell" action SetVariable("shoptab", 2)
                if shoptab == 1:
                    use test_shop
                if shoptab == 2:
                    use test_sale
    on "show" action [Show("side_tab2"), Hide("side_tab")]
    on "hide" action [Show("side_tab"), Hide("side_tab2")]
screen main_action:
    for x in player.tags:
        textbutton x.prompt action [SetVariable("act", x.name), Call("run_event")]
screen test_shop:
    for x in testshopitems:
        text '[x.name]  Cost: [x.cost]'
        hbox:
            pass
            if bag.cash >= x.cost:
                textbutton 'Buy' action [SetVariable("targ", x), Call("test_buy")]
            null width 50
            if x in bag.items:
                textbutton 'Sell' action [SetVariable("targ", x), Call("test_sell")]
screen test_sale:
    for x in bag.items:
        text '[x.name]  Cost: [x.sellcost]'
        textbutton 'Sell' action [SetVariable("targ", x), Call("test_sell")]

screen tabs:
    hbox:
        pos 100, 202
        use tab_1
        null width 50
        use tab_2
        null width 50
        use tab_3
        null width 50
        use tab_4
        null width 50
        use tab_5
screen testmain:
    #Main/ action [harvest/ sleep]
    # Group/ people
    # Quests
    # Status
    # Management
    pass
screen testplace:
    #Action [job/ train]
    # 2 people
    # 5 shop
    pass
screen testperson:
    # Talk
    # 3 Quests
    # 4 Status
    # 5 Trade
    pass
screen testgui:
    vbox:
        hbox:
            text "Hp  :  "
            bar:
                xsize 300
                ysize 20
                value AnimatedValue(value=player.hp.cur, range=player.hp.max, delay=1.0, old_value=None)
        hbox:
            text "Sta :  "
            bar:
                xsize 200
                ysize 20
                value AnimatedValue(value=player.stamina.cur, range=player.stamina.max, delay=1.0, old_value=None)
        hbox:
            text "Wp :  "
            bar:
                xsize 100
                ysize 20
                value AnimatedValue(value=player.willpower.cur, range=player.willpower.max, delay=1.0, old_value=None)
screen testinven:
    vbox:
        for x in bag.list:
            $ y = bag.list[x]
            text "[x] : [y]"

screen side_tab:
    imagebutton:
        ypos 300
        idle 'gui/texter/sidetab.png'
        action Show('testtext')
screen side_tab2:
    imagebutton:
        ypos 300
        idle 'gui/texter/sidetab.png'
        action Hide('testtext')


screen tab_1:
    imagebutton idle 'gui/texter/tab2.png' action [SetVariable("tab", 1),SetVariable("dlabel", 'Main')]
screen tab_2:
    imagebutton idle 'gui/texter/tab2.png' action [SetVariable("tab", 2),SetVariable("dlabel", 'People')]
screen tab_3:
    imagebutton idle 'gui/texter/tab2.png' action [SetVariable("tab", 3),SetVariable("dlabel", 'Unused')]
screen tab_4:
    imagebutton idle 'gui/texter/tab2.png' action [SetVariable("tab", 4),SetVariable("dlabel", 'Inventory')]
screen tab_5:
    imagebutton idle 'gui/texter/tab2.png' action [SetVariable("tab", 5),SetVariable("dlabel", 'Shop')]

##############################
############################## Test Expressions
label test_harvest:
    $ bag.add(liquid)
    "You obtained [liquid.name]"

    return
label stam1:
    $ player.stamina.cur -= 1
    return
label test_work:
    $ bag.earn(50)
    return
label testno:
    "You are tired."
    return


label test_quest:
    return
label test_dialog:
    return
label test_buy:
    $ bag.buy(targ)
    return
label test_sell:
    $ bag.sell(targ)
    return
label test_shop:
    #$ bag.buy()
    return
label test_job:
    $ bag.earn(50)
    return
label test_clothes:
    $ bag.buy('')
    return
label test_:
    return

##############################
############################## Labels
label testtext:
    "Test text"
    return
label tester:
    #call screen testtext
    jump dialog_loop

    return


##############################
############################## Python
init python:
    # name, cost = 0, mount = 0
    liquid = item('Liquid', 2000, 100)
    Clothes1 = item('Clothes', 100, 50)
    Clothes2 = item('Clothes', 100, 50)
    Clothes3 = item('Clothes', 100, 50)
    testshopitems = [Clothes1, Clothes2, Clothes3 ]
    targ = liquid
    tab = 1
    shoptab = 1


    test_npc = npc('Test')
    # test_place = place('Place')
    # if tags.num >= 1
    #tags ( name, num = 0)
    class tags:
        def __init__(self, name = 'tag', prompt = 'item', code = 0):
            self.name = name
            self.prompt = prompt
            self.num = code

    dpos = 100, 258
    dlabel = "Main"
    harvest = tags('harvest', 'Harvest Action')
    work = tags('work', 'Work Action')

    # name, stats = base_stats, growth = 0.75
    player = npc()
    player.tags = [harvest, work]

    listing = ['text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text', 'text']
    event("tester", "act == 'day'", event.only(), priority=100)
    event("testtext", "act == 'default'", priority=100)

    event("testno", "player.stamina <= 0.9", event.only(), priority=10)
    event("stam1", "act == 'work'", priority=10)
    event("stam1", "act == 'work'", priority=10)

    event("test_harvest", "act == 'harvest'", priority=100)
    event("test_work", "act == 'work'", priority=100)
