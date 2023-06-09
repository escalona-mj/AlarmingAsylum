﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Alarming Asylum")
define config.rollback_enabled = config.developer
define config.developer = "auto"
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.has_quicksave = False
define config.quicksave_slots = 0
define _dismiss_pause = False
define _game_menu_screen = None
define config.menu_include_disabled = False
define config.gl2 = True

define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
This game uses free assets. Background images are taken from {a=https://www.pexels.com}Pexels{/a}, background music are taken from {a=https://dova-s.jp/EN/}DOVA-SYNDROME{/a}, sound effects are taken from {a=https://www.pixabay.com}Pixabay{/a}, and fonts are taken from {a=https://www.fontspace.com}FontSpace{/a}. We do not claim ownership of any of the assets used in this game except for the art.

Certain effects such as {bt}"Kinetic Text Tags"{/bt} and {gtext}"renpyChromaGlitch"{/gtext} are made by {a=https://github.com/SoDaRa/Kinetic-Text-Tags}SoDaRa{/a} and {a=https://github.com/Gouvernathor/renpy-ChromaGlitch}Gouvernathor{/a} respectively.""")
# We have compiled all the terms and conditions of the respective websites in this link here. 
# FONTS

# Suicide Squadron made by {a=https://www.fontspace.com/heaven-castro}heaven castro{/a}

# Kingthings Printing Kit by {a=https://www.kingthingsfonts.co.uk/}Kevin King{/a}


# MUSIC

# "Alone Once Again" by {a=https://www.danielbirchmusic.com}Daniel Birch{/a}

# "Dark Ambient Atmosphere 2" by {a=https://pixabay.com/users/danydory-9903/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=141314"}danydory{/a}


# EFFECTS

# {bt}"Kinetic Text Tags"{/bt} effect by {a=https://github.com/SoDaRa/Kinetic-Text-Tags}SoDaRa{/a}

# {gtext}"renpyChromaGlitch"{/gtext} effect by {a=https://github.com/Gouvernathor/renpy-ChromaGlitch}Gouvernathor{/a}


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "Alarming-Asylum"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = audio.titlescreen


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = noise
define config.exit_transition = noise

define config.end_splash_transition = fade

define config.enter_yesno_transition = noise
define config.exit_yesno_transition = noise
define config.game_main_transition = fade

## Between screens of the game menu.

define config.intra_transition = noise


## A transition that is used after a game has been loaded.

define config.after_load_transition = noise


## Used when entering the main menu after the game has ended.

define config.end_game_transition = fade


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = noise_window
define config.window_hide_transition = noise_window


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "Alarming-Asylum-1656424159"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
