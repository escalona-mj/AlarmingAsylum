transform swing:
    xalign 0.5
    yalign 1.75
    zoom 2.0
    subpixel True
    rotate -1
    ease 2.0 rotate 1
    ease 2.0 rotate -1
    repeat

transform jumpscare:
    linear .2 zoom 15.0

image jumpscare1 = ("images/others/jump.jpg")
image jumpscare2 = ("images/others/scare.png")
image hang = ("images/others/hanged_person.png")

image white = Solid("#ffffff18")

label act2_hanging:
    scene bg office
    show black:
        alpha 0.8
    with wipeleft_scene
    "We enter the room."
    "Somehow, it's even darker now."
    alonso "Has it always been this dark here before?"
    raymon "No..."
    "Somewhere in the darkness, I see a figure."
    "It looks like a phantom hovering..."
    "My heartbeat starts to pick up as I start to back up."
    "Eventually, I feel my rear hit Alonso behind me."
    lucy "Can someone turn the flashlight on?"
    raymon "Okay, I'll look for it."
    "Raymon starts to rummage through his bag."
    raymon "Come on, it has to be here..."
    i "You g-guys don't see it?"
    alonso "See what?"
    i "T-there's something up ahead..."
    alonso "Really? I don't see anything..."
    raymon "I found it!"
    play sound "audio/sfx/flashlight.mp3"
    raymon "Let me just-{nw}"
    $ config.skipping = False
    play sound "audio/sfx/scare.mp3"
    play music "audio/bgm/act2.mp3" loop
    show hang at swing
    show expression AlphaMask("white", At("hang", swing)) as mask
    show expression AlphaMask("flashlight", At("hang", swing)) as mask2
    show flashlight onlayer transient
    hide black
    window hide(None)
    $ seenSuicide = True
    pause 4.5
    window auto
    "..."
    alonso "{sc}AAAAAAAAAAAAAAAAAAAHHHH!{/sc}" with vpunch
    raymon "What the..."
    "What the hell?"
    "{i}What the hell?!!{/i}"
    "My body is completely frozen."
    "There is a body hanging in the air, in front of us."
    "A lifeless body, staring down at us..."
    "Was this a recent death?"
    "Were we not alone in the asylum?"
    "Raymon suppresses his urge to vomit..."
    "But wasn't able to and vomits on the ground instead."
    "I look to Lucy, but she's taking this normally as if she isn't affected by the sudden turn of events."
    i "L-Lucy?! W-what..."
    "I froze."
    "I don't know what to say."
    "How can she be taking this so calmly?"
    raymon "If w-we aren't alone here..."
    raymon "W-who... who hunged the body?"
    alonso "I'll tell you what's even better!"
    "Alonso rushes outside of the room."
    lucy "Sire, we have to stick together!"
    "Lucy follows him outside."
    raymon "W-what do we do now, [Main]!?"
    menu:
        "\"Obviously, let's follow them!\"":
            raymon "Good idea!"
            raymon "I am NOT staying near that body!"
            "We follow the rest outside."
            jump act2
        "\"...\"":
            $ config.skipping = False
            "..."
            raymon "[Main]?"
            raymon "[Main]?!"
            raymon "[Main!u]!!?"
            "..."
            raymon "[Main], we've got to go!"
            "Raymon looks completely worried whilst shaking me."
            raymon "..."
            "I can't move."
            "I am completely frozen from the scene unfolding towards us."
            raymon "You know what? Fuck it!"
            hide flashlight onlayer transient
            show black:
                alpha 0.8
            play sound "audio/sfx/flashlight.mp3"
            hide hang
            hide expression AlphaMask("white", At("hang", swing)) as mask
            hide expression AlphaMask("flashlight", At("hang", swing)) as mask2
            stop music
            "Raymon leaves."
            "For a moment, darkness covered the room once more."
            "I'm left alone with the lifeless body here behind me."
            "I try to look back to see if it's still there."
            show black:
                alpha 1.0
            with wipeleft
            "..."
            "I reach out my hand into the void to confirm if the body is still there."
            "..."
            "It's not there anymore."
            $ quick_menu = False
            $ config.skipping = False
            show jumpscare1:
                alpha 0.0
                linear 3.8 alpha 1.0
            "I suddenly feel something moving closer on my front."
            "What in the fuc-{nw}"
            play sound "audio/sfx/jumpscare.mp3"
            hide jumpscare1
            show jumpscare2 at jumpscare:
                xalign 0.5
                yalign 0.5
            pause 0.2
            hide jumpscare2
            pause 1.5
            $ achievement_get("bad_end")
            play sound "audio/sfx/game_over.mp3"
            call screen game_over(message="I'd leave the premises if I were you.") with dissolve

label act2:
    scene bg asylum with wipeleft_scene
    i "I'm officially freaked out. Let's get out of here!"
    "I rushed through the entrance."
    "However, we were met with a terrible fate."
    "I see Alonso banging the door while Lucy is trying to maintain his temper."
    alonso "{sc}Who locked the damn door?!{/sc}" with vpunch
    lucy "Banging the door will do no good, Sire."
    lucy "I suggest that you calm down while we think this situation together."
    stop music fadeout 3.5
    alonso "Okay... okay..."
    alonso "I'm calm..."
    "Alonso takes deep breaths in and out several times."
    alonso "I'm sorry, but everything was just new to me."
    alonso "I mean I've seen dead people in my life, but those were in coffins!"
    alonso "What we saw was just..."
    raymon "Unexpected..."
    raymon "Who even hunged the corpse?"
    raymon "The body was still fresh..."
    raymon "I'm still confused."
    raymon "Did someone recently die here and hunged the corpse?"
    lucy "I am also confused as well..."
    i "Lucy, how were you so calm and emotionless when you witnessed that?"
    "Lucy looks at me with a concerned face."
    lucy "I have seen far worse things than these.{nw}"
    raymon "*cough*"
    raymon "Hello? We have more important matters to deal with!"
    raymon "How are we even going to get out of here?"
    lucy "Right, my apologies. It slipped from my mind."
    lucy "..."
    "Lucy examines the hallway."
    if room3_checked:
        lucy "The blockage in the room across the hallway seems to have subsided."
    else:
        lucy "There are no more rooms to explore besides the room across the hallway."
    lucy "Let us see if we can find an exit there."
    play music asylum
    jump asylum_mapping

label room3:
    $ config.skipping = False
    if act2 == True and seenSuicide == True:
        $ room3_done = True
        scene bg basement with wipeleft_scene
        "It's a basement?"
        "The"
    else:
        $ room3_checked = True
        "Seems like there's something blocking the way."
        "I think I'll go check out the other rooms first."
    jump asylum_mapping
