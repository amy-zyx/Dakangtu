# Fit the same pendant to each source sprite before the normal portrait scaling.
init -5 python:
    def amy_jack_with_cross(path):
        basename = path.rsplit("/", 1)[-1]
        placements = {
            "jack_black_tshirt.png": ((1024, 1536), (368, 648, 258, 240)),
            "jack_black_tshirt_thoughtful.png": ((1024, 1536), (365, 650, 254, 240)),
            "amy_autumn_jacket.png": ((1024, 1536), (378, 657, 248, 241)),
            "amy_time_school_jack.png": ((887, 1774), (358, 407, 159, 207)),
            "campus_jack.png": ((887, 1774), (344, 394, 198, 242)),
            "campus_jack_laugh.png": ((887, 1774), (345, 411, 198, 242)),
            "creator_jack.png": ((887, 1774), (383, 422, 137, 185)),
            "creator_jack_angry.png": ((887, 1774), (381, 418, 137, 185)),
            "beach_jack.png": ((887, 1774), (341, 483, 206, 270)),
            "boat_jack.png": ((887, 1774), (346, 484, 203, 268)),
            "date_jack_angry.png": ((887, 1774), (353, 500, 192, 236)),
            "date_jack_brow.png": ((887, 1774), (352, 500, 193, 236)),
            "amy_ch2_laugh_extended.png": ((887, 1774), (341, 500, 198, 241)),
            "amy_ch2_curious_extended.png": ((887, 1774), (341, 483, 198, 241)),
            "amy_ch2_thoughtful_extended.png": ((887, 1774), (341, 482, 198, 241)),
        }
        size, (x, y, width, height) = placements[basename]
        cross = Transform("images/characters/jack/amy_black_cross.svg", size=(width, height))
        return Composite(size, (0, 0), path, (x, y), cross)
