from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, ChatAction, InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram.utils.helpers import escape_markdown
import dice
from uuid import uuid4
from utils.CharManager import ReadChar
from utils.Models.MsgTpl import ResultInfo
from utils.TelegramUtils import getFullName
from utils.Models.Results import DiceResult
from utils.Models.SanCheckResult import SanCheckResult
import os
import json

enabled = True

NOCACHE = True

MSG = \
    "{user} 看到了这条消息，进行了一次 {success}/{failure} 的 San Check。\n" \
    "结果为 {result}({tresult})。\n" \
    "SAN 值： {origin} - {effect} = {after}。"


def CheckArg(a):
    if len(a) != 2:
        return False
    s = a[0]
    f = a[1]
    try:
        dice.roll(s)
        dice.roll(f)
    except:
        return False
    return True


def load():
    print("SanCheck Inline Plugin Loaded!")


def filter(arg):
    args = arg.split(" ")
    return CheckArg(args)


def run(querybody, context):
    args = querybody.query.split(" ")
    c = ReadChar(str(querybody.from_user.id))
    if not c:
        return None
    r = SanCheckResult(c, args[0], args[1])
    m = MSG.format(**{
        "user":  getFullName(querybody.from_user),
        "success": args[0],
        "failure": args[1],
        "effect": -r.effects.attrs["SAN"],
        "origin": c.SAN,
        "result": r.sanJudgeDiceResult["result"],
        "tresult": ResultInfo(r.sanJudgeDiceResult["result_state"]),
        "after": c.SAN - r.sanJudgeDiceResult["effect"]
    })
    if r.sanJudgeDiceResult["effect"] >= c.SAN:
        m = m + \
            "\n\n{} SAN 值已经归零了！".format(
                getFullName(querybody.from_user))
    else:
        if r.intDiceResult:
            m = m + "\n\n{} 智力判定{}({})。".format(
                getFullName(querybody.from_user),
                "成功" if r.intDiceSuccess else "失败",
                str(r.intDiceResult) + (" < INT " if r.intDiceSuccess else " >= INT ") +
                str(c.INT),
            )
            if not r.intDiceSuccess:
                m = m + \
                    "陷入了 {} 小时的临时疯狂。".format(r.effects.periods["crazy"])
        if "randomcrazy" in r.effects.status:
            m = m + \
                "\n{} 陷入了不定期疯狂状态！".format(
                    getFullName(querybody.from_user))
    msgid = uuid4()
    with open(os.getenv("CACHE_DIR") + str(msgid) + ".json", "w") as f:
        json.dump(r.effects.toJson(), f)
    return InlineQueryResultArticle(
        id=msgid, title="SanCheck: " + querybody.query, input_message_content=InputTextMessageContent(message_text=m, parse_mode='Markdown'), description="进行一次 San Check。")
