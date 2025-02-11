import requests
import telebot

allowed_ids = [5696226098]

sto = {"stop": True}
token = "7348550676:AAHhto8mE0bLU8SYfLKMFB8-_mLablwAvr8"
bot = telebot.TeleBot(token, parse_mode="HTML")


@bot.message_handler(commands=["stop"])
def start(message):
  sto.update({"stop": True})
  bot.reply_to(message,
               '𝐼 𝑠𝑡𝑜𝑝𝑝𝑒𝑑 𝑡𝒉𝑒 𝑐𝑜𝑚𝑏𝑜 𝑓𝑜𝑟 𝑦𝑜𝑢, 𝑤𝑖𝑡𝒉 𝑦𝑜𝑢𝑟 𝑝𝑒𝑟𝑚𝑖𝑠𝑠𝑖𝑜𝑛. 𝑊𝑎𝑖𝑡 10𝑠')


@bot.message_handler(commands=["start"])
def start(message):
  bot.send_message(message.chat.id,
                   "   Send your combo txt file now".format(
                       message.chat.first_name),
                   reply_markup=telebot.types.InlineKeyboardMarkup())


@bot.message_handler(content_types=["document"])
def main(message):
  first_name = message.from_user.first_name
  name = f"{first_name} "
  risk = 0
  bad = 0
  nok = 0
  ok = 0
  ko = (bot.reply_to(
      message,
      f" WELCOME {name}  NOW I WILL BE CHECKING YOUR CARDS FORE MY UPDATES JOIN @STARKxNETWORK ").message_id)
  ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
  with open("combo.txt", "wb") as w:
    w.write(ee)
  print(message.chat.id)
  sto.update({"stop": True})
  if message.chat.id in allowed_ids:
    with open("combo.txt") as file:
      lino = file.readlines()
      lino = [line.rstrip() for line in lino]
      total = len(lino)
      for cc in lino:
        if sto["stop"] == True:
          pass
        else:
          break
        bin = cc[:6]
        url = f"https://lookup.binlist.net/{bin}"
        try:
          req = requests.get(url).json()
        except:
          pass
        try:
          inf = req['scheme']
        except:
          inf = "------------"
        try:
          type = req['type']
        except:
          type = "-----------"
        try:
          brand = req['brand']
        except:
          brand = '-----'
        try:
          info = inf + '-' + type + '-' + brand
        except:
          info = "CREDIT-CORPORATE"
        try:
          ii = info.upper()
        except:
          ii = "----------"
        try:
          bank = req['bank']['name'].upper()
        except:
          bank = "CAPITAL ONE"
        try:
          do = req['country']['name'] + ' ' + req['country']['emoji'].upper()
        except:
          do = "-----------"
        mes = types.InlineKeyboardMarkup(row_width=1)
        GALD1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
        ##GALD2 = types.InlineKeyboardButton(f"• {cc} •",callback_data='u1')
        GALD3 = types.InlineKeyboardButton(f"• 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅ : [ {ok} ] •",
                                           callback_data='u2')
        GALD4 = types.InlineKeyboardButton(f"• 𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌  : [ {bad} ] •",
                                           callback_data='u1')
        risk6 = types.InlineKeyboardButton(f"• 𝗥𝗜𝗦𝗞 🥲  : [ {risk} ] •",
                                           callback_data='u1')
        GALD5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟   : [ {total} ] •",
                                           callback_data='u1')
        mes.add(GALD1, GALD3, GALD4, risk6, GALD5)
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=ko,
            text=f''' 𓆩 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𓆪ꪾ  {name}, 𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗰𝗮𝗿𝗱...⌛💸
    ''',
            parse_mode='markdown',
            reply_markup=mes)

        try:
          last = str(Tele(cc))
        except Exception as e:
          print(e)
          try:
            last = str(Tele(cc))
          except Exception as e:
            print(e)
            bot.reply_to(message, f"𝑪𝑨𝑹𝑫 𝑰𝑺 𝑫𝑬𝑨𝑫 𝑨𝑵𝑫 𝑰 𝑺𝑲𝑰𝑷𝑷𝑬𝑫 >> {cc}")
        if "risk" in last:
          risk += 1
          print(Fore.YELLOW + cc + "->" + Fore.CYAN + last)
        elif "Insufficient Funds" in last:
          ok += 1
          respo = f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────

[↯] 𝗕𝗢𝗧 𝗕𝗬: @Stxthunder
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────
'''
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
±++++++++++++++++++++++++++++
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────

[↯] 𝗕𝗢𝗧 𝗕𝗬: @Stxthunder
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────''')
        elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Status code 81724: Duplicate card exists in the vault." in last:
          ok += 1
          respo = (f'''
━━━━[🌹𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅🌹]━━━━
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗖𝗖 ★ <code>{cc}</code>
<a >[↯]</a> 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
<a >[↯]</a> 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼 ↯ <code>{ii}</code>
<a >[↯]</a> 𝗕𝗮𝗻𝗸 ↯ <code>{bank}</code>
<a >[↯]</a> 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ↯ <code>{do}</code>
<a >━━━━━━━━━━━━━━━━━━</a>
<a >[↯]</a> 𝗕𝗢𝗧 𝗕𝗬 ↯ <a href='t.me/Stxthunder'>Thunder</a>
<a >[↯]</a> 𝗣𝗥𝗢𝗫𝗬  ↯ <code>𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]</code>
<a >━━━━━━━━━━━━━━━━━━</a>''')
          print(Fore.YELLOW + cc + "->" + Fore.GREEN + last)
          bot.reply_to(message, respo)
          with open("hit.txt", "a") as f:
            f.write(f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅
──────────────────
[↯] 𝗖𝗖 ★ {cc}
[↯] 𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ★ 𓆩𝐁𝐫𝐚𝐢𝐧𝐭𝐫𝐞𝐞𓆪ꪾ 𝙰𝚞𝚝𝚑
[↯] 𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ★ <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱ꪜ 
──────────────────
[↯] 𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
[↯] 𝗕𝗮𝗻𝗸: {bank}
[↯] 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}
──────────────────
[↯] 𝗕𝗢𝗧 𝗕𝗬: @Stxthunder
[↯] 𝗣𝗥𝗢𝗫𝗬 : 𝗟𝗶𝘃𝗲 [1XX.XX.XX 🟢]
──────────────────''')
        else:
          bad += 1
          print(Fore.YELLOW + cc + "->" + Fore.RED + last)
      if sto["stop"] == True:
        bot.reply_to(message, 'X')
  else:
    bot.reply_to(
        message,
        "you're not premium user  \n paid premium plan  \n Not for Sell")


print("STARTED BOT @StarkxNetwork")
bot.infinity_polling()

