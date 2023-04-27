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
    ctc_position="fixed")

default a1_name = "Alonso"
define a1 = DynamicCharacter(
    'a1_name',
    kind=i)

default l1_name = "Lucy"
define lucy = DynamicCharacter(
    'l1_name',
    kind=i,
    image="lucy")

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
    Solid("#000"), ImageDissolve("images/transitions/noise.png", 0.75, reverse=True, ramplen=64),
    True])

define noise_window = ImageDissolve("images/transitions/noise.png", 0.25, ramplen=256)

transform textdissolve:
        alpha 0
        ease 0.25 alpha 1

#############################
#      DYNAMIC SCENES       #
#############################
image train1:
    im.Blur("images/bgs/train/train1.png", 5.0)

image train2:
    im.Blur("images/bgs/train/train2.png", 5.0)

image forestbackground:
    im.Blur("images/bgs/train/forestbackground.png", 5.0)
    yoffset -250
    
image bg trainstation:
    im.Blur("images/bgs/bg trainstation.jpg", 5.0)

image bg forest1:
    im.Blur("images/bgs/bg forest1.jpg", 5.0)

image bg forest2:
    im.Blur("images/bgs/bg forest2.jpg", 5.0)
    
image forest2 night:
    im.MatrixColor(im.Blur("images/bgs/bg forest2.jpg", 5.0), im.matrix.tint(.44,.65,.75))

image bg outside_asylum:
    im.MatrixColor(im.Blur("images/bgs/bg outside_asylum.jpg", 5.0), im.matrix.tint(.90,.65,1.0))

image bg asylum:
    im.Blur("images/bgs/bg asylum.jpg", 5.0)

#############################
#        MAIN MENU          #
#############################

image bird1 = SnowBlossom("gui/menu/bird1.png", count=3, border=150, xspeed=(100,250), yspeed=(-150,-90), fast=False, horizontal=False)
image bird2 = SnowBlossom("gui/menu/bird2.png", count=3, border=150, xspeed=(100,250), yspeed=(-150,-90), fast=False, horizontal=False)
image bird3 = SnowBlossom("gui/menu/bird3.png", count=3, border=150, xspeed=(100,250), yspeed=(-150,-90), fast=False, horizontal=False)

# image vigenette = Composite(
#     (1920,1080),
#     (0,0), "gui/menu/rectangle_top.png",
#     (0,871), "gui/menu/rectangle_bottom.png"
#     )

image graybg = ("gui/menu/gray.png")
image moon = ("gui/menu/moon.png")
image house = ("gui/menu/house.png")
image trees = ("gui/menu/trees.png")
image grass = ("gui/menu/grass.png")
image grunge = ("gui/menu/grunge.png")
image menuFrame = ("gui/menu/menu_frame.png")

#############################
#           SCREENS         #
#############################

image unlocked_medal = ("gui/achievements/medal.png")
image locked_medal = ("gui/achievements/locked_medal.png")

image skip_overlay:
    alpha 0.75
    xalign 0.5
    yalign 0.5
    zoom 1.2
    glitch("gui/overlay/confirm.png", chroma=True, offset=500, randomkey=None)
    pause 0.1
    glitch("gui/overlay/confirm.png", chroma=False, offset=500, randomkey=None)
    pause 0.1
    repeat

image logo:
    "gui/menu/logo.png"
    pause 0.5
    choice:
        glitch("gui/menu/logo.png", chroma=False, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
        pause 0.2
        glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
        pause 0.1
    choice:
        glitch("gui/menu/logo.png", chroma=True, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
        pause 0.1
    choice:
        glitch("gui/menu/logo.png", chroma=False, offset=1000, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=True, offset=1000, randomkey=None)
        pause 0.1
        glitch("gui/menu/logo.png", chroma=False, offset=1000, randomkey=None)
        pause 0.1
    choice:
        pause 2.0
    repeat

#  Transform blurring the image.
transform withBlur:
    blur 15
transform noBlur:
    blur 0


#############################
#      CHARACTER IMAGES     #
#############################

layeredimage lucy:

    group base: #body
        attribute base1 default:
            "lucy 1l_1r"
        attribute base2:
            "lucy 2l_2r"
        attribute base3:
            "lucy 1l_2r"
        attribute base4:
            "lucy 2l_1r"

    group eyes:
        attribute eyes default:
            "images/characters/lucy/face/eyes_normal.png"
        attribute eyes_look:
            "images/characters/lucy/face/eyes_look.png"
        attribute eyes_closed:
            "images/characters/lucy/face/eyes_closed.png"

    group brows:
        attribute brow default:
            "images/characters/lucy/face/brow_normal.png"
        attribute brow_sad:
            "images/characters/lucy/face/brow_sad.png"
        attribute brow_serious:
            "images/characters/lucy/face/brow_serious.png"

    group mouth:
        attribute mouth default:
            "images/characters/lucy/face/mouth_smile.png"
        attribute mouth_open:
            "images/characters/lucy/face/mouth_open.png"
        attribute mouth_slightopen:
            "images/characters/lucy/face/mouth_slightopen.png"
        attribute mouth_serious:
            "images/characters/lucy/face/mouth_serious.png"


image lucy 1l_1r = im.Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/1r.png")
image lucy 2l_2r = im.Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 1l_2r = im.Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 2l_1r = im.Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/1r.png")


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
define audio.titlescreen = "<loop 23.154 to 83.098>audio/bgm/titlescreen.ogg"
#<loop 23.154 to 83.098 or 1m 23.098>

define audio.train = "audio/ambient/train.ogg"
