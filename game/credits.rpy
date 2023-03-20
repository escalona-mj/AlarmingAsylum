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
    call screen dialog(message="Error: The script.rpy is missing or corrupted.\nPlease reinstall the game.", ok_action=MainMenu(confirm=False))
    return

# label bad_end:
#     $ quick_menu = False
#     $ config.skipping = False
#     $ config.allow_skipping = False
#     scene black
#     show poem_end at truecenter
#     $ _dismiss_pause = True
#     pause
#     $ _dismiss_pause = False
#     $ renpy.block_rollback()
#     play sound "audio/sfx/error.wav"
#     call screen dialog(message="Error: The game is corrupted.\nPlease reinstall the game.", ok_action=Quit(confirm=False))
#     return

label not_for_pc:
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    $ _dismiss_pause = False
    $ renpy.block_rollback()
    play sound "audio/sfx/error.wav"
    call screen dialog(message="This game is meant to be played in\nsmall Android devices. Please install it there.", ok_action=Quit(confirm=False))
    return