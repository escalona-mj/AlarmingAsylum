define hungry_flag = False
define window_scene = None

default player_score = 0
default computer_score = 0
default rps_win = False
default only_rock = 0
default only_paper = 0
default only_scissors = 0

label start:
    show black
    with noise_scene
    
    window auto
    "…"
    show text _("{i}Please… wake up.{/i}") at truecenter with noise
    "An inaudible voice murmurs towards me."
    "..."
    show text _("{i}Why won't you wake up?{/i}") at truecenter with noise
    "{i}\"You there, [Main]?\"{/i}"
    "...Huh?"
    show text _("{i}Seek out the truth...{/i}") at truecenter with noise
    "{i}\"Hey, wake up.\"{/i}"
    "..."
    "I open my mouth but nothing comes out of it."
    show text _("{i}Truth.{/i}") at truecenter with noise
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
            easeout_back 0.5 yoffset -5
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

    $ achievement_get("start")

    show merah neutral
    i "Wh-wha?"
    "Something hard hit my face, causing me to jerk out."
    $ a1_name = "???" 
    a1 "[Main], wake up!"
    a1 "And I thought I was the sleepy one..."
    "My eyes start to dart around to look at what's familiar and what isn't."
    $ a1_name = "Alonso" 
    i "Sorry Alonso, I must have dozed off."
    a1 "I tried waking you up earlier, but you wouldn't budge."
    "I know Alonso's a great friend, but he shouldn't just wake people up."
    "Unless it's an emergency."
    "Stretching to gain energy, I stare blankly at the window, looking for an ounce of motivation."
    a1 "Why are you sleeping here alone?"
    a1 "There's plenty of seats to sleep from our side though."
    i "I don't like people watching me sleep."
    i "Even if we're the only ones here."
    "..."
    "I think there's something we both wanted to say."
    "I don't have the courage to, not yet."
    "Thankfully, Alonso breaks the silence."
    a1 "Well... aren't you excited?"
    i "I'm excited to leave once everything is over."
    "I scoffed then gave him a disapproval look."
    "He isn't that bad, he just looks after my wellbeing."
    "I mean, that's what friends do, right?"
    a1 "I'm having second thoughts about going on this trip..."
    i "What?"
    a1 "W-wait! I-it's not like that or anything..."
    "I can see right through him. Typical Alonso."
    i "We're only there to discover the mystery of the asylum."
    i "It was supposedly to be your butler's secret mission, but I don't know why you had to bring yourself and us as well."
    i "Heck, why did you even disclose this information to us?"
    a1 "Hold on! Just let me explain."
    a1 "What if something bad happens to her?"
    a1 "We won't be there for her."
    a1 "I know to myself I can't do it alone, so I brought you guys."
    "I paused."
    "I didn't realized how important his butler is to him."
    i "Right. Sorry, I didn't know..."
    i "But we're going to be fine. Didn't you said that before?"
    i "Whether if we encounter something paranormal or not, we've got each other."
    a1 "Yeah, you're right..."
    "..."
    "I try to yawn discreetly into my hand, but I guess it doesn't look discreet enough."
    a1 "Have you been taking your vitamins like I told you?"
    a1 "You won't last long in trips like these."
    i "Oh, I keep forgetting it."
    "Alonso scoffs at me with worry."
    a1 "You should probably start packing up."
    i "Yeah, good idea. We might be close already."
    "I rummaged through my bag to see if I already have the necessities."
    "Do I have everything in here?"
    "Flashlight, check."
    "Phone, check."
    "Food, check."
    "Notebook, check."
    
    "Gun, chec{nw}"
    $ _history_list[-1].what = "Self-defense items, check."
    "Wait, what?{fast}"

    "Right, first-aid... check."
    "I leave my warm seat in a haste and drag all of my belongings with me."
    i "I guess I have everything right here."
    a1 "Alright, I'll go with the others. Care to join us?"
    menu:
        "Err..."
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
            "Alonso leaves the scene, giving the passenger wagon to myself all alone."
            "Dammit. I forgot to eat lunch."
            "I was hoping they'd at least offer some food here."
            
            menu:
                "Should I eat the food I brought along now?"
                "Yes.":
                    "Can't start the day with an empty stomach, right?"
                    "*munch*{w=1.5} *munch*{w=1.5} *munch*"
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
                "Should I...?"
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
                    ""
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
            i "Gah! What th-{nw}" with vpunch
            i "Don't sneak behind me like that!"
            a1 "Hehe, sorry."
            "..."
            i "Alonso... Please don't do that again."
            a1 "Right, right. I'm sorry I scared you."
            # "Flabbergasted, I went back gazing into the distance."
            a1 "By the way, my butler wants to talk to you."
            a1 "I don't know what it is, but I'll leave the two of you alone."
            i "Is that so?"
        elif window_scene == False:
            window auto
            "I wonder if..."
            "The asylum is truly haunted."
            "It's not something I should be worried of... right?"
        else:
            window auto
            a1 "Stay here while I look for Raymon."
            i "Okay."
            hide merah
            "I scanned the whole area."

        "In the corner of my eye, I see a lady suited well approaching me."
        show lucy with Dissolve(0.2)
        $ l1_name = "???"
        lucy "Greetings, [Main]."
        $ l1_name = "Lucy" 
        i "Oh. Hello Ms. Lucy."
        show lucy base3
        lucy eyes_closed "Please, Lucy is fine."
        "We head on an empty train seat that comes along with a table."

        if hungry_flag == True:
            hide lucy with Dissolve(0.2)
            "As I approach the table, she goes back to the kitchen."
            "Wait, do trains have kitchens?"
            "I'm amazed on how Lucy decides to cook on times like these. Even on her mission."
            "..."
            "I lightly shake my head." with hpunch
            "That's not important! I'm more invested on what Lucy has in store for me."
            "The scent alone coming from the kitchen swiftly made its way to my nose."
            "It smells so good that the scent alone makes me drool."
            "Soon after, Lucy comes out of the kitchen as she brings my plate."
            show lucy base3 brow_sad with Dissolve(0.2)
            lucy "I noticed that you look off today..."
            lucy -brow_sad eyes_closed -base3 "So I prepared you some food."
            show lucy -eyes_closed
            "..."
            "I struggle to come up with any words. My mind is focused entirely on Lucy's plate."
            lucy base3 brow_sad mouth_serious "Hello? Are you still there, [Main]?"
            show lucy brow_sad -mouth_serious
            i "O-oh. Sorry."
            show lucy -base3 eyes_closed -mouth_serious -brow_sad
            "Lucy chuckles back as she offers the plate in front of me."
            lucy -eyes_closed"What are you waiting for? Eat."
            i "T-thank you for the food!"
            show lucy eyes_closed
            "Surprisingly, the food tastes pretty good."
            "I can't tell what some of the spices are, but they blend together nicely."

            if window_scene == True:
                i "It would be nice if the window was open."
                lucy mouth_slightopen -eyes_closed "Is that so?"
                i "I did something like that earlier."
                lucy eyes_look base2 -mouth_slightopen brow_sad"I too would have loved it."
                lucy eyes_closed -brow_sad mouth_serious"But your food would easily get cold, so I would not recommend it."
                hide lucy
                show lucy
                i "Oh, okay."
                show lucy eyes_closed
            else:
                pass

        else:
            "Lucy pours a glass of what it seems to be water and offers it to me. It's fizzing a bit, and almost looks carbonated."
            "I give it a sniff. It smells kind of fruity."
            show lucy -base3
            lucy -eyes_closed "Go ahead, you look thirsty."
            i "Thanks. I've been needing it."
            "I take a sip on the water."
            show lucy eyes_closed
            "The fizzing sensation of the water soothes my dried mouth."
            "As I gaze on her, she traces the rim of her teacup with her fingertip."
            "..."
            "Not being sure what to say to her, I stay silent, hoping that she would say something else soon."
            "In which, an awkward silence formed between us."
            "I feel so hopeless that I can't come up with anything to say."
            "..."
            i "So Lucy, h-how are you?"
            show lucy mouth_slightopen
            show lucy -eyes_closed
            "Wow [Main], what a great start."
            lucy -mouth_slightopen "I am doing fine."
            show lucy eyes_closed
            lucy "I find the train ambience quite calming."

            if window_scene == True:
                i "Not as calm as opening a window. I did something like that earlier."
                lucy mouth_slightopen -eyes_closed "Is that so?"
                show lucy -mouth_slightopen base2
                lucy brow_sad eyes_look "I would probably do something so carefree like that..."
                lucy eyes_closed "If you didn't do it earlier."
                lucy -eyes_closed "You were sightseeing."
                show lucy base3
                lucy brow_sad eyes_closed "And I would not want it to be ruined so I left you alone."
                show lucy -base3 -eyes_closed
                i "O-oh. I see..."
                "So she saw me."
                i "Thanks for letting me have a moment for myself."
                lucy eyes_closed -brow_sad "My pleasure."
            else:
                "I focus my hearing on the surroundings."
                "She's right. It does feel relaxing."
                "I look at myself in the window..."
                "...just to see the scene at the distance nearing towards us."
                lucy "Do you want me to open the window?"
                lucy "Surely the breeze would make you feel a bit better."
                i "Oh, sure. Go ahead."
                "Lucy opens the window."
                "Suprisingly, the wind against my face is actually rather pleasant."

        window hide
        pause 3.0
        window auto

        "Where does she even get the determination to deal with our stupidity?"
        "She's quite an amazing woman. Matured, independent..."
        "I can never be as good as her."
        "She has also never shown any vulnerabilities since we've met her."
        "On second thought..."
        i "How do you do it?"
        lucy mouth_slightopen -eyes_closed"Do what?"
        i "You know, deal with us. Our group is vast, each with their own unique personalities."
        i "I'm surprised that you can manage to adjust according to our interests."
        show lucy base3 eyes_closed -mouth_slightopen
        "Lucy giggles from my compliment."
        lucy "I have seen the world far more than you know."
        i "Really? What of it?"
        lucy -eyes_closed "Oh, a lot. You will be surprised at what I can do."

        if hungry_flag == False:
            lucy eyes_look brow_sad "Maybe cook, I suppose?"
            lucy "Ahaha."
        else:
            lucy eyes_look brow_sad "Maybe share someone with a drink and enjoy the scenes unfold from the window."
            lucy "That would be nice..."

        i "I see." 
        show lucy eyes_closed -brow_sad base1
        "I've always wondered why she's always looking after us."
        "I get that she IS Alonso's butler."
        "There's no harm in asking her, right?"
        i "Why do you also look after us?"
        show lucy -eyes_closed
        i "Shouldn't you only serve Alonso?"
        show lucy mouth_serious brow_serious
        "Lucy's expression immediately changed."
        "I might have strike a nerve."
        lucy mouth_slightopen "A friend of Alonso is also my responsibility."
        lucy eyes_closed base3"It is something that we, servants, should also serve."
        show lucy mouth_serious -base3 -eyes_closed
        "Right, a butler's expertise."
        "That was a stupid question to ask."
        i "I didn't mean it like that. I'm sorry."
        lucy brow_sad eyes_look base3 -mouth_serious "I know you do."
        lucy "And I apologize for acting out so sudddenly."
        lucy -eyes_look -base3 "Now, why don't you go with the others?"
        i "Okay..."
        hide lucy with Dissolve(0.2)
        "Just as I leave Lucy, I looked back at her with sincerity."
        show lucy with Dissolve(0.2)
        i "By the way..."
        show lucy mouth_slightopen
        i "Thanks Lucy."
        show lucy brow_sad -mouth_slightopen
        extend "\nFor everything."
        i "Realizing your state, I guess you we should thank you for looking after us."
        show lucy eyes_closed -brow_sad
        "Lucy smiles genuinely at me as she continues cleaning up. I smile back naturally, leaving her."
        hide lucy with Dissolve(0.2)
        "I let out another yawn and start to glance around the room."
        "So, where are they?"
        "I walked through the long corridors of the passenger wagon to find Alonso."
        "Though I seem to come across a small reading place in the corner of the train."
        "The bookshelves are displayed in a minimalistic manner; categorized neatly with a beanbag on the floor."
        "This train sure has everything!"
        "However, there seems to be a person fully immersed in their book."

        $ m2_name = '???'
        m2 "Oh, hi [Main]."
        $ m2_name = 'Raymon'
        i "Hey, Raymon."
        "Raymon had always been a bookworm with a twist."
        "He loved the way books transported him to other worlds, filled his mind with new ideas, and gave him a sense of purpose."
        m2 "Would you like to read some books with me?"
        i "Sure."
        "He's surrounded with books ranging from literature to... manga?"
        "He surely has everything."
        m2 "Sorry about that, all the seats been taken by the books."
        "Raymon whips out a portable beanbag out from his bag."
        "That's the twist."
        "He always comes prepared."
        "Where did that even come from?"
        m2 "I know, I've come prepared for this moment."
        "Raymon showed me some of his favorite books, from classic novels to modern memoirs."
        m2 "I'm actually eager to learn about the asylum's past."
        m2 "So that's why I'm reading a lot of novels that include about characters interacting with an asylum."
        i "I-is that so?"
        i "I never thought you'd come prepared."
        m2 "Of course! I'm always prepared."
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
        "Which... ends up poorly executed."
        "I have to search my phone to find the definitions of his words."

        "He reminds me of a person who uses sugarcoating on his essa{nw}"
        $ _history_list[-1].what = "He reminds me of someone I used to know somewhere else."

        m2 "... then left all alone in the world with nothing but himself because he did not follow the order."
        m2 "..."
        "He paused for a moment, realizing he had been talking alone."
        m2 "Sorry, I must be rambling again..."
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
        i "Maybe if that happens to us, we can prevent someone else's death?"
        m2 "Ahaha!"
        m2 "What kind of analogy is that?"
        m2 "This is fiction. That wouldn't happen to us."
        "For some reason, I felt a chill down my spine after hearing that."
        "I couldn't help but feel a sense of foreboding."
        m2 "I have always wanted to embark in an abandoned haven..."
        m2 "That is, if you can still label it that..."
        i "I'm not really liking the concept of us going through a haunted house."
        m2 "It's not a haunted house. It's an abandoned sanctuary."
        m2 "We're essentially making history here by unraveling the secrets of the asylum."
        m2 "I even brought a vintage camera to capture the essence of our journey!"
        m2 "Isn't that fun?"
        i "Of course, that's something that you like."
        "I can already see the determination from his eyes."
        m2 "Oh, there's Alonso and Lucy. Just in time."
        a1 "Hey everyone!"
        a1 "Man, wandering through these empty endless passenger wagons sure is tiring."
        a1 "I've been looking everywhere for you two."
        "How did he get lost? This train is just a corridor..."
        a1 "Luckily, I came across Lucy. She pointed out exactly where you guys are."
        i "Thanks, Lucy. If it weren't for you, Alonso would've been left wandering aimlessly in the train."
        "Lucy laughs from my bad-executed joke."
        "Alonso pouts and crosses his arms on his chest."

        a1 "Hey [Main]. How about a game of rock, paper, scissors for a while?"
        a1 "Best of 3?"
        i "Sure, we're almost there anyway."
        a1 "Alright!"

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
        show text _("{size=+100}ROCK...{/size}") with Dissolve(0.1)
        pause 0.5
        show text _("{size=+100}PAPER...{/size}")
        pause 0.5
        show text _("{size=+100}SCISSORS...{/size}")
        pause 0.5
        show text _("{sc=10}{size=+500}GO!!!{/size}{/sc}")
        pause 0.5
        hide text with Dissolve(0.1)
        "I chose [player_selection] and Alonso whips out [computer_selection]."

        if player_selection == computer_selection:
            "It's a tie."
            a1 "Ooh, I'll get ya!"
            jump rps

        elif player_selection == 'rock':
            if computer_selection == 'scissors':
                $ only_rock += 1
                $ only_paper = 0
                $ only_scissors = 0
                $ player_score +=1
                "Rock beats scissors! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Paper beats rock! I lost!"
                jump rps

        elif player_selection == 'paper':
            if computer_selection == 'rock':
                $ only_paper += 1
                $ only_rock = 0
                $ only_scissors = 0
                $ player_score +=1
                "Paper beats rock! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Scissors beats paper! I lost!"
                jump rps

        elif player_selection == 'scissors':
            if computer_selection == 'paper':
                $ only_scissors += 1
                $ only_paper = 0
                $ only_rock = 0
                $ player_score +=1
                "Scissors beats paper! I win!"
                jump rps
            else:
                $ computer_score +=1
                "Rocks beats scissors! I lost!"
                jump rps
        
    label results:
        if rps_win:
            $ achievement_get("rps_game")
            i "I win."

            if only_scissors >= 3:
                $ achievement_get("rps_game_scissors")
                i "And I beat you using [player_selection]!"
            
            elif only_rock >= 3:
                $ achievement_get("rps_game_rock")
                i "And I beat you using [player_selection]!"

            elif only_paper >= 3:
                $ achievement_get("rps_game_paper")
                i "And I beat you using [player_selection]!"
            
            i "Take that!"
            if only_paper >=3 or only_rock >=3 or only_scissors >=3:
                a1 "Yeah yeah, rub it in. That was pure luck."
            else:
                a1 "I'll get you next time..."
            jump afterwards
        else:
            i "Aww, I lost."
            a1 "Bow to me!"
            jump afterwards

    label afterwards:
        hide screen scoring with noise_window
        play sound "audio/sfx/announce.mp3" volume 0.3
        "{i}\"Attention, passengers: this is your conductor speaking.\"{/i}"
        "{i}\"We are now arriving at the train stop shortly.\"{/i}"
        "{i}\"Passengers are reminded to mind the gap between the train and the platform edge when unboarding.\"{/i}"
        "{i}\"Thank you and have a nice day.\"{/i}"
        m2 "While you guys are playing your game, me and Lucy have packed your things up, thank you very much."
        a1 "Whoops, thanks."
        a1 "Do you have everything with you, [Main]?"
        "I'm not sure if I left anything at the seat I was sleeping in..."
        "If there's anything I left behind, so be it."
        i "I guess I'm all good now."
        a1 "Great! Let's go."
        stop ambient fadeout 6.0
        play sound trainstop
        window hide
        camera
        show forestbackground with dissolve:
            xalign 1.0
            linear 1 xalign 0.0
            xalign 1.0
            linear 1.5 xalign 0.0
            xalign 1.0
            linear 2.0 xalign 0.0
            xalign 1.0
            linear 2.5 xalign 0.0
            xalign 1.0
            easein 3.0 xalign 0.0
        pause 10.0
        
        window auto
        scene bg trainstation with wipeleft_scene
        i "We're here."
        "..."
        "I scanned the whole area."
        "There's nothing but trees and bushes as far as my eyes can see."
        "The sun is shining along with the birds singing, but the forest is eerily quiet."
        "Too quiet..."
        i "Um, where is the asylum?"
        lucy "Patience, [Main]. We are not there yet."
        lucy "We have to traverse through the forest."
        a1 "Adventure awaits us!" with vpunch
        "Alonso comes near me, and reaches his hand to me."
        a1 "Come along, my companion."
        i "What's up with that attitude of yours?"
        a1 "Aw, can you just appreciate my enthusiasm?"
        a1 "I'm trying to make this trip a bit fun."
        "This trip is going to be the end of me."
        i "Do you even know where're we going?"
        a1 "Err... no?"
        "I {bt=1}sighed{/bt}."
        m2 "Why don't we let Lucy lead the way?"
        m2 "She WAS assigned to this mission after all."
        i "That would make more sense."
        a1 "R-right."
        "Lucy goes in front of us and giggles as she takes the lead."
        scene bg forest1 with wipeleft_scene:
            yalign 1.0
            linear 300 yalign 0.0
        "We followed a narrow trail, with trees looming over us on either side."
        i "Wow, this place must be really hidden from the public."
        m2 "It must be a refugee site for individuals from other states."
        m2 "Hey Lucy, what kind of {i}\'asylum\'{/i} are we going to anyway?"
        m2 "Is it a rehabilitation center to treat the lunatics in nuthouses or a refugee site?"
        lucy "..."
        "Lucy remained silent."
        "I think she's trying to say something, but doesn't know how to respond yet."
        show black:
            alpha 0.0
            linear 20 alpha 0.7
        lucy "From what I have gathered... the asylum was a place for both."
        lucy "There is a reserved section for lunatics, but that was in the basement; forgotten."
        lucy "Mostly, the ground floors and upper floors were assigned to give shelter to asylum seekers."
        lucy "But for some unknown reasons, none of refugees were recorded to be released."
        lucy "I am guessing all the refugees were taken to the basement along with the lunatics."
        lucy "Where they performed... human experiments."
        lucy "It is probably the reason why the asylum was built here."
        lucy "Screams can be heard deep within the forest, even today."
        lucy "Where no one can hear you scream, which is the perfect cover up."
        lucy "It had been a prison for patients who had been locked away, forgotten by society."
        hide black
        lucy "Oh my, I might be rambling too much..."
        lucy "Surely you have heard stories about this place?"
        i "N-no..."
        "Sort of..."
        "I'm at loss for words."
        "Even Alonso is speechless."
        m2 "I do."
        "But not Raymon. I'm guessing he's read stories like these already."
        i "Poor refugees. All they wanted was a safe place..."
        i "And what they got is--{w=0.7}{nw}"
        m2 "...death."
        "..."
        m2 "Where are the people running the asylum?"
        lucy "That, I do not know."
        lucy "Only God knows where they went."
        "..."
        "We decided to keep quiet for the rest of our journey."
        window hide
        scene bg forest2 with wipeleft_scene:
            yalign 0.5
        window auto
        "As we walked deeper into the forest, the atmosphere began to change."
        "The air grew cooler, and the sunlight filtered through the trees in an eerie way."
        "I could hear strange noises in the distance, and the rustling of leaves seemed to follow us."
        a1 "Are we there yet already?"
        lucy "Yes. Just a bit more."
        lucy "It should be right around the corner."
        "..."
        "Lucy pauses for a moment and points out in the distance."
        lucy "Over there."
        window show
        scene bg outside_asylum:
            yalign 1.0
        with wipeleft
        window auto
        "I follow Lucy's degraded path."
        show bg outside_asylum:
            yalign 1.0
            linear 5 yalign 0.70
        "It was even more imposing than I had imagined, with broken walls and shattered windows."
        i "Wow, we've been walking for hours."
        "It's almost night already."
        lucy "We're here."
        lucy "Before we go ahead inside, is anyone of you ready?"
        a1 "My stuff's here."
        a1 "How about you, Raymon?"
        #TODO: play sound camera
        "{bt=2}*click*{/bt}"
        "I see Raymon waving a plastic film, taken by his camera."
        # m2 "I can almost hear the deafening souls..."
        m2 "Of course! I'm always prepared."
        a1 "The walls look it could give up at any moment..."
        lucy "Indeed, it does."
        lucy "We might have to get this mission done as soon as possible."
        i "I'm ready."
        lucy "Then let us."
        "We approached the entrance."
        scene black with wipeleft_scene
        jump scene_2

return