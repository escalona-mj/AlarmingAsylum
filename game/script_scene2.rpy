label scene_2:
    "A large door stands in front of us."
    "No matter how much strength I put to open the door, it won't budge."
    alonso "This door seems stuck."
    alonso "Raymon, do you have something that can open this door?"
    show bg door:
        linear 5.0 yalign 0.5
    alonso "Like a key or something?"
    raymon "No, but I do have something better."
    "Raymon whips out a bottle container labeled \"Motor Oil\"."
    "He then applies the oil to the hinges of the door."
    show bg door:
        linear 0.2 yalign 1.0
    i "Why do you have a specific oil for this specific moment?"
    raymon "I knew situations like these would happen."
    raymon "Knowing old doors would rust overtime and therefore hard to open..."
    raymon "I brought it just in case."
    raymon "And look at that, we're already eliminating our first obstacle."
    lucy "He is correct."
    lucy "As much as I question myself bringing all of you here to danger, I suppose you three can handle yourselves."
    "The door finally open with ease, and it was time for us to venture through the asylum."
    lucy "Watch your steps. You might stumble upon some debris on your way."
    window hide
    show black:
        alpha 0.0
        linear 2.0 alpha 1.0
    play sound "audio/sfx/big_door.mp3" volume 0.5 fadeout 2.0
    stop ambient fadeout 1.5
    pause 4.0
    window auto
    scene bg asylum with wipeleft_scene
    play music asylum
    show particle_blur onlayer front
    show particle onlayer front
    "As I entered the asylum, I saw the remnants of its dark history."
    "There were old medical equipment, broken beds, and strange markings on the walls."
    "This place screams prison."
    $ config.skipping = False
    $ renpy.notify("Saving the game is recommended.")
    play sound "audio/sfx/warning.mp3" volume 0.2
    show alonso a_brow_sad a_eyes_closed a_mouth_serious
    show expression AlphaMask("images/others/asylum_mask.png", At("alonso", center)) as a_mask
    with Dissolve(0.2)
    alonso "There aren't any... g-ghosts here, right?"
    show alonso at centertoleft_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("alonso", centertoleft_transform)) as a_mask
    show raymon r_mouth_serious at easeright_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("raymon", easeright_transform)) as r_mask
    raymon "No Alonso. Besides, aren't you a bit too old to be scared of ghosts?"
    alonso a_eyes_look a_mouth_open"Yeah, it's probably because I've gotten attached to superstitious beliefs..."
    alonso a_mouth_serious"And this place reeks."
    "I don't blame Alonso. The air was heavy with the stench of decay."
    "Despite the grim atmosphere, I carefully look at my surroundings to see if I can find something that can help Lucy on her mission."
    play sound "audio/sfx/camera.mp3" volume 0.5
    show camera_flash
    "{bt=2}*click*{/bt}{fast}"
    raymon r_mouth_slightopen"This place looks straight out from a movie."
    raymon "Oh, and there're some empty rooms over there."
    hide alonso
    hide raymon
    hide expression AlphaMask("images/others/asylum_mask.png", At("alonso", centertoleft_transform)) as a_mask
    hide expression AlphaMask("images/others/asylum_mask.png", At("raymon", easeright_transform)) as r_mask
    with Dissolve(0.2)
    play sound "audio/sfx/flashlight.mp3"
    "I opened my flashlight and pointed out to the rooms."
    "No matter how bright my flashlight is, the room I'm pointing at is still pitch black."
    raymon "Why don't we split up?"
    "What?"
    "What kind of suggestion is that?"
    show alonso a_brow_serious a_mouth_serious
    show expression AlphaMask("images/others/asylum_mask.png", At("alonso", center)) as a_mask
    with Dissolve(0.2)
    alonso "Uh, no thank you. You're asking for death."
    i "He's right!"
    show alonso at centertoleft_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("alonso", centertoleft_transform)) as a_mask
    show lucy l_brow_sad at easeright_transform
    show expression AlphaMask("images/others/asylum_mask.png", At("lucy", easeright_transform)) as l_mask
    lucy "I appreciate the suggestion that you want to make my mission go a lot smoother..."
    show expression AlphaMask("images/others/asylum_mask.png", At("lucy l_base2", right)) as l_mask
    lucy l_base2 l_brow_serious l_mouth_serious "But I cannot overlook such a lousy decision for my convenience."
    lucy "We all have to stick together."
    raymon "I see."
    hide alonso at centertoleft_transform
    hide expression AlphaMask("images/others/asylum_mask.png", At("alonso", centertoleft_transform)) as a_mask
    hide lucy l_brow_sad at easeright_transform
    hide expression AlphaMask("images/others/asylum_mask.png", At("lucy", easeright_transform)) as l_mask
    with Dissolve(0.2)
    raymon "[Main], do you have a preference?"
    i "Well, if it'll get this job done sooner, then I don't see a problem."

define room1_done = False
define room2_done = False
define room1_2_done = False
define room3_done = False
define room3_checked = False
define LucySecret = None

define act2 = False
define seenSuicide = False

label asylum_mapping:
    $ config.skipping = False #pauses skipping if turned on
    scene bg asylum with dissolve
    if room1_2_done == False and room1_done == True and room2_done == True:
        $ room1_2_done = True
        show lucy l_mouth_serious l_eyes_look at center
        show expression AlphaMask("images/others/asylum_mask.png", At("lucy", center)) as l_mask
        show raymon r_mouth_serious at right
        show expression AlphaMask("images/others/asylum_mask.png", At("raymon", right)) as r_mask
        show alonso a_mouth_serious at left
        show expression AlphaMask("images/others/asylum_mask.png", At("alonso", left)) as a_mask
        with Dissolve(0.2)
        i "So far, we've only collected some clothes and papers."
        if room3_checked == True:
            i "And the room across the hallway is blocked."
        else:
            i "The only room we haven't explored is the room across the hallway."
        alonso a_brow_sad"I really hope Lucy's finding the clues she needs."
        alonso "Are you okay, Lucy?"
        lucy "..."
        "Lucy seems like she's got a lot on her mind."
        show lucy l_mouth_slightopen -l_eyes_look
        "It took her a few seconds to reply back to Alonso."
        lucy l_eyes_look l_sweat l_brow_sad l_mouth_open"Y-Yes."
        lucy -l_mouth_open"Fortunately, all of the items we have collected are directly aiding my mission."
        raymon r_brow_sad"That's... good news, I hope."
        show lucy -l_mouth_open
        lucy "..."
        alonso a_brow_serious"Lucy, are you hiding something?"
        $ config.skipping = False
        alonso "You've been awfully quiet since{nw}"
        show alonso a_eyes_anxious -a_brow_serious a_mouth_slightopen
        show lucy l_eyes_anxious -l_brow_sad l_mouth_serious -l_sweat
        show raymon r_eyes_anxious -r_brow_sad r_mouth_serious
        window hide(None)
        stop music
        play sound "audio/sfx/fallstuff.mp3"
        pause 3.5
        window auto
        alonso a_brow_sad"{sc}WHAT WAS THAT?{/sc}"
        "Suddenly, I felt a chill sensation as the sound echoes throughout the room."
        i "The atmosphere got a little bit colder. It's not just me, right?"
        show lucy -l_eyes_anxious
        raymon r_eyes_look r_mouth_slightopen r_brow_sad r_sweat "M-must've been the wind."
        show raymon -r_mouth_slightopen
        "Lucy trying to regain her composure from the sudden noise, tries to calm Alonso."
        lucy "It sounds like something fell in the office, Sire..."
        "Nope, nope, nope."
        raymon r_mouth_open"Maybe it's the rats again."
        lucy l_eyes_closed l_mouth_slightopen"Alright, alright. Let us all calm down."
        show raymon -r_sweat -r_eyes_look -r_mouth_open
        lucy -l_eyes_closed l_mouth_serious"I will check out the source of the noise."
        alonso -a_eyes_anxious a_brow_serious a_mouth_serious"Nope! You aren't going there alone."
        alonso "We're coming with you."
        alonso a_eyes_closed"If you're going to die, we might as well die together."
        show alonso -a_eyes_closed
        raymon r_eyes_look r_sweat"..."
        lucy l_eyes_look l_sweat l_brow_sad -l_mouth_serious"..."
        i "..."
        "That's..."
        "I've got no words to describe what just Alonso said."
        show lucy l_eyes_closedhappy l_mouth_open
        show raymon r_eyes_closedhappy r_mouth_open
        show alonso a_brow_sad
        "Lucy just chuckled from the awkwardness that formed between us."
        lucy "I see. If you say so, Sire."
        show raymon -r_eyes_closedhappy -r_brow_sad -r_mouth_open -r_sweat
        show lucy -l_brow_sad -l_mouth_open -l_sweat -l_eyes_closedhappy
        lucy "Everyone, stay behind me."
        hide lucy
        hide raymon
        hide alonso
        hide expression AlphaMask("images/others/asylum_mask.png", At("alonso", left)) as a_mask
        hide expression AlphaMask("images/others/asylum_mask.png", At("raymon", right)) as r_mask
        hide expression AlphaMask("images/others/asylum_mask.png", At("lucy", center)) as l_mask
        with Dissolve(0.2)
        $ act2 = True
        $ config.skipping = False
    if persistent.reminder == None:
        $ config.rollback_enabled = True
        play sound "audio/sfx/warning.mp3" volume 0.2
        call screen confirm(message="NOTE: There are instances where the quick menu will be disabled, so make sure you've saved your file before proceeding.\n\n{color=#ffffffca}({b}Yes{/b}, I understand. {b}No{/b}, let me save first.)", yes_action=Return(), no_action=Rollback())
        $ persistent.reminder = True
        $ config.rollback_enabled = config.developer
    call screen asylum_map with dissolve

label new_room:
    i "Why don't we go here?"
    i "Seems like a good place to start."
    return

label room1:
    if seenSuicide == True:
        call screen dialog (message="I don't think I want to relive that traumatic event again.", ok_action=Return())
        jump asylum_mapping
    if act2 == True:
        jump act2_hanging
    $ wentAlonso = False
    $ wentRaymon = False
    $ wentLucy = False
    $ menuchoice = 0

    if room1_done == False:
        if room1_done == False and room2_done == False:
            call new_room
        $ room1_done = True
        scene bg office with wipeleft_scene
        "As expected, the room is a mess."
        "Books are scattered across the floor along with desks that are almost unrecognizable due to its state."
        "There's also a marking on the wall that says \"School sucks!\"."
        play sound "audio/sfx/camera.mp3" volume 0.5
        show camera_flash
        "{bt=2}*click*{/bt}{fast}"
        alonso "This must be the office."
        raymon "Let's look around."
        lucy "Do not go too far."
        lucy "I need to gather as much intel as I can."
        lucy "If you find anything, be sure to inform me."
        lucy "I will write the ones that are significant and discard any unnecessary information."
        i "Okay."
        "With that, everyone goes looking around."

        label room1_choices:
            menu:
                i "I think I'll go..."
                "Help Alonso." if wentAlonso == False:
                    $ menuchoice += 1
                    $ wentAlonso = True
                    $ likeAlonso += 1
                    "I proceeded to help Alonso."
                    "I see him wandering aimlessly at the corner of the room."
                    "He seems to be looking for something."
                    show alonso
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                    with Dissolve(0.2)
                    alonso "Oh [Main]! Check this out!"
                    alonso "I found a desk."
                    "The desk is covered in layers of dust and cobwebs."
                    "The once polished surface of the desk is now dull and scratched, and the wood is warped and split in places."
                    "The desk looks like it hasn't been used in years, perhaps even decades."
                    alonso a_brow_sad a_eyes_look a_mouth_open a_sweat"I can't seem to open the drawer though."
                    i "Let me try."
                    show alonso a_brow_serious -a_eyes_look -a_mouth_open -a_sweat
                    "I grasp the handle, tightly in my hand, but it's shut tight and won't budge when I try to pull it open."
                    "Determined, I try again with more force."
                    play sound "audio/sfx/hinge_squeak.mp3"
                    "And with a creaking sound, the drawer finally gives way."
                    "I was taken aback by my force, but I managed to regain my composure."
                    "My excitement turns to horror as I see a decaying snake lying coiled up in the drawer."
                    show alonso a_brow_sad a_eyes_anxious a_mouth_slightopen
                    i "What the hell!" with vpunch
                    alonso "What?! {w=0.2}What?!{w=0.2} What?!"
                    "Alonso paces towards me and the desk."
                    alonso -a_eyes_anxious a_mouth_serious "Oh. It's a dead snake..."
                    alonso "What's a dead snake doing in a drawer?"
                    i "Maybe food?"
                    "Alonso examines the snake's corpse."
                    i "Stay away from that thing."
                    alonso -a_brow_sad"Relax, it's dead."
                    i "Okay, but leave it alone."
                    i "It has suffered long enough trapped in that drawer."
                    alonso "Okay."
                    "Looking at the old desk, I examine the rest of the drawers."
                    "As I rummage through each of the drawers, one drawer had a paper in it."
                    "The edges are frayed and torn, and the paper has yellowed with age."
                    "It also had a distinct scent, a musty smell that is reminiscent of old books and antique stores."
                    alonso -a_mouth_serious"Oh, you found something. What does it say?"
                    "I look at the paper, which left a seemingly bizzare note."
                    $ entry("alonso_paper")
                    "Nurse A  c ...?"
                    if LucySecret == True:
                        "A l i c e..."
                        "Nurse Alice..."
                        "Lucy's mother..."
                        i "She must have cured the patient."
                        alonso a_brow_serious a_mouth_slightopen"She?"
                    else:
                        i "Who's Nurse Ac?"
                        alonso a_brow_serious a_mouth_slightopen"Nurse Ay-see?"
                    show alonso a_mouth_serious
                    "Alonso takes the paper from my hand."
                    alonso a_eyes_closedhappy a_mouth_open"Looks like someone didn't get to keep their legs."
                    "I look to Alonso with a glowering expression."
                    show alonso a_eyes_look a_mouth_serious a_brow_sad
                    i "Alonso! Rude."
                    alonso "Sorry."
                    "Judging from the handwriting, the note seems to be written by a child."
                    i "How can you joke at a disabled child's letter?"
                    alonso a_eyes_closed"Oof, now I feel even more bad."
                    alonso -a_eyes_closed"Okay, I'm sorry."
                    i "Don't apologize to me! Apologize to the child."
                    i "Even if they're not here anymore."
                    "Alonso turns around and clasps both of his hands."
                    alonso a_eyes_closed a_sweat "{size=-25}Forgive me.{/size}"
                    "I shake my head."
                    "The child must be so grateful to the nurse that they made a letter just for her."
                    "That's... heartwarming."
                    show alonso a_eyes_look -a_sweat
                    "I wonder how the nurse reacted to such a dearing letter."
                    i "This paper might be helpful."
                    $ renpy.notify("You take the paper.")
                    alonso a_mouth_open"To be honest, if we see any old paper here with information written on it, it's probably important."
                    i "Pretty much."
                    if menuchoice == 2:
                        hide alonso
                        hide expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                        with Dissolve(0.2)
                        pass
                    else:
                        i "I'll look for the others. Will you be okay alone?"
                        alonso -a_eyes_look -a_mouth_open"Yeah. I'll stay here and look around."
                        i "Okay. Take care."
                        hide alonso
                        hide expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                        with Dissolve(0.2)
                        "I leave Alonso in his business."
                        jump room1_choices
                "Help Raymon." if wentRaymon == False:
                    $ menuchoice += 1
                    $ wentRaymon = True
                    $ likeRaymon += 1
                    "I proceeded to help Raymon."
                    "I see him fully delved into the scattered books, searching for any relevant information we might pick up."
                    show raymon r_mouth_open
                    show expression AlphaMask("images/others/flashlight.png", At("raymon", center)) as r_mask
                    with Dissolve(0.2)
                    raymon "Oh, [Main]! Didn't see you there."
                    i "Found anything?"
                    raymon r_eyes_look r_brow_sad -r_mouth_open r_sweat"Not really. Most of the books are burned, and some are torn apart."
                    raymon -r_eyes_look -r_sweat -r_brow_sad"Though I spotted a filing cabinet."
                    "Raymon points out the filing cabinet."
                    "Its metal exterior is covered in rust and grime, and the drawers are jammed tight with decades of neglect."
                    "It seems the content of the cabinet is still intact, judging from the folders peeking from the side."
                    raymon r_mouth_serious"It is shut tight, possibly from the rust."
                    raymon r_eyes_closed -r_mouth_serious"Luckily, I have brought a crowbar."
                    show raymon -r_eyes_closed
                    "Raymon whips out a crowbar from the side of his bag."
                    i "Do you even know how to use it?"
                    raymon r_eyes_closedhappy r_mouth_open"Of course! Now why would I bring a crowbar if I didn't know how to use it in the first place?"
                    play sound "audio/sfx/crowbar.mp3" loop volume 0.7
                    show raymon -r_eyes_closedhappy r_brow_serious r_mouth_serious
                    "With a determined look on his face, he grasp the crowbar tightly in his hand."
                    "Raymon brings the crowbar down with all his might, striking the top of the cabinet with a resounding clang."
                    stop sound fadeout 1.5
                    play sound "audio/sfx/hinge_squeak.mp3"
                    "After several tense moments, a satisfying crack can be heard, and a section of the cabinet's top breaks away, revealing the insides."
                    play sound "audio/sfx/rats.mp3" loop volume 0.5
                    show raymon r_eyes_anxious r_brow_sad
                    "However, when opened, Raymon had unleashed two small creatures that darted out from the file cabinet."
                    show raymon at hop
                    show expression AlphaMask("images/others/flashlight.png", At("raymon", center)) as r_mask
                    raymon "{sc}AHHH! GET IT OFF ME!{/sc}" with vpunch
                    "The rats are small and scraggly, with matted fur and beady eyes that seem to follow Raymon's every move."
                    show raymon r_eyes_closed r_sweat
                    "They move quickly and without fear, scampering around Raymon's body."
                    raymon r_mouth_slightopen"{sc}[Main!u], HELP ME!{/sc}"
                    raymon "{sc}MY BAG, QUICKLY!{/sc}"
                    "I quickly grabbed Raymon's bag to see if he has anything to stop these rats."
                    "What am I suppose to grab here?!"
                    show raymon -r_eyes_closed r_mouth_open -r_sweat
                    raymon "Wait, nevermind [Main]!"
                    raymon -r_mouth_open"Look!"
                    "The rats don't seem to be aggressive. In fact, they're even not attacking him."
                    i "Are they harmless?"
                    "One of the rats reach out to Raymon's pocket."
                    raymon -r_brow_sad r_mouth_slightopen "Oh, you want this?"
                    "Raymon pulls out a snack bar from his pocket."
                    show raymon -r_mouth_slightopen
                    "He opens it and throws it away from us, in which the rats moved away from Raymon."
                    i "I guess they were only searching for food."
                    raymon r_brow_sad"They must have been trapped in that file cabinet."
                    stop sound fadeout 1.5
                    "Slowly, we relax, and watch as the rats disappear into the darkness and leaves us alone."
                    raymon r_eyes_look r_sweat"That was something."
                    i "Yeah."
                    i "Why don't we go and take a look at the cabinet you just opened?"
                    raymon -r_eyes_look -r_sweat "I almost forgot about that."
                    show raymon -r_brow_sad
                    play sound "audio/sfx/filecabinetopen.mp3" volume 0.5
                    "We opened the cabinet."
                    "The drawers are filled with old files and papers, with the edges yellowed and brittle with age."
                    play sound "audio/sfx/camera.mp3" volume 0.5
                    show camera_flash
                    "{bt=2}*click*{/bt}{fast}"
                    show raymon r_mouth_serious
                    "Raymon sifts through the folders and runs his fingers over the documents."
                    i "Well?"
                    raymon r_mouth_slightopen"Interesting. These are patient entries."
                    raymon r_mouth_serious"Take a look. Though this one is a bit harder to read."
                    "Raymon hands me over the file."
                    $ entry("entry1")
                    "The words are illegible at this point."
                    "The ink has eroded, signifying a timeless artifact."
                    "My initial curiosity and fascination quickly gave way to a sense of horror and sadness."
                    "The only words I can come up are anxiety, car accident, harm, panic attacks..."
                    "Judging only from the words I can identify, I can feel the weight of the suffering and pain that these individuals endured."
                    "This is quite a depressing entry."
                    "Despite the growing sense of dread that filled me, I continued to rummage through the cabinet once more to see if I can find anything."
                    "I eventually found another entry that's more readable."
                    $ entry("entry2")
                    "Nurse A  c ...?"
                    if LucySecret == True:
                        "A l i c e..."
                        "Nurse Alice..."
                        "Lucy's mother..."
                        "I carefully read the last statement again."
                        "..."
                        "This patient got discharged by Lucy's mother."
                        raymon r_mouth_slightopen"What did you find?"
                    else:
                        i "Who's Nurse Ac?"
                        raymon r_brow_serious r_mouth_slightopen"Nurse Ey-ssi?"
                    show raymon -r_brow_serious -r_mouth_slightopen
                    "Raymon dashes towards me."
                    raymon "Interesting."
                    raymon "..."
                    raymon r_mouth_open"So you know that asylums were used as long-term care facilities for people with mental illnesses, right?"
                    i "Yeah?"
                    raymon r_brow_sad r_mouth_slightopen r_eyes_look"Most patients were subjected to inhumane treatments, including physical and emotional abuse..."
                    raymon r_eyes_closed"Along with experimentation with unproven medical treatments."
                    raymon -r_eyes_closed -r_mouth_slightopen"However, this nurse managed to get a chronic-mentally ill patient to be cured and discharged, something that was very rare back then."
                    i "That's amazing."
                    if LucySecret == True:
                        "She's quite an astounding nurse."
                        "The fact that she managed to discharge a patient during times when medical knowledge was still limited..."
                    i "I kinda thought that asylums are eternal prisons for the mental."
                    i "Like, once you go in there... you're never leaving..."
                    i "Because of the limited knowledge available back then in the field of psychology or science or something..."
                    i "They would just assume people with psychotic episodes to be untreateable..."
                    raymon -r_brow_sad r_mouth_slightopen "Well you're not wrong."
                    raymon -r_mouth_slightopen r_brow_sad"But you are also quite wrong."
                    "I look to Raymon with a confused expression."
                    i "What's that even supposed to mean?"
                    show raymon r_eyes_closedhappy r_mouth_open -r_brow_sad
                    "We exchanged laughs."
                    $ renpy.notify("You take the paper.")
                    show raymon -r_eyes_closedhappy -r_mouth_open
                    i "I'll take this paper just in case."
                    raymon "Be my guest."
                    # raymon "Well, what do you expect from an abandoned asylum?"
                    # raymon "I would be surprised if one of the patients were still alive."
                    # raymon "All of these were dated back decades ago."
                    # raymon "It would take a miracle if one of them were to show up and haunts us, ahaha."
                    play sound "audio/sfx/filecabinetclose.mp3" volume 0.3
                    "Raymon closes the file cabinet."
                    if menuchoice == 2:
                        hide raymon
                        hide expression AlphaMask("images/others/flaslight.png", At("raymon", center)) as r_mask
                        with Dissolve(0.2)
                        pass
                    else:
                        raymon "Oh! Feel free to leave, I'm going to stay here and see if I can find more."
                        i "Okay."
                        hide raymon
                        hide expression AlphaMask("images/others/flaslight.png", At("raymon", center)) as r_mask
                        with Dissolve(0.2)
                        "I leave Raymon in his business."
                        jump room1_choices
                "Help Lucy." if wentLucy == False:
                    $ menuchoice += 1
                    $ wentLucy  = True
                    "I proceeded to help Lucy."
                    "She seems to be examining the books that are scattered across the floor."
                    "There's not much to describe what she's doing."
                    show lucy
                    show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                    with Dissolve(0.2)
                    lucy "Oh, [Main]."
                    show expression AlphaMask("images/others/flashlight.png", At("lucy l_base2", center)) as l_mask
                    lucy l_base2 l_eyes_closed "I was just glancing at the records here."
                    show lucy -l_eyes_closed -l_base2
                    show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                    "Lucy hands over the files."
                    "The files are varied from adminstrative records, patient files, and prescription medications."
                    lucy l_eyes_look l_brow_sad"By the way..."
                    show expression AlphaMask("images/others/flashlight.png", At("lucy l_base2", center)) as l_mask
                    lucy l_base2 -l_eyes_look"Would you like to know a secret?"
                    menu:
                        "\"Sure.\"":
                            show lucy -l_base2
                            show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                            call secret_lucy
                            lucy l_eyes_closedhappy l_mouth_open"Alright, that is enough drama for one day, ahaha."
                            "For a butler, I thought she's emotionless; an expert."
                            "But I guess she's still human, with feelings..."
                            lucy -l_eyes_closedhappy -l_mouth_open"Shall we?"
                            show lucy -l_brow_sad
                            "I nod."
                            play music asylum
                        "\"I don't think I'm suppose to know about it...\"":
                            $ LucySecret = False
                            lucy l_eyes_look l_mouth_serious"I see."
                            show lucy -l_base2 -l_eyes_look
                            show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                    "We go through each desk and cabinet we can find."
                    "Eventually, Lucy finds a document."
                    if LucySecret == True:
                        lucy "I finally found it!"
                        lucy "My mother's documents."
                        show lucy l_brow_sad
                        "Lucy hands me over the file."
                        "Surpisingly, the document is still intact with complete information."
                        $ entry("lucy_paper")
                        "Alice. That's a nice name."
                        if wentAlonso == True or wentRaymon == True:
                            "The name fits perfectly to the notes we found."
                        i "So, your mother's name is Alice?"
                        show lucy l_base3 l_eyes_closed
                        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
                        lucy "Yes. Such an elegant name, is it not?"
                        "Lucy holds the document dearly."
                        lucy -l_eyes_closed"The only thing left to do is find my mother."
                        lucy "After that, we can finally go home."
                    else:
                        lucy -l_mouth_serious -l_brow_sad"I finally found something that is crucial to our mission."
                        i "What is it?"
                        lucy l_eyes_closedhappy l_sweat l_mouth_open l_brow_sad"Erm... you will see."
                    i "That's great."
                    if menuchoice == 2:
                        show lucy -l_eyes_closedhappy -l_sweat -l_brow_sad -l_mouth_open -l_base2 -l_base3
                        show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                        pass
                    else:
                        if LucySecret == True:
                            show lucy -l_base3 -l_brow_sad
                            show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                            lucy "I'm going to stay here and see if I can find more documents about my mother."
                        else:
                            show lucy -l_eyes_closedhappy -l_sweat -l_brow_sad -l_mouth_open
                            lucy "I'm going to stay here and see if I can find more necessary intel."
                        i "Okay."
                        hide lucy
                        hide expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                        with Dissolve(0.2)
                        "I leave Lucy in her business."
                        jump room1_choices
            lucy "Okay everyone."
            show lucy
            show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
            with Dissolve(0.2)
            lucy "Have you all found something?"
            show alonso at easeleft_transform
            show expression AlphaMask("images/others/flashlight.png", At("alonso", easeleft_transform)) as a_mask
            show raymon at easeright_transform
            show expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
            if wentAlonso == True:
                alonso "We sure did."
                alonso "[Main], give the paper to Lucy."
                $ renpy.notify("You gave the paper.")
                i "Alright."
            else:
                alonso "I sure did."
                alonso "I found a note."
                alonso "The handwriting looked like it belong to a child."
                alonso "It's quite a heartwarming one, with the last sentence thanking {i}\"Nurse a  c \"{/i}."
            show raymon r_eyes_look r_mouth_serious r_brow_sad
            alonso a_eyes_look a_brow_sad a_mouth_serious "Also found a dead snake in a drawer, if anyone wants to know."
            lucy l_brow_sad l_mouth_serious"Were you hurt, sire?"
            alonso -a_eyes_look -a_mouth_serious"Thankfully no."
            show raymon -r_mouth_serious -r_eyes_look
            lucy -l_mouth_serious"That is a relief."
            if LucySecret == True:
                show lucy l_mouth_slightopen l_brow
                "I see Lucy's eyes flashed for a while."
                show lucy -l_mouth_slightopen
            else:
                pass
            lucy "Thank you for the letter."
            show raymon -r_brow_sad 
            if wentRaymon == True:
                raymon "We also found something."
                raymon "Oh [Main], would you kindly give Lucy the papers we found?"
                $ renpy.notify("You gave the paper.")
                i "Okay."
            else:
                raymon "I also found something."
                raymon "Patient entries."
                raymon r_eyes_closed r_mouth_serious r_brow_sad"Some of the entries have become unintelligble, torn or destroyed... by rats."
                raymon -r_eyes_closed -r_mouth_serious"So I picked up and chose the entries that are still legible."
                raymon r_mouth_slightopen -r_brow_sad"Though, one certain nurse piqued my interest. Her name is faded out, but it spells, {i}\"Nurse a  c \"{/i}."
                show raymon -r_mouth_slightopen
            # raymon "Oh, something silly happened to me a while ago. Rats crawled over my body as soon as I opened the cabinet containing the entries I found."
            # raymon "Craziest shid, I tell you."
            if LucySecret == True:
                show lucy l_mouth_slightopen l_brow
                "For the second time, I saw Lucy flashed her eyes once more."
                "Her mother must be highly respected by both patients and staff members, judging from the letters they found."
                show lucy -l_mouth_slightopen
            else:
                pass
            lucy "Thank you all for gathering all the documents you can find."
            lucy "These letters are great fundamentals for my investigation that confirms my suspicions."
            if LucySecret == True:
                "I don't think letters alone are enough to find her mother."
            if room2_done == True:
                hide alonso
                hide raymon
                hide expression AlphaMask("images/others/flashlight.png", At("alonso", left)) as a_mask
                hide expression AlphaMask("images/others/flashlight.png", At("raymon", right)) as r_mask
                with Dissolve(0.2)
                show lucy -l_brow_sad l_mouth_slightopen
                i "Lucy, can I have those papers back? I'd like to see something."
                "I take the papers from Lucy."
                show lucy -l_mouth_slightopen
                "These letters must have something hidden in plain sight."
                call room2_locker_choices
                "I think I got it."
                i "Guys, we might have a clue for the locker."
                show alonso a_brow_serious a_eyes_closedhappy a_mouth_open at easeleft_transform
                show expression AlphaMask("images/others/flashlight.png", At("alonso", easeleft_transform)) as a_mask
                show lucy l_eyes_closedhappy l_sweat l_brow_sad at centertoright_transform
                show expression AlphaMask("images/others/flashlight.png", At("lucy", centertoright_transform)) as l_mask
                alonso "Are you sure? Then lead the way!" with vpunch
                "We went back to the other room."
                scene bg locker with wipeleft_scene
                "Things stood still since we left here."
                "Let's see..."
                call locker_code
                call open_locker
            if room1_done == True and room2_done == False:     
                lucy "I am guessing that there is nothing left to find in this room."
                lucy "[Main], should we get going?"
                i "Yeah, sure."
                lucy "Then let us."
            else:
                "I guess that's everything."
            "We peacefully make our way out of the room."

    else:
        call screen dialog (message="There's nothing left to see here.", ok_action=Return())
    jump asylum_mapping
    
label secret_lucy:
    $ LucySecret = True
    lucy "If you must know, this is a family secret."
    "Family?"
    show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
    lucy l_base3 l_eyes_closed"My mother used to work in this very asylum as a nurse."
    i "Wait what?"
    show lucy -l_eyes_closed
    "I look to Lucy with a wide-eyed expression."
    lucy l_eyes_closed l_mouth_slightopen"You must be so shocked right now..."
    lucy -l_eyes_closed l_brow_serious -l_mouth_serious"But yes, my mother."
    lucy l_brow_sad l_eyes_look l_mouth_slightopen"Even if her workplace was not as good as asylums are now..."
    lucy l_eyes_closed"She helped most of the patients treated here."
    lucy -l_mouth_slightopen"My father told me she was an astounding nurse."
    show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
    lucy -l_base3"She was the only nurse who has been able to discharge a patient; a moment where no one has achieved before."
    stop music fadeout 1.5
    lucy l_eyes_look l_mouth_serious"But one fateful day, Mother never returned home."
    lucy "My father went to the asylum and looked for her..."
    lucy "But they told him that she had already left, the day when she went missing."
    
    # lucy "Ultimately, my father assumed that she was taken in the basement."
    # lucy "In there, he was right."
    # lucy "He barged in to the basement and saw my mother, tied up in a stand up bed..."
    # lucy "My mother was called a witch to pull of a stunt like that."
    # lucy "A stunt back then that no one thought was impossible to do..."
    # lucy "Tell me, [Main]."
    # lucy "Is it a crime to cure people?"
    # menu:
    #     "\"Yes.\"":
    #         pass
    #     "\"I don't know...\"":
    #         pass
    #     "\"That's for you to decide.\"":
    #         pass
    i "Wait..."
    i "So this mission of yours was to find your mother all along?"
    lucy -l_eyes_look -l_mouth_serious"Yes. My father was the one who assigned me to this mission."
    lucy "He asked me to find any traces of her and retrieve her body."
    lucy l_eyes_closed l_mouth_serious"..."
    play music windowdrops
    show lucy l_cry l_base3
    show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
    "She pauses for a moment as tears stream down her face."
    lucy l_eyes_look"I am sure my mother is dead right now."
    lucy -l_eyes_look"And it would be nice if we can get this mission done as soon as possible."
    lucy l_eyes_closed"So that my father and I can get her a proper burial."
    i "I see. I didn't know..."
    "No wonder she pauses everytime when someone asks her about the asylum."
    i "My condolences to you and your family."
    "I reached out and gently placed my hand on her hand, offering what little comfort I could."
    show lucy -l_cry
    "After a few moments of shared silence, her tears began to subside."
    lucy -l_eyes_closed"I would also like to apologize for lying to Alonso about this mission."
    "..."
    lucy l_eyes_look"You see, after my father tasked me to do this mission, Alonso was at the door already, listening I presume."
    lucy -l_eyes_look -l_mouth_serious "He asked me a ton of questions about the mission, so I fabricated it."
    lucy l_sweat "I told him it was a silly little exploration in the abandoned asylum."
    show lucy -l_base3
    show expression AlphaMask("images/others/flashlight.png", At("lucy -l_base3", center)) as l_mask
    lucy l_eyes_look"He then offered to join you and Raymon."
    lucy l_eyes_closedhappy"As much as I want to do this mission alone, I guess bringing a little bit of support would not mind."
    "So that's the story behind the mission..."
    "Alonso shouldn't really be snooping around other people's business."
    "Man."
    "But then again, Alonso doesn't want Lucy to go through this alone."
    lucy l_eyes_look l_mouth_serious -l_sweat "I do not want him to feel the sadness I am currently facing."
    i "I understand the weight of your situation..."
    i "But I think Alonso will understand if you reach out to him."
    i "Something tells me that he also wants to protect you."
    lucy -l_eyes_look"Is that so?"
    lucy l_eyes_look -l_mouth_serious "I am glad to have such a master who also looks after my wellbeing."
    i "Yeah..."
    stop music fadeout 1.5
    return

transform under_bed:
    xalign 0.5
    yalign 1.0
    easein 0.3 yalign 7.0

transform rise_bed:
    xalign 0.5
    yalign 7.0
    easein 0.3 yalign 1.0

label room2:
    $ wentBed = False
    $ wentLocker = False
    $ seenAlonso = False
    $ seenRaymon = False

    if room1_done == False and room2_done == False:
        call new_room
        
    if room2_done == False:
        $ room2_done = True
        scene bg bed with wipeleft_scene
        "The musty smell of abandonment fills my nostrils as we step inside."
        "The room was mostly empty at this point."
        "There's nothing here but a hospital bed and a locker across the room."
        play sound "audio/sfx/camera.mp3" volume 0.5
        show camera_flash
        "{bt=2}*click*{/bt}{fast}"
        raymon "Bed and a locker."
        if room1_done == False:
            raymon "Nice pick for starters, [Main]."
        raymon "Now, what do you want to to check out first?"
        label room2_choices:
            menu:
                "Let's go to..."
                "The bed." if wentBed == False:
                    $ wentBed = True
                    "A hospital bed sits with its metal frame rusted and worn."
                    "The thin mattress is torn and stained, and the pillow discolored with age."
                    "The bed seem to have been slept on by animals, judging from it."
                    play sound "audio/sfx/camera.mp3" volume 0.5
                    show camera_flash
                    "{bt=2}*click*{/bt}{fast}"
                    "I can't help but wonder how many patients have laid on this bed in the past."
                    show alonso
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                    with Dissolve(0.2)
                    alonso "Let me check underneath the bed."
                    show alonso at under_bed
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", under_bed)) as a_mask
                    "..."
                    alonso "I found err..."
                    raymon "What did you find?"
                    show alonso at rise_bed
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", rise_bed)) as a_mask
                    alonso a_brow_sad a_mouth_serious"A doll."
                    "The doll is ragged, with loose strings on each arm and its clothes."
                    "Upon taking a closer look, the doll has a pocket on its apron."
                    "In there lies a paper that's been folded to fit into the small pocket."
                    $ entry("doll_paper")
                    "I paused."
                    "..."
                    show alonso at centertoleft_transform
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", centertoleft_transform)) as a_mask
                    show raymon at easeright_transform
                    show expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                    raymon "What does it say?"
                    i "It's a note from a child."
                    i "The child seems to be treating the doll as if it was an actual person."
                    "Raymon takes the paper from my hand and reads it."
                    raymon r_brow_sad r_mouth_serious "It's a worse case of schizophrenia."
                    i "How can you say the child is schizophrenic?"
                    i "That's probably just their imagination, right?"
                    raymon "True, but why would a doll with a seemingly sad note end up in an asylum?"
                    raymon r_eyes_closed "The doll was probably taken away from the child with brute force when their parents sent the child here..."
                    alonso "That's a possible assumption."
                    show alonso at gocenter_transform
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", gocenter_transform)) as a_mask
                    show lucy l_brow_serious l_mouth_serious at easeleft_transform
                    show expression AlphaMask("images/others/flashlight.png", At("lucy", easeleft_transform)) as l_mask
                    lucy "I think we all should hurry. We do not have enough time to deal with a letter from a child."
                    lucy l_eyes_closed "If it has been left by the child in this place, we should not delve into it deeper."
                    show lucy -l_eyes_closed
                    i "Right, right... My bad."
                    hide lucy
                    hide raymon
                    hide alonso
                    hide expression AlphaMask("images/others/flashlight.png", At("alonso", centertoleft_transform)) as a_mask
                    hide expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                    hide expression AlphaMask("images/others/flashlight.png", At("lucy", centertoleft_transform)) as l_mask
                    with Dissolve(0.2)
                    "We leave the doll beside the bed."
                    jump room2_choices
                    
                "The locker." if wentLocker == False:
                    $ wentLocker = True
                    "We made our way the locker across the room."
                    window show
                    scene bg locker with wipeleft
                    window auto
                    "Against the wall is an old, dented locker with its paint chipped and peeling."
                    show alonso with Dissolve(0.2)
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                    alonso "I wonder if there's anything worth salvaging in here."
                    show alonso at centertoright_transform
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", centertoright_transform)) as a_mask
                    show lucy l_eyes_closedhappy l_sweat l_brow_sad at easeleft_transform
                    show expression AlphaMask("images/others/flashlight.png", At("lucy", easeleft_transform)) as l_mask
                    lucy "Master Alonso, I would appreciate if we leave things as they are."
                    lucy "We might disturb unwanted spirits."
                    alonso a_eyes_look a_sweat a_mouth_open a_brow_sad "Oh, right... Of course."
                    "I try to open the locker but as expected, it's locked tight."
                    show lucy -l_eyes_closedhappy -l_brow_sad -l_sweat l_mouth_serious
                    show alonso -a_eyes_look a_mouth_serious -a_sweat -a_brow_sad
                    raymon "Look at the locker door."
                    "There's a paper hanging from the side of the door gap."
                    "I take the paper."
                    $ entry("locker_paper")
                    i "There's a code."
                    i "That's... convenient."
                    i "The first 3 numbers are missing."
                    i "Where are we going to find the three numbers?"
                    alonso a_brow_sad a_eyes_closed"It'll take forever to crack that code!"
                    show expression AlphaMask("images/others/flashlight.png", At("alonso", right)) as a_mask
                    if room1_done == True:
                        i "Hmm..."
                        hide alonso
                        hide expression AlphaMask("images/others/flashlight.png", At("alonso")) as a_mask
                        with Dissolve(0.2)
                        show lucy at gocenter_transform
                        show expression AlphaMask("images/others/flashlight.png", At("lucy", gocenter_transform)) as l_mask
                        i "Lucy, give me the papers."
                        lucy l_base3"What do you need them for?"
                        show lucy l_mouth_serious
                        i "There's gotta be some sort clue we aren't seeing."
                        show lucy l_mouth_slightopen at centertoleft_transform
                        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", centertoleft_transform)) as l_mask
                        show raymon r_mouth_serious at easeright_transform
                        show expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                        raymon "What would be the correlation of random papers that we found on the previous room to the locker code?"
                        show alonso a_brow_sad a_mouth_serious
                        show expression AlphaMask("images/others/flashlight.png", At("alonso", center)) as a_mask
                        with Dissolve(0.2)
                        alonso "Don't you have something in your bag that can open it?"
                        show lucy -l_base3 -l_mouth_slightopen l_brow_sad
                        show expression AlphaMask("images/others/flashlight.png", At("lucy -l_base3", left)) as l_mask
                        show alonso -a_mouth_serious
                        raymon -r_mouth_serious"As a matter of fact, I do."
                        raymon r_eyes_closedhappy"Let me grab my crowbar."
                        hide lucy
                        hide raymon
                        hide alonso
                        hide expression AlphaMask("images/others/flashlight.png", At("alonso", centertoleft_transform)) as a_mask
                        hide expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                        hide expression AlphaMask("images/others/flashlight.png", At("lucy", centertoleft_transform)) as l_mask
                        with Dissolve(0.2)
                        play ambient "audio/sfx/crowbar.mp3" loop volume 0.7
                        "Raymon starts to open the locker with a crowbar."
                        "The sound of the clang echoes throughout the room."
                        "With that thick rust in the locker, I don't think it's going to give in."
                        "Nor the lock itself."
                        $ renpy.notify("Lucy gave you the papers.")
                        show lucy l_base3 l_brow_sad
                        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
                        with Dissolve(0.2)
                        lucy "Here, [Main]."
                        call room2_locker_choices
                        lucy "Do you have something in your mind?"
                        show lucy l_eyes_closedhappy -l_brow_sad
                        i "I think I might have."
                        hide lucy
                        hide expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
                        with Dissolve(0.2)
                        i "Raymon, can I try the lock code?"
                        raymon "Have you found something? We've been trying to open this to no avail."
                        alonso "At this point, I'm hoping if [Main] can actually open this."
                        stop ambient fadeout 2.5
                        i "Alright, let me just..."
                        call locker_code
                        call open_locker
                        lucy "This would greatly help."
                        if not LucySecret:
                            "How would a uniform alone help?"
                        raymon "Is that all?"
                        lucy "I believe so."
                        hide lucy
                        hide expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
                        with Dissolve(0.2)
                        jump room2_choices
                    else:
                        alonso -a_eyes_closed "Would a crowbar open the locker?"
                        show alonso at gocenter_transform
                        show expression AlphaMask("images/others/flashlight.png", At("alonso", gocenter_transform)) as a_mask
                        show raymon at easeright_transform
                        show expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                        raymon "As a matter of fact, it may..."
                        raymon "Let me grab my crowbar."
                        hide lucy
                        hide raymon
                        hide alonso
                        hide expression AlphaMask("images/others/flashlight.png", At("alonso", centertoleft_transform)) as a_mask
                        hide expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
                        hide expression AlphaMask("images/others/flashlight.png", At("lucy", centertoleft_transform)) as l_mask
                        with Dissolve(0.2)
                        play ambient "audio/sfx/crowbar.mp3" loop volume 0.7
                        "Raymon starts to open the locker with a crowbar."
                        "The sound of the clang echoes throughout the room."
                        stop ambient fadeout 1.5
                        show raymon r_brow_sad r_eyes_closed r_mouth_serious
                        show expression AlphaMask("images/others/flashlight.png", At("raymon", center)) as r_mask
                        with Dissolve(0.2)
                        raymon "Looks like it's shut tight."
                        if wentBed == False:
                            raymon -r_eyes_closed -r_brow_sad"Alright, let's look around to see if we can find some clues to open it."
                        else:
                            raymon r_eyes_look "We may have to resort to unlocking it using the code."
                        hide raymon
                        hide expression AlphaMask("images/others/flashlight.png", At("raymon", center)) as r_mask
                        with Dissolve(0.2)
                        jump room2_choices
            
            
            if room1_done == True:
                lucy "I think we have seen enough here."
                lucy "Is anyone ready to leave?"
                i "Yep."
                alonso "Uhuh."
                "Raymon nodded."
            else:
                # alonso "Well, we didn't find anything."
                lucy "Why don't we take a look at the other rooms?"
                i "Good idea."
            "We leave the room."
            jump asylum_mapping
    else:
        call screen dialog (message="There's nothing left to see here.", ok_action=Return())
    jump asylum_mapping


label open_locker:
    "It's a..."
    alonso "Bunch of clothes..."
    show lucy l_base3 l_brow_sad l_mouth_serious
    show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
    with Dissolve(0.2)
    "Lucy steps closer to the locker."
    lucy l_mouth_slightopen"Not just any clothes, it's nurse clothing."
    "Lucy takes the uniform."
    if LucySecret == True:
        show lucy:
            ease 0.7 blur 1 subpixel True yalign 0.0 zoom 2
        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask:
            ease 0.7 blur 1 subpixel True yalign 0.25 zoom 2

        "Then she discreetly comes closer to me."
        lucy -l_mouth_slightopen"...It's my mother's nurse uniform..."
        show lucy l_eyes_look l_sweat
        "She points out the ID with her mother's name in it."
        i "...Oh, it is..."
        "In the corner of my eye, I see something shiny from the clothes that Lucy holds."
        "Upon closer inspection, a locket emerges."
        "{i}To my beloved, Lucy.{/i}"
        i "...Lucy, I think this might be your mother's locket..."
        lucy -l_eyes_look l_mouth_slightopen -l_brow_sad"...Oh, it is..."
        lucy l_brow_sad l_eyes_look l_mouth_open"...I would like to take it from you, is that okay?..."
        i "...It's all good, I don't really have any use for it..."
        lucy l_eyes_closedhappy -l_mouth_open -l_sweat"Thank you."
        show lucy:
            ease 0.7 blur 0 subpixel True yalign 1.0 zoom 1
        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask:
            ease 0.7 blur 0 subpixel True yalign 1.0 zoom 1
        "Lucy takes the locket from me and leaves me be."
        hide lucy
        hide expression AlphaMask("images/others/flashlight.png", At("lucy l_base3", center)) as l_mask
        with Dissolve(0.2)
    else:
        show lucy -l_base3 l_eyes_look l_sweat -l_mouth_slightopen
        show expression AlphaMask("images/others/flashlight.png", At("lucy", center)) as l_mask
        "I really am hoping that she knows what she's doing."
        "It seems like she'll take anything that we see here."
        "Didn't she told us not to salvage the things lying around here?"
        "Very suspicious of her..."
    return

label room2_locker_choices:
    menu:
        "Let's see..."
        "Locker code." if room2_done == True:
            $ seenLocker = True
            $ entry("locker_paper")
            jump room2_locker_choices
        "Alonso's paper." if seenAlonso == False or True:
            $ seenAlonso = True
            $ entry("alonso_paper")
            jump room2_locker_choices
        "Raymon's papers." if seenRaymon == False or True:
            $ seenRaymon = True
            $ entry("entry1")
            $ entry("entry2")
            jump room2_locker_choices
        "Go back." if seenAlonso == True and seenRaymon == True:
            pass
    return

label locker_code:
    $ config.skipping = False
    $ code = renpy.input("What's the code?", length=5, allow='1234567890')
    if not code == "61593":
        "The lock doesn't budge."
        i "Dammit!"
        show lucy l_base2 l_brow_sad l_mouth_serious
        show expression AlphaMask("images/others/flashlight.png", At("lucy l_base2", center)) as l_mask
        with Dissolve(0.2)
        lucy "Are you sure you are remembering the order of the numbers?"
        menu:
            lucy "I can give you the papers if you need to look again."
            "\"Okay.\"":
                lucy "Here."
                call room2_locker_choices
                "I think I finally got it."
                hide lucy
                hide expression AlphaMask("images/others/flashlight.png", At("lucy l_base2", center)) as l_mask
                with Dissolve(0.2)
                jump locker_code
            "\"No, I've got this.\"":
                lucy "Alright, just making sure."
                hide lucy
                hide expression AlphaMask("images/others/flashlight.png", At("lucy l_base2", center)) as l_mask
                with Dissolve(0.2)
                jump locker_code
    else:
        play sound "audio/sfx/padunlock.mp3"
        "With a satisfying click, the lock had open itself."
        i "Yes!"
        show alonso a_mouth_open a_brow_serious a_eyes_closedhappy at easeleft_transform
        show expression AlphaMask("images/others/flashlight.png", At("alonso", easeleft_transform)) as a_mask
        alonso "Good job, [Main]!"
        show raymon r_brow_sad r_eyes_closed r_mouth_serious at easeright_transform
        show expression AlphaMask("images/others/flashlight.png", At("raymon", easeright_transform)) as r_mask
        raymon "Looks like we won't be needing our trusty crowbar."
        raymon r_brow_serious -r_eyes_closed"What bothers me is that, coincidentally, the papers did had the code."
        alonso -a_eyes_closedhappy"Well, what matters is that it's open."
        show alonso -a_mouth_open
        "I can't help but wonder what secrets might be hidden inside."
        hide raymon
        hide expression AlphaMask("images/others/flashlight.png", At("raymon", right)) as r_mask
        with Dissolve(0.2)
        show alonso at gocenter_transform
        show expression AlphaMask("images/others/flashlight.png", At("alonso", gocenter_transform)) as a_mask
        "Alonso opens the locker."
        hide alonso
        hide expression AlphaMask("images/others/flashlight.png", At("alonso")) as a_mask
        with Dissolve(0.2)
    return