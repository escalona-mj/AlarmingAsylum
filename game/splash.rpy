# image splash1 = "gui/splash1.png"
# label splashscreen:
#     $ renpy.music.play(config.main_menu_music)
#     if renpy.variant("small"):
#         if not persistent.autoload == "end":
#             $ config.allow_skipping = False
#             show splash1 at truecenter:
#                 zoom 0.35
#             with dissolve
#             $ renpy.pause(2,0, hard=True)
#             hide splash1 with dissolve
#             $ config.allow_skipping = True
#         else:
#             jump bad_end
#     else:
#         jump not_for_pc
#     return
