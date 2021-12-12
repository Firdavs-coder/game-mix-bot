import telebot
import random
import requests
from telebot import types


bot = telebot.TeleBot("5047983291:AAG4zpk91j_LMW0VWDOlUPNvjRT3NDnDA7w", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
start_text = '✅ Hi. You can get information or download information about different games on this bot. And in this bot you can find a variety of jokes and facts. You can also find pictures of Disney world actors and Forza Horizon game car.'

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if str(call.data).startswith('d_'):
        send_disney(call)
        
    else:
        send_freegame(call)
        

def send_freegame(call):
    id = str(call.data)[2:]
    r = requests.get('https://www.freetogame.com/api/games')
    response = r.json()
    for i in response:
        if i['id'] == int(id):
            title = i['title']
            thumbnail = i['thumbnail']
            short_description = i['short_description']
            game_url = i['game_url']
            developer = i['developer']
            platform  = i['platform']
            genre  = i['genre']
            text = f"""<b>{title}</b>\n\n👉 {short_description}\n\n🌐 {game_url}\n\n👨‍💻 Developer - {developer}\n\n📲💻 {platform}\n\n💾 {genre}"""
            bot.send_photo(call.from_user.id,thumbnail,caption=text,parse_mode='HTML')

def send_disney(call):
    id = str(call.data)[2:]
    r = requests.get(f'https://api.disneyapi.dev/characters/{id}')
    response = r.json()
    src = response['sourceUrl']
    name = response['name']
    
    if response['films']:
        films = ''
        for i in response['films']:
            films = f' <em>{i}.</em>'
    else:
        films = 'There is no film'
    if response['tvShows']:
        tvShows = ''
        for i in response['tvShows']:
            tvShows = f' <em>{i}.</em>'
    else:
        tvShows = 'There is no tvShows'
    if response['videoGames']:
        videoGames = ''
        for i in response['videoGames']:
            videoGames = f' <em>{i}.</em>'
    else:
        videoGames = 'There is no videoGames'
    text = f"""👉 <b>{name}</b>\n\n🌐 {src}\n\n🎬 {films}\n\n🎙 {tvShows}\n\n🕹 {videoGames}"""
    # bot.answer_callback_query(call.id, call.data)
    bot.send_photo(call.from_user.id, response['imageUrl'],caption=text, parse_mode='HTML')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    if text == '/start':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        joke_btn = types.KeyboardButton('Joke')
        fact_btn = types.KeyboardButton ('Facts')
        game_btn = types.KeyboardButton ('Games')
        disney_btn = types.KeyboardButton ('Disney World')
        forza_btn = types.KeyboardButton ('Forza Cars')
        question_btn = types.KeyboardButton ('Quiz Questions')
        markup_reply.add(
            joke_btn,
            question_btn,
            fact_btn,
            game_btn,
            disney_btn,
            forza_btn,
            )
        bot.send_message(message.chat.id,start_text)
        bot.send_message(message.chat.id, '🔍 Menu',reply_markup = markup_reply)
    elif text == 'Joke':
        joke(message)
    elif text == 'Facts':
        fact(message)
    elif text == 'Games':
        freetogame(message)
    elif text == 'Disney World':
        disney(message)
    elif text == 'Forza Cars':
        forza(message)
    elif text == 'Quiz Questions':
        question2(message)

def question2(message):
    r = requests.get('https://opentdb.com/api.php?amount=1')
    response = r.json()
    category = response['results'][0]['category']
    difficulty = response['results'][0]['difficulty']
    question = response['results'][0]['question']
    right = response['results'][0]['correct_answer']
    inc = response['results'][0]['incorrect_answers']
    inc.append(right)
    random.shuffle(inc)
    true = inc.index(right)
    text = f"""Category - {category}\n Difficulty - {difficulty}\n ❓ {question} """
    bot.send_poll(message.chat.id, question=text, options=inc, type='quiz', correct_option_id=int(true), )

def forza(message):
    r = requests.get('https://forza-api.tk/')
    response = r.json()
    image = response['image']
    bot.send_photo(message.chat.id, image)

def disney(message):
    r = requests.get('https://api.disneyapi.dev/characters')
    response = r.json()
    text = """"""
    random.shuffle(response['data'])
    id_l = []
    for i in response['data'][:10]:
        id_l.append(i['_id'])
        text += '\n' +'🤩'+ i['name']
    markup = types.InlineKeyboardMarkup(row_width=5)
    b1 = types.InlineKeyboardButton('1', callback_data=f'd_{id_l[0]}')
    b2 = types.InlineKeyboardButton('2', callback_data=f'd_{id_l[1]}')
    b3 = types.InlineKeyboardButton('3', callback_data=f'd_{id_l[2]}')
    b4 = types.InlineKeyboardButton('4', callback_data=f'd_{id_l[3]}')
    b5 = types.InlineKeyboardButton('5', callback_data=f'd_{id_l[4]}')
    b6 = types.InlineKeyboardButton('6', callback_data=f'd_{id_l[5]}',)
    b7 = types.InlineKeyboardButton('7', callback_data=f'd_{id_l[6]}',)
    b8 = types.InlineKeyboardButton('8', callback_data=f'd_{id_l[7]}',)
    b9 = types.InlineKeyboardButton('9', callback_data=f'd_{id_l[8]}',)
    b10 = types.InlineKeyboardButton('10', callback_data=f'd_{id_l[9]}',)
    markup.add(b1, b2,b3, b4, b5, b6,b7, b8, b9, b10)
    bot.send_message(message.chat.id, text,reply_markup=markup)

def freetogame(message):
    r = requests.get('https://www.freetogame.com/api/games')
    response = r.json()
    text = """"""
    random.shuffle(response)
    id_l = []
    for i in response[:10]:
        id_l.append(i['id'])
        text += '\n' +'🕹 '+ i['title']
    markup = types.InlineKeyboardMarkup(row_width=5)
    b1 = types.InlineKeyboardButton('1', callback_data=f'f_{id_l[0]}')
    b2 = types.InlineKeyboardButton('2', callback_data=f'f_{id_l[1]}')
    b3 = types.InlineKeyboardButton('3', callback_data=f'f_{id_l[2]}')
    b4 = types.InlineKeyboardButton('4', callback_data=f'f_{id_l[3]}')
    b5 = types.InlineKeyboardButton('5', callback_data=f'f_{id_l[4]}')
    b6 = types.InlineKeyboardButton('6', callback_data=f'f_{id_l[5]}',)
    b7 = types.InlineKeyboardButton('7', callback_data=f'f_{id_l[6]}',)
    b8 = types.InlineKeyboardButton('8', callback_data=f'f_{id_l[7]}',)
    b9 = types.InlineKeyboardButton('9', callback_data=f'f_{id_l[8]}',)
    b10 = types.InlineKeyboardButton('10', callback_data=f'f_{id_l[9]}',)
    markup.add(b1, b2,b3, b4, b5, b6,b7, b8, b9, b10)
    bot.send_message(message.chat.id, text,reply_markup=markup)

def fact(message):
    r = requests.get('https://asli-fun-fact-api.herokuapp.com/')
    response = r.json()
    bot.send_message(message.chat.id, '✅ '+response['data']['fact'])

def joke(message):
    if message.from_user.first_name and message.from_user.last_name:
        f_name = message.from_user.first_name
        l_name = message.from_user.last_name
        r = requests.get(f'https://api.icndb.com/jokes/random?firstName={f_name}&lastName={l_name}')
    elif message.from_user.username:
        username = message.from_user.username
        r = requests.get(f'https://api.icndb.com/jokes/random?firstName={username}')
    else:
        r = requests.get('https://api.icndb.com/jokes/random?firstName=You')
    response = r.json()
    bot.send_message(message.chat.id, '🔹 '+response['value']['joke'])
    # print(response['value']['joke'])	



bot.infinity_polling()
