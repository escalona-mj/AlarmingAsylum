label scene_2:
    "A large door stands in front of us."
    "No matter how much strength I put to open the door, it won't budge."
    a1 "This door seems stuck."
    a1 "Raymon, do you have something that can open this door?"
    show bg door:
        linear 5.0 yalign 0.5
    a1 "Like a key or something?"
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
    play music asylum volume 0.7
    "As I entered the asylum, I saw the remnants of its dark history."
    "There were old medical equipment, broken beds, and strange markings on the walls."
    "This place screams prison."
    $ config.skipping = False
    $ renpy.notify("Saving the game is recommended.")
    play sound "audio/sfx/warning.mp3" volume 0.2
    a1 "There aren't any... g-ghosts here, right?"
    raymon "No Alonso. Besides, aren't you a bit too old to be scared of ghosts?"
    a1 "Yeah, it's probably because I've gotten attached to superstitious beliefs..."
    a1 "And this place reeks."
    "I don't blame Alonso. The air was heavy with the stench of decay."
    "Despite the grim atmosphere, I carefully look at my surroundings to see if I can find something that can help Lucy on her mission."
    play sound "audio/sfx/camera.mp3" volume 0.5
    "{bt=2}*click*{/bt}{fast}"
    raymon "This place looks straight out from a movie."
    raymon "Oh, and there're some empty rooms over there."
    play sound "audio/sfx/flashlight.mp3"
    "I opened my flashlight and pointed out to the rooms."
    "No matter how bright my flashlight is, the room I'm pointing at is still pitch black."
    raymon "Why don't we split up?"
    "What?"
    "What kind of suggestion is that?"
    a1 "Uh, no thank you. You're asking for death."
    i "He's right!"
    lucy "I appreciate the suggestion that you want to make my mission go a lot smoother..."
    lucy "But I cannot overlook such a lousy decision for my convenience."
    lucy "We all have to stick together."
    raymon "I see."
    raymon "[Main], do you have a preference?"
    i "Well, if it'll get this job done sooner, then I don't see a problem."

define room1_done = 0
define room2_done = 0
define room3_done = 0
define LucySecret = False

label asylum_mapping:
    $ config.rollback_enabled = True
    $ config.skipping = False #pauses skipping if turned on
    scene bg asylum with dissolve
    if room1_done == 1 and room2_done == 1:
        "waht the fucj"
    if persistent.reminder == None:
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
    
    $ wentAlonso = False
    $ wentRaymon = False
    $ wentLucy = False
    $ menuchoice = 0

    if room1_done == 0:
        if room1_done == 0 and room2_done == 0:
            call new_room
        $ room1_done = 1
        scene bg office with wipeleft_scene
        "As expected, the room is a mess."
        "Books are scattered across the floor along with desks that are almost unrecognizable due to its state."
        "There's also a marking on the wall that says \"School sucks!\"."
        play sound "audio/sfx/camera.mp3" volume 0.5
        "{bt=2}*click*{/bt}{fast}"
        a1 "This must be the office."
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
                    "I proceeded to help Alonso."
                    "I see him wandering aimlessly at the corner of the room."
                    "He seems to be looking for something."
                    a1 "Oh [Main]! Come here quick!"
                    a1 "I found a desk."
                    "The desk is covered in layers of dust and cobwebs."
                    "The once polished surface of the desk is now dull and scratched, and the wood is warped and split in places."
                    "The desk looks like it hasn't been used in years, perhaps even decades."
                    a1 "I can't seem to open the drawer though."
                    i "Let me try."
                    "I grasp the handle, tightly in my hand, but it's shut tight and won't budge when I try to pull it open."
                    "Determined, I try again with more force."
                    play sound "audio/sfx/hinge_squeak.mp3"
                    "And with a creaking sound, the drawer finally gives way."
                    "I was taken aback by my force, but I managed to regain my composure."
                    "My excitement turns to horror as I see a decaying snake lying coiled up in the drawer."
                    i "What the hell!" with vpunch
                    a1 "What?! {w=0.2}What?!{w=0.2} What?!"
                    "Alonso paces towards me and the desk."
                    a1 "Oh. It's a dead snake..."
                    a1 "What's a dead snake doing in a drawer?"
                    i "Maybe food?"
                    "Alonso examines the snake's corpse."
                    i "Stay away from that thing."
                    a1 "Relax, it's dead."
                    i "Okay, but leave it alone."
                    i "It has suffered long enough trapped in that drawer."
                    a1 "Okay."
                    "Looking at the old desk, I examine the rest of the drawers."
                    "As I rummage through each of the drawers, one drawer had a paper in it."
                    "The edges are frayed and torn, and the paper has yellowed with age."
                    "It also had a distinct scent, a musty smell that is reminiscent of old books and antique stores."
                    a1 "Oh, you found something. What does it say?"
                    "I look at the paper, which left a seemingly bizzare note."
                    $ entry("alonso_paper")
                    "Nurse A  c ...?"
                    if LucySecret == True:
                        "A l i c e..."
                        "Nurse Alice..."
                        "Lucy's mother."
                        i "She must have cured the patient."
                        a1 "She?"
                    else:
                        i "Who's Nurse A   c ?"
                        a1 "Nurse Ay-see?"
                    "Alonso takes the paper from my hand."
                    a1 "Looks like someone didn't get to keep their legs."
                    "I look to Alonso with a glowering expression."
                    i "Alonso! Rude."
                    a1 "Sorry."
                    "Judging from the handwriting, the note seems to be written by a child."
                    i "How can you joke at a disabled child's letter?"
                    a1 "Oof, now I feel even more bad."
                    a1 "Okay, I'm sorry."
                    i "Don't apologize to me! Apologize to the child."
                    i "Even if they're not here anymore."
                    "Alonso turns around and clasps both of his hands."
                    a1 "{size=-25}Forgive me.{/size}"
                    "I shake my head."
                    "The child must be so grateful to the nurse that they made a letter just for her."
                    "That's... heartwarming."
                    "I wonder how the nurse reacted to such a dearing letter."
                    i "This paper might be helpful."
                    $ renpy.notify("You take the paper.")
                    a1 "To be honest, if we see any old paper here with information written on it, it's probably important."
                    i "Pretty much."
                    if menuchoice == 2:
                        pass
                    else:
                        i "I'll look for the others. Will you be okay alone?"
                        a1 "Yeah. I'll stay here and look around."
                        i "Okay. Take care."
                        "I leave Alonso in his business."
                        jump room1_choices
                "Help Raymon." if wentRaymon == False:
                    $ menuchoice += 1
                    $ wentRaymon = True
                    "I proceeded to help Raymon."
                    "I see him fully delved into the scattered books, searching for any relevant information we might pick up."
                    raymon "Oh, [Main]! Didn't see you there."
                    i "Found anything?"
                    raymon "Not really. Most of the books are burned, and some are torn apart."
                    raymon "Though I spotted a filing cabinet."
                    "Raymon points out the filing cabinet."
                    "Its metal exterior is covered in rust and grime, and the drawers are jammed tight with decades of neglect."
                    "It seems the content of the cabinet is still intact, judging from the folders peeking from the side."
                    raymon "It is shut tight, possibly from the rust."
                    raymon "Luckily, I have brought a crowbar."
                    "Raymon whips out a crowbar from the side of his bag."
                    i "Do you even know how to use it?"
                    raymon "Of course! Now why would I bring a crowbar if I didn't know how to use it in the first place?"
                    play sound "audio/sfx/crowbar.mp3" loop volume 0.7
                    "With a determined look on his face, he grasp the crowbar tightly in his hand."
                    "Raymon brings the crowbar down with all his might, striking the top of the cabinet with a resounding clang."
                    stop sound fadeout 1.5
                    play sound "audio/sfx/hinge_squeak.mp3"
                    "After several tense moments, a satisfying crack can be heard, and a section of the cabinet's top breaks away, revealing the insides."
                    play sound "audio/sfx/rats.mp3" loop volume 0.5
                    "However, when opened, Raymon had unleashed two small creatures that darted out from the file cabinet."
                    raymon "AHHH! GET IT OFF ME!" with vpunch
                    "The rats are small and scraggly, with matted fur and beady eyes that seem to follow the Raymon's every move."
                    "They move quickly and without fear, scampering around Raymon's body."
                    raymon "[Main!u], HELP ME!"
                    raymon "MY BAG, QUICKLY!"
                    "I quickly grabbed Raymon's bag to see if he has anything to stop these rats."
                    "What am I suppose to grab here?!"
                    raymon "Wait, nevermind [Main]!"
                    raymon "Look!"
                    "The rats don't seem to be aggressive. In fact, they're even not attacking him."
                    i "Are they harmless?"
                    "One of the rats reach out to Raymon's pocket."
                    raymon "Oh, you want this?"
                    "Raymon pulls out a snack bar from his pocket."
                    "He opens it and gives it to the rats."
                    i "I guess they were only searching for food."
                    raymon "They must have been trapped in that file cabinet."
                    stop sound fadeout 1.5
                    "Slowly, we relax, and watch as the rats disappear into the darkness and leaves us alone."
                    "..."
                    raymon "That was something?"
                    i "Yeah."
                    i "Why don't we go and take a look at the cabinet you just opened?"
                    raymon "I almost forgot about that."
                    play sound "audio/sfx/filecabinetopen.mp3" volume 0.5
                    "We opened the cabinet."
                    "The drawers are filled with old files and papers, with the edges yellowed and brittle with age."
                    "Raymon sifts through the folders and runs his fingers over the documents, feeling the rough texture of the paper."
                    i "Well?"
                    raymon "Interesting. These are patient entries."
                    raymon "Take a look. Though this one is a bit harder to read."
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
                        "Lucy's mother."
                        "I carefully read the last statement again."
                        "..."
                        "This patient got discharged by Lucy's mother."
                        raymon "What did you find?"
                    else:
                        i "Who's Nurse A  c ?"
                        raymon "Nurse Ey-ssi?"
                    "Raymon dashes towards me."
                    raymon "Interesting."
                    raymon "..."
                    raymon "So you know that asylums were used as long-term care facilities for people with mental illnesses, right?"
                    i "Yeah?"
                    raymon "Even though many of these facilities focused on custodial care, such as keeping patients fed, clothed, and sheltered..."
                    raymon "In some cases, patients were subjected to inhumane treatments, including physical and emotional abuse..."
                    raymon "Along with experimentation with unproven medical treatments."
                    raymon "However, this nurse managed to get a chronic-mentally ill patient to be cured and discharged, something that was very rare back then."
                    i "That's amazing."
                    if LucySecret == True:
                        "She's quite an astounding nurse."
                        "The fact that she managed to discharge a patient during times when medical knowledge was still limited..."
                    i "I kinda thought that asylums are eternal prisons for the mental."
                    i "Like, once you go in there... you're never leaving..."
                    i "Because of the limited knowledge available back then in the field of psychology or science or something..."
                    raymon "Well you're not wrong."
                    raymon "But you are also quite wrong."
                    "I look to Raymon with a confused expression."
                    i "What's that even supposed to mean?"
                    "We exchanged laughs."
                    $ renpy.notify("You take the paper.")
                    i "I'll take this paper just in case."
                    raymon "Be my guest."
                    # raymon "Well, what do you expect from an abandoned asylum?"
                    # raymon "I would be surprised if one of the patients were still alive."
                    # raymon "All of these were dated back decades ago."
                    # raymon "It would take a miracle if one of them were to show up and haunts us, ahaha."
                    play sound "audio/sfx/filecabinetclose.mp3" volume 0.3
                    "Raymon closes the file cabinet."
                    if menuchoice == 2:
                        pass
                    else:
                        raymon "Oh! Feel free to leave, I'm going to stay here and see if I can find more."
                        i "Okay."
                        "I leave Raymon in his business."
                        jump room1_choices
                "Help Lucy." if wentLucy == False:
                    $ menuchoice += 1
                    $ wentLucy  = True
                    "I proceeded to help Lucy."
                    "She seems to be examining the books that are scattered across the floor."
                    "There's not much to describe what she's doing."
                    lucy "Oh, [Main]."
                    lucy "I was just glancing at the records here."
                    "Lucy hands over the files."
                    "The files are varied from adminstrative records, patient files, and prescription medications."
                    lucy "By the way..."
                    lucy "Would you like to know a secret?"
                    menu:
                        "\"Sure.\"":
                            lucy "If you must know, it is a family secret."
                            "Family?"
                            call secret_lucy
                        "\"I don't think I'm suppose to know about it...\"":
                            lucy "I see."
                    "We go through each desk and cabinet we can find."
                    "Eventually, Lucy finds a document."
                    if LucySecret == True:
                        lucy "I finally found my mother's documents."
                        "Lucy gives me the file."
                        "Surpisingly, the document is still intact with complete information."
                        $ entry("lucy_paper")
                        "Alice. That's a nice name."
                        if wentAlonso == True or wentRaymon == True:
                            "The name fits perfectly to the notes we found."
                        i "So, your mother's name is Alice?"
                        lucy "Yes. Such an elegant name, is it not?"
                        "Lucy holds the document dearly."
                        lucy "The only thing left to do is find my mother."
                        lucy "After that, we can finally go home."
                    else:
                        lucy "I finally found something that is crucial to our mission."
                        lucy ""
                    i "That's great."
                    if menuchoice == 2:
                        pass
                    else:
                        if LucySecret == True:
                            lucy "I'm going to stay here and see if I can find more documents about my mother."
                        else:
                            lucy "I'm going to stay here and see if I can find more necessary intel."
                        i "Okay."
                        "I leave Lucy in her business."
                        jump room1_choices
            lucy "Okay everyone."
            lucy "Have you all found something?"
            if wentAlonso == True:
                a1 "We sure did."
                a1 "[Main], give the paper to Lucy."
                $ renpy.notify("You gave the paper.")
                i "Alright."
            else:
                a1 "I sure did."
                a1 "I found a note."
                a1 "The handwriting looked like it belong to a child."
                a1 "It's quite a heartwarming one, with the last sentence thanking {i}\"Nurse a  c \"{/i}."
            a1 "Also found a dead snake in a drawer, if anyone wants to know."
            if LucySecret == True:
                "I see Lucy's eyes flashed for a while."
            else:
                pass
            lucy "Thank you for the letter."
            if wentRaymon == True:
                raymon "We also found something."
                raymon "Oh [Main], would you kindly give Lucy the papers we found?"
                $ renpy.notify("You gave the paper.")
                i "Okay."
            else:
                raymon "I also found something."
                raymon "Patient entries."
                raymon "Some of the entries have become unintelligble, torn or destroyed..."
                raymon "So I picked up and chose the entries that are still legible."
                raymon "Though, one certain nurse piqued my interest. Her name is faded out, but it spells, {i}\"Nurse a  c \"{/i}."
            raymon "Something silly happened to me a while ago. Rats crawled over my body as soon as I opened the cabinet containing the entries I found."
            raymon "Craziest shid, I tell you."
            if LucySecret == True:
                "For the second time, I saw Lucy flashed her eyes once more."
                "It seems like she's shocked about how her mother managed to do all of this."
                "Her mother must be highly respected by both patients and staff members, judging from the letters they found."
            else:
                pass
            lucy "Thank you all for gathering all the documents you can find."
            lucy "These letters are great fundamentals for my investigation that confirms my suspicions."
            if LucySecret == True:
                "I don't think letters alone are enough to find her mother."
            if room2_done == True:
                i "Lucy, can I have those papers back? I'd like to see something."
                "I take the papers from Lucy."
                "These letters must have something hidden in plain sight."
                call room2_locker_choices
                "I think I got it."
                i "Guys, we might have a clue for the locker."
                a1 "Are you sure? Then lead the way!"
                "We went back to the other room."
                scene bg locker with wipeleft_scene
                "Things stood still since we left here."
                "Let's see..."
                call locker_code
                call open_locker
                
            lucy "I am guessing that there is nothing left to find in this room."
            lucy "[Main], should we get going?"
            i "Yeah, sure."
            lucy "Then let us."
            "We peacefully make our way out of the room."
    else:
        "We've already went there."
    jump asylum_mapping
    
label secret_lucy:
    $ LucySecret = True
    lucy "My mother used to work in this very asylum as a nurse."
    i "Wait what?"
    "I look to Lucy with a wide-eyed expression."
    lucy "You must be so shocked right now..."
    lucy "But yes, my mother."
    lucy "Even if her workplace was not as good as asylums are now..."
    lucy "She helped most of the patients treated here."
    lucy "My father told me she was an astounding nurse."
    lucy "She was the only nurse who has been able to discharge a patient; a moment where no one has achieved before."
    lucy "But one fateful day, mother never returned home."
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
    lucy "Yes. My father was the one who assigned me to this mission."
    lucy "He asked me to find any traces of her and retrieve her body."
    lucy "..."
    "She pauses for a moment as tears stream down her face."
    lucy "I am sure my mother is dead right now."
    lucy "And it would be nice if we can get this mission done as soon as possible."
    lucy "So that my father and I can get her a proper burial."
    i "I see. I didn't know..."
    "No wonder she pauses everytime when someone asks her about the asylum."
    i "My condolences to you and your family."
    "I reached out and gently placed my hand on her hand, offering what little comfort I could."
    "After a few moments of shared silence, her tears began to subside."
    lucy "I would also like to apologize for lying to Alonso about this mission."
    lucy "I do not want him to feel the sadness I am currently facing."
    i "I understand the weight of your situation..."
    i "But I think Alonso will understand if you reach out to him."
    i "Something tells me that he also wants to protect you."
    lucy "Really? I am glad to have such a master who also looks after my wellbeing."
    i "Yeah..."
    lucy "Alright, that is enough drama for one day, ahaha."
    "For a butler, I thought she's emotionless; an expert."
    "But she's still human, with feelings..."
    lucy "Shall we?"
    "I nod."
    return

label room2:
    $ wentBed = False
    $ wentLocker = False
    $ seenAlonso = False
    $ seenRaymon = False

    if room1_done == 0 and room2_done == 0:
        call new_room
        
    if room2_done == 0:
        $ room2_done = 1
        scene bg bed with wipeleft_scene
        "The musty smell of abandonment fills my nostrils as we step inside."
        "The room was mostly empty at this point."
        "There's nothing here but a hospital bed and a locker across the room."
        play sound "audio/sfx/camera.mp3" volume 0.5
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
                    "I can't help but wonder how many patients have laid on this bed in the past."
                    a1 "Let me check underneath the bed."
                    "Alonos checks underneath the bed."
                    a1 "I found err..."
                    raymon "What did you find?"
                    a1 "A doll."
                    "The doll is ragged, with loose strings on each arm and its clothes."
                    "Upon taking a closer look, the doll has a pocket on its apron. In there lies a paper that's been folded to fit into the small pocket."
                    $ entry("doll_paper")
                    "I paused."
                    "..."
                    raymon "What does it say?"
                    i "It's a note from a child."
                    i "The child seems to be talking to the doll as if it was an actual person."
                    "Raymon takes the paper from my hand and reads it."
                    raymon "It's a worse case of schizophrenia."
                    i "How can you say the child is schizophrenic?"
                    i "That's probably just their imagination, right?"
                    raymon "True, but why would a doll with a seemingly sad note end up in an asylum?"
                    raymon "The doll was probably taken away from the child with brute force when their parents sent the child here..."
                    a1 "That's a possible assumption."
                    lucy "I think we all should hurry. We do not have enough time to deal with a letter from a child."
                    lucy "If it has been left by the child in this place, we should not delve into it deeper."
                    i "Right, right... My bad."
                    "We leave the doll beside the bed."
                    jump room2_choices
                    
                "The locker." if wentLocker == False:
                    $ wentLocker = True
                    "We made our way the locker across the room."
                    window show
                    scene bg locker with wipeleft
                    window auto
                    "Against the wall is an old, dented locker with its paint chipped and peeling."
                    a1 "I wonder if there's anything worth salvaging in here."
                    lucy "Master Alonso, I would appreciate if we leave things as they are."
                    lucy "We might disturb unwanted spirits."
                    a1 "Oh, right... Of course."
                    "I try to open the locker but as expected, it's locked tight."
                    raymon "Look at the locker door."
                    "There's a paper hanging from the side of the door gap."
                    "I take the paper."
                    $ entry("locker_paper")
                    i "There's a code."
                    i "The first 3 numbers are missing."
                    i "Where are we going to find the three numbers?"
                    a1 "It'll take forever to crack that code!"
                    if room1_done == True:
                        i "Hmm..."
                        i "Lucy, give me the papers."
                        lucy "What do you need them for?"
                        i "There's gotta be some sort clue we aren't seeing."
                        raymon "What would be the correlation of random papers that we found on the previous room to the locker code?"
                        a1 "Don't you have something in your bag that can open it?"
                        raymon "As a matter of fact, I do."
                        raymon "Let me grab my crowbar."
                        play ambient "audio/sfx/crowbar.mp3" loop volume 0.7
                        "Raymon starts to open the locker with a crowbar."
                        "The sound of the clang echoes throughout the room."
                        "With that thick rust in the locker, I don't think it's going to give in."
                        "Nor the lock itself."
                        lucy "Here, [Main]."
                        "Lucy gives the papers we collected."
                        call room2_locker_choices
                        lucy "Do you have something in your mind?"
                        i "I think I might have."
                        i "Raymon, can I try the lock code?"
                        raymon "Have you found something? We've been trying to open this to no avail."
                        a1 "At this point, I'm hoping if [Main] can actually open this."
                        stop ambient fadeout 2.5
                        i "Alright, let me just..."
                        call locker_code
                        lucy "This would greatly help."
                        if not LucySecret:
                            "How would this help?"
                    else:
                        a1 "Would a crowbar open the locker?"
                        raymon "As a matter of fact, it may..."
                        raymon "Let me grab my crowbar."
                        play ambient "audio/sfx/crowbar.mp3" loop volume 0.7
                        "Raymon starts to open the locker with a crowbar."
                        "The sound of the clang echoes throughout the room."
                        stop ambient fadeout 2.5
                        raymon "Looks like it's shut tight."
                        raymon "We may have to resort to unlocking it using the code."
                        raymon "Alright, let's look around to see if we can find some clues to open it."
                        jump room2_choices
            
            
            if room1_done == True:
                lucy "I think we have seen enough here."
                lucy "Is anyone ready to leave?"
                i "Yep."
                a1 "Uhuh."
                "Raymon nodded."
            else:
                a1 "Well, we didn't find anything."
                lucy "Why don't we take a look at the other rooms?"
                raymon "Good idea."
            "We leave the room."
            jump asylum_mapping
    else:
        "We've already went there."
    jump asylum_mapping


label open_locker:
    "It's a..."
    a1 "Bunch of clothes."
    "Lucy steps closer to the locker."
    lucy "Not just any clothes, it's nurse clothing."
    "Lucy takes the uniform."
    if LucySecret == True:
        "Then she discreetly comes closer to me."
        lucy "...It's my mother's nurse uniform..."
        "She points out the ID with her mother's name in it."
        i "...Oh, it is..."
        "In the corner of my eye, I see something fall from the clothes that Lucy holds, shining in the floor."
        "Upon closer inspection, a locket emerges."
        "{i}To my beloved, Lucy.{/i}"
        i "...Lucy, I think this might be your mother's locket..."
        lucy "...Oh, it is..."
        lucy "...I'd like to take it from you, is that okay?..."
        i "...It's all good, I don't really have any use for it..."
        "Lucy takes the locket from me and leaves me be."
    else:
        "I am really hoping that she knows what she's doing."
        "It seems like she'll take anything that we see here."
        "Didn't she told us not to salvage the things lying around here?"
        "Very suspicious of her..."
    return

label room2_locker_choices:
    menu:
        "Let's see..."
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
    $ code = renpy.input("What's the code?", length=5, allow='1234567890')
    if not code == "61593":
        "The lock doesn't budge."
        i "Dammit!"
        lucy "Are you sure you are remembering the order of the numbers?"
        menu:
            lucy "I can give you the papers if you need to look again."
            "\"Okay.\"":
                lucy "Here."
                call room2_locker_choices
                "I think I finally got it."
                jump locker_code
            "\"No, I've got this.\"":
                lucy "Alright, just making sure."
                jump locker_code
    else:
        play sound "audio/sfx/padunlock.mp3"
        "With a satisfying click, the lock had open itself."
        i "Yes!"
        a1 "Good job, [Main]!"
        raymon "Looks like we won't be needing our trusty crowbar."
        raymon "Coincidentally, the papers did had the code."
        a1 "What matters is that it's open."
        "I can't help but wonder what secrets might be hidden inside."
        "Alonso opens the locker."
    return

label room3:
    $ config.skipping = False
    if room1_done == 1 and room2_done == 1:
        $ room3_done = 1
        "This is room 3."
    else:
        "Seems like there's something blocking the way."
        "I think I'll go check out the other rooms first."
    jump asylum_mapping