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
    add "gui/overlay/confirm.png"
    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            xalign 0.5
            yalign 0.5
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "scissors"
                action Return('scissors'), Hide("rps_screen", transition=noise_window)
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "paper"
                action Return('paper'), Hide("rps_screen", transition=noise_window)
            imagebutton:
                yalign 0.5
                focus_mask True
                idle "rock"
                action Return('rock'), Hide("rps_screen", transition=noise_window)
        text _("Pick a choice"):
            text_align 0.5
            xalign 0.5

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
        # if renpy.mobile:
        #         yoffset -325
                
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
            xalign 0.5
            yalign 0.5
            spacing 100

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
