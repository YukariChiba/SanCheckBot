from telegram.ext import InlineQueryHandler, CallbackContext, ChosenInlineResultHandler
from telegram import Update
import inlines as inline_plugins
from utils.CharManager import ReadChar, SaveChar, RemoveChar, ApplyChange
from utils.Models.Effects import Effects
import os
import json

enabled = True


def load():
    for plugin in inline_plugins.__all__:
        if plugin.enabled:
            plugin.load()
    print("Inline Plugin Loaded!")


def run(update: Update, context: CallbackContext) -> None:
    query = update.inline_query
    results = [
    ]
    cache_time = int(os.getenv("MODULE_INLINE_CACHETIME"))
    for plugin in inline_plugins.__all__:
        if plugin.enabled and plugin.filter(query.query):
            returnMessage = plugin.run(query, context)
            if returnMessage != None:
                if hasattr(plugin, 'NOCACHE'):
                    cache_time = 0
                results.append(returnMessage)
    update.inline_query.answer(
        results, cache_time=cache_time, is_personal=True)


def choose(update: Update, context: CallbackContext):
    msgid = update.chosen_inline_result.result_id
    uid = update.chosen_inline_result.from_user.id
    if os.path.isfile(os.getenv("CACHE_DIR") + msgid + ".json"):
        with open(os.getenv("CACHE_DIR") + msgid + ".json") as f:
            r = json.load(f)
        c = ReadChar(str(uid))
        ef = Effects().fromJson(r)
        ApplyChange(c, ef)
        SaveChar(c, str(uid))
        if c.SAN == 0:
            RemoveChar(str(uid))
            context.bot.send_message(
                chat_id=uid,
                text="您的 SAN 值已经归零，人物已经被删除，请使用 /create 重新创建一个。"
            )


handlers = [InlineQueryHandler(
    run, run_async=True), ChosenInlineResultHandler(choose, run_async=True)]
