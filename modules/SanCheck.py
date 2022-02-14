from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.utils.helpers import escape_markdown
import dice
from utils.CharManager import ReadChar, SaveChar, RemoveChar, ApplyChange
from utils.TelegramUtils import getFullName
from utils.Models.SanCheckResult import SanCheckResult
from utils.Models.MsgTpl import ResultInfo
import os

enabled = True

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
    print("SanCheck Plugin Loaded!")


def run(update: Update, context: CallbackContext) -> None:
    reply_message = update.message.reply_to_message
    if reply_message and CheckArg(context.args):
        c = ReadChar(str(update.message.from_user.id))
        if not c:
            update.message.reply_text(
                "您还没有创建角色，请私聊发送 `/start` 进行创建。", parse_mode='Markdown')
            return
        r = SanCheckResult(c, context.args[0], context.args[1])
        m = MSG.format(**{
            "user": getFullName(update.message.from_user),
            "success": context.args[0],
            "failure": context.args[1],
            "effect": -r.effects.attrs["SAN"],
            "origin": c.SAN,
            "result": r.sanJudgeDiceResult["result"],
            "tresult": ResultInfo(r.sanJudgeDiceResult["result_state"]),
            "after": c.SAN - r.sanJudgeDiceResult["effect"]
        })
        if r.sanJudgeDiceResult["effect"] >= c.SAN:
            m = m + \
                "\n\n{} SAN 值已经归零了！".format(
                    getFullName(update.message.from_user))
        else:
            if r.intDiceResult:
                m = m + "\n\n{} 智力判定{}({})。".format(
                    getFullName(update.message.from_user),
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
                        getFullName(update.message.from_user))
        update.message.reply_text(m, parse_mode='Markdown')
        c = ApplyChange(c, r.effects)
        SaveChar(c, str(update.message.from_user.id))
        if c.SAN <= 0:
            RemoveChar(str(update.message.from_user.id))
            context.bot.send_message(
                chat_id=update.message.from_user.id,
                text="您的 SAN 值已经归零，人物已经被删除，请使用 /create 重新创建一个。"
            )
    else:
        update.message.reply_text(
            "*对指定消息做一次 San Check.*\nUsage: `/sancheck <success> <fail>`.", parse_mode='Markdown')


handlers = [CommandHandler("sancheck", run, run_async=True)]
