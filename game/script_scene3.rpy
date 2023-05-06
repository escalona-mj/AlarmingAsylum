transform swing:
    xalign 0.5
    yalign 1.75
    zoom 2.0
    subpixel True
    rotate -1
    ease 2.0 rotate 1
    ease 2.0 rotate -1
    repeat

image hang = ("images/others/hanged_person.png")

image white = Solid("#ffffff2f")

label act2_hanging:
    scene bg office
    show black:
        alpha 0.5
    with wipeleft_scene
    "It's somehow even darker here now."
    alonso "Has it always been this dark?"
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
    $ config.skipping = False
    raymon "Let me just-{nw}"
    show hang at swing
    show expression AlphaMask("white", At("hang", swing)) as mask
    show expression AlphaMask("flashlight", At("hang", swing)) as mask2
    show flashlight onlayer transient
    hide black
    window hide(None)
    play sound "audio/sfx/scare.mp3"
    play music "audio/bgm/act2.mp3" loop
    pause 4.5
    window auto
    "what"