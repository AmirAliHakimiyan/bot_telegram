import telebot
from telebot import types
import random
import gtts
import qrcode

board=types.ReplyKeyboardMarkup(row_width=7)
key1=types.KeyboardButton("/game")
key2=types.KeyboardButton("/age")
key3=types.KeyboardButton("/voice")
key4=types.KeyboardButton("/max")
key5=types.KeyboardButton("/argmax")
key6=types.KeyboardButton("/qrcode")
key7=types.KeyboardButton("/help")
board.add(key1,key2,key3,key4,key5,key6,key7)
bot=telebot.TeleBot("5902046348:AAFFH8xACih2KQY57pi-8MCobulOYFFviL0",parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['start'])
def send_welcome(message):
	name = message.from_user.first_name
	nam=name+" hellow"
	bot.reply_to(message, nam,reply_markup=board)
@bot.message_handler(commands=['start'])
def help(message):
	bot.reply_to(message,"کامند start/با نام کاربر، خوش آمدید چاپ کند. مثلا (sajjad خوش آمدی)کامند game/بازی حدس عدد اجرا شود. کاربر یک عدد حدس میزند و بات راهنمایی می‌کند (برو بالا، برو پایین، برنده شدی) - در هنگام بازی، یک دکمه new game در پایین بات مشاهده شود.کامند age/تاریخ تولد را به صورت هجری شمسی دریافت نماید وکامند voice/یک جمله به انگلیسی از کاربر دریافت نماید و آن را به صورت voice ارسال نماید.کامند max/یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و بزرگترین مقدار را چاپ نمایدکامند argmax/یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و اندیس بزرگترین مقدار را چاپ نماید.کامند qrcode/یک رشته از کاربر دریافت نماید و qrcode آن را تولید نماید.")
@bot.message_handler(commands=["game"])
def game(message):
	number=random.randint(0,50)
	bot.send_message(message.chat.id,'enter the number')
	@bot.message_handler(func=lambda m:True)
	def echo_all(message):
		if number==int(message.text):
			bot.send_message(message.chat.id,"you win")
		elif number >int(message.text):
			bot.send_message(message.chat.id,"go up")
		elif number<int(message.text):
			bot.send_message(message.chat.id,"go down")
@bot.message_handler(commands=["age"])
def age(message):
	bot.send_message(message.chat.id,"enter the your age.example :1385")
	@bot.message_handler(func=lambda m:True)
	def echo_all(message):
		bot.send_message(message.chat.id,1401-int(message.text))
		
@bot.message_handler(commands=['max'])
def max_num(message):
    bot.send_message(message.chat.id, 'Enter the list of numbers: (Format: x,y,z,k,t,...)')
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        usr_num_list = list(message.text.split(','))
        int_num_list = [eval(i) for i in usr_num_list]
        maxn = max(int_num_list)
        bot.reply_to(message, 'Max Number is ' + str(maxn))

@bot.message_handler(commands=['voice'])
def max_num_arg(message):
    bot.send_message(message.chat.id, 'Enter the English text you want to convert to Voice: ')
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        text_to_voice = message.text
        tts = gtts.gTTS(text_to_voice)
        tts.save('1.mp3')
        audio = open('1.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
    
    
    
    
@bot.message_handler(commands=['argmax'])
def max_num_arg(message):
    bot.send_message(message.chat.id, 'Enter the list of numbers: (Format: x,y,z,k,t,...)')
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        usr_num_list = list(message.text.split(','))
        int_num_list = [eval(i) for i in usr_num_list]
        maxn = max(int_num_list)
        maxarg = int_num_list.index(maxn)
        bot.reply_to(message, 'Max Number is ' + str(maxarg))
@bot.message_handler(commands=['qrcode'])
def qr_code(message):
    bot.send_message(message.chat.id, "let's go to make qrcode")
    @bot.message_handler(func=lambda m:True)
    def echo_all(message):
        text_input = message.text
        q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
        q.add_data(text_input)
        i = q.make_image(fill_color = 'white', back_color = 'black')
        i.save('1.png')
        photo = open('1.png', 'rb')
        bot.send_photo(message.chat.id, photo)
bot.infinity_polling()
