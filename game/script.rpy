# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    hide window
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
    if apo < 1:
        stop music
        jump night
    hide All
    #show screen gen()
    #call screen s1()
    $ apo -= 1
    ## "Stat change: [bty]"
    ##  call screen movement()
    jump day

label night:
    scene bedroom night
    window hide

    ##  reset ap, go home,
    $ act = "night"
    call events_run_period()
    $ apo = sta/24
    scene black with fade
    jump morning

    return
