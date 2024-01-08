import re
import random

def remove_symbols(novel_text) :
    trimmed_text = novel_text.replace("、", "").replace("。", "").replace("「", "").replace("」", "").replace("\n", "").replace(" ", "").replace("？", "").replace("?", "").replace("　", "").replace("…", "").replace("!", "").replace("！", "")
    return trimmed_text

def search_keyword(string, text):
    hits = re.finditer(string, text)
    result = []
    for i in hits:
        result.append(i)
    random.shuffle(result)
    return result[0]

def pick_text_by_keyword(string, text) :
    picked = search_keyword(string, text)
    start = picked.start()
    end = picked.end()

    randomNumber = random.randint(end - 31, start)
    tankaText = text[randomNumber:randomNumber+31]

    semitoneStr = 'ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ'
    semitoneCount = len(re.findall(semitoneStr, tankaText))

    tankaText = text[randomNumber:randomNumber+31+semitoneCount]

    return tankaText

def split_five_seven_five(tankaText):
    semitoneStr = "ぁ|ぃ|ぅ|ぇ|ぉ|ゃ|ゅ|ょ|ァ|ィ|ゥ|ェ|ォ|ャ|ュ|ョ"

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

    return {
        "termOne": termOne,
        "termTwo": termTwo,
        "termThree": termThree,
        "termFour": termFour,
        "termFive": termFive,
    }

def hayabusa():
    return """
    ハヤブサをおもいうかべてください。そらをかけぬけて、かぜをうけ、それでもやはりそらをきりさくハヤブサです。ものすごいかいかんでしょう。ぼくはいま、ハヤブサになっています。あなたがしんじようがしんじまいが、ぼくにはどうでもいい。あるのはぼくがハヤブサになったということだけです。
    ぼくはハヤブサになってトンネルをぬけました。そらがきんいろにかがやいています。よくみると、それはすべて、ほどよくそらにかかるくもでした。きんいろのたいようがくもをてらし、あたりいちめんをきんいろのせかいへとかえています。
    ふとよこをみると、いちわ、ハヤブサがとんでいるようです。むこうもぼくにきづきました。
    「あのきんいろのくもがみえますか？ぼくはいまからあそこまでとんでいこうとおもっています。」
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
