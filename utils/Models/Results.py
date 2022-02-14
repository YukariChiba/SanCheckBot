from enum import IntEnum


class DiceResult(IntEnum):
    SUCCESS = 1
    SUCCESS_HARD = 2
    SUCCESS_EXTREME = 3
    SUCCESS_ALL = 4
    FAILURE = -1
    FAILURE_ALL = -2
