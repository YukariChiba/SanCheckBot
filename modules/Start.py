from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, ChatAction, InlineKeyboardButton, InlineKeyboardMarkup
import utils.CharManager as CharManager
from utils.Models.MsgTpl import CharInfo
import os

enabled = True


def load():
    print("Start Plugin Loaded!")


def run(update: Update, context: CallbackContext) -> None:
    if update.message.chat.type == 'private':
        uid = str(update.message.from_user.id)
        if CharManager.CharExists(uid):
            update.message.reply_text(
                "您好，欢迎回来。", parse_mode='Markdown')
        else:
            update.message.reply_text(
                "您好，请使用 /create [可选年龄] 创建您的角色。", parse_mode='Markdown')


handlers = [CommandHandler("start", run, run_async=True)]
