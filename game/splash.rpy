image splash1 = "gui/splash1.png"
image renpy_logo = "gui/renpy-logo.png"
default persistent.firstLaunch = False
define in_splash = False

label splashscreen:
    # if config.developer == False:
    if renpy.variant("mobile"):
        if persistent.firstLaunch == False:
            show bwAsylum:
                alpha 1.0
            show skip_overlay
            with Dissolve(2.0)
            $ quick_menu = False
            disclaimer "Warning: This game contains elements including themes of cruelty, horror, blood, and other graphic content that are not suitable for all ages."
            disclaimer "It should be played with caution by those who are sensitive to these types of topics."
            disclaimer "Please be aware that playing this game may cause distress, anxiety, or other negative emotions."
            $ in_splash = True
            menu:
                disclaimer "By continuing to play, you acknowledge that you are aware of the content and voluntarily assume any risks associated with playing this game."
                "I agree.":
                    $ persistent.firstLaunch = True
                    $ renpy.pause(1.0, hard=True)
                    hide skip_overlay with Dissolve(1.5)
                    hide bwAsylum
                    $ in_splash = False
                "I would like to stop playing immediately.":
                    $ renpy.quit()
        # $ renpy.music.play(config.main_menu_music)
        # call screen disclaimer with dissolve
        
        show renpy_logo at truecenter:
            yalign 0.45
        show text "Made with Ren'Py" at truecenter:
            yalign 0.60
        with dissolve
        $ renpy.pause(2.0)
        hide renpy_logo
        hide text
        with dissolve
        
        show splash1 at truecenter:
            zoom 0.5
        play sound "audio/sfx/splash.mp3" volume 0.3
        with noise_splash
        $ renpy.pause(2.5)
        hide splash1 with dissolve
        
        show text "This game contains horror elements that\nare not suitable for all ages." at truecenter with dissolve
        $ renpy.pause(3.0)
        hide text with dissolve
    else:
        jump not_for_big_screens
    # else:
    #     return
