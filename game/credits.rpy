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
    call screen dialog(message="Error: The script.rpy is missing or corrupted.\nPlease reinstall the game.", ok_action=MainMenu(confirm=False))
    return
# label bad_end:
#     stop music fadeout 2.0
#     window hide
#     show black
#     with fade
#     scene bg meadow blurred
#     with dissolve_scene_full
#     window auto
#     $ quick_menu = False
    
#     m "..."
#     m "..."
#     m "W-What..."
#     m "..."
#     m "This..."
#     m "What is this...?"
#     m "Oh no..."
#     m "No..."
#     m "This can't be it."
#     m "This can't be all there is."
#     m "What is this?"
#     m "What am I?"
#     m "Make it stop!"
#     m "PLEASE MAKE IT STOP!"
#     $ persistent.autoload = "end"
#     $ renpy.quit()

# return