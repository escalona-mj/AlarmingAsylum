#############################
#         CHARCTERS         #
#############################
define narrator = Character(window_background = Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0),ctc="ctc", ctc_position="fixed")

default m_name = "Merah"
define m = DynamicCharacter('m_name', window_background = Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0), what_prefix='"', what_suffix='"', ctc="ctc", ctc_pause="ctc_pause", ctc_position="fixed")

define mc = DynamicCharacter('player', window_background = Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0), what_prefix='"', what_suffix='"', ctc="ctc", ctc_pause="ctc_pause", ctc_position="fixed")
define mc_pov = DynamicCharacter('player', window_background = Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0), what_prefix='{i}', what_suffix='{/i}', ctc="ctc", ctc_pause="ctc_pause", ctc_position="fixed")

default love_affection = 0


#############################
#        TRANSITIONS        #
#############################

define flash = Fade(0.1, 0.5, 0.5, color="#fff")

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
#           IMAGES          #
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


image merah neutral = ("images/characters/merah neutral.png")

image medal = ("gui/achievements/medal.png")

image locked_medal = ("gui/achievements/locked_medal.png")

image vigenette = Composite(
    (1920,1080),
    (0,0), "gui/menu/rectangle_top.png",
    (0,871), "gui/menu/rectangle_bottom.png"
    )

image asylum:
    im.Blur("gui/menu/asylum.jpg", 3.0)

image bg meadow blurred:
    im.Blur("images/bgs/bg meadow.jpg", 5.0)

image bg uni blurred:
    im.Blur("images/bgs/bg uni.jpg", 5.0)

image bg lecturehall blurred:
    im.Blur("images/bgs/bg lecturehall.jpg", 5.0)

image bg schoolhallway blurred:
    im.Blur("images/bgs/bg schoolhallway.jpg", 5.0)

#############################
#            FONT           #
#############################

style partner_handwriting:
    font "fonts/NaomisHand-Regular.ttf"

style author_font:
    color "#ffffff"
    font "fonts/DFG W5.ttf"

# define titlescreen = "<loop 3>audio/bgm/1.ogg"
