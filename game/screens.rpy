﻿################################################################################
## Initialization
################################################################################

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    color u'#ffcf00'
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound "audio/sfx/click.ogg"
    hover_sound "audio/sfx/hover.ogg"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

screen dialog(message, ok_action):
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"


        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"# at textdissolve
            
        text what id "what"# at textdissolve
    use quick_menu
    
    


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
    

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name")
    xalign gui.name_xalign
    color '#ffffff'
    yalign 0.5
    xoffset 100

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing 10

image ctc:
    xalign 0.9 yalign 0.95 alpha 0.0 subpixel True
    "gui/ctc/ctc.png"
    block:
        easeout 0.25 alpha 1.0 yoffset 0
        easein 0.25 alpha 0.5 yoffset -5
        repeat

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            # xalign gui.dialogue_text_xalign
            # xpos gui.dialogue_xpos
            # xsize gui.dialogue_width
            yalign 0.5
            # if renpy.variant("small"):
            #     ypos 0.5
            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

# screen choice(items):
#     style_prefix "choice"
#     vbox:
#         for i in items:
#             textbutton i.caption action i.action

define in_splash = False

screen choice(items):
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    
    if in_splash == False:
        style_prefix "choice"
        vbox at choice_transform:
            for i in items:
                textbutton i.caption action i.action
    
    #for splash only
    elif in_splash == True:
        style_prefix "custom_choice"
        vbox at choice_transform:
            for i in items:
                textbutton i.caption action i.action

transform choice_transform:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.25 alpha 0.0


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/sfx/click.ogg"
    hover_sound "audio/sfx/hover.ogg"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    # outlines [ (3, "#00000049", 2, 2) ]


style custom_choice_vbox is vbox
style custom_choice_button is button
style custom_choice_button_text is button_text

style custom_choice_vbox:
    xalign 0.5
    yalign 0.75
    spacing 10

style custom_choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/sfx/click.ogg"
    hover_sound "audio/sfx/hover.ogg"

style custom_choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    # outlines [ (3, "#00000049", 2, 2) ]

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100
    #hbox:
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0

            #textbutton _("Back") action Rollback()

            textbutton _("History") action ShowMenu('history')
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            textbutton _("Settings") action ShowMenu('preferences')

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")

default quick_menu = True

default quick_menu_frame = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    # properties gui.button_properties("quick_button")
    activate_sound "audio/sfx/click.ogg"

style quick_button_text:
    font gui.interface_text_font
    properties gui.button_text_properties("quick_button")
    # outlines [ (absolute(1.5), "#0000007c", absolute(0), absolute(0)) ]


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

transform menu_appear:
    on show:
        alpha 0 yoffset 500
        pause 2.0
        easein 1.5 alpha 1 yoffset 0
        
screen navigation():
    if renpy.get_screen("main_menu"):
        hbox at menu_appear:
            style_prefix "hnavigation"

            xalign 0.5
            yalign 0.95
            spacing 70

            textbutton _("Start") action (Show(screen='name_input', transition=noise, message="What is your name?", ok_action=Function(FinishEnterName), back_action=Hide(screen='name_input', transition=noise)))

            textbutton _("Load") action ShowMenu("load")

            textbutton _("Settings") action ShowMenu("preferences")

            textbutton _("Extras") action ShowMenu("achievements")

            textbutton _("About") action ShowMenu("about")

            if config.developer == True:
                textbutton _("Debug") action Start("debug")
            else:
                pass

            # if renpy.variant("pc"):

            #     ## The quit button is banned on iOS and unnecessary on Android and
            #     ## Web.
            textbutton _("Quit") action Quit(confirm=main_menu)

    else:
        vbox:
            style_prefix "navigation"
            xpos gui.navigation_xpos
            yalign 0.5

            spacing 5

            if not main_menu:
                textbutton _("History") action ShowMenu("history")

            if not main_menu:
                textbutton _("Save Game") action ShowMenu("save")

            textbutton _("Load Game") action ShowMenu("load")

            textbutton _("Settings") action ShowMenu("preferences")

            if main_menu:
                textbutton _("Extras") action ShowMenu("achievements")

            textbutton _("About") action ShowMenu("about")

            if not main_menu:
                textbutton _("Main Menu") action MainMenu()

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("Quit") action Quit(confirm=True)

    if _in_replay:

        textbutton _("End Replay") action EndReplay(confirm=True)



    #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        ## Help isn't necessary or relevant to mobile devices.
        #textbutton _("Help") action ShowMenu("help")


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style hnavigation_button is gui_button
style hnavigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font gui.game_menu_label_font

style hnavigation_button_text:
    xalign 0.5
    font gui.game_menu_label_font


screen bg_main_menu():
    add "graybg"

    add "moon":
        at transform:
            on show:
                alpha 0.0
                pause 1.0
                linear 1.5 alpha 1.0

    add "bird1"
    add "bird2"
    add "bird3"

    add "house":
        at transform:
            on show:
                yoffset 900
                pause 2.0
                easein 1.5 yoffset 0
    
    add "trees":
        at transform:
            on show:
                yoffset 900
                pause 2.0
                easein 1.5 yoffset 0

    add "grass":
        at transform:
            on show:
                yoffset 600
                pause 2.0
                easein 1.5 yoffset 0
                
    # add "grunge"

    add "gui/overlay/confirm.png":
        alpha 0.5
    
    if renpy.get_screen("main_menu"):
        add "logo":
            xalign 0.5
            yalign 0.25
            at transform:
                on show:
                    alpha 0.0
                    pause 4.0
                    linear 0.7 alpha 1.0

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu     

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    
    tag menu
    use bg_main_menu
    # add gui.main_menu_background

    ## This empty frame darkens the main menu.
    # frame:
    #     style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation
    
    add "menuFrame"
    
    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        use bg_main_menu
        add "gui/overlay/confirm.png":
            alpha 0.75

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

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    right_margin 30
    top_margin 15
    xfill True
    ysize 825

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 250

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
    font gui.game_menu_label_font

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t!u]":
                xalign 0.5
            text _("Version [config.version!t]\n"):
                xalign 0.5

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is text

style about_label_text:
    # size gui.label_text_size
    size 100
    font "fonts/Rayando-xj18.ttf"


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu

    use file_slots(_("Save"))


screen load():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y\n%H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("{font=/fonts/Co2-wdOx.ttf}<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _("{font=/fonts/Co2-wdOx.ttf}>") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    font gui.game_menu_label_font

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

init python:
    renpy.music.register_channel("ambient", mixer="ambient", loop=True, tight=False)

screen preferences():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        
        vbox:
            text _("Text Settings"):
                font gui.game_menu_label_font
                xalign 0.5
            null height 25
            hbox:
                spacing 50

                # if renpy.variant("pc") or renpy.variant("web"):
                
                # if config.developer == True:
                #     vbox:
                #         style_prefix "radio"
                #         label _("Display")
                #         textbutton _("Window") action Preference("display", "window")
                #         textbutton _("Fullscreen") action Preference("display", "fullscreen")

                # vbox:
                #     style_prefix "radio"
                #     label _("Rollback Side")
                #     textbutton _("Disable") action Preference("rollback side", "disable")
                #     textbutton _("Left") action Preference("rollback side", "left")
                #     textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    xsize 690
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle"):
                        tooltip "Skips the dialogue regardless if seen or unseen."
                    textbutton _("After Choices") action Preference("after choices", "toggle"):
                        tooltip "Keeps skipping, even on choices."

                vbox:
                    style_prefix "slider"
                    xsize 500
                    label _("Text Speed")
                    bar value Preference("text speed"):
                        tooltip "The speed of the in-game dialogue text."

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time"):
                        tooltip "The speed of the automation per dialogue.\n(The lower it is, the faster it gets.)"

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            # null height 400

            text _("Music Settings"):
                font gui.game_menu_label_font
                xalign 0.5
            null height 25
            hbox:
                style_prefix "slider"
                spacing 50
                
                vbox:
                    xsize 690
                    if config.has_music:
                        label _("BGM Volume")
                        bar value Preference("music volume"):
                            tooltip "The loudness of background music throughout the game."

                        label _("Ambient Volume")
                        bar value Preference("ambient volume"):
                            tooltip "The loudness of ambient music throughout the game."
                vbox:
                    xsize 500
                    if config.has_sound:

                        label _("Sound Volume")

                        vbox:
                            bar value Preference("sound volume"):
                                tooltip "The loudness of sound effects throughout the game."

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                                
                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            tooltip "Mute all sounds."
                            style "mute_all_button"
                
            null height 25

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                padding (30,20,20,20)
                text tooltip style "tooltip_hover":
                    size 45

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_text:
    font gui.interface_text_font
    size 35
style check_button is empty
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_text:
    font gui.interface_text_font
    size 35
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    left_padding 75
    activate_sound "audio/sfx/click.ogg"
    hover_sound "audio/sfx/hover.ogg"
    # properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    idle_color u'#929292'
    hover_color u'#fff'
    selected_color u'#fff'
    size 60
    # properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

# screen history():

#     tag menu

#     predict False

#     add "gui/overlay/confirm.png"

#     frame:
#         background None

#         style_prefix "history"

#         ## If you have a custom image you want to use for the screen, you can set it as
#         ## a Frame below.
#         # background Frame(["gui/frame.png"], gui.history_frame_borders, tile=True)

#         ## Style this as needed in the style definitions
#         label _("History")

#         ## Using margin properties will allow the screen to automatically adjust should
#         ## you choose to use a different resolution than 1080p, and will always be centered. 
#         ## You can also resize the screen using "xmaximum", "ymaximum", or "maximum(x,y)"
#         ## if desired, but you will need to use "align(x,y)" to manually position it.

#         ## xmargin essentially combines the left_margin and right_margin properties
#         ## and sets them to the same value
#         xmargin 200

#         ## ymargin essentially combines the top_margin and bottom_margin properties
#         ## and sets them to the same value
#         ymargin 50

#         ## xpadding essentially combines the left_padding and right_padding properties
#         ## and sets them to the same value
#         xpadding 50

#         ## ypadding essentially combines the top_padding and bottom_padding properties
#         ## and sets them to the same value
#         ypadding 150
#         vpgrid:

#             cols 1
#             yinitial 1.0

#             draggable True
#             mousewheel True
#             scrollbars "vertical"

#             vbox:
#                 for h in _history_list:

#                     window:

#                         ## This lays things out properly if history_height is None.
#                         has fixed:
#                             yfit True
#                             yalign 0.5

#                         if h.who:

#                             label h.who:
#                                 style "history_name"
#                                 substitute False

#                                 ## Take the color of the who text from the Character, if
#                                 ## set.
#                                 if "color" in h.who_args:
#                                     text_color h.who_args["color"]

#                         $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                         text what:
#                             line_spacing 5
#                             substitute False
                    
#                     ## This puts some space between entries so it's easier to read
#                     null height 100

#                 if not _history_list:

#                     text "The text log is empty.":
#                         xpos 700
#                         ypos 10
#                         line_spacing 10
#                     ## Adding line_spacing prevents the bottom of the text
#                     ## from getting cut off. Adjust when replacing the
#                     ## default fonts.
            

#         textbutton "Return":
#             style "history_return_button"
#             action Return()
#             alt _("Return")
#             yoffset 100


screen history():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:
                padding (0,50,0,50)

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
                
        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text:
    font gui.name_text_font
style history_text is gui_text

style history_text:
    size 45

style history_label is gui_label
style history_label_text is game_menu_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos 0.5
    xanchor 0.5
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align 0.5
    font gui.name_text_font

style history_text:
    xpos 0.5
    ypos 75
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True
    top_margin -100

style history_label_text:
    xalign 0.5

style history_return_button:
    align(0.5,1.0)
    yoffset 100

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    font gui.game_menu_label_font


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"
    add "skip_overlay"
    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"
    vbox:
        xalign 0.5
        yalign 0.5
        if not renpy.is_seen(ever=True):
            text "Skipping is highly discouraged.\nYou have been warned." at animated_glitch:
                color u'#ffffff33'
                size 75
                text_align 0.5
        else:
            pass

        


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0 xoffset -100
        easein .5 alpha 1.0 xoffset 0
    on hide:
        easeout .5 alpha 0.0 xoffset -100


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.       

screen quick_menu():
    variant "mobile"
    if quick_menu:
        imagebutton auto _("gui/quickmenu/menu_%s.png"):
                action ToggleVariable("quick_menu_frame", True, False)
                xalign 1.0
                yalign 0.0
                xoffset -25
                yoffset 25
                activate_sound "audio/sfx/click.ogg"
        zorder 100

        if quick_menu_frame:
            frame:
                background Frame("gui/quickmenu/quickmenu_border.png")
                padding (20, 20, 20, 20)
                xalign 1.0
                yalign 0.0
                xoffset -110
                yoffset 10
                vbox:
                    hbox:
                        style_prefix "quick"
                        if config.developer == True:
                            textbutton _("Back") action Rollback()
                            textbutton _("Debug") action Call("debug")
                            textbutton _("Achieve") action ShowMenu("achievements")
                        imagebutton auto _("gui/quickmenu/history_%s.png"):
                            action ShowMenu('history')
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "History"
                        imagebutton auto _("gui/quickmenu/hide_%s.png"):
                            action HideInterface()
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Hide"
                        imagebutton auto _("gui/quickmenu/auto_%s.png"):
                            action Preference("auto-forward", "toggle")
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Auto-Forward"
                        imagebutton auto _("gui/quickmenu/skip_%s.png"):
                            action Skip() alternate Skip(fast=True, confirm=True)
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Skip"
                        imagebutton auto _("gui/quickmenu/load_%s.png"):
                            action ShowMenu('load')
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Load"
                        imagebutton auto _("gui/quickmenu/save_%s.png"):
                            action ShowMenu('save')
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Save"
                        imagebutton auto _("gui/quickmenu/settings_%s.png"):
                            action ShowMenu('preferences')
                            activate_sound "audio/sfx/click.ogg"
                            tooltip "Settings"
    

    # This has to be the last thing shown in the screen.

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                background None
                xalign 0.5
                text tooltip style "tooltip_hover":
                    size 35
                    
                
                
                
 
style window:
    variant "mobile"
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    variant "mobile"
    xanchor 0.5
    xsize gui.namebox_width
    ypos 75
    ysize gui.namebox_height
    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

style say_label:
    variant "mobile"
    properties gui.text_properties("name")
    xalign gui.name_xalign
    color '#ffffff'
    yalign 0.5
    xoffset 0
    outlines [(0, "#1a1a1a", 2, 2)]

style say_dialogue:
    variant "mobile"
    properties gui.text_properties("dialogue")
    outlines [(0, "#1a1a1a", 2, 2)]
    line_spacing 0
    ypos 150

style choice_vbox:
    variant "mobile"
    # xalign 0.95
    # yalign 0.65
    #ypos 405
    #yanchor 0.5

    spacing gui.choice_spacing

style radio_button:
    variant "mobile"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "mobile"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "mobile"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "mobile"
    # background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "mobile"
    # background "gui/phone/overlay/game_menu.png"
    background None

style game_menu_navigation_frame:
    variant "mobile"
    xsize 420

style game_menu_content_frame:
    variant "mobile"
    top_margin 0
    
style pref_vbox:
    variant "mobile"
    xsize None

style bar:
    variant "mobile"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "mobile"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "mobile"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "mobile"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable "hide"

style slider:
    variant "mobile"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "mobile"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "mobile"
    xsize None

style slider_slider:
    variant "mobile"
    xsize 525
