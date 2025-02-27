# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon import Button, custom

from plugins import ATRA_COL, InlinePlugin
from pyEvoXD import *
from pyEvoXD import _ult_cache
from pyEvoXD._misc import owner_and_sudos
from pyEvoXD._misc._assistant import asst_cmd, callback, in_pattern
from pyEvoXD.fns.helper import *
from pyEvoXD.fns.tools import get_stored_file
from strings import get_languages, get_string

OWNER_NAME = EvoXD_bot.full_name
OWNER_ID = EvoXD_bot.uid

AST_PLUGINS = {}


async def setit(event, name, value):
    try:
        udB.set_key(name, value)
    except BaseException as er:
        LOGS.exception(er)
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    return [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
