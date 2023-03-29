define persistent.Beginning = False
define dream_flag = False
define hungry_flag = False
define window_scene = None
label start:
    show black
    with dissolve_scene_full
    
    window auto
    "…"
    show text _("{i}Please… wake up.{/i}") at truecenter with wipeleft
    "An inaudible voice murmurs towards me."
    "..."
    show text _("{i}Why won't you wake up?{/i}") at truecenter with wipeleft
    "{i}\"You there, [Main]?\"{/i}"
    "...Huh?"
    show text _("{i}Seek out the truth...{/i}") at truecenter with wipeleft
    "{i}\"Hey, wake up.\"{/i}"
    "..."
    "I open my mouth but nothing comes out of it."
    show text _("{i}Truth.{/i}") at truecenter with wipeleft
    "I feel like I'm slipping in and out of consciousness..."
    "{i}\"Maybe I shouldn't wake [Main] up...\"{/i}"
    "What do they want from me?"
    show text _("{i}...{/i}") at truecenter
    "{i}\"Hello? Earth to [Main]?\"{/i}"
    "{i}\"This sleepyhead...\"{/i}"
    show text _("{sc=10}{size=+500}WAKE UP{/size}{/sc}") at truecenter  
    window hide(None)
    pause 0.2
    stop music
    hide text

    window show(None)
    play ambient train volume 0.6 loop

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
    "Something hard hit my face, causing me to jerk out."
    $ a1_name = "???" 
    a1 "[Main], wake up! You sleepyhead."
    a1 "And I thought I was the sleepy one..."
    "My eyes start to dart around to look at what's familiar and what isn't."
    $ a1_name = "Alonso" 
    i "Sorry [a1_name],{w=0.2} I must have dozed off."
    a1 "I tried waking you up earlier, but you wouldn't budge."
    "I know [a1_name]'s a great friend, but he shouldn't just wake people up."
    "Unless it's an emergency."
    "Stretching to gain energy, I stare blankly at the window, looking for an ounce of motivation."
    a1 "Why are you sleeping here alone?"
    a1 "There's plenty of space to sleep from our side though."
    i "I don't like people watching me sleep."
    i "Even if we're the only ones here."
    window hide
    pause 2.0
    window auto
    "There's an awkward silence."
    "I think there's something we both wanted to say."
    "Thankfully, [a1_name] breaks the silence."
    a1 "Well...{w=0.2} aren't you excited?"
    i "I'm excited to leave once everything is over."
    a1 "You'll be fine. We'll take great care of you."
    "I scoffed then gave him a disapproval look."
    "He isn't that bad, he just looks after my wellbeing."
    "I mean, that's what friends do, right?"
    a1 "Man... why do we have to go to an {sc=2}a-abandoned asylum?{/sc}"
    i "What? Are you scared?"
    i "Don't tell me you're scared?"
    a1 "No! {sc=2}I-it's not like that or anything...{/sc}"
    i "We're only there to discover the history of the asylum as per the coordinator's request."
    i "Nothing else, as far as I know."
    a1 "Yeah, you're right."
    a1 "But I just can't help but wonder, what will happen to us?"
    a1 "What if something bad happens to us?"
    a1 "Just the thought of it scares me."
    i "Pfft, you've been watching too many horror documentaries."
    i "We're going to be fine."
    i "Whether if we encounter something paranormal or not, we've got each other."
    a1 "Yeah, you're right..."
    a1 "{sc=1}W-w{/sc}hat am I getting scared of?"
    a1 "I'm the bravest among the group!"
    "He says that while proudly keeping his chest up."
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
            a1 "Okay. Right this way."
            "We left the current passenger wagon onto the other one."
            window hide
            hide train1
            show train2 behind merah
            with wipeleft_scene
            window auto
            jump char_intro
        "\"No thanks, I need some more time alone.\"":
            a1 "I see. Take care."
            hide merah
            "[a1_name] leaves the scene, giving the passenger wagon to myself all alone."
            "Dammit. I forgot to eat this morning."
            "I was hoping they'd at least offer some food here."
            "Should I eat the food I brought along now?"
            menu:
                "Yes.":
                    "Can't start my day with an empty stomach... am I right?"
                    "*munch*{w=1.5} *munch*{w=1.5} *munch*"
                    
                "No.":
                    "Keep it together, [Main]."
                    "Just a few more minutes and this trip will be over."
                    "I have to save my food for the worst."
                    $ hungry_flag = True

            "I think getting some fresh air would ease me off."
            "I open the window."
            "Suprisingly, the wind against my face is actually rather pleasant."
            menu:
                "Lean outside.":
                    "I lean myself a bit outside the window frame."
                    hide train1
                    show forestbackground:
                        yoffset 250
                        xalign 1.0
                        linear 1 xalign 0.0
                        repeat
                    with dissolve
                    "It's a bit chilly, but in a good way. I feel myself waking up even more."
                    i "{cps=5}Ahhh...{/cps}"
                    window hide
                    pause 5.0
                    $ window_scene = True
                "Stay in.":
                    "I don't think I should. I might fall."
                    "I'll just look at the scenery."
                    window hide
                    pause 5.0
                    $ window_scene = False
    

    label char_intro:
        if window_scene == True:
            show train1
            show forestbackground behind train1:
                yoffset 0
                xalign 1.0
                linear 1 xalign 0.0
                repeat
            window show(None)
            a1 "{size=+50}[Main!u]!{/size}{fast}" with vpunch
            window auto
            i "Gah! What th-{w=0.5}{nw}" with vpunch
            i "Don't sneak behind me like that..."
            a1 "Hehe, sorry."
        elif window_scene == False:
            window auto
            a1 "[Main], we're here."
            i "Oh, sorry. I didn't see you guys."
        else:
            window auto
            a1 "Stay here while I look for [m2_name]."
            i "Okay."
            hide merah
            "I scanned the whole area."
            "In a corner, I see a lady reading a book."

        $ m1_name = "???"
        m1 "Greetings, [Main]."
        $ m1_name = "Lucy" 
        i "Oh, hello [m1_name]."

        if hungry_flag == True:
            "[m1_name] approaches me and offered to join at her table."
            "As I approach the table, she goes back to the kitchen."
            "Wait, do trains have kitchens?"
            pause 2.0
            window auto
            "I lightly shake my head." with hpunch
            "That's not important! I'm more invested on what [m1_name] has in store for me."
            "The scent alone coming from the kitchen swiftly made its way to my nose."
            "My goodness, what is this woman cooking?"
            "It smells so good that the scent alone makes me drool."
            "Soon after, [m1_name] comes out of the kitchen as she brings my plate."
            m1 "I noticed that you look off today..."
            m1 "So I prepared you some lunch."
            ".{w=0.5}.{w=0.5}.{w=0.5}"
            "I struggle to come up with any words. My mind is focused entirely on [m1_name]'s plate."
            m1 "Hello? Earth to [Main]?"
            i "O-oh. Sorry."
            "[m1_name] chuckles back as she offers the plate in front of me."

            m1 "What are you waiting for? Eat."
            menu:
                "\"T-thank you for the food!\"":
                    m1 "My pleasure."
                "Eat.":
                    pass

            "Surprisingly, the food tastes pretty good."
            "I can't tell what some of the spices are, but they blend together nicely."

            if window_scene == True:
                i "It would be nice if the window was open."
                m1 "Is that so?"
                i "I did something like that earlier."
                m1 "I too would have loved it."
                m1 "But your food would easily get cold, so I would not recommend it."
                i "Oh, okay."
            else:
                pass

        else:
            "[m1_name] pours a glass of what it seems to be water and offers it to me. It's fizzing a bit, and almost looks carbonated."
            "I give it a sniff. It smells kind of fruity."
            m1 "Go ahead, you look thirsty."
            i "Thanks. I've been needing it."
            "I take a sip on the water."
            "The fizzing sensation of the water soothes my dried mouth."
            window hide
            pause 3.0
            window auto
            "There's an awkward silence between us."
            i "So [m1_name], how are you?"
            "Wow [Main], what a great start."
            m1 "I am doing fine."
            m1 "I do find the train ambience quite calming."

            if window_scene == True:
                i "Not as calm as opening a window. I did something like that earlier."
                m1 "Is that so?"
                m1 "I would probably do something so carefree like that..."
                m1 "If you didn't do it earlier."
                m1 "You were having your moment."
                m1 "And I would not want it to be ruined so I left you alone."
                i "O-oh. I see..."
                i "Thanks for letting me have a moment for myself."
                m1 "My pleasure."
            else:
                "I focus my hearing on the surroundings."
                "She's right. It does feel relaxing."
                "I look at myself in the window..."
                "...just to see the scene at the distance nearing towards us."
                m1 "Do you want me to open the window?"
                m1 "Surely the breeze would make you feel a bit better."
                i "Oh, sure. Go ahead."
                "[m1_name] opens the window."
                "Suprisingly, the wind against my face is actually rather pleasant."

        window hide
        pause 3.0
        window auto

        "I've always wondered why she's always looking after us."
        "Even if conflict stirs up in the group."
        "I have to say, where does she even get the determination to deal with our stupidity?"
        "She's quite an amazing woman. Matured, independent..."
        "I can never be as good as her."
        "She has never shown any vulnerabilities since we've met her."
        "It's as if she's very cautious of her actions..."
        "On second thought..."
        i "How do you do it?"
        m1 "Do what?"
        i "You know, deal with us. Our group is vast, each with their own unique personalities."
        i "I'm surprised that you can manage to adjust according to our interests."
        "[m1_name] giggles from my compliment."
        m1 "I have seen the world far more than you know."
        i "Really? What of it?"
        m1 "Oh, a lot. You will be surprised at what I can do."

        if hungry_flag == False:
            m1 "Maybe cook, I suppose?"
        else:
            m1 "Maybe share someone with a drink and enjoy the scenes unfold from the window."

        m1 "But right now, why don't you go with the others?"
        i "Oh, okay."
        "Just as I leave [m1_name], I looked back at her with sincerity."
        i "By the way..."
        i "Thanks [m1_name]."
        extend " For everything."
        i "Seeing where you are now, I guess you needed a single thank you from us."
        "[m1_name] smiled back to me genuinely."
        "I let out another yawn and start to glance around the room."
        "So, where are they?"
        "I walked across the long hallway of the passenger wagon to find [a1_name]."
        "Though I seem to pass along a person busy with their phone."
        $ m2_name = '???'
        m2 "Oh, hi [Main]."
        $ m2_name = 'Raymon'
        i "Hey, [m2_name]."
        m2 "Oh, there's [a1_name]. Just in time."
        m2 "Anyway, one of the coordinators got in touch with me a while ago."
        m2 "As far as we know, we're going to rendezvous in a forgotten asylum deep within the forest to dig up the tragic history behind it."
        m2 "We're essentially making history here by unraveling the secrets of the asylum."
        m2 "Isn't it fun?"
        "Of course, that's something he likes."
        "This guy is probably the most questionable history buff person I have encountered."
        "I sometimes couldn't even comprehend his usage of words."
        "Does he think lowly of us?"
        "I mean, he tries his best to make it comprehensible for us..."
        "Which...{w=0.5} ends up poorly executed."
        "I have to search my phone to find the definitions of his words."

        "He reminds me of a person who uses sugarcoating on his essa{nw}"
        $ _history_list[-1].what = "I find his words hard to describe."

        m2 "I have always wanted to embark in an abandoned haven..."
        m2 "That is, if you can still label it like that..."
        a1 "I'm not really liking the concept of us going through a haunted house."
        m2 "It's not a haunted house. It's an abandoned sanctuary."
        m2 "I mean, we're getting paid to do this for them."
        a1 "I don't know... The coordinators offering a huge amount of money for just exploring the abandoned place?"
        a1 "I don't think so."
        a1 "They must be expecting that something bad might to happen to us."
        a1 "So them offering a huge asset would mean anyone would be willing to explore it in exchange for money."
        a1 "They don't want their hands to get dirty so they just leave it to some random group of friends."
        m1 "That could be true."
        "What the hell!"
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
