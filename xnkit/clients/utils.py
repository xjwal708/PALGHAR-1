import logging
import platform
import time

from pyrogram import __version__ as pyro_version
from telegraph import Telegraph

from xnkit.database import Database
from xnkit.helpers import Helpers
from xnkit.pyrogramx.methods import Methods
from config import Config


class Utils(Methods, Config, Database, Helpers):
    # versions /

    userbot_version = "v1"
    assistant_version = "v1"
    python_version = str(platform.python_version())
    pyrogram_version = str(pyro_version)

    # containers /

    CMD_HELP = {}

    # owner details /

    owner_name = "xɴᴋɪᴛ 🇮🇳 [ᴏꜰꜰʟɪɴᴇ]"
    owner_id = 2127221861
    owner_username = "@XnKiTKuMaR"

    # other /

    Repo = "https://github.com/XnKiT/XnKiT-UB.git"
    StartTime = time.time()

    # debugging /

    logging.getLogger("pyrogram.syncer").setLevel(
        logging.CRITICAL
    )  # turn off pyrogram logging
    logging.getLogger("pyrogram").setLevel(logging.CRITICAL)

    logging.basicConfig(format="%(asctime)s %(message)s")
    log = logging.getLogger("———")

    # telegraph /

    telegraph = Telegraph()
    telegraph.create_account(
        short_name=Config.TL_NAME if Config.TL_NAME else "XnKiT"
    )
