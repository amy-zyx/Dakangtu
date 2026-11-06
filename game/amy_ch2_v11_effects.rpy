# Sound and motion cues local to Amy's second chapter.
define amy_v11_custom_cues = (
    "glass", "latch", "step", "guitar", "landing", "portal",
    "card", "fusion", "alert", "repair", "surf", "canal", "room",
)

define amy_v11_reused_cues = {
    "drive": "car.ogg",
    "door": "act3_car_door.wav",
    "wind": "wind.ogg",
    "rain": "rain.ogg",
    "send": "act3_msg_send.wav",
    "message": "act3_msg_notify.wav",
    "impact": "act3_ground_give.wav",
}

define amy_v11_scene_ambience = {
    "drive": ("drive", .24),
    "bar": ("room", .32),
    "bookshelf": ("room", .26),
    "secret": ("room", .32),
    "counter": ("room", .32),
    "street": ("wind", .19),
    "rain_corridor": ("rain", .24),
    "rain_path": ("rain", .43),
    "beach": ("surf", .56),
    "water_town": ("canal", .35),
    "boat": ("canal", .44),
    "rooftop": ("wind", .14),
}

init python:
    renpy.music.register_channel("amy_v11_amb", mixer="sfx", loop=True)
    renpy.music.register_channel("amy_v11_fx", mixer="sfx", loop=False)

    def amy_v11_cue_path(cue):
        filename = amy_v11_reused_cues.get(cue)
        if filename:
            return "audio/sfx/" + filename
        return "audio/sfx/amy_v11/" + cue + ".wav"

    def amy_v11_cue(cue, volume=.46):
        renpy.music.play(amy_v11_cue_path(cue), channel="amy_v11_fx", relative_volume=volume)

    def amy_v11_ambience(background=None):
        ambience = amy_v11_scene_ambience.get(background)
        if ambience is None:
            renpy.music.stop(channel="amy_v11_amb", fadeout=.65)
            return
        cue, volume = ambience
        renpy.music.play(amy_v11_cue_path(cue), channel="amy_v11_amb",
                         fadein=.75, fadeout=.65, if_changed=True, relative_volume=volume)

define amy_v11_portal_dissolve = Dissolve(.65)

transform amy_v11_slow_camera:
    align (.5, .5)
    zoom 1.0
    ease 14.0 zoom 1.035

transform amy_v11_expression_motion(mood):
    yoffset 0
    easeout .13 yoffset (-8 if mood == "laugh" else -4)
    easein .24 yoffset 0

transform amy_v11_rain_fall:
    xoffset 0
    yoffset -125
    linear .7 xoffset -28 yoffset 0
    repeat

image amy_v11_rain = Composite(
    (1920, 1205),
    *[part for i in range(76)
      for part in ((37 + (i * 193) % 1915, (i * 251) % 1205),
                   Transform(Solid("#c6ddf62c", xysize=(2, 54)), rotate=12))]
)
