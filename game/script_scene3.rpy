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
    linear .3 zoom 15.0

image jumpscare1 = ("images/others/jump.jpg")
image jumpscare2 = ("images/others/scare.png")
image hang = ("images/others/hanged_person.png")

image white = Solid("#ffffff18")

label act2_hanging:
    hide particle_blur onlayer front
    hide particle onlayer front
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
    show particle_blur onlayer front
    show particle onlayer front
    show hang at swing
    show expression AlphaMask("white", At("hang", swing)) as mask
    show expression AlphaMask("flashlight", At("hang", swing)) as mask2
    hide black
    show flashlight onlayer transient
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
            show raymon r_eyes_anxious r_mouth_slightopen r_brow_sad at rise_bed
            show expression AlphaMask("images/others/flashlight.png", At("raymon", rise_bed)) as r_mask
            raymon "[Main]?"
            show raymon at hop
            raymon "[Main]?!"
            raymon "[Main!u]!!?" with vpunch
            "..."
            camera at shaking
            raymon r_mouth_serious"[Main], we've got to go!"
            "Raymon looks completely worried whilst shaking me."
            raymon "..."
            "I can't move."
            "I am completely frozen from the scene unfolding towards us."
            camera
            raymon r_brow_serious "You know what? Fuck it!"
            play sound "audio/sfx/flashlight.mp3"
            pause 0.5
            show raymon:
                easeout 0.1 offscreenright
            hide particle_blur onlayer front
            hide particle onlayer front
            hide flashlight onlayer transient
            show black:
                alpha 0.8
            hide hang
            hide expression AlphaMask("white", At("hang", swing)) as mask
            hide expression AlphaMask("flashlight", At("hang", swing)) as mask2
            stop music
            "Raymon runs towards the entrance, leaving me."
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
            window hide(None)
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
            window auto
            ###GAME OVER###

label act2:
    scene bg asylum with wipeleft_scene
    i "I'm officially freaked out. Let's get out of here!"
    "I rushed through the entrance."
    "However, we were met with a terrible fate."
    show alonso a_brow_sad a_mouth_serious a_cry a_eyes_closed at left
    show expression AlphaMask("images/others/asylum_mask.png", At("alonso", left)) as a_mask
    show lucy l_brow_sad l_mouth_serious at right
    show expression AlphaMask("images/others/asylum_mask.png", At("lucy", right)) as l_mask
    with Dissolve(0.2)
    "I see Alonso banging the door while Lucy is trying to maintain his temper."
    alonso "{sc}Who locked the damn door?!{/sc}" with vpunch
    show lucy l_base3 l_eyes_closed behind alonso at gocenter_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("lucy l_base3", fromrighttocenter_transform)) as l_mask behind alonso
    #TODO: angry mouth expression for alonso
    show alonso -a_eyes_closed
    lucy "Banging the door will do no good, Sire."
    lucy -l_eyes_closed"I suggest that you calm down while we think this situation together."
    stop music fadeout 3.5
    alonso "Okay... okay..."
    alonso a_eyes_closed "I'm calm..."
    show alonso -a_cry
    "Alonso takes deep breaths in and out several times."
    alonso -a_eyes_closed "I'm sorry, but everything was just new to me."
    alonso a_sweat a_eyes_look"I mean I've seen dead people in my life, but those were in coffins!"
    alonso -a_sweat a_eyes_closed"What we saw was just..."
    show alonso -a_eyes_closed
    show raymon r_brow_sad r_mouth_serious at easeright_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("raymon", easeright_transform)) as r_mask
    raymon "Unexpected..."
    show lucy -l_base3
    show expression AlphaMask("images/others/asylum_mask.png", At("lucy", center)) as l_mask behind alonso
    raymon "Who even hunged the corpse?"
    raymon r_eyes_closed r_sweat"The body was still fresh..."
    raymon "I'm still confused."
    raymon r_eyes_look"Did someone recently die here and hunged the corpse?"
    lucy -l_eyes_closed l_sweat"I am also confused as well..."
    show raymon -r_eyes_look -r_sweat
    i "Lucy, how were you so calm and emotionless when you witnessed that?"
    show lucy -l_mouth_serious -l_sweat
    "Lucy looks at me with a concerned face."
    lucy l_mouth_slightopen"I have seen far worse things than these{nw}"
    show lucy l_mouth_serious
    raymon r_brow_serious"{i}*cough*{/i}"
    raymon "Hello? We have more important matters to deal with!"
    raymon r_mouth_slightopen"How are we even going to get out of here?"
    show raymon r_mouth_serious
    lucy l_sweat l_eyes_closedhappy -l_mouth_serious"Right, my apologies. It slipped from my mind."
    lucy "..."
    show lucy -l_sweat -l_eyes_closedhappy -l_brow_sad l_mouth_serious
    "Lucy examines the hallway."
    show lucy l_mouth_slightopen
    if room3_checked:
        lucy "The blockage in the room across the hallway seems to have subsided."
    else:
        lucy "There are no more rooms to explore besides the room across the hallway."
    show lucy l_mouth_serious
    lucy "Let us see if we can find an exit there."
    play music asylum
    jump asylum_mapping

label room3:
    $ config.skipping = False
    if act2 == True and seenSuicide == True:
        $ room3_done = True
        scene bg stairBasement with wipeleft_scene
        "We cautiously made our way down a dark and musty stairwell."
        "With the flashlights illuminating the way, we eventually reached the bottom."
        window show
        scene bg basement with wipeleft
        window auto
        "It's a basement?"
        "Obviously."
        "The basement is in a damp and eerie state, surrounded by decaying and withering walls."
        "Adding to the ominous atmosphere, the sound of dripping water echoes in the background."
        "With that, we started to look for any tools or ways that might help us escape."
        "It's not that hard to escape after seeing a dead body appearing out of nowhere, right?"
        "..."
        "The scene I saw earlier still lingers in my thoughts."
        "It's still fresh..."
        "..."
        "No."
        "I have to keep myself together."
        "Right now, getting out of here is our first priority."
        "Anomaly or not, we're all in this together."
        stop music fadeout 1.5
        if likeAlonso == 3: #if u went with alonso in the train, play rps, and went investigating with alonso
            show alonso a_brow_sad a_mouth_serious
            show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
            with Dissolve(0.2)
            show screen whisper("It's not your fault.")
            alonso "..."
            "Alonso comes closer to me discreetly."
            alonso "You know..."
            play music windowdrops
            alonso a_mouth_slightopen "I should make up for the times I've been such an asshole."
            alonso a_mouth_serious a_sweat a_eyes_closed"And... I've been thinking I should mature."
            alonso a_eyes_look"I've noticed how I'm always aided by Lucy, always by my side..."
            alonso -a_eyes_look -a_sweat"I have to face the moment if she disappears in my life, you know?"
            alonso "This is the reason why I went in this mission of hers."
            alonso a_eyes_closed"Just to have one last moment with her..."
            alonso "Tell me [Main]..."
            alonso -a_eyes_closed"Should I leave her alone?"

            menu:
                "Yes.":
                    i "Yes. You should be."
                    i "But you'll have to face it alone."
                    i "Facing independence as a person can be challenging..."
                    i "I think for starters, it's all about self-discovery."
                    i "What are you, without Lucy?"
                    i "Who is Alonso?"
                    i "Who are you?"
                    i "Understand who you are as an individual and what matters to you."
                    i "She can't be with us forever, she has a life after all."
                    i "I think you should try and talk things with Lucy."
                    i "Say something that will make her feel pride towards you."
                "No.":
                    i "No. Lucy needs you as much as you need her."
                    i "You both have some sort have a synergy, something that can't be replicated."
                    i "If you consider her as family, I think you should let her stay."
                    i "The bond that you formed with her is something irreplaceable."

            i "I mean, I'm already proud of you."
            i "Back then, you only see your butler, Lucy, as your extension of aid."
            i "But something changed, and now you've developed empathy towards her."
            show alonso -a_mouth_serious
            i "You've matured already."
            show alonso a_cry
            "Alonso wasn't able to keep his emotions stable."
            show alonso a_eyes_closed
            "As a result, he cries in front of me."
            "Wow. I guess he has a soft spot after all-{nw}"
            show alonso -a_eyes_closed:
                ease 0.2 xalign 0.45 blur 25 subpixel True yalign 0.25 zoom 7
            show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask:
                ease 0.2 xalign 0.45 blur 25 subpixel True yalign 0.25 zoom 7
            pause 0.1
            show black
            hide particle_blur onlayer front
            hide particle onlayer front
            with vpunch
            "!!!{fast}"
            "Unexpectedly, Alonso hugs me."
            alonso "Thanks [Main]. I needed that."
            "I caress his back while he's buried in my shoulder, sniffing."
            "{i}There, there...{/i}"
            "He's crushing me... but at the cost of comforting him, I'd say it's worth being crushed."
            "We stayed like this for a couple of seconds."
            "But all things must come to an end."
            show alonso:
                xalign 0.5 yalign 1.0 zoom 1.0 blur 0
            show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask:
                xalign 0.5 yalign 1.0 zoom 1.0 blur 0
            hide black
            show particle_blur onlayer front
            show particle onlayer front
            with dissolve
            "Alonso lets me go from his embrace."
            show alonso a_eyes_closed
            "Truth to be told, I was really enjoying the company."
            show alonso -a_cry
            "I've never been hugged for the past few years..."
            "So this was relieving."
            show alonso -a_eyes_closed
            "Relieving enough to make us feel less anxious about our current situation."
            hide alonso
            hide expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
            with Dissolve(0.2)
            hide screen whisper

        elif likeRaymon == 3: #if u ignored alonso in the train, not play rps, and went investigating with raymon
            show raymon r_brow_sad r_mouth_serious
            show expression AlphaMask("images/others/flashlight.png", At("raymon", center)) as r_mask
            with Dissolve(0.2)
            raymon "..."
            "Raymon comes closer to me discreetly."
            i "Oh, hey, Raymon."
            i "You seem distant lately. Is something the matter?"
            raymon "..."
            raymon "You know how I'm always prepared most of the time?"
            raymon "That scene earlier..."
            play music windowdrops
            raymon "I'm really sorry. I was supposed to be the brains of this group."
            raymon "Help everyone out... Solve everyone's problems."
            raymon "Right now, I feel as useless as the clues we found earlier."

            menu:
                "Comfort him.":
                    "I take a moment and placed my comforting hand on his."
                    i "Nothing in the world could have prepared us eariler."
                    i "It's normal to feel that."
                    i "And besides, you've already helped us."
                    i "Without you, we wouldn't have made it this far."
                    i "So please... stop crying."
                    "Raymon smiles back through an incredibly pained expression."
                    "His tears began to subside."
                    "And for a moment, his body gesture welcomes me to hug him."
                    "..."
                    "It's only natural to give back a hug, right?"
                "Talk some sense to him.":
                    i "You aren't expecting us to look down on you after failing to please us, right?"
                    raymon "I was..."
                    "Poor thing. He must've been pent up from preparing too much."
                    i "Oh, Raymon. It's okay to fail."
                    i "Nothing in the world could have prepared us eariler."
                    

            raymon "I really appreciate that you took the time and hang out with me..."
            raymon "I enjoyed the times we read back in the train."
            raymon "Does the defeaning silence make you feel remorse or not?"
        else:
            "Lucy's moment goes here."

        hide screen whisper
        


    else:
        $ room3_checked = True
        call screen dialog (message="Seems like there's something blocking the way.", ok_action=Return())
        # "I think I'll go check out the other rooms first."
    jump asylum_mapping
