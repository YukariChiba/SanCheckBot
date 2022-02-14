import dice
from utils.Models.Results import DiceResult


def DiceSum(d):
    r = dice.roll(d)
    if isinstance(r, int):
        return r
    return sum(list(r))


def DiceSumMax(d):
    return dice.roll_max(d)


def DiceSumMin(d):
    return dice.roll_min(d)


def CheckDiceSum(d, skillvalue, targetcondition=None):
    if targetcondition == DiceResult.SUCCESS_HARD:
        skillvalue = skillvalue / 2
    if targetcondition == DiceResult.SUCCESS_EXTREME:
        skillvalue = skillvalue / 5
    s = sum(list(dice.roll(d)))
    if s == 1:
        return s, DiceResult.SUCCESS_ALL
    if s <= skillvalue / 5:
        return s, DiceResult.SUCCESS_EXTREME
    if s <= skillvalue / 2:
        return s, DiceResult.SUCCESS_HARD
    if s <= skillvalue:
        return s, DiceResult.SUCCESS
    if skillvalue < 50 and s >= 96:
        return s, DiceResult.FAILURE_ALL
    if skillvalue >= 50 and s == 100:
        return s, DiceResult.FAILURE_ALL
    return s, DiceResult.FAILURE


def JudgeDiceSum(success_value, failure_value, d, skillvalue, targetcondition=None):
    r = CheckDiceSum(d, skillvalue, targetcondition=targetcondition)
    if r[1] > 0:
        if r[1] == DiceResult.SUCCESS_ALL:
            return {
                "result": r[0],
                "result_state": r[1],
                "effect": DiceSumMin(success_value)
            }
        return {
            "result": r[0],
            "result_state": r[1],
            "effect": DiceSum(success_value)
        }
    else:
        if r[1] == DiceResult.FAILURE_ALL:
            return {
                "result": r[0],
                "result_state": r[1],
                "effect": DiceSumMax(failure_value)
            }
        return {
            "result": r[0],
            "result_state": r[1],
            "effect": DiceSum(failure_value)
        }
