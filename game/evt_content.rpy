########################################
########################################
    ##  General Events
label introduction:
    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    #$ period = acom    ## the time of day
    #$ act = "room"     ## the action you do

    # Execute the events for the morning.
    #call events_run_period
    $ day = 0
    "Look at this cheap silly room"
    "Is that even a bed"
    "Oh hi there, I'm the voice in your head"
    "This totally doesn't make you crazy"
    "Not that crazy"
    return

label do_stuff:
    "just kind of do stuff, ya know"
    return
label do_talk:
    if cur_aff == 1:
        $ rand1
    elif cur_aff == 2:
        $ rand2
    elif cur_aff == 3:
        $ rand3
    elif cur_aff == 4:
        $ rand4
    elif cur_aff == 5:
        $ rand5
    elif cur_aff == 0:
        $ rand0
########################################
########################################
    ##  Places
label p_home:
    scene bedroom
    "You go home"
    call screen  s1()
    return
label p_gym2:
    scene gym
    "You go to the gym"
    call screen  s1()
    return
label p_gym:
    "You go to the gym"
    call screen gym_screen()
    return
#Event notes
#.depends("") .only() .once() priority=200

########################################
########################################
    #Morning
label M:
    $ day += 1
    centered "Morning Day [day]"
    return
label M0001:
    $ day += 1
    centered "Morning Day [day]"
    centered "Morning"
    "You wake up."
    "Everything is normal"
    return
label M0002:
    $ day += 1
    centered "Morning Day [day]"
    "Yawn"
    "You wake up."
    "Everything is normal"
    return
label M0003:
    $ day += 1
    centered "Morning Day [day]"
    "You wake up."
    "Something seems off"
    return
########################################
########################################
    #Day
label D:
    "What a lovely day"
    return
    
label D0001:
    "What a lovely day"
    return
########################################
########################################
    #Night
label N:
    centered "Night"
    return
label N0001:
    centered "Night"
    return
########################################
########################################
    #Plots
#Start End
#Time over, High stats, time over with high stats
label E:
    ""
    return
########################################
########################################
    #Game stuff
    #xp, lvls, progress, acheiments
    #walking, random events
label xp:
    $ x = 10 + 2
    "You gained [x] xp points."
    return
########################################
########################################
