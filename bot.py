from rubpy import Client, handlers, models, methods
from aiohttp import ClientSession, ClientTimeout
from random import choice
from requests import get,post
from translate import Translator
from datetime import datetime
from re import findall, search
from time import sleep
import requests, json, random, os, time, collections, openai
from asyncio import run, sleep
import aiofiles
from googletrans import Translator
from gtts import gTTS
start = "10:54"
end = "10:55"
g = Translator()
my_group = 'g0CX4C50c1f13d1305474e7676936ad3'
my_filters = ('@', 'join', 'rubika.ir')
group_admins = []
silence_list = []
no_gifs = False
PASOKH = False
lockphoto = False
lockvideo = False
lockMusic = False
lockVoice = False
lockFile = False
AUTOLOCK = False
text_pasokhs = (

    ["عشقم😎😘", "زندگیم🥰❤", "نفسم💕😍", "عزیزم💋😊"]

)
my_insults = (
    'کیر',
    'کص',
    'کون',
    'کس ننت',
    'کوس',
    'کوص',
    'ممه',
    'ننت',
    'بی ناموس',
    'بیناموس',
    'بیناموص',
    'بی ناموص',
    'گایید',
    'جنده',
    'جندع',
    'جیندا',
    'پستون',
    'کسکش',
    'ننه کس',
    'اوبی',
    'هرزه',
    'قحبه',
    'عنتر',
    'فاک',
    'کسعمت',
    'کصخل',
    'کسخل',
    'تخمی',
    'سکس',
    'صکص',
    'کسخول',
    'کسشر',
    'کسشعر',
)

def getAds(string: str) -> bool:
    string = string.lower()
    for filter in my_filters:
        if filter in string:
            return True
        else:
            continue
    return False

def getInsults(string: str) -> bool:
    for filter in my_insults:
        if filter in string:
            return True
        else:
            continue
    return False

async def updateAdmins(client: Client) -> None:
    global group_admins
    results = await client(methods.groups.GetGroupAdminMembers(my_group))
    results = results.to_dict().get('in_chat_members')
    for result in results:
        GUID = result.get('member_guid')
        if not GUID in group_admins:
            group_admins.append(GUID)
        else:
            continue

async def main():
    async with ClientSession(timeout=ClientTimeout(5)) as CS:
        async with Client(session='test') as client:
            await updateAdmins(client)
            @client.on(handlers.MessageUpdates(models.is_group()))
            async def updates(update):
                if update.object_guid == my_group:
                    if not update.author_guid in group_admins and 'forwarded_from' in update.to_dict().get('message').keys():
                        await update.delete_messages()
                        result = await client.get_user_info(update.author_guid)
                        first_name = result.user.first_name
                        await client.ban_group_member(update.object_guid,update.author_guid)
                        await update.reply(f"کاربر [{first_name}]({update.author_guid}) شما به علت فوروارد از گروه اخراج میشوید")
                        print('Delete A Forward.')

                    if update.raw_text != None:
                        if not update.author_guid in group_admins and getAds(update.raw_text):
                            await update.delete_messages()
                            result = await client.get_user_info(update.author_guid)
                            first_name = result.user.first_name
                            await client.ban_group_member(update.object_guid,update.author_guid)
                            await update.reply(f"کاربر [{first_name}]({update.author_guid}) شما به علت تبلیغات از گروه اخراج میشوید")
                            print('Delete A Link.')

                        elif getInsults(update.raw_text):
                            await update.delete_messages()
                            print('Delete A Insult.')

                        elif update.author_guid in group_admins and update.raw_text == '/PANEL':
                            await update.reply("""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/KARBORD လ کاربردی

/GAMES လ بازی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/SETTING':
                            await update.reply("""
											💠 | 𝕊𝔼𝕋𝕋𝕀ℕ𝔾: 

/OPEN လ بازکردن گروه

/CLOSE လ قفل گروه

/LOCKGIF လ قفل گیف

/UNLOCKGIF လ بازکردن گیف

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/CONDITION':
                            await update.reply("""
											پلن یک ماهه برای شما فعال است |💠
											
											/BACK လ برگشت به منوی اصلی
											
                                            """)

                        elif update.author_guid in group_admins and update.raw_text == '/BACK':
                            await update.reply("""
											💠 | ᑭᗩᑎᗴᒪ: 

/SETTING လ تنظیمات

/CONDITION လ وضعیت

/STATUS လ آمار

/KARBORD လ کاربردی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/STATUS':
                            await update.reply("𝙥𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩...")
                            await update.reply("""
											لینک هایی که ربات در انها فعال است |💠
											___________________________________
											https://rubika.ir/joing/ECBDABCC0AEEBIQIWWSFNCFASVIDTWKK
											___________________________________
											___________________________________
											https://rubika.ir/joing/EDAEACHA0MOHHMLACCJBGHSFEJYWQQZU
											___________________________________
											___________________________________
											https://rubika.ir/joing/ECEGIDGC0UBSZJEVRCQPKAYNQTUWPYLR
											___________________________________
                                            ___________________________________
											https://rubika.ir/joing/DJFJGEFI0VMXESRRPECXQPEKSNDOZDXM
											___________________________________
											جهت ثبت لینک خود به ایدی (@ID_Coder) پیام بدهید |💠
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/KARBORD':
                            await update.reply("""
											💠 | kαɾճօɾժ: 

/JOK လ ارسال جوک

/ZEKR လ ذکر امروز

/HADIS လ حدیث

/BIO လ ارسال بیوگرافی

/TIME လ تاریخ دقیق

/ARZ လ دریافت نرخ ارز
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/GAME':
                            await update.reply("""
											💠 | 𝓖𝓐𝓜𝓔𝓢: 

/JRAT လ بازی جرعت حقیقت

/BACK လ برگشت به منوی اصلی
 ‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‍‌‍‍‍‌‌‍‍‌‌‍‌‌‍‍‌‌‍‍‌‍‍‌‍‌‍‌‍‍‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍‌‌‍‌‌‍‍‍‌‍‌‍‍‌‌‍‍‌‌‍‌‌‍‌‍‌‌‍‍‍‍‍‌‍‍‌‌‌‌
											""")

                        elif update.author_guid in group_admins and update.raw_text == '/JRAT':
                            await update.reply("""
											۱🔓عاشق شدی؟اسمش❤️
۲🔓رل زدی تاحالا؟اسمش
۳🔓کراش داری؟اسمش
۴🔓چند بار تا الان رابطه جنسی داشتی؟با کی😐💦
۵🔓از کی خوشت میاد؟
۶🔓از کی بدت میاد؟
۷🔓منو دوس داری؟بهم ثابت کن
۸🔓کی دلتو شکونده؟
۹🔓دل کیو شکوندی؟
۱۰🔓وقتی عصبانی هستی چجوری میشی؟
۱۱🔓دوس داری کیو بزنی یا بکشی؟
۱۲🔓دوس داری کیو بوس کنی؟😉💋
۱۳🔓از تو گالریت عکس بده
۱۴🔓از مخاطبینت عکس بده
۱۵🔓از صفحه چت روبیکات عکس بده
۱۶🔓لباس زیرت چه رنگیه؟🙊
۱۷🔓از وسایل آرایشت عکس بده
۱۸🔓از لباسای کمدت عکس بده
۱۹🔓از کفشات عکس بده
۲۰🔓تالا بهت تجاوز شده؟😥
۲۱🔓تاحالا مجبور شدی به زور به کسی بگی دوست دارم؟
۲۲🔓تاحالا یه دخترو بردی خونتون؟
۲۳🔓تاحالا یه پسرو بردی خونتون؟
۲۴🔓با کی ل....ب گرفتی؟😜
۲۵🔓خود ار.ض..ای..ی کردی؟😬💦
۲۶🔓خانوادت یا رفیقت یا عشقت؟
۲۷🔓سلامتی یا علم یا پول؟
۲۸🔓شهوتی شدی تاحالا؟😂
۲۹🔓خونتون کجاس؟
۳۰🔓خاستگار داری؟عکسش یا اسمش
۳۱🔓به کی اعتماد داری؟
۳۲🔓تاحالا با کسی رفتی تو خونه خالی؟
۳۳🔓چاقی یا لاغر؟
۳۴🔓قد بلندی یا کوتاه؟
۳۵🔓رنگ چشمت؟
۳۶🔓رنگ موهات؟
۳۷🔓موهات فرفریه یا صاف و تا کجاته؟
۳۸🔓تاریخ تولدت؟
۳۹🔓تاریخ تولد عشقت؟
۴۰🔓عشقت چجوری باهات رفتار میکنه؟
۴۱🔓با دوس پسرت عشق بازی کردی؟🤤
۴۲🔓پیش عشقت خوابیدی؟
۴۳🔓عشقتو بغل کردی؟
۴۴🔓حاضری ۱۰ سال از عمرتو بدی به عشقت؟
۴۵🔓مامان و بابات چقد دوست دارن؟
۴۶🔓دعوا کردی؟
۴۸🔓چند بار کتک زدی؟
۴۹🔓چند بار کتک خوردی؟
۵۰🔓تاحالا تورو دزدیدن؟
۵۱🔓تاحالا کسی ل..خ....ت تورو دیده؟🤭
۵۲🔓تاحالا ل...خ...ت کسیا دیدی؟
۵۳🔓دست نام....حرم بهت خورده؟
۵۴🔓دلت برا کی تنگ شده؟
۵۵🔓دوس داشتی کجا بودی؟
۵۶🔓به خودکشی فکر کردی؟
۵۷🔓عکستو بده
۵۸🔓ممه هات بزرگ شدن؟🙈
۵۹🔓با دیدن بدن خودت ح...ش....ری میشی؟
۶۰🔓پیش کسی ضایع شدی؟
۶۱🔓از مدرسه فرار کردی؟
۶۲🔓میخوای چند سالگی ازدواج کنی؟
۶۳🔓اگه مامان و بابات اجازه ندن با عشقت ازدواج کنی چیکار میکنی؟
۶۴🔓چند سالگی پ....ری....و..د شدی؟😶
۶۵🔓وقتی پریودی چجوری هستی؟
۶۶🔓رنگ مورد علاقت؟
۶۷🔓غذای مورد علاقت؟
۶۸🔓پولدارین یا فقیر؟
۶۹🔓دوس داری با من بری بیرون؟
۷۰🔓منو بوس میکنی؟☺️😚
۷۱🔓منو میکنی؟😬
۷۲🔓س...ک...س چت داشتی؟
۷۳🔓خوشت میاد از س....ک.....س؟
۷۴🔓خجالتی هستی یا پررو؟
۷۵🔓دوس داری بکنمت؟🤤
۷۶🔓تاحالا کسی برات خورده؟😁
۷۷🔓من ببوسمت خوشحال میشی؟
۷۸🔓خفن ترین کاری که تا الان کردی؟
۷۹🔓آرزوت چیه؟
۸۰🔓سیگار یا قلیون میکشی؟
۸۱🔓منو میبری خونتون؟
۸۲🔓میذاری بیام خونتون؟
۸۳🔓تاحالا شکست عشقی خوردی؟💔
۸۴🔓اگه به زور شوهرت بدن تو چیکار میکنی؟
۸۵🔓اگه به زور زنت بدن تو چیکار میکنی؟
۸۶🔓تاحالا با پسر غریبه خوابیدی؟
۸۷🔓تاحالا با دختر غریبه خوابیدی؟
۸۸🔓با همجنست خوابیدی؟
۸۹🔓مدرسه یا گوشی؟
۹۰🔓سر کار میری؟
۹۱🔓کلن اخلاقت چجوریه؟
۹۲🔓هنوز پرده داری؟😐
۹۳🔓قلقلکی هستی؟
۹۴🔓سکس خشن دوس داری یا ملایم؟
۹۵🔓کصکش ناله های دختر مردمو میخوای ببینی😐⚔
۹۶🔓چند بار سوتی میدی؟
۹۷🔓مواظب کصت باش تا بیام بگیرمت باشه؟🤭👍🏻
۹۸🔓تاحالا مچ عشقتو موقع لب بازی با یه دختر دیگه گرفتی؟
۹۹🔓تاحالا مچ عشقتو موقع لب بازی با یه پسر دیگه گرفتی؟
۱۰۰🔓اگه یه نفر مزاحم ناموست بشه باهاش چجوری رفتار میکنی؟
۱۰۱🔓شمارتو بده
۱۰۲🔓چقد آرایش میکنی؟
۱۰۳🔓پسر بازی رو دوس داری؟
۱۰۴🔓دختر بازی رو دوس داری؟
۱۰۵🔓اگه یه کص مفتی گیرت بیاد بازم پسش میزنی؟😁👍🏻
۱۰۶🔓پشمالو دوس داری؟🤧
۱۰۷🔓دوس داری شوهر آیندت چجوری باشه؟
۱۰۸🔓دوس داری زن آیندت چجوری باشه؟
۱۰۹🔓دوس داری چند تا بچه داشته باشی؟
۱۱۰🔓قشنگ ترین اسم پسر بنظرت؟
۱۱۱🔓قشنگ ترین اسم دختر بنظرت؟
۱۱۲🔓من خوشگلم یا زشت؟
۱۱۳🔓خوشگل ترین پسر گپ کیه؟
۱۱۴🔓خوشگل ترین دختر گپ کیه؟
۱۱۵🔓کی صداش از همه زیباتره؟
۱۱۶🔓خانومت خوشگله یا زشته؟
۱۱۷🔓خوشتیپ هستی یا خوش قیافه؟
۱۱۸🔓تاحالا احساس کردی یکی روت کراش زده باشه؟
۱۱۹🔓اگه یکی رو ناراحت ببینی چیکار میکنی؟
۱۲۰🔓بی رحمی یا دلت زود به رحم میاد؟
۱۲۱🔓تاحالا پیش کسی گوزیدی؟
۱۲۲🔓تاحالا خودتو خیس کردی؟
۱۲۳🔓اگه بیدار شی ببینی یکی خوابیده روت واکنشت چیه؟
۱۲۴🔓اگه روی یه صندلی کیک باشه یکیش کیر باشه،رو کدوم میشینی و کدومو میخوری؟
۱۲۵🔓جنسیتتو دوس داری عوض کنی؟
۱۲۶🔓دوس داری بری سربازی؟
۱۲۷🔓عکس یهوی بده؟
۱۲۸🔓شام دعوتت کنم قبول میکنی؟
۱۲۹🔓اگه همین الان بهت بگم دوست دارم واکنشت چیه؟
											""")
                            await update.reply('سوالات فرستاده شده اند با کلمه (بپرس) ربات از شما سوال میپرسد.')

                        #elif update.author_guid in group_admins and update.raw_text == '/SETTING' or update.raw_text == 'تنظیمات':
                           # await update.reply("""""")

                        #elif update.author_guid in group_admins and update.raw_text == '/SETTING' or update.raw_text == 'تنظیمات':
                            #await update.reply("""""")

                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن گروه':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, ['SendMessages']))
                            await update.reply('گروه با موفقیت باز شد.🔓')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل گروه':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, []))
                            await update.reply('گروه با موفقیت بسته شد.🔐')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل گیف':
                            global no_gifs
                            no_gifs = True
                            await update.reply('گیف قفل شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل عکس':
                            global lockphoto
                            lockphoto = True
                            await update.reply('عکس قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'باز کردن عکس':
                            lockphoto = False
                            await update.reply('قفل گیف رفع شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل بازی':
                            global PASOKH
                            PASOKH = True
                            await update.reply('عکس قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'باز کردن بازی':
                            PASOKH = False
                            await update.reply('قفل گیف رفع شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل فیلم':
                            global lockvideo
                            lockvideo = True
                            await update.reply('فیلم قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن فیلم':
                            lockvideo = False
                            await update.reply('قفل فیلم خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل موزیک':
                            global lockMusic
                            lockMusic = True
                            await update.reply('موزیک قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن موزیک':
                            lockMusic = False
                            await update.reply('قفل موزیک خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل ویس':
                            global lockVoice
                            lockVoice = True
                            await update.reply('ویس قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن ویس':
                            lockVoice = False
                            await update.reply('قفل ویس خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'قفل فایل':
                            global lockFile
                            lockFile = True
                            await update.reply('فایل قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == 'بازکردن فایل':
                            lockFile = False
                            await update.reply('قفل فایل خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == 'حالت خوش امد گویی روشن':
                            global AUTOLOCK
                            AUTOLOCK = True
                            await update.reply("خوش امد گویی فعال شد.")
                        elif update.author_guid in group_admins and update.raw_text == 'خاموش کردن حالت خوش امد گویی':
                            AUTOLOCK = False
                            await update.reply('خوش امد گویی خاموش شد.')

                        ########
                        elif update.author_guid in group_admins and update.raw_text == 'باز کردن گروه':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, ['SendMessages']))
                            await update.reply('گروه با موفقیت باز شد.🔓')

                        elif update.author_guid in group_admins and update.raw_text == '/ClOSE':
                            result = await client(methods.groups.SetGroupDefaultAccess(my_group, []))
                            await update.reply('گروه با موفقیت بسته شد.🔐')

                        elif update.author_guid in group_admins and update.raw_text == '/GIFLOCK':
                            no_gifs = True
                            await update.reply('گیف قفل شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/PHOTOLOCK':
                            lockphoto = True
                            await update.reply('عکس قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENPHOTO':
                            lockphoto = False
                            await update.reply('قفل عکس رفع شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/LOCKGAME':
                            PASOKH = True
                            await update.reply('بازی قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENGAME':
                            PASOKH = False
                            await update.reply('قفل بازی رفع شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/LOCKVIDEO':
                            lockvideo = True
                            await update.reply('فیلم قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENVIDEO':
                            lockvideo = False
                            await update.reply('قفل فیلم خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/LOCKMUSIC':
                            lockMusic = True
                            await update.reply('موزیک قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENMUSIC':
                            lockMusic = False
                            await update.reply('قفل موزیک خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/LOCKVOICE':
                            lockVoice = True
                            await update.reply('ویس قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENVOICE':
                            lockVoice = False
                            await update.reply('قفل ویس خاموش شد.')

                        elif update.author_guid in group_admins and update.raw_text == '/LOCKFILE':
                            lockFile = True
                            await update.reply('فایل قفل شد.')
                        elif update.author_guid in group_admins and update.raw_text == '/OPENFILE':
                            lockFile = False
                            await update.reply('قفل فایل خاموش شد.')

                        elif update.raw_text == 'قیمت ارز':
                            string = ''
                            async with CS.get('https://api.codebazan.ir/arz/?type=arz') as response:
                                response = await response.json()
                                if response.get('Ok'):
                                    results = response.get('Result')
                                    for result in results:
                                        try:
                                            string += ''.join(['● ', result.get('name'), '\n', '• قیمت: ', result.get('price'), ' ریال','\n', '• به روزرسانی: ', result.get('update'), '\n\n'])
                                        except TypeError:
                                            continue
                                    await update.reply(string)

                        elif update.raw_text == 'دانستنی':
                            rando = ["گذاشتن سبیل مصنوعی ای که یاعث خنده شود در کلیساهای آلاباما ممنوع است.","اثر زبان شما مانند اثر انگشتان شما منحصر به فرد است.","بهترین زمان برای بنزین زدن چه زمانیست؟🤔 اصولا قبل از روشن شدن چراغ بنزین باید بنزین بزنید زیرا اگر چراغ بنزین روشن شود رسوبات وارد پمپ بنزین و سپس آسیب فیلتر بنزین و انژکتور میشود","مزه سیب، پیاز و سیب زمینی یکسان میباشد.و تنها بواسطه بوی آنهاست که طعم های متفاوتی می یابند.","98 درصد وزن آب از اكسيژن تشكيل يافته است.","قلب میگو در سرش قرار گرفته است.","خرس های قطبی چپ دست هستند.","10 درصد وزن بدن انسان (بدون آب) را باكتريها تشكيل ميدهند.","آیا میـدانستیـد کـه سس مایونز به دلیل ترکیب خاصی که دارد در کنفرانس های علمی به عنوان سم کبد معرفی میشود","یکی از بهترین مواقع خرید کردن چیست؟🤔 کافیه 👈 با معده پر به خرید بروید زمانی که با معده خالی به خرید میروید 60% خرید هایی میکنید که به آن احتیاج ندارید","فندک قبل از کبریت اختراع شد.","شکسپیر این دو کلمه رو از خود اختراع کرد...ترور و دست انداز.","زنبور های نر بعد از برقراری رابطه میمیرن.","در سال ۲۰۰۸، پلیس بریتانیا به یک کودک ۷ ساله مجوز حمل اسلحه داد.","ختراع پيچ گوشتي پيش از پيچ صورت گرفت.","دوس دارین ماندگاری پنیر رو زیاد کنین و طعم شور شو برطرف کنین...؟؟🧀😋🧀 کاری نداره که... کافیه به جای استفاده از آب پنیر از دوغ برای خیساندن پنیر استفاده کنید...👍😎","تمام قوهاي كشور انگليس جزو دارايي هاي ملكه انگليس ميباشند.","دوران بارداری فیل ها ۲ سال طول میکشد.","مثل اثر انگشت، هرکس اثر زبان منحصر بفرد خودش را دارد.","یک رستوران در ژاپن وجود دارد که گارسون های آن میمون هستند.","هویج در اصل ارغوانی رنگ است و رنگ نارنجی امروزی به خاطر آن است که در قرن 17 میلادی هلندی ها با پیوند زدن هویج های مختلف رنگ نارنجی آن را پرورش دادند.","فقط ۱۵٪ صحرای آفریقا با شن پوشیده شده است.1","وقتی عطسه میکنید قلب شما به اندازه یک میلیونیم ثانیه میایستد.","ظروف پلاستيكي 50 هزار سال طول ميكشد تا در طبيعت شروع به تجزيه شدن كنند.","لئوناردو داوینچی قیچی را اختراع کرده است.","بى‌خوابى سريعتر از بى‌غذايى موجب مرگ آدمى می‌‌شود","چطوری رشد ابرو ها رو زیاد و تارهای ابرو رو ضخیم کنیم؟ رشد سریع ابرو 👈 دوبار روغن زیتون در روز ضخیم کردن تارهای ابرو 👈 استفاده از وازلین 👌😎","در قرن ۱۶ در اروپا اعتقاد بر این بود که خوردن گوجه فرنگی میتواند شما را تبدیل به گرگ کند","روشنايي قرص كامل ماه 9 برابر هلال ماه ميباشد.","وقتی موش ها را قلقلک بدهید میخندند.","استرانسیم از بقایای موجودات دریایی به دست می آید","شيشه در ظاهر جامد به نظر ميرسد ولي در واقع مايعي است که بسيار کند حرکت ميکند.","اکسید کروم در ساخت نوار کاست و فیلم ویدئو استفاده می شود","بدن ما حاوی ۰.۲ میلی گرم طلاست که بیشتر آن در خون ماست.","تمام قوهاي كشور انگليس جزو دارايي هاي ملكه انگليس ميباشند."]
                            renn= choice(rando)
                            await update.reply(renn)

                        elif update.raw_text == 'حدیث':
                            rando = ["اگر مدارا مخلوقی بود که دیده می شد هیچ مخلوقی از مخلوقات خدا از او نیکوتر نبود","خوشا آنکه زیادی دارایی‌اش را انفاق کند و زبانش را از زیاده‌گویی نگه‌دارد","فال بد زدن شرک ‏است ‏و هیچ‏کس ‏ازما نیست‏ مگر این‏که‏ به‏ نحوى ‏دستخوش فال بد زدن مى ‏شود، اما خداوند با توکل به او آن را از بین مى ‏برد","ملاک ارزیابى کارها، پایان آن‌هاست","بالاترین دستاویزهای ایمان این است که کسی را برای خدا دوست داری و کسی را برای خدا دشمن داری","مدارا نمودن مایه ی برکت و درشتی کردن مایه ی شومی است","كدو بخوريد، چرا كه عقل را تيز و (كارآيى) مغز را زياد مى‏كند","هر گاه بنده‏اى هنگام خوابش، بسم اللّه‏ الرحمن الرحیم بگوید، خداوند به فرشتگان مى‏گوید: به تعداد نفس‏هایش تا صبح برایش حسنه بنویسید","بدان که راستگویى، پر برکت است و دروغگویى، شوم","صله رحم و نيكى، حساب (قيامت) را آسان و از گناهان جلوگيرى می‏كند","فال بد زدن شرک ‏است ‏و هیچ‏کس ‏ازما نیست‏ مگر این‏که‏ به‏ نحوى ‏دستخوش فال بد زدن مى ‏شود، اما خداوند با توکل به او آن را از بین مى ‏برد","هر کس بسیار استغفار کند خدا براى او از هر غمى گشایش، از هر تنگنایى رهایى و از جایى که انتظار ندارد روزى مى‏دهد","صله رحم و نيكى، حساب (قيامت) را آسان و از گناهان جلوگيرى می‏كند","فاطمه پاره وجود من است، هر که او را بیازارد مرا آزار داده و هر که او را خوشحال کند مرا خوشحال کرده است","دو چیز را خداوند در این جهان کیفر میدهد : تعدی ، و ناسپاسی پدر و مادر","فال بد زدن شرک ‏است ‏و هیچ‏کس ‏ازما نیست‏ مگر این‏که‏ به‏ نحوى ‏دستخوش فال بد زدن مى ‏شود، اما خداوند با توکل به او آن را از بین مى ‏برد","بدبختترین بدبختان کسی است که فقر دنیا و عذاب آخرت را با هم دارد","آدم بردبار به پيامبرى نزديك است","هر کس چهل روز خود را براى خدا خالص کند چشمه‏ هاى حکمت از قلب وى بر زبانش جارى مى ‏شود","بدبخت‏ترین مردم پادشاهانند و خوشبخت‏ترین مردم کسى است که با مردم بزرگوار معاشرت کند","حضرت علي عليه السلام : با مستمندان همنشين باش تا روحيه شكر در تو بيشترگردد. حضرت علي عليه السلام"]
                            renn= choice(rando)
                            await update.reply(renn)

                        elif update.raw_text == "ساعت":
                            response = requests.get("http://api.codebazan.ir/time-date/?td=timeen").text
                            await update.reply(response)
                        elif update.raw_text == "تاریخ":
                            response = requests.get("http://api.codebazan.ir/time-date/?td=all").text
                            await update.reply(response)
                        elif update.raw_text == "قوانین":
                            rules = open("rules.txt","r",encoding='utf-8').read()
                            await update.reply(rules)
                        elif update.raw_text.startswith("//"):
                            text_wb = update.text.split("/")[-1]
                            #text_wb=update.text()[1:]
                            await client.send_message(my_group,f"لطفا صبر کنید...")
                            r = get(f"https://api2.haji-api.ir/gpt/gpt.php?text={text_wb}").json()
                            text=(r['result']['answer'])
                            await update.reply(text)
                        elif update.raw_text.startswith("اپدیت قوانین") or update.raw_text.startswith("/update_rules"):
                            rules = open("rules.txt","w",encoding='utf-8').write(str(update.raw_text.replace("اپدیت قوانین","").replace("/update_rules","")))
                            await update.reply("قوانین بروز شد.")

                        elif update.text.startswith("ترجمه به انگلیسی :"):
                                trans_text = update.text.split(":")[-1]
                                try:
                                    if trans_text != "":
                                        g = Translator()
                                        response = g.translate(
                                            trans_text(),'fa')
                                        await update.reply(response.text)
                                    else:
                                        await update.reply("لطفا یک متن را وارد کنید!")
                                except:
                                    await update.reply("خطا در اتصال به سرور!")

                        elif update.text.startswith("ترجمه به فارسی :"):
                                trans_text = update.text.split(":")[-1]
                                try:
                                    if trans_text != "":
                                        response = g.translate(
                                            trans_text.lower(),
                                            dest="fa",
                                            src="auto",
                                        )
                                        await update.reply(response.text)
                                    else:
                                        await update.reply("لطفا یک متن را وارد کنید!")
                                except:
                                    await update.reply("خطا در اتصال به سرور!")

                        #elif update.raw_text == 'جوک':
                           # path = choice(['سلام'])
                            #async with CS.post(f'http://haji-api.ir/sokhan?text={path}/') as response:
                             #   await update.reply(await response.text())

                        elif update.raw_text == 'ذکر امروز' or update.raw_text == 'ذکر':
                            await update.reply("یا ذالجلال والاکرام")

                        #elif update.raw_text == 'حدیث':
                           # async with CS.post('http://api.codebazan.ir/hadis/') as response:
                               # await update.reply(await response.text())

                        elif update.author_guid in group_admins and update.raw_text == 'باز کردن گیف' or update.raw_text == 'بازکردن گیف' or update.raw_text == '/UNLOCKGIF':
                            no_gifs = False
                            await update.reply('قفل گیف رفع شد.')

                        elif update.author_guid in group_admins and update.raw_text.startswith('سکوت'):
                            if update.reply_message_id != None:
                                try:
                                    result = await client(methods.messages.GetMessagesByID(my_group, [update.reply_message_id]))
                                    result = result.to_dict().get('messages')[0]
                                    if not result.get('author_object_guid') in group_admins:
                                        global silence_list
                                        silence_list.append(result.get('author_object_guid'))
                                        await update.reply('کاربر مورد نظر در حالت سکوت قرار گرفت.')
                                    else:
                                        await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                except IndexError:
                                    await update.reply('ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است.')
                            elif update.text.startswith('سکوت @'):
                                username = update.text.split('@')[-1]
                                if username != '':
                                    result = await client(methods.extras.GetObjectByUsername(username.lower()))
                                    result = result.to_dict()
                                    if result.get('exist'):
                                        if result.get('type') == 'User':
                                            user_guid = result.get('user').get('user_guid')
                                            if not user_guid in group_admins:
                                                #global silence_list
                                                silence_list.append(user_guid)
                                                await update.reply('کاربر مورد نظر در حالت سکوت قرار گرفت.')
                                            else:
                                                await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                        else:
                                            await update.reply('کاربر مورد نظر کاربر عادی نیست.')
                                    else:
                                        await update.reply('آیدی مورد نظر اشتباه است.')
                                else:
                                    await update.reply('آیدی مورد نظر اشتباه است.')
                            else:
                                await update.reply('روی یک کاربر ریپلای بزنید.')

                        elif update.author_guid in group_admins and update.raw_text.startswith('لیست سکوت خالی'):
                            if silence_list == []:
                                await update.reply('لیست سکوت خالی است.')
                            else:
                                silence_list = []
                                await update.reply('لیست سکوت خالی شد.')

                        elif update.raw_text == 'لینک':
                            result = await client(methods.groups.GetGroupLink(my_group))
                            result = result.to_dict().get('join_link')
                            await update.reply(f'لینک گروه:\n{result}')

                        elif update.author_guid in group_admins and update.text == '!update-admins':
                            reply = await update.reply('در حال به روزرسانی لیست ادمین ها...')
                            await updateAdmins(client)
                            await sleep(2)
                            await reply.edit('به روزرسانی لیست ادمین ها انجام شد.')

                        elif update.author_guid in group_admins and update.text.startswith('بن'):
                            if update.reply_message_id != None:
                                try:
                                    result = await client(methods.messages.GetMessagesByID(my_group, [update.reply_message_id]))
                                    result = result.to_dict().get('messages')[0]
                                    if not result.get('author_object_guid') in group_admins:
                                        result = await client(methods.groups.BanGroupMember(my_group, result.get('author_object_guid')))
                                        await update.reply('کاربر مورد نظر از گروه حذف شد.')
                                    else:
                                        await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                except IndexError:
                                    await update.reply('ظاهرا پیامی که روی آن ریپلای کرده اید پاک شده است.') # created by shayan heidari | rubpy
                            elif update.text.startswith('!ban @'):
                                username = update.text.split('@')[-1]
                                if username != '':
                                    result = await client(methods.extras.GetObjectByUsername(username.lower()))
                                    result = result.to_dict()
                                    if result.get('exist'):
                                        if result.get('type') == 'User':
                                            user_guid = result.get('user').get('user_guid')
                                            if not user_guid in group_admins:
                                                result = await client(methods.groups.BanGroupMember(my_group, user_guid))
                                                await update.reply('کاربر مورد نظر از گروه حذف شد.')
                                            else:
                                                await update.reply('کاربر مورد نظر در گروه ادمین است.')
                                        else:
                                            await update.reply('کاربر مورد نظر کاربر عادی نیست.')
                                    else:
                                        await update.reply('آیدی مورد نظر اشتباه است.')
                                else:
                                    await update.reply('آیدی مورد نظر اشتباه است.')
                            else:
                                await update.reply('روی یک کاربر ریپلای بزنید.') # created by shayan heidari | rubpy

            @client.on(handlers.MessageUpdates(models.is_group()))
            async def updates(update):
                if update.object_guid == my_group:
                    if update.author_guid in silence_list:
                        await update.delete_messages()
                    else:
                        if no_gifs:
                            if not update.author_guid in group_admins:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Gif':
                                    await update.delete_messages() # created by shayan heidari | rubpy
                                    print('Delete A Gif.')

                        if PASOKH:
                            if not update.author_guid in group_admins:
                                if update.raw_text == 'بعدی' or update.raw_text == 'بپرس':
                                    rando = ["۱۱۸🔓تاحالا احساس کردی یکی روت کراش زده باشه؟","۱۱۹🔓اگه یکی رو ناراحت ببینی چیکار میکنی؟","۱۲۰🔓بی رحمی یا دلت زود به رحم میاد؟","۱۲۱🔓تاحالا پیش کسی گوزیدی؟","۱۲۲🔓تاحالا خودتو خیس کردی؟","۱۲۳🔓اگه بیدار شی ببینی یکی خوابیده روت واکنشت چیه؟","۱۲۴🔓اگه روی یه صندلی کیک باشه یکیش کیر باشه،رو کدوم میشینی و کدومو میخوری؟","۱۲۵🔓جنسیتتو دوس داری عوض کنی؟","۱۲۶🔓دوس داری بری سربازی؟","۱۲۷🔓عکس یهوی بده؟","۱۲۸🔓شام دعوتت کنم قبول میکنی؟","۱۲۹🔓اگه همین الان بهت بگم دوست دارم واکنشت چیه؟","۱۰۰🔓اگه یه نفر مزاحم ناموست بشه باهاش چجوری رفتار میکنی؟","۱۰۱🔓شمارتو بده","۱۰۲🔓چقد آرایش میکنی؟","۱۰۳🔓پسر بازی رو دوس داری؟","۱۰۴🔓دختر بازی رو دوس داری؟","۱۰۵🔓اگه یه کص مفتی گیرت بیاد بازم پسش میزنی؟😁👍🏻","۱۰۶🔓پشمالو دوس داری؟🤧","۱۰۷🔓دوس داری شوهر آیندت چجوری باشه؟","۱۰۸🔓دوس داری زن آیندت چجوری باشه؟","۱۰۹🔓دوس داری چند تا بچه داشته باشی؟","۱۱۰🔓قشنگ ترین اسم پسر بنظرت؟","۱۱۱🔓قشنگ ترین اسم دختر بنظرت؟","۱۱۲🔓من خوشگلم یا زشت؟","۱۱۳🔓خوشگل ترین پسر گپ کیه؟","۱۱۴🔓خوشگل ترین دختر گپ کیه؟","۱۱۵🔓کی صداش از همه زیباتره؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۶🔓خانومت خوشگله یا زشته؟","۱۱۷🔓خوشتیپ هستی یا خوش قیافه؟","۸۰🔓سیگار یا قلیون میکشی؟","۸۱🔓منو میبری خونتون؟","۸۲🔓میذاری بیام خونتون؟","۸۳🔓تاحالا شکست عشقی خوردی؟💔","۸۴🔓اگه به زور شوهرت بدن تو چیکار میکنی؟","۸۵🔓اگه به زور زنت بدن تو چیکار میکنی؟","۸۶🔓تاحالا با پسر غریبه خوابیدی؟","۸۷🔓تاحالا با دختر غریبه خوابیدی؟","۸۸🔓با همجنست خوابیدی؟","۸۹🔓مدرسه یا گوشی؟","۹۰🔓سر کار میری؟","۹۱🔓کلن اخلاقت چجوریه؟","۹۲🔓هنوز پرده داری؟😐","۹۳🔓قلقلکی هستی؟","۹۴🔓سکس خشن دوس داری یا ملایم؟","۹۵🔓کصکش ناله های دختر مردمو میخوای ببینی😐⚔","۹۶🔓چند بار سوتی میدی؟","۹۷🔓مواظب کصت باش تا بیام بگیرمت باشه؟🤭👍🏻","۹۸🔓تاحالا مچ عشقتو موقع لب بازی با یه دختر دیگه گرفتی؟","۹۹🔓تاحالا مچ عشقتو موقع لب بازی با یه پسر دیگه گرفتی؟","۶۰🔓پیش کسی ضایع شدی؟","۶۱🔓از مدرسه فرار کردی؟","۶۲🔓میخوای چند سالگی ازدواج کنی؟","۶۳🔓اگه مامان و بابات اجازه ندن با عشقت ازدواج کنی چیکار میکنی؟","۶۴🔓چند سالگی پ....ری....و..د شدی؟😶","۶۵🔓وقتی پریودی چجوری هستی؟","۶۶🔓رنگ مورد علاقت؟","۶۷🔓غذای مورد علاقت؟","۶۸🔓پولدارین یا فقیر؟","۶۹🔓دوس داری با من بری بیرون؟","۷۰🔓منو بوس میکنی؟☺️😚","۷۱🔓منو میکنی؟😬","۷۲🔓س...ک...س چت داشتی؟","۷۳🔓خوشت میاد از س....ک.....س؟","۷۴🔓خجالتی هستی یا پررو؟","۷۵🔓دوس داری بکنمت؟🤤","۷۶🔓تاحالا کسی برات خورده؟😁","۷۷🔓من ببوسمت خوشحال میشی؟","۷۸🔓خفن ترین کاری که تا الان کردی؟","۷۹🔓آرزوت چیه؟","۳۰🔓خاستگار داری؟عکسش یا اسمش","۳۱🔓به کی اعتماد داری؟","۳۲🔓تاحالا با کسی رفتی تو خونه خالی؟","۳۳🔓چاقی یا لاغر؟","۳۴🔓قد بلندی یا کوتاه؟","۳۵🔓رنگ چشمت؟","۳۶🔓رنگ موهات؟","۳۷🔓موهات فرفریه یا صاف و تا کجاته؟","۳۸🔓تاریخ تولدت؟","۳۹🔓تاریخ تولد عشقت؟","۴۰🔓عشقت چجوری باهات رفتار میکنه؟","۴۱🔓با دوس پسرت عشق بازی کردی؟🤤","۴۲🔓پیش عشقت خوابیدی؟","۴۳🔓عشقتو بغل کردی؟","۴۴🔓حاضری ۱۰ سال از عمرتو بدی به عشقت؟","۴۵🔓مامان و بابات چقد دوست دارن؟","۴۶🔓دعوا کردی؟","۴۸🔓چند بار کتک زدی؟","۴۹🔓چند بار کتک خوردی؟","۵۰🔓تاحالا تورو دزدیدن؟","۵۱🔓تاحالا کسی ل..خ....ت تورو دیده؟🤭","۵۲🔓تاحالا ل...خ...ت کسیا دیدی؟","۵۳🔓دست نام....حرم بهت خورده؟","۵۴🔓دلت برا کی تنگ شده؟","۵۵🔓دوس داشتی کجا بودی؟","۱🔓عاشق شدی؟اسمش❤️","۲🔓رل زدی تاحالا؟اسمش","۳🔓کراش داری؟اسمش","۴🔓چند بار تا الان رابطه جنسی داشتی؟با کی😐💦","۵🔓از کی خوشت میاد؟","۶🔓از کی بدت میاد؟","۷🔓منو دوس داری؟بهم ثابت کن","۸🔓کی دلتو شکونده؟","۹🔓دل کیو شکوندی؟","۱۰🔓وقتی عصبانی هستی چجوری میشی؟","۱۱🔓دوس داری کیو بزنی یا بکشی؟","۱۲🔓دوس داری کیو بوس کنی؟😉💋","۱۳🔓از تو گالریت عکس بده","۱۴🔓از مخاطبینت عکس بده","۱۵🔓از صفحه چت روبیکات عکس بده","۱۶🔓لباس زیرت چه رنگیه؟🙊","۱۷🔓از وسایل آرایشت عکس بده","۱۷🔓از وسایل آرایشت عکس بده","۱۸🔓از لباسای کمدت عکس بده","۱۹🔓از کفشات عکس بده","۲۰🔓تالا بهت تجاوز شده؟😥","۲۱🔓تاحالا مجبور شدی به زور به کسی بگی دوست دارم؟","۲۲🔓تاحالا یه دخترو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۳🔓تاحالا یه پسرو بردی خونتون؟","۲۴🔓با کی ل....ب گرفتی؟😜","۲۵🔓خود ار.ض..ای..ی کردی؟😬💦"]
                                    renn= choice(rando)
                                    await update.reply(renn)
                            
                        if lockphoto:
                            if lockphoto:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                #result = update.to_dict().get("message")
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Image':
                                    await update.delete_messages()
                                    print('Delete A Photo.')

                        if lockvideo:
                            if lockvideo:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                #result = update.to_dict().get("message")
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Video':
                                    await update.delete_messages()
                                    print('Delete A video.')

                        if lockMusic:
                            if lockMusic:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                #result = update.to_dict().get("message")
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Music':
                                    await update.delete_messages()
                                    print('Delete A Music.')

                        if lockVoice:
                            if lockVoice:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                #result = update.to_dict().get("message")
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'Voice':
                                    await update.delete_messages()
                                    print('Delete A Voice.')

                        if lockFile:
                            if lockFile:
                                result = await client(methods.messages.GetMessagesByID(my_group, [update.message_id]))
                                result = result.to_dict().get('messages')[0]
                                #result = update.to_dict().get("message")
                                if result.get('type') == 'FileInline' and result.get('file_inline').get('type') == 'File':
                                    await update.delete_messages()
                                    print('Delete A File.')

                        if AUTOLOCK:
                            if AUTOLOCK:
                                if update.raw_text == "یک عضو از طریق لینک به گروه افزوده شد.":
                                    result = await client.get_user_info(update.author_guid)
                                    first_name = result.user.first_name
                                    await update.reply(f"سلام [{first_name}]({update.author_guid}) عزیز 🌹 \n • به گروه ما خوش اومدی 😍 \n 📿 لطفا قوانین رو رعایت کن .\n 💎 برای مشاهده قوانین کافیه کلمه (قوانین) رو ارسال کنی .")
                                if update.raw_text == "یک عضو از طریق لینک به گروه افزوده شد.":
                                    result = await client.get_user_info(update.author_guid)
                                    first_name = result.user.first_name
                                    await update.reply(f"خدانگهدار [{first_name}]({update.author_guid}) 👋 ")                                



            await client.run_until_disconnected()

run(main())