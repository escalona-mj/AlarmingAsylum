label credits:
    hide screen slow_fade_txt
    hide particle_blur onlayer front
    hide particle onlayer front
    scene black
    show text "{i}{size=+35}\"To be continued...\"{/i}"
    with long_dissolve
    $ _dismiss_pause = True
    $ achievement_get("end")
    pause
    $ _dismiss_pause = False
    stop music fadeout 2.0
    hide text with Dissolve(2.0)
    return