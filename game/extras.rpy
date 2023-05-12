
############# achievement toast
transform achievement_transform:
    on show:
        alpha 0.0
        yoffset -150 alpha 0.0
        easein 0.7 yoffset 0 alpha 1.0
    on hide:
        alpha 1.0
        easeout 0.7 alpha 0.0
        

screen achievement_toast(title, description):
    zorder 500
    frame at achievement_transform:
        xalign 0.0
        yalign 0.0
        padding (20,20,40,20)
        background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
        hbox:
            yalign 0.5
            add "unlocked_medal" size (150, 150) yalign 0.5

            vbox:
                yalign 0.5
                label title style "achievements_label"
                text description style "achievements_text"
    timer 5.0 action Hide("achievement_toast")

init python:
    def achievement_get(ach_id):
        ach = persistent.achievement_list[ach_id]
        if not achievement.has(ach_id):
            achievement.grant(ach_id)
            persistent.unlocked_achievement += 1
            renpy.show_screen(_screen_name='achievement_toast', title=ach[0], description=ach[1])
            renpy.play("audio/sfx/notify.ogg", channel="sound")
        else:
            pass
        
############# achievement list
default persistent.unlocked_achievement = 0 #counts the unlocked achievements
default locked_achievement = len(persistent.achievement_list)

if not persistent.achievement_list:
    default persistent.achievement_list = {
        # "KeyName": [_("Achievement Name"), _("Achievement Description"), Achievement Type],
        "start": [
            _("New Beginnings"),
            _("Start a new game for the very first time.")
            ],

        "end": [
            _("Closure"),
            _("Complete the story normally.")
            ],
        
        "no_time": [
            _("Bad Things Come To Those Who Wait."),
            _("Fail to catch up with the quick time events.")
            ],
        
        "rps_game": [
            _("Master of the Hand Games"),
            _("Emerge victorious in a game of Rock, Paper, Scissors.")
            ],
        
        "rps_game_rock": [
            _("Rock Solid"),
            _("Win three consecutive rounds using only rock."),
            ],
        
        "rps_game_scissors": [
            _("Twin Blades"),
            _("Win three consecutive rounds using only scissors.")
            ],
        
        "rps_game_paper": [
            _("Wrap It Up"),
            _("Win three consecutive rounds using only paper."),
            ],
        
        "bad_end": [
            _("Better Luck Next Time!"),
            _("Achieve a bad ending.")
            ],

        "wall_break": [
            _("Behind the Curtain"),
            _("Uncover a 4th-wall-break joke within the game.")
            ],
        
        "all_bad_end": [
            _("Failure is Not an Option"),
            _("Achieve all bad endings.")
            ],

        }

define lockaname = "Achievement Locked."
define lockdesc = "???"

screen achievements():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu
    if main_menu:
        use bg_main_menu
        add "gui/overlay/confirm.png"
    else:
        add "gui/overlay/confirm.png"
    use extras_navigation
    
    label "Achievements {color=#ffcf00}[persistent.unlocked_achievement]{/color}/[locked_achievement]" style "game_menu_label":
        xalign 0.5
    
        
    viewport:
        xsize 1300
        ysize 750
        xalign 0.5
        yalign 0.55
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        style_prefix "achievements"
        vbox:
            spacing 5
            for k, v in persistent.achievement_list.items():
                frame:
                    background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
                    if achievement.has(k):
                        hbox:
                            yalign 0.5
                            add "unlocked_medal" size (150, 150) yalign 0.5

                            vbox:
                                yalign 0.5
                                label _(v[0])
                                text _(v[1])
                    else:
                        hbox:
                            yalign 0.5
                            add "locked_medal" size (150, 150) yalign 0.5

                            vbox:
                                yalign 0.5
                                style_prefix "locked"
                                label _("[lockaname]")
                                text _("[lockdesc]")
            text "You have unlocked {color=#ffcf00}[persistent.unlocked_achievement]{/color} out of [locked_achievement] achievements.":
                xalign 0.5
                size 45
        
style achievements_vbox is vbox
style achievements_frame is empty 

style achievements_label_text:
    yalign 0.5
    color u'#ffcf00'

style locked_label_text:
    yalign 0.5
    color u'#404040'

style achievements_text:
    yalign 0.5
    size 45

style locked_text:
    yalign 0.5
    color u'#404040'
    size 45

style achievements_frame:
    padding (20, 20, 20, 20)
    xfill True

define dev_note = _p("""
Your dedication to completing the game means the world to us. In our gratitude, please accept this small gift from us.
""")

screen secret_menu():
    tag menu
    if main_menu:
        use bg_main_menu
        add "gui/overlay/confirm.png"
    else:
        add "gui/overlay/confirm.png"
    use extras_navigation

    label "Hall of Completionists" style "game_menu_label":
        xalign 0.5
        
    viewport:
        xsize 1300
        ysize 750   
        xalign 0.5
        yalign 0.55 
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            frame:
                style_prefix "achievements"
                xalign 0.5
                background Frame("gui/achievements/hidden_achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
                xfill True
                hbox:
                    yalign 0.5
                    xalign 0.5
                    add "unlocked_medal" size (150, 150) yalign 0.5
                    
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        label _("Outstanding!"):
                            xalign 0.5
                        text _("You unlocked all achievements!"):
                            xalign 0.5
                    
                    add "unlocked_medal" size (150, 150) yalign 0.5
            text "[dev_note]":
                xalign 0.5
            text "{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Click here to get your gift!{/a}":
                xalign 0.5

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.
screen extras_navigation():

    hbox:
        style_prefix "hnavigation"
        xalign 0.5
        yalign 0.95
        spacing 70

        textbutton _("Achievements") action ShowMenu("achievements") alt "Achievements"

        #for completionists
        if persistent.unlocked_achievement == locked_achievement:
            textbutton _("Hall of Completionists") action ShowMenu("secret_menu") alt "Hall of Completionist"

        else:

            textbutton _("???") action None alt "Locked Option"

    textbutton _("Return"):
        style "return_button"
        action Return()