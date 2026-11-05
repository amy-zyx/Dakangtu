# Shared Amy Chapter 2 state, persistent collection, and legacy-label compatibility.
define amy_ch2_jack_narrator = Character(None, what_color="#cccccc")
define amy_ch2_system = Character("系统", color="#b7d9ff")
default amy_ch2_stats = {"love": 50, "wisdom": 50, "luck": 50}
default amy_ch2_awarded_nodes = []
default amy_ch2_choices = {}
default amy_ch2_completed = []
default amy_ch2_fragments = []
default amy_ch2_true_ending_seen = False
default amy_ch2_schema = 0
default amy_ch2_selected_route = None
default amy_ch2_rule_visual = ""
default persistent.amy_ch2_cards = []
default persistent.amy_ch2_endings = []
default persistent.amy_ch2_true_ending_completed = False
default amy_ch2_card_new = False

define amy_ch2_backgrounds = {
    "大学迎新摊位": "images/backgrounds/amy_ch2/amy_time_welcome.png",
    "大学林荫道": "images/backgrounds/amy_ch2/amy_time_path.png",
    "黄昏长椅": "images/backgrounds/amy_ch2/amy_time_bench.png",
    "巴黎街道": "images/backgrounds/amy_ch2/amy_space_paris.png",
    "塞纳河与埃菲尔铁塔": "images/backgrounds/amy_ch2/amy_space_seine.png",
    "纽约华尔街": "images/backgrounds/amy_ch2/amy_space_newyork.png",
    "硅谷科技园": "images/backgrounds/amy_ch2/amy_space_siliconvalley.png",
    "夏威夷海边": "images/backgrounds/amy_ch2/amy_space_hawaii.png",
    "悬浮方块世界": "images/backgrounds/amy_ch2/amy_rules_floating.png",
}

image amy_ch2_split_rooms = Composite(
    (1920, 1080),
    (0, 0), Transform(Transform("images/backgrounds/amy_ch2/amy_space_amy_room.png", size=(1920, 1080)), crop=(480, 0, 960, 1080)),
    (960, 0), Transform(Transform("images/backgrounds/amy_ch2/amy_space_jack_room.png", size=(1920, 1080)), crop=(480, 0, 960, 1080)),
    (957, 0), Solid("#182239", xysize=(6, 1080)),
)

image amy_ch2_school_ami = Composite(
    (900, 1080),
    (32, 195), Transform("images/characters/ami/amy_time_school_ami_ponytail.png", zoom=0.95),
)
image amy_ch2_school_jack = Composite(
    (900, 1080),
    (89, 66), Transform("images/characters/jack/amy_time_school_jack.png", zoom=0.82),
)

init python:
    def amy_ch2_award_once(node, stat, delta, notify=True):
        if node in store.amy_ch2_awarded_nodes:
            return
        store.amy_ch2_awarded_nodes = store.amy_ch2_awarded_nodes + [node]
        if stat:
            stats = dict(store.amy_ch2_stats)
            stats[stat] = max(0, min(100, stats[stat] + delta))
            store.amy_ch2_stats = stats
            if notify:
                title = {"love": "心动", "wisdom": "理智", "luck": "幸运"}[stat]
                renpy.notify(title + " +" + str(delta))
        elif notify:
            renpy.notify("属性未变")

    def amy_ch2_sync_cards():
        routes = ("time", "space", "rules")
        cards = [r for r in routes if r in (persistent.amy_ch2_cards or []) or r in (persistent.amy_ch2_endings or []) or r in store.amy_ch2_completed or r in store.amy_ch2_fragments]
        persistent.amy_ch2_cards = list(cards)
        persistent.amy_ch2_endings = list(cards)
        store.amy_ch2_completed = list(cards)
        store.amy_ch2_fragments = list(cards)

    def amy_ch2_migrate():
        amy_ch2_sync_cards()
        if store.amy_ch2_schema:
            return
        # Convert saved choices from the earlier Chapter 2 draft once.
        drink = {"classic": "favorite"}.get(store.amy_ch2_drinkChoice, store.amy_ch2_drinkChoice)
        book = {"solve": "together", "ask": "staff", "fail": "failed"}.get(store.amy_ch2_bookshelfChoice)
        if drink in ("surprise", "gin", "favorite"):
            store.amy_ch2_choices["cocktail"] = drink
            amy_ch2_award_once("cocktail", {"surprise": "love", "gin": "wisdom", "favorite": "luck"}[drink], 10, False)
        if book:
            store.amy_ch2_choices["bookshelf"] = book
            amy_ch2_award_once("bookshelf", {"together": "love", "staff": "wisdom", "failed": None}[book], 10, False)
        store.amy_ch2_schema = 4

    def amy_ch2_finish_world(route):
        amy_ch2_sync_cards()
        is_new = route not in persistent.amy_ch2_cards
        if is_new:
            persistent.amy_ch2_cards = list(persistent.amy_ch2_cards) + [route]
        amy_ch2_sync_cards()
        renpy.save_persistent()
        return is_new


label amy_ch2_bookshelf:
    jump amy_v11_date4

label amy_ch2_secret_bar:
    jump amy_v11_date5

label amy_ch2_bar_chat:
    jump amy_v11_date6

label amy_ch2_street_walk:
    jump amy_v11_date7

label amy_ch2_car_question:
    jump amy_v11_date8

label amy_ch2_route_hub:
    jump amy_v11_hub

label amy_ch2_time:
    jump amy_v11_time

label amy_ch2_space:
    jump amy_v11_space

label amy_ch2_rules:
    jump amy_v11_rules

label amy_ch2_true_ending:
    jump amy_v11_true

label amy_ch2_scene_4:
    jump amy_v11_date4

label amy_ch2_scene_5:
    jump amy_v11_date5

label amy_ch2_scene_6:
    jump amy_v11_date7

label amy_ch2_bookshelf_draft:
    jump amy_v11_date4

label amy_ch2_epilogue:
    jump amy_v11_hub

label amy_ch2_tbc:
    jump amy_v11_date4

label amy_ch2_route_complete:
    jump amy_v11_ending

label amy_ch2_card_fusion:
    jump amy_v11_fusion

label amy_ch2_kiss(travel=False):
    scene amy_autumn_car
    with dissolve
    return
