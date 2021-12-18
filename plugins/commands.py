

import os
from pyrogram import Client,filters 
from telegraph import upload_file



@Client.on_message(filters.command(["start"]))
async def start(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"Hello {message.from_user.first_name},\n<b>𝙸'𝚖 Telgram.ph 𝙿𝚑𝚘𝚝𝚘 𝚘𝚛 𝚅𝚒𝚎𝚍𝚘 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚛. \n 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 @REX_BOTZ</b> \n 𝙲𝚕𝚒𝚌𝚔 ☞︎︎︎ /help 𝙵𝚘𝚛 𝙼𝚘𝚛𝚎(•̀ᴗ•́)و",
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await client.send_message(
        chat_id=message.chat.id,
        text=f"<b>𝚂𝚎𝚗𝚍 𝚖𝚎 𝚊𝚗𝚢 𝙿𝚑𝚘𝚝𝚘 𝚘𝚛 𝚅𝚒𝚎𝚍𝚘 𝙱𝚎𝚕𝚘𝚠 5𝙼𝙱. \n 𝙸'𝚕𝚕 𝚄𝚙𝚕𝚘𝚊𝚍 𝚝𝚘 Telegra.ph. \n 𝙼𝚊𝚒𝚗𝚝𝚊𝚒𝚗𝚎𝚍 𝙱𝚢 @REX_BOTS_SUPPORT</b>",
        reply_to_message_id=message.message_id
    )
    
@Client.on_message(filters.photo)
async def getimage(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    imgdir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".jpg"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=imgdir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(imgdir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @Rex_Bots_Support")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(imgdir)
    except:
        pass

@Client.on_message(filters.video)
async def getvideo(client, message):
    location = "./FILES"
    if not os.path.isdir(location):
        os.makedirs(location)
    viddir = location + "/" + str(message.chat.id) + "/" + str(message.message_id) +".mp4"
    dwn = await client.send_message(
          text="<b>Downloading...</b>",
          chat_id = message.chat.id,
          reply_to_message_id=message.message_id
          )          
    await client.download_media(
            message=message,
            file_name=viddir
        )
    await dwn.edit_text("<b>Uploading...</b>")
    try:
        response = upload_file(viddir)
    except Exception as error:
        await dwn.edit_text(f"Oops Something Went Wrong\n{error} Contact @Rex_Bots_Support"")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    try:
        os.remove(viddir)
    except:
        pass

