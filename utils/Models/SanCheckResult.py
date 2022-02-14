from utils.DiceUtils import JudgeDiceSum, DiceSum
from utils.Models.Effects import Effects


class SanCheckResult:
    def __init__(self, c, sVal, fVal):
        self.sanJudgeDiceResult = JudgeDiceSum(sVal, fVal, "1d100", c.SAN)
        self.intDiceResult = None
        self.intDiceSuccess = True

        self.effects = Effects()
        self.effects.attrs["SAN"] = -self.sanJudgeDiceResult["effect"]
        if self.sanJudgeDiceResult["effect"] > 5:
            self.intDiceResult = DiceSum("1d100")
            if self.intDiceResult >= c.INT:
                self.intDiceSuccess = False
                self.effects.periods["crazy"] = DiceSum("1d10")
        if self.sanJudgeDiceResult["effect"] > c.initSAN / 5:
            self.effects.periods["randomcrazy"] = 24
