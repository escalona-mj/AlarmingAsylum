default persistent.achievement_list = {
    # "KeyName": [_("Achievement Name"), _("Achievement Description"), Achievement Type],
    "start": [
        _("New Beginnings"),
        _("Start a new game for the very first time."),
        None
        ],

    "end": [
        _("Closure"),
        _("Complete the story normally."),
        None],
    
    "no_time": [
        _("Bad Things Come To Those Who Wait."),
        _("Fail to catch up with the quick time events."),
        None],
    
    "rps_game": [
        _("Master of the Hand Games"),
        _("Emerge victorious in a game of Rock, Paper, Scissors."),
        None],
    
    "rps_game_rock": [
        _("Rock Solid"),
        _("Win three consecutive rounds using only rock."),
        'secret'],
    
    "rps_game_scissors": [
        _("Twin Blades"),
        _("Win three consecutive rounds using only scissors."),
        'secret'],
    
    "rps_game_paper": [
        _("Wrap It Up "),
        _("Win three consecutive rounds using only paper."),
        'secret'],
    
    "bad_end": [
        _("Better Luck Next Time!"),
        _("Achieve a bad ending."),
        None],
    
    "all_bad_end": [
        _("Failure is Not an Option"),
        _("Achieve all bad endings."),
        'secret'],

    }

define lockaname = "Achievement Locked."
define lockdesc = "???"

screen achievements():
    tag menu
    use extras_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"
        vbox:
            box_wrap True
            for k, v in persistent.achievement_list.items():
                #display all achievements except hidden
                if v[2] != 'secret':
                    frame:
                        # background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
                        hbox:
                            yalign 0.5

                            if achievement.has(k):
                                add "medal" size (150, 150) yalign 0.5

                                vbox:
                                    yalign 0.5
                                    label _(v[0])
                                    text _(v[1])

                            else:
                                add "locked_medal" size (150, 150) yalign 0.5

                                vbox:
                                    yalign 0.5
                                    style_prefix "locked"
                                    label _("[lockaname]")
                                    text _("[lockdesc]")
                    null height 25
                #display secret achievement until it is granted
                else:
                    if achievement.has(k):
                        frame:
                            background Frame("gui/achievements/hidden_achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
                            hbox:
                                yalign 0.5
                                add "medal" size (150, 150) yalign 0.5
                                vbox:
                                    yalign 0.5
                                    label _(v[0])
                                    text _(v[1])
                        null height 25
                    else:
                        pass

            

    # add "gui/phone/overlay/border_bottom.png":
    #     pos (461, 972)
    # add "gui/phone/overlay/border_top.png":
    #     pos (476, 175)       
                    
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
    size 35

style locked_text:
    yalign 0.5
    color u'#404040'
    size 35

style achievements_frame:
    # background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding (20, 20, 20, 20)
    xfill True

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.
screen extras_navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5

        spacing 5

        textbutton _("Achievements") action ShowMenu("achievements") alt "Achievements"

        if achievement.has("all_bad_end"):
            textbutton _("Developer Notes") action NullAction() alt "Developer Notes"
            # textbutton _("Developer Notes") action ShowMenu("dev_notes") alt "Developer Notes"

        else:

            textbutton _("???") action None alt "Locked Option"

    textbutton _("Return"):
        style "return_button"
        action Return()


## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.
screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    
    if main_menu:
        use bg_main_menu
        add "gui/overlay/confirm.png"
    else:
        add "gui/overlay/confirm.png"

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    label title

    use extras_navigation
    

# style extras_menu_content_frame:
#     left_padding 50
#     top_margin 0

#     left_margin 60
#     right_margin 30

#     xsize 1300
#     ysize 825