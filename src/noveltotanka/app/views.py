from django.shortcuts import render
from django.http import HttpResponse
from app.modules import novel_string
from app.forms import WordForm
from pathlib import Path

import random
import re
import os
import cv2

def search_keyword(string, text):
    hitted = re.finditer(string, text)
    result = []
    for i in hitted:
        result.append(i)
    random.shuffle(result)
    return result[0]

def index(request):
    # BASE_DIR = Path(__file__).resolve().parent.parent

    # img = cv2.imread(os.path.join(BASE_DIR, "static/app/img/sample.jpg"),0)
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(output_path, img_gray)
    # print(img)

    return render(request, "app/index.html", context=None)

def run1(request):
    novel_text = novel_string.hayabusa()
    trimmed = novel_string.remove_symbols(novel_text)

    string = 'あなた'

    picked = search_keyword(string, trimmed)
    start = picked.start()
    end = picked.end()

    tankaText = trimmed[start:start+31]

    semitoneStr = 'ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ'
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = trimmed[start:start+31+semitoneCount]

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/index.html", context=context)

def run2(request):
    word = request.POST.get('word')

    novel_text = novel_string.hayabusa()
    trimmed = novel_string.remove_symbols(novel_text)

    string = word

    tankaText = novel_string.pick_text_by_keyword(string, trimmed)

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/index.html", context=context)

def run3(request):
    novel_text = novel_string.hayabusa()
    trimmed_text = novel_string.remove_symbols(novel_text)

    textCount = len(trimmed_text)
    randomNumber = (random.randint(0, textCount - 31))

    tankaText = trimmed_text[randomNumber:randomNumber + 31]

    semitoneStr = "ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ"
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = trimmed_text[randomNumber:randomNumber+31+semitoneCount]

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/index.html", context=context)

def hiragana(request):
    form = WordForm()
    word = novel_string.hayabusa_word()

    context = {
        'form': form,
        'word': word,
    }

    return render(request, "app/hiragana.html", context=context)

def hiragana2(request):
    form = WordForm()
    words = novel_string.hayabusa_words()

    context = {
        'form': form,
        'words': words,
    }

    return render(request, "app/hiragana2.html", context=context)
