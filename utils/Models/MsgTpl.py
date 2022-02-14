from utils.Models.Results import DiceResult

ATTRLIST = {
    "AGE": "年龄",
    "STR": "力量",
    "CON": "体质",
    "DEX": "敏捷",
    "APP": "外貌",
    "POW": "意志",
    "SIZ": "体型",
    "INT": "智力",
    "EDU": "教育",
    "LUK": "幸运",
    "SAN": "理智",
    "HP": "生命",
    "MP": "法力",
    "MOV": "移动力",
    "DB": "伤害加成",
    "BUILD": "体格",
}

SKILLLIST = {
    "accounting": 10,
    "anthropology": 1,
    "archaeology": 1,
    "art": 5,
    "astronomy": 1,
    "bargain": 5,
    "biology": 1,
    "chemistry": 1,
    "climb": 40,
    "conceal": 15,
    "craft": 5,
    "credit_rating": 15,
    "cthulhu_mythos": 0,
    "disguise": 1,
    "dodge": 0,
    "drive_auto": 20,
    "electric_repair": 10,
    "fast_talk": 5,
    "first_aid": 30,
    "geology": 1,
    "hide": 10,
    "history": 20,
    "jump": 25,
    "law": 5,
    "library Use": 25,
    "listen": 25,
    "locksmith": 1,
    "martial_arts": 1,
    "mechanical_repair": 20,
    "medicine": 5,
    "natural_history": 10,
    "navigate": 10,
    "occult": 5,
    "operate_heavy_machinery": 1,
    "other_language": 1,
    "own_language": 0,
    "persuade": 15,
    "pharmacy": 1,
    "photography": 10,
    "physics": 1,
    "pilot": 1,
    "psychoanalysis": 1,
    "psychology": 5,
    "ride": 5,
    "sneak": 10,
    "spot_hidden": 25,
    "wwim": 25,
    "throw": 25,
    "track": 10
}


def CharInfo(c):
    ret = ""
    for attr in ATTRLIST.keys():
        ret = ret + "你的 *{}* 值为: {}\n".format(ATTRLIST[attr], getattr(c, attr))
    return ret


def ResultInfo(r):
    if r == DiceResult.SUCCESS_ALL:
        return "大成功"
    if r == DiceResult.SUCCESS_EXTREME:
        return "极限成功"
    if r == DiceResult.SUCCESS_HARD:
        return "困难成功"
    if r == DiceResult.SUCCESS:
        return "成功"
    if r == DiceResult.FAILURE:
        return "失败"
    if r == DiceResult.FAILURE_ALL:
        return "大失败"
    return "未知"
