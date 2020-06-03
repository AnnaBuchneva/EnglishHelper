# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("start good.mp3")

# from tts_watson.TtsWatson import TtsWatson
#
# ttsWatson = TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice')
# ttsWatson.play("Hello World")
#
# import pyttsx3
# tts = pyttsx3.init()
# # Перебрать голоса и вывести параметры каждого
# for voice in tts.getProperty('voices'):
#     print('=======')
#     print('Имя: %s' % voice.name)
#     print('ID: %s' % voice.id)
#     print('Язык(и): %s' % voice.languages)
#     print('Пол: %s' % voice.gender)
#     print('Возраст: %s' % voice.age)

# import pyttsx3
# tts = pyttsx3.init()
# voices = tts.getProperty('voices')
# # Задать голос по умолчанию
# tts.setProperty('voice', 'ru')
# # Попробовать установить предпочтительный голос
# for voice in voices:
#     if voice.name == 'Aleksandr':
#         tts.setProperty('voice', voice.id)
#
# tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
# tts.runAndWait()

# import pyttsx3
# tts = pyttsx3.init()
# # EN_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20DSK"
# EN_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# # RU_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Anna"
# RU_VOICE_ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
# # Использовать английский голос
# tts.setProperty('voice', EN_VOICE_ID)
# tts.say("Can you hear me say it's a lovely day?")
# # Теперь — русский
# tts.setProperty('voice', RU_VOICE_ID)
# tts.say("А напоследок я скажу")
# tts.runAndWait()

# import pyttsx3
# tts = pyttsx3.init()
# voices = tts.getProperty('voices')
# # Перебрать голоса и вывести параметры каждого
# for voice in voices:
#     print('=======')
#     print('Имя: %s' % voice.name)
#     print('ID: %s' % voice.id)
#     print('Язык(и): %s' % voice.languages)
#     print('Пол: %s' % voice.gender)
#     print('Возраст: %s' % voice.age)
# import pyttsx3
# def onStart(name):
#    print('starting', name)
# def onWord(name, location, length):
#    print('word', name, location, length)
# def onEnd(name, completed):
#    print('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
#
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()
# # import pywin32

import os
import copy
import random
import pyttsx3
import googletrans
import spellchecker
import difflib
import re
import speech_recognition
# import pyaudio


def update_dict():
    with open(r'C:\Users\Demo\Documents\spelling.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        line = line.strip()
        if '-' in line:
            line = line.split('-')[1:]
        elif '–' in line:
            line = line.split('–')[1:]
        else:
            line = [line]
        res_lines = []
        for ln in line:
            if ',' in ln:
                res_lines += ln.split(',')
            else:
                res_lines.append(ln)
        for ln in res_lines:
            new_lines.append(ln.strip().lower() + '\n')
    with open(r'C:\Users\Demo\Documents\spelling_new.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


tts = pyttsx3.init()
EN_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
RU_VOICE_ID = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

translator = googletrans.Translator()

spell = spellchecker.SpellChecker()


def say(text):
    tts.say(text)
    tts.runAndWait()


def say_en(text):
    tts.setProperty('voice', EN_VOICE_ID)
    say(text)


def say_ru(text):
    tts.setProperty('voice', RU_VOICE_ID)
    say(text)


def translate(text, dest='ru', full=True):
    src = 'en' if dest == 'ru' else 'ru'
    translations = translator.translate([text], src=src, dest=dest)
    if not full:
        for translation in translations:
            return translation.text.lower()
    else:
        result = []
        for translation in translations:
            if translation.extra_data and translation.extra_data.get('all-translations'):
                for element in translation.extra_data['all-translations']:
                    for word in element[2]:
                        if len(word) > 3 and word[3]:
                            if word[3] >= 0.001:
                                result.append(word[0])
            if not result:
                result.append(translation.text.lower())
        return result


def translate_to_en(text):
    return translate(text, dest='en')


def translate_to_ru(text):
    return translate(text, dest='ru')


def test_spell(text):
    # find those words that may be misspelled
    misspelled = spell.unknown([text])
    for word in misspelled:
        # Get the one `most likely` answer
        return spell.correction(word)
        # Get a list of `likely` options
        # print(spell.candidates(word))
    return None


def cls():
    os.system('cls')


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Word:

    def __init__(self, raw):
        self.were_errors = False
        raw = raw.strip().lower()
        self.word = raw
        self.synonym = None
        self.value = 0

        if re.match(r'.+\s\(.+\)', raw):
            self.synonym = re.findall(r'\(.+\)', raw)[0].strip('() ')
            self.word = raw.split(self.synonym)[0].strip('() ')
        else:
            self.word = raw
        if ';' in raw:
            self.word = self.word.split(';')[0]
            self.value = int(raw.split(';')[1])

    def match(self, check, use_stat=True):
        check = check.strip().lower()
        result = check == self.word
        if use_stat:
            if result:
                self.value += 1
            else:
                self.value -= 1
                self.were_errors = True
        return result

    def learned(self):
        return self.value >= Queue.limit or (not self.were_errors and self.value > 0)

    def dump(self):
        wrd = self.word
        if self.synonym:
            wrd = f'{self.word} ({self.synonym})'
        return f'{wrd};{self.value}'

    def __str__(self):
        return self.word


class Queue:
    limit = 3

    def __init__(self, input_list=None, file=None):
        self.__source = []
        self.__left = []
        if input_list:
            self.set(input_list)
        if file:
            self.read(file)

    def get(self):
        word = self.get_word()
        if word:
            word = str(word)
        return word

    def get_word(self):
        if self.full():
            return self.__left[0]
        return None

    def poll(self):
        if self.full():
            element = self.__left[0]
            self.__left = self.__left[1:]
            return element
        return None

    def add(self, element):
        self.__left.append(element)
        random.shuffle(self.__left)

    def set(self, input_list):
        self.__source = input_list
        self.__left = [Word(line) for line in input_list]
        self.mix()

    def mix(self):
        random.shuffle(self.__left)

    def full(self):
        return len(self.__left) > 0

    def read(self, path):
        if not path:
            return
        result = []
        if not type(path) is list:
            path = [path]
        for file in path:
            result += [ln.strip() for ln in open(file, 'r', encoding='utf-8').readlines()]
        self.set(result)

    def write(self, path):
        open(path, 'w', encoding='utf-8').write('\n'.join([el.dump() for el in self.__left]))

    def say(self):
        say_en(self.get())

    def ru(self):
        return translate_to_ru(self.get())

    def say_ru(self):
        say_ru(translate_to_ru(self.get()))

    def synonym(self):
        return self.get_word().synonym

    @staticmethod
    def to_bold(text):
        return Color.BOLD + text + Color.END

    @staticmethod
    def get_diff(result, expected, bold=True):
        word = ''
        for s in difflib.ndiff(result, expected):
            if s[0] == ' ':
                word += s[-1]
                continue
            elif s[0] == '-':
                letter = s[-1].capitalize()
                if bold:
                    letter = Queue.to_bold(letter)
                word += letter
        return word

    @staticmethod
    def learn_str(result, expected, comment=''):
        return input(f'{comment + " " if comment else ""}Expected "{expected}", got "{result}". '
                     f'Diff: {Queue.get_diff(result, expected)}. '
                     f'Print again to learn: ').strip().lower()

    def match(self, check):
        if not self.get_word().match(check):
            while not self.get_word().match(check):
                mis_check = check
                misspelled = test_spell(mis_check)
                if mis_check and misspelled and not self.get_word().match(misspelled, use_stat=False):
                    while misspelled and not mis_check == misspelled:
                        mis_check = Queue.learn_str(mis_check, misspelled, comment='Misspelled')
                        misspelled = test_spell(mis_check)

                check = Queue.learn_str(check, self.get())
        elif self.get_word().learned():
            self.poll()
        self.mix()

    def iterate(self, question, assist=None, path='result.txt'):
        def run(func):
            if not type(func) is list:
                func = [func] if func else []
            for f in func:
                out = f()
                if out is not None:
                    print(out)

        while self.full():
            try:
                run(question)
                answer = input('Your answer: ')
                if answer == 'r':
                    continue
                if answer == 'q':
                    print('Quitting')
                    self.write(path)
                    break
                if answer == 'h':
                    run(assist)
                    continue
                self.match(answer)
            except Exception as e:
                self.write(path)
                print(e)


def spelling():
    queue = Queue(file=r'spelling_left.txt')
    queue.iterate(queue.say, queue.ru, path=r'spelling_left.txt')


def synonyms():
    queue = Queue(file=r'synonyms.txt')
    queue.iterate(queue.ru, queue.synonym, path=r'synonyms_left.txt')


def test(inf, out=None):
    if not out:
        out = inf
    queue = Queue(file=inf)
    queue.iterate(queue.ru, path=out)


test(r'academic_left.txt')
# test([r'academic.txt', r'synonyms.txt', r'spelling.txt', r'my_words.txt'], r'all_left.txt')
#spelling()
# test(r'my_words.txt', r'my_words_left.txt')
# "there is no doubt"
# recoop