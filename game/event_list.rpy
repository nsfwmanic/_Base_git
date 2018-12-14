init python:
########################################
########################################
    ## TODO Register events
    ## Register events
    # example event("introduction", "act == 'day'", event.once(), event.only())
    event("introduction", "act == 'day'", event.once(), event.only())
    #event("acoverseWelcome", "act == 'day'", event.once(), event.only())
    event("M", "act == 'morn'", event.once(), event.only(), priority=201)
    event("N", "act == 'night'", event.once(), event.only(), priority=201)

    ##Gerneal Events
    event("D", "act == 'day'", event.once(), priority=200)
    event("N", "act == 'night'", priority=200)
    event("M0002", "act == 'morn'", event.choose_one('morn'), priority=200)
    event("M0003", "act == 'morn'", event.choose_one('morn'), priority=200)

    ##  Going places
    event("p_home", "act == 'home'")
    event("p_gym", "act == 'gym'")

    ##  Action events
    event("do_stuff", "act == 'stuff'")
########################################
########################################
