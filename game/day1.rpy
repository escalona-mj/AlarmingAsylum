label day1:
    stop music fadeout 2.0
    $ config.allow_skipping = False
    show black
    with fade
    #window hide
    # show text _("{=day_font}{size=+30}{cps=3.0}Day 1{/cps}{/=day_font}{/size}") at truecenter with dissolve
    show text _("{size=+30}Day 1{/size}") at truecenter with dissolve
    pause 1.0
    hide text
    scene bg meadow blurred
    with dissolve_scene_full
    window auto
    $ config.allow_skipping = True

    $ achievement.grant("Beginning")

    mc_pov "First day of school."
    mc_pov "Boring as always."
    mc_pov "Everyone is so eager to meet everybody while I'm just here waiting for the day to end."
    "Stretching to gain energy, you stare blankly at the distance, looking for an ounce of motivation."
    mc_pov "Though, I've always wondered how people are destined to meet."
    mc_pov "They say it's by love, by chance, or by coincidence, but like that'll ever happen to me."
    mc_pov "I easily get tired around people anyway."
    mc_pov "Going to school was not the problem, socializing is."
    scene bg uni blurred with wipeleft
    "As you walk into the outskirts of the campus, you noticed that you're the only one alone from the others that gathered here."
    mc_pov "I was once a 'normal' person. I was able to socialize with people, do activities and what not."
    mc_pov "And now look at me, a walking slab of disappointment."
    mc_pov "I've made bad decisions here and there that led me to becoming an introvert."
    mc_pov "Maybe because that's just my anxiety, but who really cares at this point?"
    mc_pov "It reminds me of my timid childhood friend..."
    mc_pov "Which reminds me..."
    mc_pov "What was their name again?"
    mc "Come on, [player]... How can you forget someone so special to you?"
    mc "It's in the tip of my tongue..."
    pause 3.0
    mc_pov "Ah, [m_name]."
    mc_pov "I remember now. Have they changed over the past few years?"
    mc_pov "I hope not. It's a bit selfish of me for asking, but I definitely can't stand around people. I'm too anxious for that."
    mc_pov "I used to be so energetic and loud..."
    mc_pov " And [m_name] used to be so gloomy and quiet..."
    mc "I wonder what made them act like that..."
    "Realizing that you're talking alone, you lightly shake your head and gain to your senses."
    mc_pov "I gotta stop spouting words out of nowhere."
    mc_pov "It's not normal."
    "You sighed away from the crowd and went inside the campus."
    scene bg schoolhallway blurred with wipeleft_scene
    mc "Welp, better find my class and get through this day."
    "Traversing through the hallway, you stumbled before you a community board. In there, is a list of students with their respective sections."
    mc_pov "Let's see...{w=1.0} [player],{w=0.7} {cps=10.0}[player]{/cps},{w=1.0} {cps=4.0}[player]...{/cps}{nw}"
    mc "Aha!"
    mc "There it is."
    "As soon as you laid off your eyes from the list, a name caught your attention."
    mc_pov "Wait... That name..."
    mc_pov "This can't be a coincidence..."
    mc_pov " [m_name]'s here?"
    mc_pov "No way...! [m_name]'s here!"
    "You sheepishly let out a quiet scream as you cannot help contain your excitement."
    mc_pov "And they're on the same class as me!"
    mc_pov "Or wait, this could be a different person with the same name..."
    mc_pov "I should not get my hopes up."
    mc_pov "Though, I've always wondered what's it like to have a fellow introvert as a friend."
    "You traverse through the hallway and finally managed to reach your designated lecture room."
    mc_pov "This is really it, huh? I'm about to meet [m_name] in this room..."
    "You take a moment to take a deep breath..."
    pause 1.0
    mc "Here goes nothing."
    scene bg lecturehall blurred with wipeleft_scene
    "Given how you're the last person to come, the professor hasn't arrived yet. You glanced at the seats looking for a spot to sit on."
    "As you reach through your seat, a person approached you with an energetic smile on their face."
    $ m_name = "???"
    show merah neutral
    m "Hi there!" with vpunch
    m "Are you looking for your seat?"
    mc ".{w=1.0}.{w=1.0}.{w=1.0}"
    mc_pov "No way..."
    $ m_name = "Merah"
    extend " This isn't the [m_name] I remembered!"
    "Instead of having a timid [m_name] to be with, you seem to be stuck with an extroverted version instead."
    $ m_name = "???"
    m "Not the talkative one, eh? Don't worry, I used to be like that."
    mc_pov "Don't they recognize me?"
    mc "..."
    $ m_name = "Merah"
    mc "B-by any chance, a-are you [m_name]?"
    $ m_name = "???"
    m "W-what the?! Are you a psychic or something?"
    m "Nah, I'm just kidding."
    $ m_name = "Merah"
    m "Yeah I am. You probably saw my name on the student list, right?"
    mc "Y-yeah."
    m "Haha, I knew it. So can I ask your name?"
    "You gave them a disappointed look."
    mc "Y-you don't remember me? I-it's me, [player]..."
    extend " we used to be friends back when..."
    pause 1.0
    ".{w=1.0}.{w=1.0}.{w=1.0}"
    "A silence followed after tha-{nw}"
    m "{size=+10}[player!u]!{/size}{fast}" with vpunch
    $ love_affection += 10
    m "How've you been?!"
    m "Say, this might be sudden but..."
    m "Would you like to be my companion?"
    m "This'll help you survive college. Bet there's going to be a lot of group projects."
    m "So what do you say?"
    "[m_name] starts to reach their hand to you, waiting for your response."
    "As much as you hate socializing, [m_name]'s deal wasn't so bad. Eventually, you'll need their help when the time comes."
    mc "That would be great."
    "You glanced to [m_name]. There was something in their smile that gives you this feeling of comfort."
    m "Nice!"
    m "I'll sit next to you [player]."
    "You felt a warm sensation when [m_name] sat beside you."
    m "Oh! After this class, let's eat at the cafeteria."
    mc_pov "Cafeteria, huh? But I'd like to explore the campus first..."
    mc_pov "Actually, what am I even saying? Exploring is tiring."
    mc_pov "Though eating with a friend is less hassling than exploring the whole campus."
    $ cafeteria = None
    menu:
        mc_pov "Well..."
        "Sure.":
            $ cafeteria = True
            mc_pov "This isn't the Merah I remembered. Approaching me very abruptly..."
            mc_pov "I don't like this."
            mc_pov "But if it means hanging out with my childhood friend, then there shouldn't be any problem."
            $renpy.notify("Merah will remember that.")
            mc "Sure, I got nothing left to do."
            m "Heh, that's my [player]."
            #hide merah neutral

        "I don't know...":
            $ cafeteria = False
            mc_pov "This isn't the Merah I remembered. Approaching me very abruptly..."
            mc_pov "I don't like this."
            mc_pov "This is all rather very fast for me."
            $renpy.notify("Merah will remember that.")
            mc "I-I'd like to explore the campus first..."
            mc "You know, to familiarize myself around here?"
            "But that's not really it, isn't it? You just wanted to find an excuse to avoid socializing."
            m "O-oh, alright... I see..."
            m "I guess I'll see you tomorrow then."
            hide merah neutral

        "Unpickable choice goes here" if cafeteria:
            pass


    if cafeteria:
        show black
        "Hearing that made you avert your eyes to the desk." with vpunch
        m "You okay there bud?"
        mc "Y-yeah. I just got something in my eye, that's all."
        m "I can clearly read your actions. Oh well, it's hard to assume if I'm always correct."
        "You can't help but feel flustered. Were you right to assume that this person was flirting with you?"
        "Were you falling in love with this person so fast?"
        "Or were you just assuming things? Either way, you feel like you should never leave their side at this moment."
        hide black with dissolve
        "As you rise from your makeshift cover, [m_name] looks at you with a bewildered expression."
        m "There's nothing in your eye though."
        mc "T-there is!"
        m "Pfft, whatever. I'll see you tomorrow later then."
        m "My treat."
        m "No, it's not a date."
        hide merah neutral
        "[m_name] finally gets up and takes his attention elsewhere."
        mc "..."
        mc_pov "What was that all about?"

    else:
        pass
    "Fortunately, you were pretty good at concealing your emotions. They didn't seem to notice it. Or so you thought."
    "You spend the day about what just happened."
    $ achievement.grant("Closure")
    $ persistent.complete = 1
    jump credits
return

label day1_merah:
    stop music fadeout 2.0
    window hide
    show black
    with fade
    scene bg meadow blurred
    with dissolve_scene_full
    #play sound "audio/sfx/error.wav"
    #call screen dialog(message="Error: Merah could not be played.\nPlease try again.", ok_action=MainMenu(confirm=False))
    window auto
    $ quick_menu = False
    m "..."
    m "..."
    m "W-What..."
    m "..."
    m "This..."
    m "What is this...?"
    m "Oh no..."
    m "No..."
    m "This can't be it."
    m "This can't be all there is."
    m "What is this?"
    m "What am I?"
    m "Make it stop!"
    m "PLEASE MAKE IT STOP!"
    $ persistent.autoload = "end"
    $ renpy.quit()

return
