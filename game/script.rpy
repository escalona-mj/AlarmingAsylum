define persistent.Beginning = False
define persistent.LizardSpock = False
define persistent.RockSolid = False
define persistent.TwinBlades = False
define persistent.WrapItUp = False
define hungry_flag = False
define window_scene = None

default player_score = 0
default computer_score = 0
default rps_win = False
default only_rock = 0
default only_paper = 0
default only_scissors = 0

$ ann = 'Announcer'

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

    $ achievement.grant("start")
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
    a1 "There's plenty of seats to sleep from our side though."
    i "I don't like people watching me sleep."
    i "Even if we're the only ones here."
    "..."
    "There's an awkward silence."
    "I think there's something we both wanted to say."
    "I don't have the courage to, not yet."
    "Thankfully, [a1_name] breaks the silence."
    a1 "Well...{w=0.2} aren't you excited?"
    i "I'm excited to leave once everything is over."
    a1 "We'll be fine. We'll take great care of you."
    i "You mean YOUR butler will take care of us."
    "I scoffed then gave him a disapproval look."
    "He isn't that bad, he just looks after my wellbeing."
    "I mean, that's what friends do, right?"
    a1 "Man... why do we have to go to an {sc=2}a-abandoned{/sc} asylum?"
    i "What? Are you scared?"
    i "You're the one to tell that we'll be fine."
    a1 "N-no!{w=0.3} I mean yes! {w=0.4}{sc=2}I-it's not like that or anything...{/sc}"
    "I can see right through him. Typical [a1_name]."
    i "We're only there to discover the history of the asylum as per the coordinator's request."
    i "Nothing else."
    a1 "Yeah, you're right."
    a1 "But I just can't help but wonder, what will happen to us?"
    a1 "What if something bad happens to us?"
    a1 "Just the thought of it scares me."
    i "Pfft, you've been watching too many horror documentaries."
    i "We're going to be fine. Didn't you said that before?"
    i "Or are you going to leave everything to your butler?"
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
    a1 "Why don't we play rock, paper, scissors for a while? Best of 3?"
    i "Alright."

    label rps:
        if player_score == 3:
            $ rps_win = True
            jump results
        elif computer_score == 3:
            jump results
        elif player_score == 2 and computer_score == 2:
            a1 "It's now or never!"
        else:
            pass
        show screen scoring with noise_window
        call screen rps_screen with noise_window
        $ player_selection = _return
        $ computer_selection = renpy.random.choice(['rock', 'paper', 'scissors'])
        pause 0.5
        show text _("{size=+100}ROCK...{/size}")
        pause 0.5
        show text _("{size=+100}PAPER...{/size}")
        pause 0.5
        show text _("{size=+100}SCISSORS...{/size}")
        pause 0.5
        show text _("{sc=10}{size=+500}GO!!!{/size}{/sc}")
        pause 0.5
        hide text with Dissolve(0.1)
        "I chose [player_selection] and [a1_name] whips out [computer_selection]."

        if player_selection == computer_selection:
            "It's a tie."
            a1 "Ooh, I'll get ya!"
            jump rps

        elif player_selection == 'rock':
            if computer_selection == 'scissors':
                "Rock beats scissors! I win!"
                $ only_rock += 1
                $ only_paper = 0
                $ only_scissors = 0
                $ player_score +=1
                jump rps
            else:
                "Paper beats rock! I lost!"
                $ computer_score +=1
                jump rps

        elif player_selection == 'paper':
            if computer_selection == 'rock':
                "Paper beats rock! I win!"
                $ only_paper += 1
                $ only_rock = 0
                $ only_scissors = 0
                $ player_score +=1
                jump rps
            else:
                "Scissors beats paper! I lost!"
                $ computer_score +=1
                jump rps

        elif player_selection == 'scissors':
            if computer_selection == 'paper':
                "Scissors beats paper! I win!"
                $ only_scissors += 1
                $ only_paper = 0
                $ only_rock = 0
                $ player_score +=1
                jump rps
            else:
                "Rocks beats scissors! I lost!"
                $ computer_score +=1
                jump rps
        
    label results:
        if rps_win:
            $ achievement.grant("rps_game")
            if persistent.LizardSpock == False:
                $ renpy.display_notify("Achievement Get:\n\"Lizard, Spock!\"")
                play sound "audio/sfx/notify.ogg"
                $ persistent.LizardSpock = True
            i "I win."

            if only_scissors >= 3:
                $ achievement.grant("rps_game_scissors")
                if persistent.TwinBlades == False:
                    $ renpy.display_notify("Hidden Achievement Get:\n\"Twin Blades\"")
                    play sound "audio/sfx/notify.ogg"
                    $ persistent.TwinBlades = True
                i "And I beat you using [player_selection]!"
            
            elif only_rock >= 3:
                $ achievement.grant("rps_game_rock")
                if persistent.RockSolid == False:
                    $ renpy.display_notify("Hidden Achievement Get:\n\"Rock Solid\"")
                    play sound "audio/sfx/notify.ogg"
                    $ persistent.RockSolid = True
                i "And I beat you using [player_selection]!"

            elif only_paper >= 3:
                $ achievement.grant("rps_game_paper")
                if persistent.WrapItUp == False:
                    $ renpy.display_notify("Hidden Achievement Get:\n\"Wrap It Up!\"")
                    play sound "audio/sfx/notify.ogg"
                    $ persistent.WrapItUp = True
                i "And I beat you using [player_selection]!"
            
            i "Take that!"
            if only_paper >=3 or only_rock >=3 or only_scissors >=3:
                a1 "Yeah yeah, rub it in. That was pure luck."
            jump afterwards
        else:
            i "Aww, I lost."
            a1 "Bow to me!"
            jump afterwards

    label afterwards:
        hide screen scoring with noise_window
        a1 "Surely you're fully awake now?"
        if rps_win:
            i "A bit. Thanks for the game though, I feel replenished."
            a1 "Awesome!"
        else:
            i "I really don't feel any changes."
            a1 "Well, I tried."
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
        "I leave my warm seat in a haste and drag all of my belongings with me."
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
                "Dammit. I forgot to eat lunch."
                "I was hoping they'd at least offer some food here."
                "Should I eat the food I brought along now?"
                menu:
                    "Yes.":
                        "Can't start the day with an empty stomach, right?"
                        "*munch*{w=1.5} *munch*{w=1.5} *munch*"
                        window hide
                        pause 1.0
                        window auto
                        
                    "No.":
                        "Keep it together, [Main]."
                        "Just a few more minutes and this trip will be over."
                        "I have to save my food for the worst."
                        $ hungry_flag = True

                "I think getting some fresh air would ease me off."
                "I open the window."
                "Suprisingly, the wind against my face is actually rather pleasant."
                menu:
                    i "Should I...?"
                    "Peek outside.":
                        "I peek a bit outside the window frame."
                        hide train1
                        show forestbackground:
                            yoffset 250
                            xalign 1.0
                            linear 1 xalign 0.0
                            repeat
                        with dissolve
                        "It's a bit chilly, but in a good way. I feel myself waking up even more."
                        "As much as I hate going to this stupid assignment, the wind does make me feel a bit safer."
                        window hide
                        show screen slow_text_center("{bt=h5-p2.0-s0.5}{size=+35}Ahhh...{/bt}")
                        pause 5.0
                        hide screen slow_text_center with Dissolve(3.0)
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
            i "Don't sneak behind me like that!"
            a1 "Hehe, sorry."
            "Flabbergasted, I went back gazing into the distance."
            a1 "By the way, my assistant wants to talk to you."
            a1 "I don't know what it is, but I'll leave the two of you alone."
            i "Is that so?"
        elif window_scene == False:
            window auto
            "I wonder if..."
            "The asylum is truly haunted."
            "It's not something I should be worried of... right?"
        else:
            window auto
            a1 "Stay here while I look for [m2_name]."
            i "Okay."
            hide merah
            "I scanned the whole area."

        "In the corner of my eye, I see a lady suited well approaching me."
        $ l1_name = "???"
        l1 "Greetings, [Main]."
        $ l1_name = "Lucy" 
        i "Oh. Hello Ms. [l1_name]."
        l1 "Please,{w=0.2} [l1_name] is fine."
        "We head on an empty train seat that comes along with a table."

        if hungry_flag == True:
            "As I approach the table, she goes back to the kitchen."
            "Wait, do trains have kitchens?"
            "..."
            "I lightly shake my head." with hpunch
            "That's not important! I'm more invested on what [l1_name] has in store for me."
            "The scent alone coming from the kitchen swiftly made its way to my nose."
            "It smells so good that the scent alone makes me drool."
            "Soon after, [l1_name] comes out of the kitchen as she brings my plate."
            l1 "I noticed that you look off today..."
            l1 "So I prepared you some food."
            "..."
            "I struggle to come up with any words. My mind is focused entirely on [l1_name]'s plate."
            l1 "Hello? Are you still there, [Main]?"
            i "O-oh. Sorry."
            "[l1_name] chuckles back as she offers the plate in front of me."

            l1 "What are you waiting for? Eat."
            i "T-thank you for the food!"
            "Surprisingly, the food tastes pretty good."
            "I can't tell what some of the spices are, but they blend together nicely."

            if window_scene == True:
                i "It would be nice if the window was open."
                l1 "Is that so?"
                i "I did something like that earlier."
                l1 "I too would have loved it."
                l1 "But your food would easily get cold, so I would not recommend it."
                i "Oh, okay."
            else:
                pass

        else:
            "[l1_name] pours a glass of what it seems to be water and offers it to me. It's fizzing a bit, and almost looks carbonated."
            "I give it a sniff. It smells kind of fruity."
            l1 "Go ahead, you look thirsty."
            i "Thanks. I've been needing it."
            "I take a sip on the water."
            "The fizzing sensation of the water soothes my dried mouth."
            "..."
            "Not being sure what to say to her, I stay silent, hoping that she would say something else soon."
            "To which, an awkward silence formed between us."
            "I feel so hopeless that I can't come up with anything to say."
            "..."
            i "So [l1_name], h-how are you?"
            "Wow [Main], what a great start."
            l1 "I am doing fine."
            l1 "I do find the train ambience quite calming."

            if window_scene == True:
                i "Not as calm as opening a window. I did something like that earlier."
                l1 "Is that so?"
                l1 "I would probably do something so carefree like that..."
                l1 "If you didn't do it earlier."
                l1 "You were sightseeing."
                l1 "And I would not want it to be ruined so I left you alone."
                i "O-oh. I see..."
                i "Thanks for letting me have a moment for myself."
                l1 "My pleasure."
            else:
                "I focus my hearing on the surroundings."
                "She's right. It does feel relaxing."
                "I look at myself in the window..."
                "...just to see the scene at the distance nearing towards us."
                l1 "Do you want me to open the window?"
                l1 "Surely the breeze would make you feel a bit better."
                i "Oh, sure. Go ahead."
                "[l1_name] opens the window."
                "Suprisingly, the wind against my face is actually rather pleasant."

        window hide
        pause 3.0
        window auto

        "I've always wondered why she's always looking after us."
        "I mean she IS [a1_name]'s butler."
        "Where does she even get the determination to deal with our stupidity?"
        "She's quite an amazing woman. Matured, independent..."
        "I can never be as good as her."
        "She has also never shown any vulnerabilities since we've met her."
        "On second thought..."
        i "How do you do it?"
        l1 "Do what?"
        i "You know, deal with us. Our group is vast, each with their own unique personalities."
        i "I'm surprised that you can manage to adjust according to our interests."
        "[l1_name] giggles from my compliment."
        l1 "I have seen the world far more than you know."
        i "Really? What of it?"
        l1 "Oh, a lot. You will be surprised at what I can do."

        if hungry_flag == False:
            l1 "Maybe cook, I suppose?"
            l1 "Ahaha."
        else:
            l1 "Maybe share someone with a drink and enjoy the scenes unfold from the window."
            l1 "That would be nice..."

        i "I see. Why do you also look after us?"
        i "Shouldn't you only serve [a1_name]?"
        l1 "A friend of [a1_name] is also my responsibility."
        l1 "It is something that we, servants, should also serve."

        if rps_win == True:
            l1 "I heard you won against [a1_name] in a game of rock, paper, scissors right?"
            l1 "I give you my congratulations."
        else:
            l1 "I heard you lost against [a1_name] in a game of rock, paper, scissors right?"
            l1 "There is always next time."
            "She gives me a pat in the head, giving me a comfortable feeling."

        i "Th-thanks, [l1_name]."
        i "How did you know?"
        l1 "[a1_name] told me."
        l1 "Now, why don't you go with the others?"
        "Just as I leave [l1_name], I looked back at her with sincerity."
        i "By the way..."
        i "Thanks [l1_name]."
        extend "\nFor everything."
        i "Realizing your state, I guess you we should thank you for looking after us."
        "[l1_name] smiles genuinely at me as she continues cleaning up. I smile back naturally, leaving her."
        "I let out another yawn and start to glance around the room."
        "So, where are they?"
        "I walked across the long hallway of the passenger wagon to find [a1_name]."
        "Though I seem to pass along a person busy with their phone."

        $ m2_name = '???'
        m2 "Oh, hi [Main]."
        $ m2_name = 'Raymon'
        i "Hey, [m2_name]."
        "[m2_name] had always been a bookworm with a twist."
        "He loved the way books transported him to other worlds, filled his mind with new ideas, and gave him a sense of purpose."
        m2 "Would you like to read some books with me?"
        i "Sure."
        "His seat is filled with books ranging from literature to...{w=0.5} manga?"
        "He surely has everything."
        m2 "Sorry about that, all the seats been taken by my books."
        "[m2_name] whips out a foldable chair out from his bag."
        "That's the twist."
        "He always comes prepared."
        "Where did that even come from?"
        m2 "I know, I've come prepared for this moment."
        "[m2_name] showed me some of his favorite books, from classic novels to modern memoirs."
        m2 "I'm actually eager to learn about the asylum's past."
        m2 "So that's why I'm reading a lot of novels that include about charcaters interacting with an asylum."
        i "I-is that so?"
        i "I never thought you'd come prepared."
        m2 "Of course! I'm always prepared."
        i "Unlike the other one."
        "We exchanged laughs."
        m2 "I find reading a bit mesmerizing. I always imagine myself being at the shoes of the main character."
        m2 "Ooh, about that..."
        m2 "A certain book caught my attention yesterday and I was hoping to read it with someone here."
        m2 "It's about a group of friends traveling in an abandoned mansion."
        m2 "Where... you guessed it, someone had to die."
        m2 "If only he had accepted that her death was inevitable. I always think of different ways on how the story could have gone to."
        m2 "The way of he enunciated their feelings to other characters..."
        "I could see the excitement in his eyes and the way his voice became animated when he talked about his favorite books."
        "I sometimes couldn't even comprehend his usage of words."
        "I mean, he tries his best to make it comprehensible for us..."
        "Which...{w=0.5} ends up poorly executed."
        "I have to search my phone to find the definitions of his words."

        "He reminds me of a person who uses sugarcoating on his essa{nw}"
        $ _history_list[-1].what = "I find his words hard to describe."

        m2 "... then left all alone in the world with nothing but himself because he did not follow the order."
        m2 "..."
        "He paused for a moment, realizing he had been talking alone."
        m2 "Sorry,{w=0.2} I must be rambling again..."
        i "No no, it's fine!"
        i "I like the way..."
        i "The uhh..."
        i "Uhm..."
        i "..."
        "Oh crap, I was lost in thought!"

        m2 "It's fine anyway. The book was too much for you, wasn't it?"
        m2 "You wouldn't like it anyway."
        "He gives me a disappointing look."
        i "I-I mean, why don't we take lessons from that book of yours?"
        i "Surely if that happens to us, we can prevent someone else's death?"
        m2 "Ahaha. You're funny."
        m2 "This is fiction. It wouldn't happen to us."
        "This is some foreboding moment."
        m2 "I have always wanted to embark in an abandoned haven..."
        m2 "That is, if you can still label it that..."
        i "I'm not really liking the concept of us going through a haunted house."
        m2 "It's not a haunted house. It's an abandoned sanctuary."
        m2 "We're essentially making history here by unraveling the secrets of the asylum."
        m2 "Isn't that fun?"
        i "Of course, that's something that you like."
        "I can already see the determination from his eyes."
        m2 "Oh,{w=0.2} there's [a1_name]. Just in time."
        "[m2_name] and [l1_name] arrives at the scene."
        a1 "Hey guys! We heard the announcement."

        "{i}\"Attention, passengers: this is your conductor. We are now arriving at the train stop.{/i}\""
        m2 "And we're almost there."
        
        # a1 "Hey guys, one of the coordinators got in touch with me a while ago."
        # a1 "As far as we know, we're going to rendezvous in a forgotten asylum deep within the forest to dig up the tragic history behind it."
        # a1 "I don't know... The coordinators offering a huge amount of money for just exploring the abandoned place?"
        # a1 "I don't think so."
        # a1 "They must be expecting that something bad might to happen to us."
        # a1 "So them offering a huge asset would mean anyone would be willing to explore it in exchange for money."
        # a1 "They don't want their hands to get dirty so they just leave it to some random group of friends."
        # l1 "That could be true."
        # "What the hell!"
        # i "Is that so?"
        # i "If it's offering more money than we initially agreed on, then I'm in."
        # a1 "Woah, woah, woah, woah!"
        # a1 "Not so fast!"
        # a1 "[m2_name], surely we won't be staying there for too long right?"
        # m2 "3 days."
        # a1 "{sc}3 d-days?!{/sc}"
        # "Wait what?!"
        # "My eyes grew wide."
        # "I thought we're only investigating the asylum?"
        # "I smell trouble..."
        # m2 "There's still the reward money after all of this."
        # m2 "It's worth it."
        camera
        scene bg trainstation blurred with noise_scene
        
        i "We're here."



        

return
