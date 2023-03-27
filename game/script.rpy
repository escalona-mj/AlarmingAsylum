define persistent.Beginning = False
define dream_flag = False
define hungry_flag = False
label start:
    show black
    with dissolve_scene_full
    window auto
    "…"
    show text _("{i}Please… wake up.{/i}") at truecenter with wipeleft
    "An inaudible voice murmurs."
    show text _("{i}Why won't you wake up?{/i}") at truecenter with wipeleft
    "{i}\"You there, [Main]?\"{/i}"
    "...Huh?"
    show text _("{i}End our suffering...{/i}") at truecenter with wipeleft
    "{i}\"Hey, wake up.\"{/i}"
    "..."
    "I open my mouth but nothing comes out of it."
    "I feel like I'm slipping in and out of consciousness..."
    "Who are they?"
    show text _("{i}...{/i}") at truecenter with wipeleft
    "{i}\"Hello? Earth to [Main]?\"{/i}"
    "{i}\"This sleepyhead...\"{/i}"
    show text _("{sc=10}{size=+500}WAKE UP{/size}{/sc}") at truecenter  
    window hide(None)
    pause 0.2
    stop music
    hide text 
    window show(None)
    play ambient train loop
    show black behind train1

    #shaky train camera
    camera:
        pause 0.5
        choice:
            pause 1.0
        choice:
            easeout_back 0.5 yoffset -10
            easein_bounce 0.5 yoffset 0
        choice:
            easeout_back 0.5 yoffset -10
            easein_bounce 0.5 yoffset 0
        pause 0.5
        repeat
    
    #bg train1
    show train1
    show forestbackground behind train1:
        xalign 1.0
        linear 1 xalign 0.0
        repeat
    window auto

    $ achievement.grant("Beginning")
    if persistent.Beginning == False:
        $ renpy.display_notify("Achievement Get:\n\"Beginning\"")
        play sound "audio/sfx/notify.ogg"
        $ persistent.Beginning = True

    show merah neutral 
    i "Wh-wha?"
    "Something hard hit my forehead, causing me to jerk out."
    $ a1_name = "???" 
    a1 "[Main], wake up! You sleepyhead."
    a1 "And I thought I was the sleepy one..."
    "My eyes start to dart around to look at what's familiar and what isn't."
    $ a1_name = "Alonso" 
    i "Sorry [a1_name], I must have dozed off."
    "Stretching to gain energy, I stare blankly at the window, looking for an ounce of motivation."
    a1 "Why are you sleeping here alone?"
    a1 "There's plenty of space to sleep from the other side."
    i "I don't like people watching me sleep."
    a1 "{cps=9}Oh...{/cps}{w=0.5} {sc=2}U-understandable.{/sc}"
    "I know [a1_name]'s a great friend, but he shouldn't just wake some random stranger up."
    "I give him a disapproval look."
    a1 "{cps=5}Err...{/cps}"
    "He advertedly rolled his eyes down to avoid my gaze."
    "He isn't that bad, he just looks after my wellbeing."
    "I mean, that's what friends do, right?"
    "He looks strong and independent on the outside, but deep down that's not what he really is."
    a1 "Man... why do we have to go to an {sc=2}a-abandoned asylum?{/sc}"
    "There it is."
    a1 "{sc=2}I-it's not like I'm afraid or anything...{/sc}"
    i "We're only there to discover the history of the asylum as per the coordinator's request."
    i "Nothing else, as far as I know."
    a1 "Yeah, you're right."
    a1 "What am I getting scared of?"
    a1 "I'm the bravest among the group!"
    "He says that while proudly keeping his chest up."
    pause 3.0
    a1 "Anyway, we're almost there."
    "I try to yawn discreetly into my hand, but I guess it doesn't look discreet enough."
    a1 "Man, I keep telling you to take your vitamins."
    a1 "You won't last long in trips like these."
    i "Sorry, I keep forgetting it."
    "[a1_name] scoffs at me with worry."
    a1 "Yeah yeah, typical behavior of yours."
    a1 "You should probably start packing up."
    i "Good idea. I can see our destination."
    "I rummaged through my bag to see if I already have the necessities."
    "Do I have everything in here?"
    "Flashlight,{w=0.5} check."
    "Phone,{w=0.5} check."
    "Food,{w=0.5} check."
    "Notebook,{w=0.5} check."
    
    "Gun,{w=0.5} chec{nw}"
    $ _history_list[-1].what = "Self-defense items, check."
    "Wait, what?{fast}"

    "Right, first-aid...{w=0.5} check."
    "And then my supplements...{w=0.5} check."
    i "I guess I have everything right here."
    a1 "Alright, I'll go with the others. Care to join us?"
    menu:
        "\"Sure.\"":
            a1 "Okay. Come with me."
            "We left the current passenger wagon onto the other one."
            $ hungry_flag = True
            hide merah
            window hide
            show black with wipeleft_scene
            window auto
            jump char_intro
        "\"No thanks, I need some more time alone.\"":
            a1 "Take care."
            hide merah
            "[a1_name] leaves the scene, giving the passenger wagon to myself all alone."
            "The sound of the train ambience is so soothing, it's giving me enough focus on what matters."
            "Speaking on what matters..."
            "Oh right! The dream!"
            "There were voices that kept calling me to wake up."
            "..."
            "I'm not sure if that was just [a1_name] waking me up."
            show text _("{i}End our suffering...{/i}") at truecenter with wipeleft
            "But what do the voices mean about \"End our suffering...\"?"
            "That couldn't be [a1_name]."
            "..."
            show text _("{i}Suffering...{/i}") at truecenter
            "Am I missing some crucial information or something?"
            "..."
            hide text
            "Dreams do tend to not make sense."
            "I probably shouldn't give it too much attention."
            "..."
            "A lot of things are driving in my mind, and I'm not sure how will I handle this information."
            "I'm probably just overthinking."
            #play hungry sound
            window hide
            pause 3.5
            window auto
            "Dammit. I was hoping they'd at least offer some breakfast."
            "Should I eat the food I brought along now?"
            menu:
                "Yes.":
                    "Maybe I'll eat some biscuits."
                    "It won't hurt to eat it, right?"
                    "*munch*{w=1.5} *munch*{w=1.5} *munch*"
                    
                "No.":
                    "Keep it together, [Main]."
                    "Just a few more minutes and I'll be out of this miserable train."
                    $ hungry_flag = True
            # "This train, I mean."
            # "This transportation costed us more than my entire savings in a month!"
            # "Luckily my money accumulated, so I think I won't be dealing with running out of money anytime soon."
            window hide
            pause 5.0
            window auto
            "Well, this is boring."
            "I should've brought my book to pass the time."
            "I think I'll snooze off again..."
            window hide
            $ dream_flag = True
            pause 5.0
    
    
    label char_intro:
        if dream_flag == True:
            window show(None)
            a1 "{size=+50}[Main!u]!{/size}{fast}" with vpunch
            window auto
            i "Gah! What the fu-{w=0.5}{nw}" with vpunch
            i "Don't sneak behind me like that..."
            "Like a cat with a cucumber on its behind, I pounced out of my seat."
            
        else:
            a1 "Hey everyone! [Main]'s awake!" with vpunch
            i "Jeez, you didn't have to announce my awakening."
            
        a1 "Hehe, sorry."
        $ m1_name = "???" 
        m1 "Greetings, [Main]."
        $ m1_name = "Lucy" 
        i "Oh, [m1_name]."
        if hungry_flag == True:
            "[m1_name] approaches me and offered to join at her table."
            "As I approach the table, she goes back to the kitchen."
            "Wait, do trains have kitchens?"
            pause 2.0
            window auto
            "I lightly shake my head." with hpunch
            "That's not important! I'm more invested on what [m1_name] has in store for me."
            "The scent alone from the kitchen swiftly made its way to my nose which made me drool."
            "Soon after, [m1_name] comes out of the kitchen as she brings my plate."
            m1 "I noticed that you look off today..."
            m1 "So I prepared you some breakfast."
            ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"
            pause 2.0
            window auto
            m1 "Hello? Earth to [Main]?"
            "I look at her with a bewildered expression."
            "[m1_name] chuckles back."
            m1 "What are you waiting for? Eat."
            menu:
                "\"T-thank you for the food!\"":
                    m1 "My pleasure."
                "Eat.":
                    pass
            "Surprisingly, the food tastes pretty good."
            "I can't tell what some of the spices are, but they blend together nicely."
        else:
            "[m1_name] pours a glass of what it seems to be water and offers it to me. It's fizzing a bit, and almost looks carbonated."
            "I give it a sniff. It smells kind of fruity."
            m1 "Go ahead, you look thirsty."
            i "Thanks."
            "I take a sip on the carbonated water."
            "The fizzing sensation of the water soothes my dried mouth."
            "I am refreshed!"
            pause 1.0

        "Though I am quite surprised, she always looks after us even if conflict stirs up in the group."
        "I have to say, where does she even get the determination to deal with our stupidity?"
        "She's quite an amazing woman. She has never shown any vulnerabilities since we've met her."
        "She's an all-in-one-package! Matured, independent... I can never be as good as her."
        "It's as if she's like a butler..."
        "On second thought..."
        i "How do you do it?"
        m1 "Do what?"
        i "You know, deal with us. Our group is vast, each with their own unique personalities."
        i "I'm surprised that you can manage to adjust according to our interests."
        "[m1_name] giggles from my compliment."
        m1 "I've seen the world far more than you know."
        i "Really? What of it?"
        m1 "Maybe later. But right now, why don't you go with the others? I'll clean up."
        i "Oh, okay."
        "Just as I leave [m1_name], I looked back at her with sincerity."
        i "By the way..."
        i "Thanks [m1_name]."
        extend " For everything."
        i "Seeing where you are now, I guess you needed a single thank you from us."
        "[m1_name] smiled back to me and went back to cleaning."
        "So, where are they?"
        "I walked across the long hallway of this passenger wagon to find the others."
        "Soon, I heard faint voices growing stronger."

        a1 "...How's the situation, [m2_name]? Got any updates?"
        m2 "One of the coordinators got in touch with me a while ago."
        m2 "As far as we know, we're going to rendezvous in a forgotten asylum deep within the forest to discover the tragic history behind it."
        m2 "However, they changed our plans in the last minute."
        m2 "Our new task is to investigate the anomalies that have been occurring there."
        a1 "What anomalies?"
        m2 "They updated me that there's a signal coming from the place."
        m2 "It's bizarre that the sanctum is capable of emitting signals..."
        m2 "There's no electricity there..."
        "I see [a1_name] somewhat shivering after hearing [m2_name]'s words."
        "[m2_name] then shoves out an odd device from his pocket, with an antenna protruding from the top side."
        "What device even is that?"
        m2 "Even in here, it picks up the waves."
        "Oh..."
        "His ways of using available technology we currently have is somewhat mesmerizing."
        "I couldn't even comprehend his words."
        "Does he think lowly of us?"
        "I mean, I can somewhat understand him, but he tries his best to make it comprehensible for us."
        "Which...{w=0.5} ends up poorly executed."
        "I have to search my phone to find the definitions of his words."
        "He reminds me of a person who uses sugarcoating on his essa{nw}"
        $ _history_list[-1].what = "I find his words hard to describe."
        a1 "Oh! [Main], you're here."
        m2 "Hello, [Main]."
        m2 "As much as I do NOT want to embark in an abandoned haven..."
        m2 "That is, if you can still label it like that..."
        m2 "We're being waged to do our part."
        i "Is that so?"
        i "If it's offering more money than we initially agreed on, then I'm in."
        a1 "Woah, woah, woah, woah!"
        a1 "Not so fast!"
        a1 "[m2_name], surely we won't be staying there for too long right?"
        m2 "3 days."
        a1 "{sc}3 d-days?!{/sc}"
        "Wait what?!"
        "My eyes grew wide."
        "I thought we're only investigating the asylum?"
        "I smell trouble..."
        m2 "There's still the reward money after all of this."
        m2 "It's worth it."
        camera
        scene bg trainstation blurred with wipeleft_scene
        
        i "We're here."



        

return
