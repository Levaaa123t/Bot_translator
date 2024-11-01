# Задание №3
from translate import Translator
import requests
from collections import defaultdict

# Задание №5
qwestions = {'как тебя зовут'or'Как тебя зовут'or 'Как тебя зовут?'or 'как тебя зовут?' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "сколько тебе лет" or 'Сколько тебе лет' or 'сколько тебе лет?' : "Это слишком философский вопрос",
             'что ты делаешь' or 'Что ты делаешь':'Я выполняю свои обязанности, а именно - я перевожу слова и фразы которые ты мне пишешь'
             }
class TextAnalysis():   
    
    # Задание №1
    memory = defaultdict(list)
    def __init__(self, text, owner):

        # Задание №2
        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        # Задание №6
        self.response = self.get_answer()
        if self.text.lower() in qwestions.keys():
            self.response =  qwestions[self.text.lower()]
        else:
            self.response = self.get_answer() 
    
    def get_answer(self):
        res = self.__translate("I don't know how to help", "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Задание №4
            translator = Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"

