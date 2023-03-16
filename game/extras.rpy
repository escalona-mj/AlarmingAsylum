python early:
    simple_achievement_list = (
        # ("Achievement Name", "Description when not unlocked", "Description when unlocked"),
        ("Beginning", "???", "Start a new game."),
        ("Closure", "???", "Complete the story."),
        ("Bad Things Come To Those Who Wait.", "???", "Fail to catch up with the quick time events."),
        ("Rock, Paper, Scissors, Champion!", "???", "Get 3 consecutive points against someone."),
        ("Better Luck Next Time!", "???", "Achieve a bad ending.")
    )

screen achievements():

    tag menu
    use extras_menu(_("Achievements"), scroll="viewport"):

        style_prefix "about"
        vbox:
            for aname, lockdesc, unlockdesc in simple_achievement_list:
                hbox:
                    if achievement.has(aname):
                        add "medal"
                        vbox:
                            label _("[aname]")
                            text _("[unlockdesc]")

                    else:
                        add "locked_medal"
                        vbox:
                            label _("[aname]")
                            text _("[lockdesc]")

                null height 35
                    



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
        
    if main_menu:
        textbutton _("Return"):
            style "return_button"
            action Return()
    else:
        textbutton _("Return"):
            style "return_button"
            action ShowMenu("preferences")

    add "gui/phone/overlay/border_bottom.png":
        pos (461, 972)
    add "gui/phone/overlay/border_top.png":
        pos (476, 175)

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.
screen extras_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add "asylum"
        add "particle"
        add "particle_blur"
    else:
        add "gui/overlay/confirm.png"

    frame:
        style "extras_menu_outer_frame"

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

style extras_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/phone/overlay/extras_menu.png"