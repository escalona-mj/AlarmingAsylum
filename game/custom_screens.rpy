################    RPS     ##########################
screen scoring():
    zorder 100
    frame:
        xalign 0.5
        yalign 0.05
        xpadding 75
        ypadding 50
        background Frame("gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
            
        vbox:
            text _("Score"):
                font gui.game_menu_label_font
                text_align 0.5
                xalign 0.5
            text _("[player_score]  -  [computer_score]"):
                font gui.game_menu_label_font
                size 100
                text_align 0.5
                xalign 0.5

screen rps_screen():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    add "gui/overlay/confirm.png":
        alpha 0.7
    if config.developer == True:
        use quick_menu
    else:
        pass
    vbox:
        xalign 0.5
        yalign 0.5
        null height 100
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "scissors"
                tooltip "Scissors"
                activate_sound "audio/sfx/click.ogg"
                hover_sound "audio/sfx/hover.ogg"
                action Return('scissors'), Hide("rps_screen", transition=Dissolve(0.25))
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "paper"
                tooltip "Paper"
                activate_sound "audio/sfx/click.ogg"
                hover_sound "audio/sfx/hover.ogg"
                action Return('paper'), Hide("rps_screen", transition=Dissolve(0.25))
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "rock"
                tooltip "Rock"
                activate_sound "audio/sfx/click.ogg"
                hover_sound "audio/sfx/hover.ogg"
                action Return('rock'), Hide("rps_screen", transition=Dissolve(0.25))
        text _("Pick a choice"):
            text_align 0.5
            xalign 0.5
    
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

################    CUSTOM NAME INPUT     ##########################
default Main = persistent.playername
define persistent.playername = ''

#custom name input
screen name_input(message, ok_action, back_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [ok_action]
    
    frame:
        yalign 0.25
        has vbox:
            xalign .5
            yalign .5
            spacing 30
            xfill True

        label _(message):
            style "confirm_prompt"
            xalign 0.5
            yalign 0.5

        input default "" value VariableInputValue("Main") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            xalign 0.5
            yalign 0.5
    
    hbox:
            xalign 0.97
            yalign 0.35
            spacing 10

            textbutton _("OK") action ok_action
            textbutton _("Back") action back_action
        
init python:
    def FinishEnterName():
        if not Main: return
        persistent.playername = Main
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen slow_text_center(txt):
    fixed:
        add Text(txt, slow_cps=2, text_align=0.5) xalign 0.5 yalign 0.5

screen whisper(txt):
    fixed:
        add Text(txt, slow_cps=10, text_align=0.5, color=u'#910303') xalign 0.5 yalign 0.5:
            at transform:
                alpha 0.25

################    ASYLUM MAP     ##########################
transform blink_blur:
    blur 3
    linear 1.0 alpha 0.5
    linear 2.0 alpha 0.0
    repeat

transform blink:
    zoom .5
    linear 1.0 alpha 0.0 blur 3
    linear 5.0 alpha 1.0 blur 0
    repeat

image particle_blur = SnowBlossom(At("gui/menu/particle.png", blink_blur), border=150, count=10, start=0.00000000001, fast=False,  yspeed=(-100, -80),  xspeed=(-200,200), horizontal=True)
image particle = SnowBlossom(At("gui/menu/particle.png", blink), count=10, border=150, xspeed=(0, -10), start=10, fast=False, horizontal=False)

screen asylum_map():
    if config.developer == True:
        use quick_menu # TODO: REMOVE when PUBLISHING
    else:
        pass
    fixed:
        imagebutton auto "images/screen_maps/room1_%s.png":
            action Jump("room1")
            xpos 233
            ypos 461
            activate_sound "audio/sfx/click.ogg"
            hover_sound "audio/sfx/hover.ogg"
            focus_mask True
            if not room1_done:
                tooltip "???"
            else:
                tooltip "Office"
            
        imagebutton auto "images/screen_maps/room2_%s.png":
            action Jump("room2")
            xpos 637
            ypos 574
            activate_sound "audio/sfx/click.ogg"
            hover_sound "audio/sfx/hover.ogg"
            focus_mask True
            if not room2_done:
                tooltip "???"
            else:
                tooltip "Bedroom"

        imagebutton auto "images/screen_maps/room3_%s.png":
            action Jump("room3")
            xpos 1689
            ypos 393
            activate_sound "audio/sfx/click.ogg"
            hover_sound "audio/sfx/hover.ogg"
            focus_mask True
            tooltip "???"
        frame:
            xalign 0.5
            yalign 0.95
            background None
            text "Tap and hold to hover and inspect a room.":
                size gui.text_size
        

    # add "particle"
    # add "particle_blur"

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

style tooltip_hover:
    xalign 0.5
    color '#ffffff'
    yalign 0.5
    outlines [(3, "#1a1a1a", 2, 2)]

################    PAPER     ##########################

init python:
    def entry(entry_id):
        ent = persistent.entry_list[entry_id]
        _window_hide(trans=False, auto=True)
        config.skipping = False
        renpy.play("audio/sfx/page.ogg", channel="sound")
        renpy.call_screen(_screen_name='entry', content=ent[0])

transform paper:
    on show:
        alpha 0
        linear 0.25 alpha 1
    on hide:
        alpha 1
        linear 0.25 alpha 0

screen entry(content):
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    fixed:
        textbutton "Return":
            xalign 1.0
            yalign 1.0
            xoffset -10
            yoffset -10
            action Return()
    style_prefix "entry"
    frame at paper:
        background None
        add "images/screen_maps/paper.jpg" at truecenter
        viewport at truecenter:
            xsize 1000
            ysize 1080
            mousewheel True
            draggable True
            has vbox
            null height 50
            text content
            null height 50

style entry_text:
    size 30
    color u'#000000'

style entry_button_text:
    font gui.game_menu_label_font

################    GAME OVER     ##########################
screen game_over(message):

    style_prefix "game_over"

    frame:
        background None
        xalign 0.5
        yalign 0.5

        has vbox:
            xalign 0.5
            yalign 0.5

        label "GAME OVER.":
            xalign 0.5
            
        text message:
            at transform:
                alpha 0.0
                pause 2.0
                xalign 0.5
                linear 0.5 alpha 1.0

    fixed:
        style_prefix "info"
        textbutton "Click here to return to the main menu." at info:
            xalign 0.5
            yalign 0.95
            action MainMenu(confirm=False)

transform info:
    alpha 0.0
    pause 3.0
    block:
        ease 1.0 alpha 1.0
        ease 1.0 alpha 0.5
        repeat

style game_over_label_text:
    font gui.game_menu_label_font
    color u'#730f0fff'
    size 200

style info_button is empty

style info_button_text:
    size 35
    hover_color '#ffffff'