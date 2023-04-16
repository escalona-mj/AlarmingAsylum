image poem_end = "images/poem_end.png"
label credits:
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    show poem_end at truecenter
    $ _dismiss_pause = True
    pause
    $ _dismiss_pause = False
    $ renpy.block_rollback()
    play sound "audio/sfx/error.wav"
    $ achievement.grant("Better Luck Next Time!")
    if persistent.BadLuck == 0:
        $ renpy.display_notify("Achievement Get:\n\"Better Luck next Time!\"")
        play sound "audio/sfx/notify.ogg"
        $ persistent.BadLuck = 1 
    call screen dialog(message="Error: The script.rpy is missing or corrupted.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
    return

label not_for_big_screens:
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    $ _dismiss_pause = False
    $ renpy.block_rollback()
    play sound "audio/sfx/error.wav"
    call screen dialog(message="This game is meant to be played in small\nAndroid devices. Please install it there.", ok_action=Quit(confirm=False))
    return
