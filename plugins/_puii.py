# Puii - UserBot
# Copyright (C) 2021-2022 TeamPuii
#
# This file is a part of < https://github.com/TeamPuii/Puii/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamPuii/Puii/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, EvoXD_cmd

REPOMSG = """
• **EVOXD USERBOT** •\n

• Addons - [Click Here](https://github.com/EvoXDpro/PuiiAddons)
• Support - @EvoXpro
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/EvoXDpro/Puii"),
        Button.url("Addons", "https://github.com/EvoXDpro/Puiiaddons"),
    ],
    [Button.url("Support Group", "t.me/EvoXpro")],
]

ULTSTRING = """🎇 **Thanks for Deploying EvoXD Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@EvoXD_cmd(
    pattern="repo$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@EvoXD_cmd(pattern="pEvoXD$")
async def usePuii(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/a0df3b90c174b5948abfb.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
