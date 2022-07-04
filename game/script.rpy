# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define jasmine = npc("jasmine")

# The game starts here.

label start:
    hide window
    show screen testgui
    scene bedroom with dissolve
    ##show screen hud
    #show screen display_stats
    stop music
    jump day

label morning:
    scene bedroom
    window hide
    $ act = "morn"
    call events_run_period()
    ## wake up
    jump day

label day:
    $ act = "day"
    call events_run_period()
    hide All
    jump day

label night:
    scene bedroom night
    window hide

    ##  reset ap, go home,
    $ act = "night"
    call events_run_period()
    #$ apo = sta/24
    python:
        player.stamina.reset()
    scene black with fade
    jump morning

    return
label run_event:
    call events_run_period()
    return
label dialog_loop:
    if player.stamina.cur <=0:
        jump night
    call screen side_tab
    jump dialog_loop
