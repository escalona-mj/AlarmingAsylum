python early:
    achievement_list = (
        # ("Achievement Name", "Locked Description", "Unlocked Description"),
        ("Beginning", "???", "Start a new game."),
        ("Closure", "???", "Complete the story."),
        ("Bad Things Come To Those Who Wait.", "???", "Fail to catch up with the quick time events."),
        ("Rock, Paper, Scissors, Champion!", "???", "Get 3 consecutive points against someone."),
        ("Better Luck Next Time!", "???", "Achieve a bad ending.")
    )

define lockaname = "Achievement Locked."

screen achievements():
    modal True
    use extras_menu(_("Achievements"), scroll="viewport"):

        style_prefix "achievements"
        vbox:
            for aname, lockdesc, unlockdesc in achievement_list:
                frame:
                    xfill True
                    hbox:
                        yalign 0.5

                        if achievement.has(aname):
                            add "medal" size (150, 150) yalign 0.5

                            vbox:
                                yalign 0.5
                                label _("[aname]")
                                text _("[unlockdesc]")

                        else:
                            add "locked_medal" size (150, 150) yalign 0.5

                            vbox:
                                yalign 0.5
                                style_prefix "locked"
                                label _("[lockaname]")
                                text _("[lockdesc]")

                null height 25

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
    background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
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

        if persistent.game_clear:

            textbutton _("Developer Notes") action ShowMenu("dev_notes") alt "Developer Notes"

        else:

            textbutton _("???") action None alt "Locked Option"

    textbutton _("Return"):
        style "return_button"
        action Hide(screen='achievements', transition=noise)


## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.
screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

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

style extras_menu_content_frame:
    left_padding 50
    top_margin 0

    left_margin 60
    right_margin 30

    xsize 1300
    ysize 825