#############################
#         CHARCTERS         #
#############################

define narrator = Character(
    ctc="ctc",
    ctc_position="fixed")

define i = Character(
    '[Main]',
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_pause="ctc_pause",
    ctc_position="fixed")

default a1_name = "Alonso"
define a1 = DynamicCharacter(
    'a1_name',
    kind=i)

default l1_name = "Lucy"
define l1 = DynamicCharacter(
    'l1_name',
    kind=i)

default m2_name = "Raymon"
define m2 = DynamicCharacter(
    'm2_name',
    kind=i)

#############################
#        TRANSITIONS        #
#############################
define wipeleft = ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    True])

define eyeopen = ImageDissolve("images/transitions/eyes.png", 1.5, 100)
define eyeclose = ImageDissolve("images/transitions/eyes.png", 1.5, 100, reverse=True)

define noise = ImageDissolve("images/transitions/noise.png", 0.75, ramplen=64)

define noise_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/noise.png", 0.75, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/noise.png", 0.75, ramplen=64),
    True])

define noise_window = ImageDissolve("images/transitions/noise.png", 0.25, ramplen=256)

#############################
#      DYNAMIC SCENES       #
#############################
image train1:
    im.Blur("images/bgs/train/train1.png", 3.0)

image train2:
    im.Blur("images/bgs/train/train2.png", 3.0)

image forestbackground:
    im.Blur("images/bgs/train/forestbackground.png", 5.0)
    yoffset -250
    

#############################
#        MAIN MENU          #
#############################

transform blink_blur:
    blur 10
    linear 1.0 alpha 0.5
    linear 2.0 alpha 0.0
    repeat

transform blink:
    zoom .5
    linear 1.0 alpha 0.0 blur 5
    linear 5.0 alpha 1.0 blur 0
    repeat

image particle_blur = SnowBlossom(At("gui/menu/particle_small.png", blink_blur), border=150, count=10, start=0.00000000001, fast=False,  yspeed=(-100, -80),  xspeed=(-200,200), horizontal=True)
image particle = SnowBlossom(At("gui/menu/particle_small.png", blink), count=10, border=150, xspeed=(0, -10), start=10, fast=False, horizontal=False)

image medal = ("gui/achievements/medal.png")
image locked_medal = ("gui/achievements/locked_medal.png")

image vigenette = Composite(
    (1920,1080),
    (0,0), "gui/menu/rectangle_top.png",
    (0,871), "gui/menu/rectangle_bottom.png"
    )

image asylum:
    im.Blur("gui/menu/asylum.jpg", 3.0)

image bg trainstation blurred:
    im.Blur("images/bgs/bg trainstation.jpg", 5.0)

#############################
#      CHARACTER IMAGES     #
#############################

image merah neutral = Composite(
    (980,980),
    (0,25), "images/characters/merah neutral.png")

#############################
#            FONT           #
#############################

style partner_handwriting:
    font "fonts/NaomisHand-Regular.ttf"

style disclaimer_font:
    color "#ffffff"
    font "fonts/Astonished-KMrD.ttf"

#############################
#           AUDIO           #
#############################
define audio.titlescreen = "audio/bgm/titlescreen.ogg"

define audio.train = "audio/ambient/train.ogg"
