#############################
#        TRANSFORMS         #
#############################
transform textdissolve:
    alpha 0
    ease 0.25 alpha 1

transform hop:
    easein .1 yoffset -20
    easeout .1 yoffset 0

transform shaking:
    truecenter zoom 1.01
    choice:
        linear 0.1 xoffset -2 yoffset 2 
    choice:
        linear 0.1 xoffset 3 yoffset -3 
    choice:
        linear 0.1 xoffset 2 yoffset -2
    choice:
        linear 0.1 xoffset -3 yoffset 3
    choice:
        linear 0.1 xoffset 0 yoffset 0
    repeat

# Transform that blurs the background when opening screens.
transform withBlur:
    blur 15
transform noBlur:
    blur 0

transform fromrighttocenter_transform:
    right yalign 1.0
    ease 0.5 center


transform rewind:
    truecenter
    zoom 1.20
    parallel:
        easeout_bounce 0.2 xalign 0.55
        easeout_bounce 0.2 xalign 0.45
        repeat
    parallel:
        easeout_bounce 0.33 yalign 0.55
        easeout_bounce 0.33 yalign 0.45
        repeat

#dream text blur
transform truecenter_blur:
    xalign 0.5
    yalign 0.5
    blur 5

#transforms for characters
transform offscreenleft_transform:
    yalign 1.0
    ease 0.5 offscreenleft

transform offscreenright_transform:
    yalign 1.0
    ease 0.5 offscreenright

transform easeleft_transform:
    offscreenleft yalign 1.0
    ease 0.5 left
     
transform easeright_transform:
    offscreenright yalign 1.0
    ease 0.5 right
     
transform gocenter_transform:
    yalign 1.0
    ease 0.5 center
     
transform centertoleft_transform:
    center yalign 1.0
    ease 0.5 left
     
transform centertoright_transform:
    center yalign 1.0
    ease 0.5 right


#############################
#         CHARCTERS         #
#############################

define disclaimer = Character(None, centered)

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
define alonso = DynamicCharacter(
    'a1_name',
    kind=i,
    image="alonso")

default l1_name = "Lucy"
define lucy = DynamicCharacter(
    'l1_name',
    kind=i,
    image="lucy")

default m2_name = "Raymon"
define raymon = DynamicCharacter(
    'm2_name',
    kind=i,
    image="raymon")

#############################
#        TRANSITIONS        #
#############################
define wipeleft = ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64)

# define dissolve_scene_full = MultipleTransition([
#     False, Dissolve(1.0),
#     Solid("#000"), Pause(1.0),
#     Solid("#000"), Dissolve(1.0),
#     True])

define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    True])

define eyeopen = ImageDissolve("images/transitions/eyes.png", 1.5, 100)
define eyeclose = ImageDissolve("images/transitions/eyes.png", 1.5, 100, reverse=True)

define noise = ImageDissolve("images/transitions/noise.png", 0.40, ramplen=64)

define noise_splash = ImageDissolve("images/transitions/noise.png", 0.75, ramplen=64)

# define noise_scene = MultipleTransition([
#     False, ImageDissolve("images/transitions/noise.png", 0.5, ramplen=64),
#     Solid("#000"), Pause(0.25),
#     Solid("#000"), ImageDissolve("images/transitions/noise.png", 0.5, reverse=True, ramplen=64),
#     True])

define noise_window = ImageDissolve("images/transitions/noise.png", 0.25, ramplen=256)

image camera_flash:
    Solid("#ffffff2c")
    pause 0.1
    Solid("#00000000")

#############################
#      DYNAMIC SCENES       #
#############################

image bwAsylum:
    im.Blur("gui/asylum.jpg", 5.0)

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

image bg outside_asylum:
    im.MatrixColor(im.Blur("images/bgs/bg outside_asylum.jpg", 5.0), im.matrix.tint(.90,.65,1.0))

image bg door:
    im.MatrixColor(im.Blur("images/bgs/bg door.jpg", 5.0), im.matrix.tint(.90,.65,1.0))

image bg asylum:
    im.Blur("images/bgs/bg asylum.jpg", 5.0)

image bg office:
    im.Blur("images/bgs/bg office.jpg", 5.0)

image bg bed:
    im.Blur("images/bgs/bg bed.jpg", 5.0)

image bg locker:
    im.Blur("images/bgs/bg locker.jpg", 5.0)

image bg stairBasement:
    im.Blur("images/bgs/bg stairBasement.jpg", 5.0)

image bg basement:
    im.Blur("images/bgs/bg basement.jpg", 5.0)

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
image logo = ("gui/menu/logo.png")
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

# image logo_glitch:
#     "gui/menu/logo.png"
#     pause 0.5
#     choice:
#         glitch("gui/menu/logo.png", chroma=False, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
#         pause 0.2
#         glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
#         pause 0.1
#     choice:
#         glitch("gui/menu/logo.png", chroma=True, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=False, offset=60, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=True, offset=60, randomkey=None)
#         pause 0.1
#     choice:
#         glitch("gui/menu/logo.png", chroma=False, offset=1000, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=True, offset=1000, randomkey=None)
#         pause 0.1
#         glitch("gui/menu/logo.png", chroma=False, offset=1000, randomkey=None)
#         pause 0.1
#     choice:
#         pause 2.0
#     repeat

#############################
#      CHARACTER IMAGES     #
#############################

layeredimage lucy:

    group base: #body
        attribute l_base1 default:
            "lucy 1l_1r"
        attribute l_base2:
            "lucy 2l_2r"
        attribute l_base3:
            "lucy 1l_2r"
        attribute l_base4:
            "lucy 2l_1r"

    group water:
        attribute l_sweat:
            "images/characters/lucy/face/sweat.png"
        attribute l_cry:
            "images/characters/lucy/face/cry.png"

    group eyes:
        attribute l_eyes default:
            "images/characters/lucy/face/eyes_normal.png"
        attribute l_eyes_look:
            "images/characters/lucy/face/eyes_look.png"
        attribute l_eyes_closed:
            "images/characters/lucy/face/eyes_closed.png"
        attribute l_eyes_closedhappy:
            "images/characters/lucy/face/eyes_closedhappy.png"
        attribute l_eyes_anxious:
            "images/characters/lucy/face/eyes_anxious.png"

    group brows:
        attribute l_brow default:
            "images/characters/lucy/face/brow_normal.png"
        attribute l_brow_sad:
            "images/characters/lucy/face/brow_sad.png"
        attribute l_brow_serious:
            "images/characters/lucy/face/brow_serious.png"

    group mouth:
        attribute l_mouth default:
            "images/characters/lucy/face/mouth_smile.png"
        attribute l_mouth_open:
            "images/characters/lucy/face/mouth_open.png"
        attribute l_mouth_slightopen:
            "images/characters/lucy/face/mouth_slightopen.png"
        attribute l_mouth_serious:
            "images/characters/lucy/face/mouth_serious.png"


image lucy 1l_1r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/1r.png")
image lucy 2l_2r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 1l_2r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 2l_1r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/1r.png")


layeredimage raymon:

    group base: #body
        attribute r_base default:
            "images/characters/raymon/raymon_base.png"

    group eyes:
        attribute r_eyes default:
            "images/characters/raymon/face/eyes_normal.png"
        attribute r_eyes_look:
            "images/characters/raymon/face/eyes_look.png"
        attribute r_eyes_closed:
            "images/characters/raymon/face/eyes_closed.png"
        attribute r_eyes_closedhappy:
            "images/characters/raymon/face/eyes_closedhappy.png"
        attribute r_eyes_anxious:
            "images/characters/raymon/face/eyes_anxious.png"
    
    group water:
        attribute r_sweat:
            "images/characters/raymon/face/sweat.png"
        attribute r_cry:
            "images/characters/raymon/face/cry.png"

    group brows:
        attribute r_brow default:
            "images/characters/raymon/face/brow_normal.png"
        attribute r_brow_sad:
            "images/characters/raymon/face/brow_sad.png"
        attribute r_brow_serious:
            "images/characters/raymon/face/brow_serious.png"

    group mouth:
        attribute r_mouth default:
            "images/characters/raymon/face/mouth_smile.png"
        attribute r_mouth_open:
            "images/characters/raymon/face/mouth_open.png"
        attribute r_mouth_slightopen:
            "images/characters/raymon/face/mouth_slightopen.png"
        attribute r_mouth_serious:
            "images/characters/raymon/face/mouth_serious.png"

layeredimage alonso:

    group base: #body
        attribute a_base default:
            "images/characters/alonso/alonso_base.png"

    group water:
        attribute a_sweat:
            "images/characters/alonso/face/sweat.png"
        attribute a_cry:
            "images/characters/alonso/face/cry.png"

    group eyes:
        attribute a_eyes default:
            "images/characters/alonso/face/eyes_normal.png"
        attribute a_eyes_look:
            "images/characters/alonso/face/eyes_look.png"
        attribute a_eyes_closed:
            "images/characters/alonso/face/eyes_closed.png"
        attribute a_eyes_closedhappy:
            "images/characters/alonso/face/eyes_closedhappy.png"
        attribute a_eyes_anxious:
            "images/characters/alonso/face/eyes_anxious.png"

    group brows:
        attribute a_brow default:
            "images/characters/alonso/face/brow_normal.png"
        attribute a_brow_sad:
            "images/characters/alonso/face/brow_sad.png"
        attribute a_brow_serious:
            "images/characters/alonso/face/brow_serious.png"

    group mouth:
        attribute a_mouth default:
            "images/characters/alonso/face/mouth_smile.png"
        attribute a_mouth_open:
            "images/characters/alonso/face/mouth_open.png"
        attribute a_mouth_slightopen:
            "images/characters/alonso/face/mouth_slightopen.png"
        attribute a_mouth_serious:
            "images/characters/alonso/face/mouth_serious.png"

#############################
#           AUDIO           #
#############################
define audio.titlescreen = "<loop 12.975 to 84.371>audio/bgm/wind.mp3"

# define audio.titlescreen = "<loop 23.154 to 83.098>audio/bgm/titlescreen.ogg"
#<loop 23.154 to 83.098 or 1m 23.098>

define audio.train = "audio/ambient/train.ogg"
define audio.forest = "audio/ambient/forest.mp3"

define audio.asylum = "<loop 105.970 to 203.363>audio/bgm/brokenclock.mp3"
#<loop 1m 45.970/105.970 to 3m 23.363/203.363>

define audio.merrygoround = "<loop 24.171>audio/bgm/merrygoround.mp3"

define audio.merrygoround2 = "<loop 24.162>audio/bgm/merrygoround2.mp3"

define audio.windowdrops = "<loop 43.330 to 117.347>audio/bgm/windowdrops.mp3"
