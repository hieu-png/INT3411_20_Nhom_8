from difflib import get_close_matches
import json
from random import choice
import datetime


class DateTime:
    def currentTime(self):
        time = datetime.datetime.now()
        x = " A.M."
        if time.hour > 12: x = " P.M."
        time = str(time)
        time = time[11:16] + x
        return time

    def currentDate(self):
        now = datetime.datetime.now()
        day = now.strftime('%A')
        date = str(now)[8:10]
        month = now.strftime('%B')
        year = str(now.year)
        result = f'{day}, {date} {month}, {year}'
        return result


# chao buoi x
def wishMe():
    now = datetime.datetime.now()
    hr = now.hour
    if hr < 12:
        wish = "Good Morning"
    elif hr >= 12 and hr < 16:
        wish = "Good Afternoon"
    else:
        wish = "Good Evening"
    return wish


def isContain(text, lst):
    for word in lst:
        if word in text:
            return True
    return False


def chat(text):
    dt = DateTime()
    result = ""
    if isContain(text, ['chào']):
        result = wishMe()
    elif isContain(text, ['giờ']):
        result = "Bây giờ là: " + dt.currentTime()
    elif isContain(text, ['năm', 'hôm nay', 'ngày', 'tháng']):
        result = dt.currentDate()

    return result


data = json.load(open('extrafiles/NormalChat.json', encoding='utf-8'))

# rep lai tro chuyen
def reply(query):
    if query in data:
        response = data[query]
    else:
        query = get_close_matches(query, data.keys(), n=2, cutoff=0.6)
        if len(query) == 0: return "None"
        return choice(data[query[0]])

    return choice(response)

# dich
def lang_translate(text):
    # print(language)
    from googletrans import Translator, LANGUAGES
    # if language in LANGUAGES.keys():
    translator = Translator()
    result = translator.translate(text, dest='vi')
    return result
# else:
#	return "None"
