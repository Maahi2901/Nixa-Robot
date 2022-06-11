import os
import aiofiles
import aiohttp
from random import randint
from pyrogram import filters
from NixaRobot import pbot as Nixa

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

async def ai_nixa(url):
    ai_name = "nixa.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@Nixa.on_message(filters.command("Nixa"))
async def Lycia(_, message):
    if len(message.command) < 2:
        await message.reply_text("Nixa AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    Nixa = text.replace(" ", "%20")
    m = await message.reply_text("Nixa Is Best...")
    try:
        L = await fetch(f"https://api.affiliateplus.xyz/api/chatbot?message={lycia}&botname=amelia&ownername=Abhishek&user=1")
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "nixa"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @Simple_Mundaa...")
    NixaVoice = await ai_Nixa(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=NixaVoice, title=chatbot, performer=name)
    os.remove(NixaVoice)
    await m.delete()
