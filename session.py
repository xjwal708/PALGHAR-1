import asyncio
import os

os.system('clear')

import pyrogram
from pyrogram import Client


APP_ID = int(input("enter Telegram APP ID: "))
API_HASH = input("enter Telegram API HASH: ")
with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as app:
        app.send_message(
            "me",
            f"#PYROGRAM_SESSION By ~(c) @XnKiTKuMaR \n\n```{app.export_session_string()}``` **TAP TO COPY**"
        )
        print("Done !, session string has been sent to saved messages!")
