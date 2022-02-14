from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
import utils.CharManager as CharManager
from utils.Models.MsgTpl import CharInfo
import os

enabled = True


def load():
    print("Create Plugin Loaded!")


def CheckArg(a):
    if len(a) != 0 and len(a) != 1:
        return False
    if len(a) == 1:
        if not a[0].isdigit():
            return False
        if int(a[0]) > 85 or int(a[0]) < 15:
            return False
    return True


def run(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == 'private':
        if CheckArg(context.args):
            uid = str(update.message.from_user.id)
            if CharManager.CharExists(uid):
                update.message.reply_text(
                    "您好，欢迎回来。", parse_mode='Markdown')
            else:
                a = int(context.args[0]) if len(context.args) == 1 else None
                c = CharManager.InitSaveChar(uid, age=a)
                initInfo = CharInfo(c)
                update.message.reply_text(
                    "您好，您的角色已创建成功，以下是基本信息：\n" + initInfo, parse_mode='Markdown')
        else:
            update.message.reply_text(
                "*创建您的角色.*\nUsage: `/create [AGE]`.", parse_mode='Markdown')


handlers = [CommandHandler("create", run, run_async=True)]
