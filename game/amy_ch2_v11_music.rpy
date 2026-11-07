# Soundtrack for Ami Chapter 2, including approved music for release builds.
define amy_v11_music_tracks = {
    "chapter": "audio/bgm/bgm_act3_2.ogg",
    "time": "audio/bgm/ami_custom/love dream.mp3",
    "space": "audio/bgm/ami_custom/flower dance.mp3",
    "rules": "audio/bgm/bgm_act3_2.ogg",
    "ending_time": "audio/bgm/ami_custom/love romance.mp3",
    "ending_rules": "audio/bgm/bgm_act3.ogg",
    "ending_true": "audio/bgm/ami_custom/Clair de Lune - Claude Debussy.mp3",
    "ending_friends": "audio/bgm/bgm_act3.ogg",
    "ending_lottery": "audio/bgm/ami_custom/Another_Day_Of_Sun.mp3",
}

init python:
    def amy_v11_play_music(section):
        track = amy_v11_music_tracks[section]
        stem = track.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        balanced_track = "audio/bgm/ami_custom/balanced/" + stem + ".ogg"
        if renpy.loadable(balanced_track):
            track = balanced_track
        elif not renpy.loadable(track):
            track = "audio/bgm/bgm_act2_1.ogg"
        volume = 2.0 if track == amy_v11_music_tracks["time"] else 1.0
        renpy.music.play(track, channel="music", loop=True, fadeout=.7, fadein=1.25,
                         if_changed=True, relative_volume=volume)
