from django.shortcuts import render
from django.http import HttpResponse
from app.modules import novel_string
from app.forms import WordForm
from pathlib import Path

import random
import re
import os

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

    tankaText = novel_string.pick_text_by_keyword2(string, trimmed)

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/result.html", context=context)

def run3(request):
    click_count = request.POST.get('click_count')

    if click_count == None:
        click_count = 0
    else:
        try:
            click_count = int(click_count)
        except ValueError:
            click_count = 0

    novel_text = novel_string.hayabusa()
    trimmed_text = novel_string.remove_symbols(novel_text)

    textCount = len(trimmed_text)
    randomNumber = (random.randint(0, textCount - 31))

    tankaText = trimmed_text[randomNumber:randomNumber + 31]

    semitoneStr = "ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ"
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = trimmed_text[randomNumber:randomNumber+31+semitoneCount]

    context = novel_string.split_five_seven_five(tankaText)

    context['click_count'] = click_count + 1

    return render(request, "app/result.html", context=context)

def run4(request):
    word = request.POST.get('word')

    novel_text = novel_string.hayabusa()
    trimmed = novel_string.remove_symbols(novel_text)

    string = word

    tankaText = novel_string.pick_text_by_keyword(string, trimmed)

    context = novel_string.split_five_seven_five(tankaText)

    return render(request, "app/result.html", context=context)

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

# import json

def runx(request):
    # text = novel_string.kissaten()
    # # keyword = ["テーブル", "鞄", "喫茶店", "固定", "危", "移動", "香水"]
    # # color = ["#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])]
    # # print_hl(text, keyword, color)
    # context = json.loads(text)

    return render(request, "app/runx1.html")

# class pycolor:
# def print_hl(text, keyword, color):
#     for kw in keyword:
#         bef = kw
#         aft = color + kw + color["end"]
#         text = re.sub(bef, aft, text)
#     print(text)

def runx2(request):
    return render(request, "app/runx2.html")

def runx3(request):
    return render(request, "app/runx3.html")
