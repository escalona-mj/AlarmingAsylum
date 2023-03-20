image splash1 = "gui/splash1.png"
label splashscreen:
    $ renpy.music.play(config.main_menu_music)
    if renpy.variant("small"):
        # if not persistent.autoload == "end":
        $ config.allow_skipping = False
        show splash1 at truecenter:
            zoom 0.35
        with noise
        $ renpy.pause(2.0, hard=True)
        hide splash1 with noise
        show text _("This game is not suitable for children\nor those who are easily disturbed.") at truecenter with noise
        $ renpy.pause(2.0, hard=True)
        hide text with noise
        $ config.allow_skipping = True
        # else:
        #     jump bad_end
    else:
        jump not_for_pc
    return

# label before_main_menu:
#     show text _("{size=+30}Continue{/size}{w}") at truecenter with dissolve
#     return