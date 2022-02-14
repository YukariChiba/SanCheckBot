from utils.DiceUtils import DiceSum


def EDUAdd(c):
    if DiceSum("1d100") > c.EDU:
        c.EDU = c.EDU + DiceSum("1d10")
    if c.EDU > 99:
        c.EDU = 99
    return c


def AGEEffect(c, v):
    pSTR = DiceSum("1d100")
    pDEX = DiceSum("1d" + str(100 - pSTR))
    pCON = (100 - pSTR - pDEX)
    pSTR = pSTR / 100
    pDEX = pDEX / 100
    pCON = pCON / 100
    c.STR = round(c.STR - v * pSTR)
    c.DEX = round(c.DEX - v * pSTR)
    c.CON = round(c.CON - v * pSTR)
    return c


def CharInit(c, age=None):
    if age:
        c.AGE = age
    else:
        c.AGE = DiceSum("1d72") + 14
    c.STR = DiceSum("3d6") * 5
    c.CON = DiceSum("3d6") * 5
    c.DEX = DiceSum("3d6") * 5
    c.APP = DiceSum("3d6") * 5
    c.POW = DiceSum("3d6") * 5
    c.SIZ = (DiceSum("2d6") + 6) * 5
    c.INT = (DiceSum("2d6") + 6) * 5
    c.EDU = (DiceSum("2d6") + 6) * 5
    c.LUK = DiceSum("3d6") * 5

    if c.AGE < 19:
        if DiceSum("1d2") == 2:
            c.STR = c.STR - 1
        else:
            c.SIZ = c.SIZ - 1
        c.EDU = c.EDU - 5
        c.LUK = max(c.LUK, DiceSum("3d6") * 5)
    elif c.AGE < 39:
        c = EDUAdd(c)
    elif c.AGE < 49:
        c = EDUAdd(EDUAdd(c))
        c.APP = c.APP - 5
        c = AGEEffect(c, 5)
    elif c.AGE < 59:
        c = EDUAdd(EDUAdd(EDUAdd(c)))
        c.APP = c.APP - 10
        c = AGEEffect(c, 10)
    elif c.AGE < 69:
        c = EDUAdd(EDUAdd(EDUAdd(EDUAdd(c))))
        c.APP = c.APP - 15
        c = AGEEffect(c, 20)
    elif c.AGE < 79:
        c = EDUAdd(EDUAdd(EDUAdd(EDUAdd(c))))
        c.APP = c.APP - 20
        c = AGEEffect(c, 40)
    elif c.AGE < 89:
        c = EDUAdd(EDUAdd(EDUAdd(EDUAdd(c))))
        c.APP = c.APP - 25
        c = AGEEffect(c, 80)
    c.SAN = c.POW
    c.HP = (c.SIZ + c.CON) // 10
    c.MP = c.POW // 5
    if c.DEX < c.SIZ and c.STR < c.SIZ:
        c.MOV = 7
    elif c.DEX > c.SIZ and c.STR > c.SIZ:
        c.MOV = 9
    else:
        c.MOV = 8
    c.MOV = c.MOV - (c.AGE - 40) // 10
    if c.STR + c.SIZ < 64:
        c.DB = -2
        c.BUILD = -2
    elif c.STR + c.SIZ < 84:
        c.DB = -1
        c.BUILD = -1
    elif c.STR + c.SIZ < 124:
        c.DB = 0
        c.BUILD = 0
    elif c.STR + c.SIZ < 164:
        c.DB = DiceSum("1d4")
        c.BUILD = 1
    elif c.STR + c.SIZ < 204:
        c.DB = DiceSum("1d6")
        c.BUILD = 2
    for a in c.attributes:
        setattr(c, "init" + a, getattr(c, a))
    return c
