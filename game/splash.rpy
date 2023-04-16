image splash1 = "gui/splash1.png"
label splashscreen:
    if config.developer == False:
        $ renpy.music.play(config.main_menu_music)
        if renpy.variant("small"):
            $ config.allow_skipping = False
            show splash1 at truecenter:
                zoom 0.5
            with noise
            $ renpy.pause(2.0, hard=True)
            hide splash1 with noise
            show text _("This game contains horror elements that\nare not suitable for all ages.") at truecenter with noise
            $ renpy.pause(2.5, hard=True)
            hide text with noise
            $ config.allow_skipping = True
        else:
            jump not_for_big_screens
    else:
        return

# label before_main_menu:
#     call screen title_screen
#     return

transform bg_title_screen:
    on show:
        alpha 0.0 zoom 0.95
        easein 1.5 alpha 1 zoom 1

# transform continue_button:
#     alpha 0 yoffset 500
#     easein 2.5 alpha 1 yoffset 0

# screen title_screen():
#     tag menu
#     add "asylum" at bg_title_screen:
#         xalign 0.5
#         yalign 0.5

#     add "particle"
#     add "particle_blur"

#     add "gui/logo.png" at logoease:
#         xalign 0.5
#         yalign 0.25
#         zoom 0.5

#     textbutton "Click to continue" at continue_button:
#         xalign 0.5
#         yalign 0.75
#         action ShowMenu("main_menu")