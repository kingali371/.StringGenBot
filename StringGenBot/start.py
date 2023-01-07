from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""📟¦اهلا بـك عزيـزي 📬 {msg.from_user.mention},

📟¦اهلا بـك عزيـزي 📬
⚡¦يـمكنك استـخـراج الـتـالـي
♻️¦تيرمـكـس تليثون للحسـابـات🏂
♻️¦تيرمـكـس تليثون للبوتــات🤖
🎧¦بايـروجـرام مـيوزك للحسابات🙋🏼‍♂️
🗽¦بايـروجـرام مـيوزك احدث اصدار🎊
🎧¦بايـروجـرام مـيوزك للبوتات🤖
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني تم انشـاء هـذا البـوت بواسطـة

بواسطـة : [ٌٍꪎ.ًٍᘔٍᥱᎥٍَꪀ](tg://user?id=1355571767) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🌐 ⍆ اضغط لبدا استخراج كود ⍅🌐", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⚙ الــســــوࢪسـ ⚙️", url="https://t.me/pp_g3"),
                    InlineKeyboardButton("ժᥱ᥎ ρ᥆kᥱꪔ᥆ꪀ", user_id=1355571767)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
