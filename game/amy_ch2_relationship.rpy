# Hidden relationship scoring. Each node contributes only its currently selected option.
define amy_v12_base_stats = {"love": 60, "wisdom": 50, "luck": 50}
define amy_v12_rewards = {'cocktail': {'让 Jack 选一杯 Surprise Me': {'luck': 5},
              '试试 Gin：Aviation': {'wisdom': 10, 'love': 3},
              '点熟悉的 Creamy Panna Cotta': {'wisdom': 10}},
 'bookshelf': {'两个人一起寻找机关': {'love': 10}, '直接请工作人员打开': {'wisdom': 10, 'love': 3}, '自己试了半天没找到': {}},
 'time_welcome': {'陪她去吉他社试听': {'love': 5},
                  '先带她办完新生手续': {'wisdom': 5, 'love': 3},
                  '带她走滑板社发现的校园近路': {'luck': 5}},
 'space_paris': {'带 Ami 去挑一件巴黎的小礼物': {'love': 5},
                 '去左岸书店，各选一本书交换': {'wisdom': 5, 'love': 3},
                 '跟着街头音乐随机拐进一条小巷': {'luck': 5}},
 'space_market': {'先保护本金，再争取收益': {'wisdom': 5, 'love': 3},
                  '为未来的自由设立目标': {'love': 5},
                  '留一小部分资金尝试新机会': {'luck': 5}},
 'space_boundary': {'每次出现前先问对方愿不愿意': {'wisdom': 5, 'love': 5},
                    '约定一个只属于两人的暗号': {'love': 5},
                    '把下一站交给彼此的共同记忆': {'luck': 5}},
 'rules_bridge': {'建立可重复的物理测试': {'wisdom': 5, 'love': 3},
                  '先保护居民再试验': {'love': 5},
                  '用一次大胆的现场实验': {'luck': 5}},
 'rules_stone': {'移走石头，邀请他探索世界': {'wisdom': 5, 'love': 3},
                 '和他一起推一次': {'love': 5},
                 '把石头改造成会滚动的音乐舞台': {'luck': 5}},
 'rules_contract': {'平等权限，各自拥有独立项目': {'wisdom': 5, 'love': 5},
                    '共同建造一座可以自由进出的家': {'love': 5},
                    '让所有居民都能提出修改世界的建议': {'luck': 5}}}
define amy_v12_choice_aliases = {'cocktail': {'surprise': '让 Jack 选一杯 Surprise Me',
              'gin': '试试 Gin：Aviation',
              'favorite': '点熟悉的 Creamy Panna Cotta',
              'classic': '点熟悉的 Creamy Panna Cotta'},
 'bookshelf': {'together': '两个人一起寻找机关',
               'staff': '直接请工作人员打开',
               'failed': '自己试了半天没找到',
               'solve': '两个人一起寻找机关',
               'ask': '直接请工作人员打开',
               'fail': '自己试了半天没找到'},
 'space_paris': {'带 Amy 去挑一件巴黎的小礼物': '带 Ami 去挑一件巴黎的小礼物'}}

define amy_v12_true_love_min = 86
define amy_v12_friends_wisdom_min = 81

init python:
    def amy_v12_recalculate():
        totals = dict(amy_v12_base_stats)
        for node, choice in store.amy_ch2_choices.items():
            choice = amy_v12_choice_aliases.get(node, {}).get(choice, choice)
            for stat, amount in amy_v12_rewards.get(node, {}).get(choice, {}).items():
                totals[stat] += amount
        store.amy_ch2_stats = {k: max(0, min(100, v)) for k, v in totals.items()}

    def amy_v12_has_all_cards():
        return all(route in (persistent.amy_ch2_cards or []) for route in ("time", "space", "rules"))

    def amy_v12_true_ready():
        stats = store.amy_ch2_stats
        return (amy_v12_has_all_cards()
                and stats["love"] >= amy_v12_true_love_min
                and stats["love"] > max(stats["wisdom"], stats["luck"]))

    def amy_v12_friends_ready():
        stats = store.amy_ch2_stats
        return (amy_v12_has_all_cards()
                and stats["love"] < stats["wisdom"]
                and stats["wisdom"] >= amy_v12_friends_wisdom_min)

    def amy_v12_lottery_ready():
        stats = store.amy_ch2_stats
        return (not renpy.amy_session_lottery_seen
                and amy_v12_has_all_cards()
                and stats["luck"] >= max(stats["love"], stats["wisdom"]))

    def amy_v12_feedback():
        stats = store.amy_ch2_stats
        if stats["wisdom"] >= 70 and stats["luck"] >= 70:
            return "相处印记：认真理解彼此，也愿意一起探索未知。"
        if stats["wisdom"] >= 70:
            return "相处印记：尊重彼此的判断，一起寻找解决问题的方法。"
        if stats["luck"] >= 70:
            return "相处印记：愿意给未知留出位置，享受共同探索的可能。"
        if stats["love"] > 90:
            return "相处印记：一次次主动靠近，已经积累了深厚的默契。"
        return "相处印记：故事已经发生，彼此仍有值得探索的可能。"

    config.after_load_callbacks.append(amy_v12_recalculate)
