# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#
# Userbot module for having some fun.

import asyncio, re, time
from cowpy import cow
from random import randint, choice, getrandbits
from userbot import CMD_HELP, ZALG_LIST, CMDPREFIX
from userbot.events import register, errors_handler


#
# ================= CONSTANT =================
#


METOOSTR = [
    "Me too thanks","Haha yes, me too","Same lol","Me irl",
    "Haha same","Same here","Haha yes","Yeah, same bro","Me rn",
    "I, too, exhibit this","I share this experience",
    "Indeed my good chum","Same, haha","Me three",
    "The condition you're exclaiming is one that I, too, experience as a human.",
    "Dude, like, same","Same","I feel ya","O\nM\nG\n\nSame",
    """What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.\n\n I mean.. uh.. me too."""
]

EMOJIS = [
    "😂","😂","👌","✌","💞","👍","👌","💯","🎶",
    "👀","😂","👓","👏","👐","🍕","💥","🍴","💦","💦",
    "🍑","🍆","😩","😏","👉👌","👀","👅","😩","🚰"
]

UWUS = [
    '(・`ω´・)',';;w;;','owo','UwU','>w<','^w^',r'\(^o\) (/o^)/',
    '( ^ _ ^)∠☆','(ô_ô)','~:o',';____;','(*^*)','(>_','(♥_♥)',
    '*(^O^)*','((+_+))','(づ｡◕‿‿◕｡)づ','(◕‿◕✿)','(｡◕‿‿◕｡)',
    '(｡◕‿◕｡)','(─‿‿─)','(´• ω •`)','(^◕ᴥ◕^)','(^◔ᴥ◔^)',
    '(^˵◕ω◕˵^)','( =ω=)..nyaa','( ; ω ; )'
]

FACEREACTS = [
    "ʘ‿ʘ","ヾ(-_- )ゞ","(っ˘ڡ˘ς)","(´ж｀ς)","( ಠ ʖ̯ ಠ)","(° ͜ʖ͡°)╭∩╮",
    "(ᵟຶ︵ ᵟຶ)","(งツ)ว","ʚ(•｀","(っ▀¯▀)つ","(◠﹏◠)","( ͡ಠ ʖ̯ ͡ಠ)",
    "( ఠ ͟ʖ ఠ)","(∩｀-´)⊃━☆ﾟ.*･｡ﾟ","(⊃｡•́‿•̀｡)⊃","(._.)","{•̃_•̃}",
    "(ᵔᴥᵔ)","♨_♨","⥀.⥀","ح˚௰˚づ ","(҂◡_◡)","ƪ(ړײ)‎ƪ​​","(っ•́｡•́)♪♬",
    "◖ᵔᴥᵔ◗ ♪ ♫ ","(☞ﾟヮﾟ)☞","[¬º-°]¬","(Ծ‸ Ծ)","(•̀ᴗ•́)و ̑̑","ヾ(´〇`)ﾉ♪♪♪",
    "(ง'̀-'́)ง","ლ(•́•́ლ)","ʕ •́؈•̀ ₎","♪♪ ヽ(ˇ∀ˇ )ゞ","щ（ﾟДﾟщ）","( ˇ෴ˇ )",
    "눈_눈","(๑•́ ₃ •̀๑) ","( ˘ ³˘)♥ ","ԅ(≖‿≖ԅ)","♥‿♥","◔_◔",
    "⁽⁽ଘ( ˊᵕˋ )ଓ⁾⁾","乁( ◔ ౪◔)「      ┑(￣Д ￣)┍","( ఠൠఠ )ﾉ","٩(๏_๏)۶",
    "┌(ㆆ㉨ㆆ)ʃ","ఠ_ఠ","(づ｡◕‿‿◕｡)づ","(ノಠ ∩ಠ)ノ彡( \\o°o)\\",
    "“ヽ(´▽｀)ノ”","༼ ༎ຶ ෴ ༎ຶ༽","｡ﾟ( ﾟஇ‸இﾟ)ﾟ｡","(づ￣ ³￣)づ","(⊙.☉)7",
    "ᕕ( ᐛ )ᕗ","t(-_-t)","(ಥ⌣ಥ)","ヽ༼ ಠ益ಠ ༽ﾉ","༼∵༽ ༼⍨༽ ༼⍢༽ ༼⍤༽",
    "ミ●﹏☉ミ","(⊙_◎)","¿ⓧ_ⓧﮌ","ಠ_ಠ","(´･_･`)","ᕦ(ò_óˇ)ᕤ","⊙﹏⊙",
    "(╯°□°）╯︵ ┻━┻",r"¯\_(⊙︿⊙)_/¯","٩◔̯◔۶","°‿‿°","ᕙ(⇀‸↼‶)ᕗ",
    "⊂(◉‿◉)つ","V•ᴥ•V","q(❂‿❂)p","ಥ_ಥ","ฅ^•ﻌ•^ฅ","ಥ﹏ಥ",
    "（ ^_^）o自自o（^_^ ）","ಠ‿ಠ","ヽ(´▽`)/","ᵒᴥᵒ#","( ͡° ͜ʖ ͡°)",
    "┬─┬﻿ ノ( ゜-゜ノ)","ヽ(´ー｀)ノ","☜(⌒▽⌒)☞","ε=ε=ε=┌(;*´Д`)ﾉ",
    "(╬ ಠ益ಠ)","┬─┬⃰͡ (ᵔᵕᵔ͜ )","┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",r"¯\_(ツ)_/¯",
    "ʕᵔᴥᵔʔ","(`･ω･´)","ʕ•ᴥ•ʔ","ლ(｀ー´ლ)","ʕʘ̅͜ʘ̅ʔ","（　ﾟДﾟ）",
    r"¯\(°_o)/¯","(｡◕‿◕｡)",
]

RUNSREACTS = [
    "Runs to Thanos",
    "Runs far, far away from earth",
    "Running faster than usian bolt coz I'mma Bot",
    "Runs to Marie",
    "This Group is too cancerous to deal with.",
    "Cya bois",
    "Kys",
    "I am a mad person. Plox Ban me.",
    "I go away",
    "I am just walking off, coz me is too fat.",
    "I Fugged off!",
]


#
# ===========================================
#


@register(outgoing=True, pattern=f"^{CMDPREFIX}(\w+)say (.*)")
@errors_handler
async def univsaye(cowmsg): # For .cowsay module, userbot wrapper for cow which says things.
    arg = cowmsg.pattern_match.group(1).lower()
    text = cowmsg.pattern_match.group(2)

    if arg == "cow":
        arg = "default"
    if arg not in cow.COWACTERS:
        return
    cheese = cow.get_cow(arg)
    cheese = cheese()

    await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^:/$")
@errors_handler
async def kek(keks): # Check yourself ;)
    uio = ["/", "\\"]
    for i in range(1, 15):
        time.sleep(0.3)
        await keks.edit(":" + uio[i % 2])


@register(outgoing=True, pattern="^-_-$")
@errors_handler
async def lol(lel): # Ok...
    okay = "-_-"
    for _ in range(10):
        okay = okay[:-1] + "_-"
        await lel.edit(okay)


@register(outgoing=True, pattern=f"^{CMDPREFIX}cp(?: |$)(.*)")
@errors_handler
async def copypasta(cp_e): # Copypasta the famous meme
    textx = await cp_e.get_reply_message()
    message = cp_e.pattern_match.group(1)

    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await cp_e.edit("`😂🅱️IvE👐sOME👅text👅 for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
        return

    reply_text = choice(EMOJIS)
    # choose a random character in the message to be substituted with 🅱️
    b_char = choice(message).lower()
    for owo in message:
        if owo == " ":
            reply_text += choice(EMOJIS)
        elif owo in EMOJIS:
            reply_text += owo
            reply_text += choice(EMOJIS)
        elif owo.lower() == b_char:
            reply_text += "🅱️"
        else:
            if bool(getrandbits(1)):
                reply_text += owo.upper()
            else:
                reply_text += owo.lower()
    reply_text += choice(EMOJIS)
    await cp_e.edit(reply_text)


@register(outgoing=True, pattern=f"^{CMDPREFIX}vapor(?: |$)(.*)")
@errors_handler
async def vapor(vpr): # Vaporize everything!
    reply_text = list()
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await vpr.edit("".join(reply_text))


@register(outgoing=True, pattern=f"^{CMDPREFIX}str(?: |$)(.*)")
@errors_handler
async def stretch(stret): # Stretch it.
    textx = await stret.get_reply_message()
    message = stret.text
    message = stret.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
        return

    reply_text = re.sub(r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
                        (r"\1" * randint(3, 10)), message)
    await stret.edit(reply_text)


@register(outgoing=True, pattern=f"^{CMDPREFIX}zal(?: |$)(.*)")
@errors_handler
async def zal(zgfy): # Invoke the feeling of chaos.
    reply_text = list()
    textx = await zgfy.get_reply_message()
    message = zgfy.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await zgfy.edit(
            "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
        )
        return

    for charac in message:
        if not charac.isalpha():
            reply_text.append(charac)
            continue

        for _ in range(0, 3):
            charac = charac.strip() + \
                choice(ZALG_LIST[randint(0,2)]).strip()

        reply_text.append(charac)

    await zgfy.edit("".join(reply_text))


@register(outgoing=True, pattern="^hi$")
@errors_handler
async def hoi(hello): # Greet everyone!
    await hello.edit("Hoi!😄")


@register(outgoing=True, pattern=f"^{CMDPREFIX}owo(?: |$)(.*)")
@errors_handler
async def faces(owo): # UwU
    textx = await owo.get_reply_message()
    message = owo.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await owo.edit("` UwU no text given! `")
        return

    reply_text = re.sub(r"(r|l)", "w", message)
    reply_text = re.sub(r"(R|L)", "W", reply_text)
    reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
    reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
    reply_text = re.sub(r"\!+", " " + choice(UWUS), reply_text)
    reply_text = reply_text.replace("ove", "uv")
    reply_text += " " + choice(UWUS)
    await owo.edit(reply_text)


@register(outgoing=True, pattern=f"^{CMDPREFIX}react$")
@errors_handler
async def react_meme(react): # Make your userbot react to everything.
    await react.edit(choice(FACEREACTS))


@register(outgoing=True, pattern=f"^{CMDPREFIX}shg$")
@errors_handler
async def shrugger(shg): # ¯\_(ツ)_/¯
    await shg.edit(r"¯\_(ツ)_/¯")


@register(outgoing=True, pattern=f"^{CMDPREFIX}runs$")
@errors_handler
async def runner_lol(run): # Run, run, RUNNN!
    index = randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[index]
    await run.edit(reply_text)


@register(outgoing=True, pattern=f"^{CMDPREFIX}metoo$")
@errors_handler
async def metoo(hahayes): # Haha yes
    await hahayes.edit(choice(METOOSTR))


@register(outgoing=True, pattern=f"^{CMDPREFIX}mock(?: |$)(.*)")
@errors_handler
async def spongemocktext(mock): # Do it and find the real fun.
    reply_text = list()
    textx = await mock.get_reply_message()
    message = mock.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
        return

    for charac in message:
        if charac.isalpha() and randint(0, 1):
            to_app = charac.upper() if charac.islower() else charac.lower()
            reply_text.append(to_app)
        else:
            reply_text.append(charac)

    await mock.edit("".join(reply_text))


@register(outgoing=True, pattern=f"^{CMDPREFIX}clap(?: |$)(.*)")
@errors_handler
async def claptext(memereview): # Praise people!
    textx = await memereview.get_reply_message()
    message = memereview.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await memereview.edit("`Hah, I don't clap pointlessly!`")
        return
    reply_text = "👏 "
    reply_text += message.replace(" ", " 👏 ")
    reply_text += " 👏"
    await memereview.edit(reply_text)


@register(outgoing=True, pattern=f"^{CMDPREFIX}bt$")
@errors_handler
async def bluetext(bt_e): # Believe me, you will find this useful.
    if await bt_e.get_reply_message():
        await bt_e.edit(
            "`BLUETEXT MUST CLICK.`\n"
            "`Are you a stupid animal which is attracted to colours?`")


@register(pattern=f'{CMDPREFIX}type(?: |$)(.*)')
@errors_handler
async def typewriter(typew): # Just a small command to make your keyboard become a typewriter!
    textx = await typew.get_reply_message()
    message = typew.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await typew.edit("`Give a text to type!`")
        return
    sleep_time = 0.03
    typing_symbol = "|"
    old_text = ''
    await typew.edit(typing_symbol)
    await asyncio.sleep(sleep_time)
    for character in message:
        old_text = old_text + "" + character
        typing_text = old_text + "" + typing_symbol
        await typew.edit(typing_text)
        await asyncio.sleep(sleep_time)
        await typew.edit(old_text)
        await asyncio.sleep(sleep_time)


CMD_HELP.update({"memes": "Ask 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for that."})
