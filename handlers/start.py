import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━───⊶⛧•[EᖇᖇOᖇ](https://t.me/RDPDDP)•⛧⊷───━**\n

🎻¦**انا بوت تشغيل وتنزيل الاغاني والفديو**\n

 👮🏼‍♂️¦**اضفني مشرف في مجموعتك لأعمل**\n

 🌐¦**اتبع مايلي لمعرفه كيفيه الاستخدام**\n

 ❓¦**اضغط علي ذر طريقه الاستخدام**\n

 ◍**مميزات الروبوت يعمل بجودة فائقه**\n

**━───⊶⛧•[EᖇᖇOᖇ](https://t.me/RDPDDP)•⛧⊷───━**\n""",
    reply_markup=InlineKeyboardMarkup(
             [
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ],
            [
            InlineKeyboardButton( "🔎 كيف تستخدمني؟ قائمة الأوامر.",url=f"https://t.me/RDPDDP/228"),
            ],
            [
            InlineKeyboardButton("DEV", url=f"https://t.me/MC_0p"),
              ],
              [
                  InlineKeyboardButton(
                         " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                ),
            ],
            [
                InlineKeyboardButton("EᖇᖇOᖇ", url=f"https://t.me/RDPDDP"),
            ]
         ]
     )
  )

@Client.on_message(
    command(["مبرمج السورس","ايرور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7905bfc32ffadc86bd7f2.jpg",
        caption=f"""المبرمج ايرور مبرمج جميع السورس لو حاابب تتواصل معاه بالاسفل ⬇️ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "DEV", url=f"https://t.me/K_1_1_0"),
                ],
                [
                    InlineKeyboardButton(
                    "EᖇᖇOᖇ", url=f"https://t.me/RDPDDP"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["مطور السورس" ,"مصطفي","المطور","المبرمجه لوكا"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0b633e936adc7c1d723db.jpg",
        caption=f""" المطور جميع السورس لو حاابب تتواصل معاه بالاسفل ⬇️ """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("المطور", url=f"https://t.me/K_1_1_0"),
           ],
            [ 
                InlineKeyboardButton(
                    "EᖇᖇOᖇ", url=f"https://t.me/RDPDDP"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["سورس","ياسورس","السورس","source","يا سورس"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/c97c98e67a90bbba24a66.mp4",
        caption=f"""[━═━═━ٰ˚₊·ERROR.↺═━═━•](https://t.me/RDPDDP)
 [✨╎𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚂𝙾𝚄𝚁𝙲𝙴 ERROR](https://t.me/RDPDDP)

 [⚙╎𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝙴𝙶𝚈𝙿𝚃](https://t.me/RDPDDP)
 
 [⚡╎𝚁𝚄𝙽 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚆𝙸𝚃𝙷 𝚄𝚂 𝙽𝙾𝚆](https://t.me/RDPDDP)
[━═━═━ٰ˚₊·ERROR.↺═━═━•](https://t.me/RDPDDP)
──┈┈┈┄┄╌╌╌╌┄┄┈┈┈
[◍ 𝐶𝐻"✈َٰ𝚂𝙾𝚄𝚁𝙲𝙴 ERROR.↺ ◍](https://t.me/RDPDDP)
[━═━═━═━ٰ═━═━═━•](https://t.me/RDPDDP)""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("لطلب بوت", url=f"https://t.me/K_1_1_0"),
            ],
            [
            InlineKeyboardButton("المطور", url=f"https://t.me/K_1_1_0"),
            ],
            [
                InlineKeyboardButton(
                        "EᖇᖇOᖇ", url=f"https://t.me/RDPDDP"
                ),
            ],
            [
                InlineKeyboardButton("أضف لبوت لمجموعتك ✅", url=f"https://t.me/{bu}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                " **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                " **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            ],
                            [
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "أضف لبوت لمجموعتك ✅", url=f'https://t.me/{bu}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
