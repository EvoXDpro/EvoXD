from . import *


def main():
    import os
    import sys
    import time

    from .fns.helper import bash, time_formatter, updater
    from .startup.funcs import (
        WasItRestart,
        autopilot,
        customize,
        fetch_ann,
        plug,
        ready,
        startup_stuff,
    )
    from .startup.loader import load_other_plugins

    try:
        from apscheduler.schedulers.asyncio import AsyncIOScheduler
    except ImportError:
        AsyncIOScheduler = None

    # Option to Auto Update On Restarts..
    if (
        udB.get_key("UPDATE_ON_RESTART")
        and os.path.exists(".git")
        and EvoXD_bot.run_in_loop(updater())
    ):
        EvoXD_bot.run_in_loop(bash("bash installer.sh"))

        os.execl(sys.executable, sys.executable, "-m", "pyEvoXD")

    EvoXD_bot.run_in_loop(startup_stuff())

    EvoXD_bot.me.phone = None

    if not EvoXD_bot.me.bot:
        udB.set_key("OWNER_ID", EvoXD_bot.uid)

    LOGS.info("Initialising...")

    EvoXD_bot.run_in_loop(autopilot())

    pmbot = udB.get_key("PMBOT")
    manager = udB.get_key("MANAGER")
    addons = udB.get_key("ADDONS") or Var.ADDONS
    vcbot = udB.get_key("VCBOT") or Var.VCBOT
    if HOSTED_ON == "okteto":
        vcbot = False

    if (HOSTED_ON == "termux" or udB.get_key("LITE_DEPLOY")) and udB.get_key(
        "EXCLUDE_OFFICIAL"
    ) is None:
        _plugins = "autocorrect autopic audiotools compressor forcesubscribe fedutils gdrive glitch instagram nsfwfilter nightmode pdftools profanityfilter writer youtube"
        udB.set_key("EXCLUDE_OFFICIAL", _plugins)

    load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

    suc_msg = """
            ----------------------------------------------------------------------------
                💫 𝗘𝗩𝗢 𝗫𝗗 ❤️🥀 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝗱𝗲𝗽𝗹𝗼𝘆𝗲𝗱!✨ 𝗩𝗶𝘀𝗶𝘁 @EvoXpro 𝗳𝗼𝗿 𝘂𝗽𝗱𝗮𝘁𝗲𝘀!🥀!
            ----------------------------------------------------------------------------
    """

    # for channel plugins
    plugin_channels = udB.get_key("PLUGIN_CHANNEL")

    # Customize EvoXD Assistant...
    EvoXD_bot.run_in_loop(customize())

    # Load Addons from Plugin Channels.
    if plugin_channels:
        EvoXD_bot.run_in_loop(plug(plugin_channels))

    # Send/Ignore Deploy Message..
    if not udB.get_key("LOG_OFF"):
        EvoXD_bot.run_in_loop(ready())
    if AsyncIOScheduler:
        scheduler = AsyncIOScheduler()
        scheduler.add_job(fetch_ann, "interval", minutes=12 * 60)
        scheduler.start()

    # Edit Restarting Message (if It's restarting)
    EvoXD_bot.run_in_loop(WasItRestart(udB))

    try:
        cleanup_cache()
    except BaseException:
        pass

    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start *EVOXD*"
    )
    LOGS.info(suc_msg)


if __name__ == "__main__":
    main()

    asst.run()
