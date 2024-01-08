from django.shortcuts import render
from django.http import HttpResponse

import random
import re

def index(request):
    return render(request, "app/index.html", context=None)

def run3(request):
    text = """
    ハヤブサをおもいうかべてください。そらをかけぬけて、かぜをうけ、それでもやはりそらをきりさくハヤブサです。ものすごいかいかんでしょう。ぼくはいま、ハヤブサになっています。あなたがしんじようがしんじまいが、ぼくにはどうでもいい。あるのはぼくがハヤブサになったということだけです。

    ぼくはハヤブサになってトンネルをぬけました。そらがきんいろにかがやいています。よくみると、それはすべて、ほどよくそらにかかるくもでした。きんいろのたいようがくもをてらし、あたりいちめんをきんいろのせかいへとかえています。
    ふとよこをみると、いちわ、ハヤブサがとんでいるようです。むこうもぼくにきづきました。
    「あのきんいろのくもがみえますか？　ぼくはいまからあそこまでとんでいこうとおもっています。」
    「キレイですね、くもはふあんで、かなしみとさみしさだというのに、キレイですね。」
    「くもは……。そうですね。くもはいつもそうです。でもいまはきんいろですよ。せっかくですから、いっしょにとんでいきませんか？」
    「いいですよ。でも、そのまえに、まえにあるトンネルを、あそこをいちどとおってもいいですか？」
    「いいですよ。ぼくもトンネルはすきです。」
    トンネルはあおでした。なにもかもをかんつうしてしまうあおです。
    「きみはトンネルがすきなのですか？」
    「ええ、いや、さきほどあなたがトンネルからでてきたすがたがあまりにすきとおっていて、はいってみたくなりました。」
    「なるほど。おお。ありがとうございます。」
    このトンネルはすこしながいようです。
    トンネルにはむすうのひかりがあり、まるで、なんでしょう、どこかでみたことがあるようなきがするのですが、それがなんなのかわかりません。
    「トンネルはなにかににていませんか？」
    「ちょうどわたしもおなじことをかんがえていました。なんでしょうね。」
    「なんでしょう。」

    「あの、あなたとははじめてあったのに、みょうにあんしんしますね。なにか、どこかおなじねっこをもつようで……。」
    「うれしいです。ぼくもきみといるとあんしんするみたいです。」
    「わたしもあなたも、こころがぬまのようなかんじがします。どうですか？」
    「ぬま……。そうかもしれません。うん。たしかにぬまのようですね。」
    トンネルはまだつづいています。すこしカーブしているようです。ぶつからないように、けれどスピードをおとさず。

    「あ！」
    「どうしました？」
    「トンネルは、こいのようじゃないですか？」
    「こい。」
    「はい、どこかでみたことがあるきがしたのは、それがりゆうなきがして……。」
    ぼくはまんぞくして、すこしスピードをあげてみました。
    うしろからこえがしました。
    「わたしも。わたしもそんなきがしてきました。トンネルはこいににていますね。」
    ぼくたちはふたたびならんでとびはじめました。
    しばらくして、トンネルのでぐちがみえてきました。

    あかいそら。まっかなそらです。きんいろのそらはどこかへいってしまいました。
    「ごめんなさい。わたしがトンネルにはいりたいといったばかりに……。」
    「いいんです。あかいそらもすごくすてきだ。」
    たいようはみえません。でも、おそらくこのあかはたいようのあかでしょう。とてもあたたかくて、ぼくのさみしいところによくとどくから。
    「わたし、これまであおいそらばかりをみてきました。きんいろのそらも、あかいそらも、はじめてです。」
    「ぼくもですよ。ほんとうにきれいですね。」
    「いままたあおいそらをみたら、これまでとちがってみえるのでしょうか。」
    「どうなんでしょう。でも、みつけたら、ぜひいっしょにみましょうよ。きみのかんそうがききたいです。」
    「いいですね。わたしもあなたのかんそうがききたいです。」

    「またトンネルがありますね。」
    「はいりますか？」
    「きみはどうです？」
    「やっぱりはいってみたいです。」
    「じゃあ、いきましょう！」
    こんどのトンネルは、だいだいいろです。どこまでもつづくさばくのような、どんなかこもいまもうけいれてくれそうな、そんなだいだいいろです。
    「このトンネルは、こいとはまたちがいますね。」
    「そうですね。それにさっきとちがって、はじめてのきぶんです。」
    「わたしもはじめてのきぶんです。でもどこか、どこかでふれたこともあるような、そんなきがします。」
    「どこでしょうね。」
    「どこでしょう。」
    こんどのトンネルは、みるところがおくであればあるほど、ひろがっていくようにみえました。でも、きのせいのようです。トンネルのおおきさはずっとおなじです。それでもやはり、とおくをみると、ひろがっていくようにみえます。だいだいいろのせいでしょうか。

    ぼくたちは、あまりはなさず、さっきよりもすこしおそいそくどでとびつづけました。

    ずっととびつづけていましたが、やはりさいごまでトンネルのおおきさはかわりませんでした。
    そとはまっくらです。
    「トンネルをぬけましたね。」
    「そうですね。まっくらですね。」
    「これだと、そらがどこにあるのかもわかりませんね。」
    「ええ。こんなにまっくらなところも、はじめてきました。」
    「ぼくもです。」
    「すこしこわいですね。」
    「すこし、おはなをしながらとびましょうか。」
    「ええ。ありがとうございます。」
    「あの、むかし、ぼくにはねこのともだちがいました。かれはいつもスズメをつかまえてあそんでいました。そしてぼくのところにつかまえたスズメをもってきては、こころからうれしそうな、そしてほめてほしそうなめでこっちをみてくるのです。ぼくはほんとうはスズメなんていらなかったのですが、かれのあまりのむくにいつもまけ、ありがとうといってもらっていました。」
    「かれはそこなしにげんきでした。いつでもあそびをもとめていて、スズメがみあたらないときは、どのつよいメガネをかけてあそんでいました。めのちいさくなったかれは、ともだちだというのになんだかいとおしく、かれがしぬまでそのままであってほしいとさえおもっていました。」
    「あるひ、かれはたびにでるといいだしました。いつものあそびのえんちょうかとおもいましたが、かれはねんいりにたびのけいかくをたてているようでした。ぼくはとてもさみしかった。かれとはなれることよりも、かれがたびにけいかくをもとめたことが、です。しばらくして、かれはたびにでました。それから、かれとはあっていません。」
    「ぼくはなによりも、かれのよこにぼくがいないことをかなしみました。あれだけのむくのとなりのせきは、ずっとすわっていてこそかちがあるようにおもってしまうのです。なさけないことだとおもいます。でも、ぼくらはそうおもってしまうものじゃないですか？　きみはこのきもちがわかりますか？」
    ぼくのしつもんにたいするへんじはありませんでした。
    くらやみが、いちだんとふかくなったようにおもいます。ぼくはいま、たぶん、ひとりぼっちにもどりました。とんでいるのかもわかりません。
    すべてがやみにのみこまれていくようです。
    あのひとは、そしてぼくは、どこへ……。


    """

    # kakasi = kakasi()
    # # モードの設定：J(Kanji) to H(Hiragana)
    # kakasi.setMode('J', 'H')
    # conv = kakasi.getConverter()
    # novelText = (conv.do(text))
    novelText = text
    trimedText = novelText.replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("\n", "").replace(" ", "").replace("？", "").replace("?", "").replace("　", "").replace("…", "").replace("！", "")
    textCount = len(trimedText)
    randomNumber = (random.randint(0, textCount - 31))
    tankaText = trimedText[randomNumber:randomNumber + 31]
    semitoneStr = "ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ"
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = trimedText[randomNumber:randomNumber+31+semitoneCount]

    index = 0
    termOne = tankaText[index:index+5]
    semitoneCountOne = len(re.findall(semitoneStr, termOne))
    termOne = tankaText[index:index+5+semitoneCountOne]

    index = index+5+semitoneCountOne
    termTwo = tankaText[index:index+7]
    semitoneCountTwo = len(re.findall(semitoneStr, termTwo))
    termTwo = tankaText[index:index+7+semitoneCountTwo]

    index = index+7+semitoneCountTwo
    termThree = tankaText[index:index+5]
    semitoneCountThree = len(re.findall(semitoneStr, termThree))
    termThree = tankaText[index:index+5+semitoneCountThree]

    index = index+5+semitoneCountThree
    termFour = tankaText[index:index+7]
    semitoneCountFour = len(re.findall(semitoneStr, termFour))
    termFour = tankaText[index:index+7+semitoneCountFour]

    index = index+7+semitoneCountFour
    termFive = tankaText[index:index+7]
    semitoneCountFive = len(re.findall(semitoneStr, termFive))
    termFive = tankaText[index:index+7+semitoneCountFive]
    # print(trimedText)
    # print(textCount)
    # print(randomNumber)
    # print(tankaText)
    print(termOne)
    print(termTwo)
    print(termThree)
    print(termFour)
    print(termFive)

    context = {
        "termOne": termOne,
        "termTwo": termTwo,
        "termThree": termThree,
        "termFour": termFour,
        "termFive": termFive,
    }

    return render(request, "app/index.html", context=context)