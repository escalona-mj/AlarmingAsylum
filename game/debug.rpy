image gray = Solid("#808080")
label debug:
    $ quick_menu = False
    scene bg gray
    menu:
        i "This is only to test certain screens and functions."
        "Notify screen":
            jump notifying
        "Choice selection":
            jump choosing
        "Persistent name test":
            jump naming
        "Message box":
            jump message_box
        "{color=#c41f1f}Delete persistent data{/color}":
            menu:
                "Are you sure you want to delete the persistent data including achievements?\n{color=#c41f1f}(WARNING: This will close the game.){fast}{/color}"
                "{color=#c41f1f}Yes.{/color}":
                    "Deleting persistent data...{nw=3.0}"
                    $ persistent._clear(progress=False)
                    $ achievement.clear_all()
                    $ renpy.quit(relaunch=True)
                "No.":
                    pass
            jump debug
        "Exit debug":
            return

label notifying:
    $ renpy.notify("This is a really really long notify message using the renpy.notify() function.")
    i "This is a long test message using the notify screen."
    $ renpy.notify("Hello World!")
    i "This is a short test message using the notify screen."
    menu:
        i "Would you like to test the Achievement notification?"
        "Yes.":
            $ renpy.display_notify("Achievement Get:\n\"Achievement Name\"")
            play sound "audio/sfx/notify.ogg"
            i "Achievement granted."
            jump debug
        "No.":
            jump debug

label naming:
    call screen name_input(message="What is your name?", ok_action=Return())
    $ persistent.playername = Main
    i "... is my name."
    $ renpy.notify("Your name is " + Main + ".")
    i "You will now see the inputted name in the screen notify using concatination."
    i "The persistent name can be used in certain cases if you want the end user to use the name they inputted initally in starting a new game in other labels such as a post game or a chapter selection screen."
    i "However, do NOTE that the name will not carry between saves."
    i "For example, if the user inputted \"Eileen\" while starting a new game, and loaded a different save file with a different name such as \"Neelie\"..."
    i "The game will still use \"Eileen\" in different labels outside the label start. Whatever the user has inputted while starting a new game will become the default name unless it is changed again in the naming screen."
    jump debug

label choosing:
    $ choice_a = False
    $ choice_b = False
    $ choice_c = False
    $ menuchoice = 0

    menu:
        i "Which choice selection would you like to try?"
        "Able to pick all and display a hidden choice":
            jump choices_abc
        "Only able to pick less than the max choices":
            jump pick_2_choices
        "Only able to pick less than the max choices and choose the required choices":
            jump pick_2_choices_required
        "Go back":
            jump debug

    label pick_2_choices_required:
        if choice_a == True and choice_c == True and menuchoice == 2:
            jump choice_ac
        elif menuchoice == 2:
            jump choice_not
        menu:
            i "Choose an option."
            "Required Choice A" if choice_a == False:
                $ menuchoice += 1
                i "Choice A is selected."
                $ choice_a = True
                jump pick_2_choices_required

            "Choice B" if choice_b == False:
                $ menuchoice += 1
                i "Choice B is selected."
                $ choice_b = True
                jump pick_2_choices_required

            "Required Choice C" if choice_c == False:
                $ menuchoice += 1
                i "Choice C is selected."
                $ choice_c = True
                jump pick_2_choices_required
        jump debug

label choice_ac:
    i "Choice A and Choice C have been selected."
    i "You will arrive here once you chose the required choices no matter the order."
    jump debug

label choice_not:
    i"Two required choices weren't selected."
    i "You will arrive here once you did not choose the required choices."
    jump debug

    label pick_2_choices:
        menu:
            i "Choose an option."
            "Choice A" if choice_a == False:
                $ menuchoice += 1
                i "Choice A is selected."
                $ choice_a = True
                if menuchoice == 2:
                    pass
                else:
                    jump pick_2_choices

            "Choice B" if choice_b == False:
                $ menuchoice += 1
                i "Choice B is selected."
                $ choice_b = True
                if menuchoice == 2:
                    pass
                else:
                    jump pick_2_choices

            "Choice C" if choice_c == False:
                $ menuchoice += 1
                i "Choice C is selected."
                $ choice_c = True
                if menuchoice == 2:
                    pass
                else:
                    jump pick_2_choices
        i "You will arrive here once you chose 2 choices no matter the order are."
        jump debug

    label choices_abc:
        menu:
            i "Choose an option."
            "Choice A" if choice_a == False:
                $ menuchoice += 1
                i "Choice A is selected."
                $ choice_a = True
                jump choices_abc

            "Choice B" if choice_b == False:
                $ menuchoice += 1
                i "Choice B is selected."
                $ choice_b = True
                jump choices_abc

            "Choice C" if choice_c == False:
                $ menuchoice += 1
                i "Choice C is selected."
                $ choice_c = True
                jump choices_abc

            "Hidden choice: Choice D" if menuchoice == 3:
                i "All choices have been chosen."
                i "Choice D will only appear if all of the other choices have been picked."
                
        i "You will arrive here once you got all the choices no matter the order are."
        jump debug

    label message_box:
        call screen dialog(message="This is test message using the screen dialog.\n{size=35}(This is our custom-made message box.){/size}", ok_action=Return())
        call screen confirm(message="This is test message using the screen confirm.\n{size=35}(This message box is made by Ren'Py itself.)\n(Choosing {b}Yes{/b} will return to the custom message box. Choosing {b}No{/b} will close the message box.){/size}", yes_action=Jump("message_box"), no_action=Return())
        jump debug
