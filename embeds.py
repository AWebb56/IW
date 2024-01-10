from fugashi import Tagger
import csv
from gensim import models
import stops
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from matplotlib import pyplot as plt
import matplotlib.font_manager as fm
fprop = fm.FontProperties(fname='text\\NotoSansJP-VariableFont_wght.ttf')
tagger = Tagger('-Owakati -u mydic.dic')
sents = []
stops = test5.STOP_WORDS
count1 = 0
count2 = 0
count3 = 0
count4 = 0
sents1 = []
jpmin = 11111111
jpmax = 0
enmin = 1111111111
enmax = 0
lemmatizer = WordNetLemmatizer()
dictsjp = {}
dictsjen= {}

with open("jptweets1.csv", "r", encoding='utf-8') as file:
    for test in file:
        count1 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = tagger(text)
        sent = []
        sentcount = 0
        for word in tag:
            if str(word.feature.lemma) not in stops and word != '　' and str(word) not in stops:
                sent.append(str(word))
                count2 +=1
                sentcount +=1
                if str(word) in dictsjp:
                    dictsjp[str(word)] += 1
                else:
                    dictsjp[str(word)] = 1
        sents.append(sent)
        if sentcount > jpmax:
            jpmax = sentcount
        if sentcount < jpmin:
            jpmin = sentcount
with open("jptweets2.csv", "r", encoding='utf-8') as file:
    for test in file:
        count1 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = tagger(text)
        sent = []
        sentcount = 0
        for word in tag:
            if str(word.feature.lemma) not in stops and word != '　' and str(word) not in stops:
                sent.append(str(word))
                count2 +=1
                sentcount +=1
                if str(word) in dictsjp:
                    dictsjp[str(word)] += 1
                else:
                    dictsjp[str(word)] = 1
        sents.append(sent)
        if sentcount > jpmax:
            jpmax = sentcount
        if sentcount < jpmin:
            jpmin = sentcount
with open("jptweets3.csv", "r", encoding='utf-8') as file:
    for test in file:
        count1 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = tagger(text)
        sent = []
        sentcount = 0
        for word in tag:
            if str(word.feature.lemma) not in stops and word != '　' and str(word) not in stops:
                sent.append(str(word))
                count2 +=1
                sentcount +=1
                if str(word) in dictsjp:
                    dictsjp[str(word)] += 1
                else:
                    dictsjp[str(word)] = 1
        sents.append(sent)
        if sentcount > jpmax:
            jpmax = sentcount
        if sentcount < jpmin:
            jpmin = sentcount
with open("jptweets4.csv", "r", encoding='utf-8') as file:
    for test in file:
        count1 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = tagger(text)
        sent = []
        sentcount = 0
        for word in tag:
            if str(word.feature.lemma) not in stops and word != '　' and str(word) not in stops:
                sent.append(str(word))
                count2 +=1
                sentcount +=1
                if str(word) in dictsjp:
                    dictsjp[str(word)] += 1
                else:
                    dictsjp[str(word)] = 1
        sents.append(sent)
        if sentcount > jpmax:
            jpmax = sentcount
        if sentcount < jpmin:
            jpmin = sentcount
print(count2/count1)
print(count2)
print(jpmax)
print(jpmin)
srtjp = dict(sorted(dictsjp.items(), key=lambda item: item[1]))
keysjp = list(srtjp.keys())[::-1]
plts = []
for i in range(50):
    plts.append(srtjp[keysjp[i]])
plt.bar(range(50),plts)
plt.xticks(range(50),keysjp[:50],fontproperties=fprop, rotation=90)
plt.title("Japanese Word Frequency")
plt.xlabel("Japanese Word")
plt.ylabel("Frequency")
plt.show()
print(keysjp[:100])
with open("entweets1.csv", "r", encoding='utf-8') as file:
    for test in file:
        count3 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = word_tokenize(text)
        sent = []
        sentcount = 0
        for word in tag:
            word = str(lemmatizer.lemmatize(word))
            if word.lower() not in stops:
                if not str(word).isalpha():
                    if re.search(r"[💯💤🗨🗯💭💣💬💨👶🏿🕳🧒🏻🏼🏽🏾👦👧🧑👱👨🧔♂🦰🦱🦳🦲👩♀🧓👴👵🙍🙎🙅🙆💁🙋🧏🙇🤦🤷⚕🎓🏫⚖🌾🍳🔧🏭💼🔬💻🎤🎨✈🚀🚒👮🕵💂👷🤴👸👳🧕🤵👰🤰🤱👼🎅🤶🦸🦹🧙🧚🧛🧜🧝🧞🧟💆💇🚶🧍🧎🦯🦼🦽🏃💃🕺🕴👯🧖🧗🤺🏇⛷🏂🏌🏄🚣🏊⛹🏋🚴🚵🤸🤼🤽🤾🤹🧘🛀🛌🤝👭👫👬💏❤💋💑👪🗣👤👥👣🐵🐒🦍🦧🐶🐕🦮🦺🐩🐺🦊🦝🐱🐈🦁🐯🐅🐆🐴🐎🦄🦓🦌🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🦙🦒🐘🦏🦛🐭🐁🐀🐹🐰🐇🐿🦔🦇🐻🐨🐼🦥🦦🦨🦘🦡🐾🦃🐔🐓🐣🐤🐥🐦🐧🕊🦅🦆🦢🦉🦩🦚🦜🐸🐊🐢🦎🐍🐲🐉🦕🦖🐳🐋🐬🐟🐠🐡🦈🐙🐚🐌🦋🐛🐜🐝🐞🦗🕷🕸🦂🦟🦠💐🌸💮🏵🌹🥀🌺🌻🌼🌷🌱🌲🌳🌴🌵🌿☘🍀🍁🍂🍃🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🌶🥒🥬🥦🧄🧅🍄🥜🌰🍞🥐🥖🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🥙🧆🥚🥘🍲🥣🥗🍿🧈🧂🥫🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🥮🍡🥟🥠🥡🦀🦞🦐🦑🦪🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧃🧉🥢🍽🍴🥄🔪🏺🌍🌎🌏🌐🗺🗾🧭🏔⛰🌋🗻🏕🏖🏜🏝🏞🏟🏛🏗🧱🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏬🏯🏰💒🗼🗽⛪🕌🛕🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉♨🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🏎🏍🛵🛺🚲🛴🛹🚏🛣🛤🛢⛽🚨🚥🚦🛑🚧⚓⛵🛶🚤🛳⛴🛥🚢🛩🛫🛬🪂💺🚁🚟🚠🚡🛰🛸🛎🧳⌛⏳⌚⏰⏱⏲🕰🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌡☀🌝🌞🪐⭐🌟🌠🌌☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄☄🔥💧🌊🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫🎖🏆🏅🥇🥈🥉⚽⚾🥎🏀🏐🏈🏉🎾🥏🎳🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸🎣🤿🎽🎿🛷🥌🎯🪀🪁🎱🔮🧿🎮🕹🎰🎲🧩🧸♠♥♦♣♟🃏🀄🎴🎭🖼🧵🧶👓🕶🥼👔👕🧣🧥🧦👗👘🥻🩱🩳👙👚👛👜👝🛍🎒👞👟🥾🥿👠👡🩰👢👑👒🎩🧢⛑📿💄💍💎🔇🔈🔉🔊📢📣📯🔔🔕🎼🎵🎶🎙🎚🎛🎧📻🎷🎸🎹🎺🎻🪕🥁📱📲☎📞📟📠🔋🔌🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎞📽🎬📺📷📸📹📼🔍🔎🕯💡🔦🏮🪔📔📕📖📗👁📘📙📚📓📒📃📜📄📰🗞📑🔖🏷💰💴💵💶💷💸💳🧾💹💱💲✉📧📨📩📤📥📦📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝📁📂🗂📅📆🗒🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑🔒🔓🔏🔐🔑🗝🔨🪓⛏⚒🛠🗡⚔🔫🏹🛡🔩⚙🗜🔗⛓🧰🧲⚗🧪🧫🧬🔭📡💉🩸💊🩹🩺🚪🛏🛋🪑🚽🚿🛁🪒🧴🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰⚱🗿🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅⚠🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢☣⬆↗➡↘⬇↙⬅↖↕↔↩↪⤴⤵🔃🔄🔙🔚🔛🔜🔝🛐⚛🕉✡☸☯✝☦☪☮🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂▶⏩⏭⏯◀⏪⏮🔼⏫🔽⏬⏸⏹⏺⏏🎦🔅🔆📶📳📴♾♻⚜🔱📛💢🔰⭕✅☑✔✖❌❎➕➖➗➰➿〽✳✴❇‼⁉❓❔❕❗〰©®™#⃣*🔟🔠🔡🔢🔣🔤🅰🆎🅱🆑🆒🆓ℹ🆔Ⓜ🆕🆖🅾🆗🅿🆘🆙🆚🈁🈂🈷🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳㊗㊙🈺🈵🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔷🔸🔹🔺🔻💠🔘🔳🔲🏁🚩🎌🏴🏳☠🇦🇨🇩🇪🇫🇮🇱🇲🇴🇶🇷🇸🇹🇺🇼🇽Å🇿🇧🇬🇭🇯é🇳🇻🇾ô🇰🇵ç😀😃😄😁😆😅🤣😂🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙😋😛😜🤪😝🤑🤗🤭🤫🤔🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪🤤😴😷🤒🤕🤢🤮🤧🥵🥶🥴😵🤯🤠🥳😎🤓🧐😕😟🙁☹😮😯😲😳🥺😦😧😨😰😥😢😭😱😖😣😞😓😩😫🥱😤😡😠🤬😈👿💀💩🤡👹👺👻👽👾🤖😺😸😹😻😼😽🙀😿😾🙈🙉🙊💌💘💝💓💞💕💟❣💔🧡💛💚💙💜🤎🖤🤍💥💫💦👋🤚🖐✋🖖👌🤏✌🤞🤟🤘🤙👈👉👆🖕👇☝👍👎✊👊🤛🤜👏🙌👐🤲🙏✍💅🤳💪🦾🦿🦵🦶👂🦻👃🧠🦷🦴👀👅👄💗💖🥽🧤👖🧊🩲👲🥲🫠🫢🫣🫡🫥🥸🥹🫤🫱🫲🫳🤌🫴🫰🫵🫀🫁🫦🧋🪸🪞🥷🪷🦭🪨🪙🪳🪃🧌🦬🪵🫘🛞🫕🦫🪪🫧🪰🪱🪲🪜🪝🪣🦣🫒🪟🫙🛗🫐🪶🪛🛖🫑🪤🪢🪠🛻🫖⚧🪬🫔🪅ñ🫓🩻🪄🪥🪗🛼🩼🪫🪹🪦🪆🪡🪩🪴🪖🛝🫂🛟🩴🫗🪺🪚🪘🫅🟰]", word):
                        word = re.sub(r'[a-zA-Z0-9.]', "", word)
                        for words in word:
                            sent.append(str(words))
                            count4 +=1
                            sentcount +=1
                            if str(word) in dictsjen:
                                dictsjen[str(word)] += 1
                            else:
                                dictsjen[str(word)] = 1
                else:
                    sent.append(str(lemmatizer.lemmatize(word)).lower())
                    count4 +=1
                    sentcount +=1
                    if str(word) in dictsjen:
                        dictsjen[str(word)] += 1
                    else:
                        dictsjen[str(word)] = 1
        sents1.append(sent)
        if sentcount > enmax:
            enmax = sentcount
        if sentcount < enmin:
            enmin = sentcount
with open("entweets2.csv", "r", encoding='utf-8') as file:
    for test in file:
        count3 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = word_tokenize(text)
        sent = []
        sentcount = 0
        for word in tag:
            word = str(lemmatizer.lemmatize(word))
            if word.lower() not in stops:
                if not str(word).isalpha():
                    if re.search(r"[💯💤🗨🗯💭💣💬💨👶🏿🕳🧒🏻🏼🏽🏾👦👧🧑👱👨🧔♂🦰🦱🦳🦲👩♀🧓👴👵🙍🙎🙅🙆💁🙋🧏🙇🤦🤷⚕🎓🏫⚖🌾🍳🔧🏭💼🔬💻🎤🎨✈🚀🚒👮🕵💂👷🤴👸👳🧕🤵👰🤰🤱👼🎅🤶🦸🦹🧙🧚🧛🧜🧝🧞🧟💆💇🚶🧍🧎🦯🦼🦽🏃💃🕺🕴👯🧖🧗🤺🏇⛷🏂🏌🏄🚣🏊⛹🏋🚴🚵🤸🤼🤽🤾🤹🧘🛀🛌🤝👭👫👬💏❤💋💑👪🗣👤👥👣🐵🐒🦍🦧🐶🐕🦮🦺🐩🐺🦊🦝🐱🐈🦁🐯🐅🐆🐴🐎🦄🦓🦌🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🦙🦒🐘🦏🦛🐭🐁🐀🐹🐰🐇🐿🦔🦇🐻🐨🐼🦥🦦🦨🦘🦡🐾🦃🐔🐓🐣🐤🐥🐦🐧🕊🦅🦆🦢🦉🦩🦚🦜🐸🐊🐢🦎🐍🐲🐉🦕🦖🐳🐋🐬🐟🐠🐡🦈🐙🐚🐌🦋🐛🐜🐝🐞🦗🕷🕸🦂🦟🦠💐🌸💮🏵🌹🥀🌺🌻🌼🌷🌱🌲🌳🌴🌵🌿☘🍀🍁🍂🍃🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🌶🥒🥬🥦🧄🧅🍄🥜🌰🍞🥐🥖🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🥙🧆🥚🥘🍲🥣🥗🍿🧈🧂🥫🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🥮🍡🥟🥠🥡🦀🦞🦐🦑🦪🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧃🧉🥢🍽🍴🥄🔪🏺🌍🌎🌏🌐🗺🗾🧭🏔⛰🌋🗻🏕🏖🏜🏝🏞🏟🏛🏗🧱🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏬🏯🏰💒🗼🗽⛪🕌🛕🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉♨🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🏎🏍🛵🛺🚲🛴🛹🚏🛣🛤🛢⛽🚨🚥🚦🛑🚧⚓⛵🛶🚤🛳⛴🛥🚢🛩🛫🛬🪂💺🚁🚟🚠🚡🛰🛸🛎🧳⌛⏳⌚⏰⏱⏲🕰🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌡☀🌝🌞🪐⭐🌟🌠🌌☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄☄🔥💧🌊🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫🎖🏆🏅🥇🥈🥉⚽⚾🥎🏀🏐🏈🏉🎾🥏🎳🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸🎣🤿🎽🎿🛷🥌🎯🪀🪁🎱🔮🧿🎮🕹🎰🎲🧩🧸♠♥♦♣♟🃏🀄🎴🎭🖼🧵🧶👓🕶🥼👔👕🧣🧥🧦👗👘🥻🩱🩳👙👚👛👜👝🛍🎒👞👟🥾🥿👠👡🩰👢👑👒🎩🧢⛑📿💄💍💎🔇🔈🔉🔊📢📣📯🔔🔕🎼🎵🎶🎙🎚🎛🎧📻🎷🎸🎹🎺🎻🪕🥁📱📲☎📞📟📠🔋🔌🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎞📽🎬📺📷📸📹📼🔍🔎🕯💡🔦🏮🪔📔📕📖📗👁📘📙📚📓📒📃📜📄📰🗞📑🔖🏷💰💴💵💶💷💸💳🧾💹💱💲✉📧📨📩📤📥📦📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝📁📂🗂📅📆🗒🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑🔒🔓🔏🔐🔑🗝🔨🪓⛏⚒🛠🗡⚔🔫🏹🛡🔩⚙🗜🔗⛓🧰🧲⚗🧪🧫🧬🔭📡💉🩸💊🩹🩺🚪🛏🛋🪑🚽🚿🛁🪒🧴🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰⚱🗿🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅⚠🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢☣⬆↗➡↘⬇↙⬅↖↕↔↩↪⤴⤵🔃🔄🔙🔚🔛🔜🔝🛐⚛🕉✡☸☯✝☦☪☮🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂▶⏩⏭⏯◀⏪⏮🔼⏫🔽⏬⏸⏹⏺⏏🎦🔅🔆📶📳📴♾♻⚜🔱📛💢🔰⭕✅☑✔✖❌❎➕➖➗➰➿〽✳✴❇‼⁉❓❔❕❗〰©®™#⃣*🔟🔠🔡🔢🔣🔤🅰🆎🅱🆑🆒🆓ℹ🆔Ⓜ🆕🆖🅾🆗🅿🆘🆙🆚🈁🈂🈷🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳㊗㊙🈺🈵🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔷🔸🔹🔺🔻💠🔘🔳🔲🏁🚩🎌🏴🏳☠🇦🇨🇩🇪🇫🇮🇱🇲🇴🇶🇷🇸🇹🇺🇼🇽Å🇿🇧🇬🇭🇯é🇳🇻🇾ô🇰🇵ç😀😃😄😁😆😅🤣😂🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙😋😛😜🤪😝🤑🤗🤭🤫🤔🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪🤤😴😷🤒🤕🤢🤮🤧🥵🥶🥴😵🤯🤠🥳😎🤓🧐😕😟🙁☹😮😯😲😳🥺😦😧😨😰😥😢😭😱😖😣😞😓😩😫🥱😤😡😠🤬😈👿💀💩🤡👹👺👻👽👾🤖😺😸😹😻😼😽🙀😿😾🙈🙉🙊💌💘💝💓💞💕💟❣💔🧡💛💚💙💜🤎🖤🤍💥💫💦👋🤚🖐✋🖖👌🤏✌🤞🤟🤘🤙👈👉👆🖕👇☝👍👎✊👊🤛🤜👏🙌👐🤲🙏✍💅🤳💪🦾🦿🦵🦶👂🦻👃🧠🦷🦴👀👅👄💗💖🥽🧤👖🧊🩲👲🥲🫠🫢🫣🫡🫥🥸🥹🫤🫱🫲🫳🤌🫴🫰🫵🫀🫁🫦🧋🪸🪞🥷🪷🦭🪨🪙🪳🪃🧌🦬🪵🫘🛞🫕🦫🪪🫧🪰🪱🪲🪜🪝🪣🦣🫒🪟🫙🛗🫐🪶🪛🛖🫑🪤🪢🪠🛻🫖⚧🪬🫔🪅ñ🫓🩻🪄🪥🪗🛼🩼🪫🪹🪦🪆🪡🪩🪴🪖🛝🫂🛟🩴🫗🪺🪚🪘🫅🟰]", word):
                        word = re.sub(r'[a-zA-Z0-9.]', "", word)
                        for words in word:
                            sent.append(str(words))
                            count4 +=1
                            sentcount +=1
                            if str(word) in dictsjen:
                                dictsjen[str(word)] += 1
                            else:
                                dictsjen[str(word)] = 1
                else:
                    sent.append(str(lemmatizer.lemmatize(word)).lower())
                    count4 +=1
                    sentcount +=1
                    if str(word) in dictsjen:
                        dictsjen[str(word)] += 1
                    else:
                        dictsjen[str(word)] = 1
        sents1.append(sent)
        if sentcount > enmax:
            enmax = sentcount
        if sentcount < enmin:
            enmin = sentcount
with open("entweets3.csv", "r", encoding='utf-8') as file:
    for test in file:
        count3 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = word_tokenize(text)
        sent = []
        sentcount = 0
        for word in tag:
            word = str(lemmatizer.lemmatize(word))
            if word.lower() not in stops:
                if not str(word).isalpha():
                    if re.search(r"[💯💤🗨🗯💭💣💬💨👶🏿🕳🧒🏻🏼🏽🏾👦👧🧑👱👨🧔♂🦰🦱🦳🦲👩♀🧓👴👵🙍🙎🙅🙆💁🙋🧏🙇🤦🤷⚕🎓🏫⚖🌾🍳🔧🏭💼🔬💻🎤🎨✈🚀🚒👮🕵💂👷🤴👸👳🧕🤵👰🤰🤱👼🎅🤶🦸🦹🧙🧚🧛🧜🧝🧞🧟💆💇🚶🧍🧎🦯🦼🦽🏃💃🕺🕴👯🧖🧗🤺🏇⛷🏂🏌🏄🚣🏊⛹🏋🚴🚵🤸🤼🤽🤾🤹🧘🛀🛌🤝👭👫👬💏❤💋💑👪🗣👤👥👣🐵🐒🦍🦧🐶🐕🦮🦺🐩🐺🦊🦝🐱🐈🦁🐯🐅🐆🐴🐎🦄🦓🦌🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🦙🦒🐘🦏🦛🐭🐁🐀🐹🐰🐇🐿🦔🦇🐻🐨🐼🦥🦦🦨🦘🦡🐾🦃🐔🐓🐣🐤🐥🐦🐧🕊🦅🦆🦢🦉🦩🦚🦜🐸🐊🐢🦎🐍🐲🐉🦕🦖🐳🐋🐬🐟🐠🐡🦈🐙🐚🐌🦋🐛🐜🐝🐞🦗🕷🕸🦂🦟🦠💐🌸💮🏵🌹🥀🌺🌻🌼🌷🌱🌲🌳🌴🌵🌿☘🍀🍁🍂🍃🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🌶🥒🥬🥦🧄🧅🍄🥜🌰🍞🥐🥖🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🥙🧆🥚🥘🍲🥣🥗🍿🧈🧂🥫🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🥮🍡🥟🥠🥡🦀🦞🦐🦑🦪🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧃🧉🥢🍽🍴🥄🔪🏺🌍🌎🌏🌐🗺🗾🧭🏔⛰🌋🗻🏕🏖🏜🏝🏞🏟🏛🏗🧱🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏬🏯🏰💒🗼🗽⛪🕌🛕🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉♨🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🏎🏍🛵🛺🚲🛴🛹🚏🛣🛤🛢⛽🚨🚥🚦🛑🚧⚓⛵🛶🚤🛳⛴🛥🚢🛩🛫🛬🪂💺🚁🚟🚠🚡🛰🛸🛎🧳⌛⏳⌚⏰⏱⏲🕰🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌡☀🌝🌞🪐⭐🌟🌠🌌☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄☄🔥💧🌊🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫🎖🏆🏅🥇🥈🥉⚽⚾🥎🏀🏐🏈🏉🎾🥏🎳🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸🎣🤿🎽🎿🛷🥌🎯🪀🪁🎱🔮🧿🎮🕹🎰🎲🧩🧸♠♥♦♣♟🃏🀄🎴🎭🖼🧵🧶👓🕶🥼👔👕🧣🧥🧦👗👘🥻🩱🩳👙👚👛👜👝🛍🎒👞👟🥾🥿👠👡🩰👢👑👒🎩🧢⛑📿💄💍💎🔇🔈🔉🔊📢📣📯🔔🔕🎼🎵🎶🎙🎚🎛🎧📻🎷🎸🎹🎺🎻🪕🥁📱📲☎📞📟📠🔋🔌🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎞📽🎬📺📷📸📹📼🔍🔎🕯💡🔦🏮🪔📔📕📖📗👁📘📙📚📓📒📃📜📄📰🗞📑🔖🏷💰💴💵💶💷💸💳🧾💹💱💲✉📧📨📩📤📥📦📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝📁📂🗂📅📆🗒🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑🔒🔓🔏🔐🔑🗝🔨🪓⛏⚒🛠🗡⚔🔫🏹🛡🔩⚙🗜🔗⛓🧰🧲⚗🧪🧫🧬🔭📡💉🩸💊🩹🩺🚪🛏🛋🪑🚽🚿🛁🪒🧴🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰⚱🗿🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅⚠🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢☣⬆↗➡↘⬇↙⬅↖↕↔↩↪⤴⤵🔃🔄🔙🔚🔛🔜🔝🛐⚛🕉✡☸☯✝☦☪☮🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂▶⏩⏭⏯◀⏪⏮🔼⏫🔽⏬⏸⏹⏺⏏🎦🔅🔆📶📳📴♾♻⚜🔱📛💢🔰⭕✅☑✔✖❌❎➕➖➗➰➿〽✳✴❇‼⁉❓❔❕❗〰©®™#⃣*🔟🔠🔡🔢🔣🔤🅰🆎🅱🆑🆒🆓ℹ🆔Ⓜ🆕🆖🅾🆗🅿🆘🆙🆚🈁🈂🈷🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳㊗㊙🈺🈵🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔷🔸🔹🔺🔻💠🔘🔳🔲🏁🚩🎌🏴🏳☠🇦🇨🇩🇪🇫🇮🇱🇲🇴🇶🇷🇸🇹🇺🇼🇽Å🇿🇧🇬🇭🇯é🇳🇻🇾ô🇰🇵ç😀😃😄😁😆😅🤣😂🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙😋😛😜🤪😝🤑🤗🤭🤫🤔🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪🤤😴😷🤒🤕🤢🤮🤧🥵🥶🥴😵🤯🤠🥳😎🤓🧐😕😟🙁☹😮😯😲😳🥺😦😧😨😰😥😢😭😱😖😣😞😓😩😫🥱😤😡😠🤬😈👿💀💩🤡👹👺👻👽👾🤖😺😸😹😻😼😽🙀😿😾🙈🙉🙊💌💘💝💓💞💕💟❣💔🧡💛💚💙💜🤎🖤🤍💥💫💦👋🤚🖐✋🖖👌🤏✌🤞🤟🤘🤙👈👉👆🖕👇☝👍👎✊👊🤛🤜👏🙌👐🤲🙏✍💅🤳💪🦾🦿🦵🦶👂🦻👃🧠🦷🦴👀👅👄💗💖🥽🧤👖🧊🩲👲🥲🫠🫢🫣🫡🫥🥸🥹🫤🫱🫲🫳🤌🫴🫰🫵🫀🫁🫦🧋🪸🪞🥷🪷🦭🪨🪙🪳🪃🧌🦬🪵🫘🛞🫕🦫🪪🫧🪰🪱🪲🪜🪝🪣🦣🫒🪟🫙🛗🫐🪶🪛🛖🫑🪤🪢🪠🛻🫖⚧🪬🫔🪅ñ🫓🩻🪄🪥🪗🛼🩼🪫🪹🪦🪆🪡🪩🪴🪖🛝🫂🛟🩴🫗🪺🪚🪘🫅🟰]", word):
                        word = re.sub(r'[a-zA-Z0-9.]', "", word)
                        for words in word:
                            sent.append(str(words))
                            count4 +=1
                            sentcount +=1
                            if str(word) in dictsjen:
                                dictsjen[str(word)] += 1
                            else:
                                dictsjen[str(word)] = 1
                else:
                    sent.append(str(lemmatizer.lemmatize(word)).lower())
                    count4 +=1
                    sentcount +=1
                    if str(word) in dictsjen:
                        dictsjen[str(word)] += 1
                    else:
                        dictsjen[str(word)] = 1
        sents1.append(sent)
        if sentcount > enmax:
            enmax = sentcount
        if sentcount < enmin:
            enmin = sentcount
with open("entweets4.csv", "r", encoding='utf-8') as file:
    for test in file:
        count3 += 1
        test = test.split(',')
        if test == []:
            continue
        if len(test) > 2:
            test[0] = test[0].join(test[1:-1])
        text = test[0]
        tag = word_tokenize(text)
        sent = []
        sentcount = 0
        for word in tag:
            word = str(lemmatizer.lemmatize(word))
            if word.lower() not in stops:
                if not str(word).isalpha():
                    if re.search(r"[💯💤🗨🗯💭💣💬💨👶🏿🕳🧒🏻🏼🏽🏾👦👧🧑👱👨🧔♂🦰🦱🦳🦲👩♀🧓👴👵🙍🙎🙅🙆💁🙋🧏🙇🤦🤷⚕🎓🏫⚖🌾🍳🔧🏭💼🔬💻🎤🎨✈🚀🚒👮🕵💂👷🤴👸👳🧕🤵👰🤰🤱👼🎅🤶🦸🦹🧙🧚🧛🧜🧝🧞🧟💆💇🚶🧍🧎🦯🦼🦽🏃💃🕺🕴👯🧖🧗🤺🏇⛷🏂🏌🏄🚣🏊⛹🏋🚴🚵🤸🤼🤽🤾🤹🧘🛀🛌🤝👭👫👬💏❤💋💑👪🗣👤👥👣🐵🐒🦍🦧🐶🐕🦮🦺🐩🐺🦊🦝🐱🐈🦁🐯🐅🐆🐴🐎🦄🦓🦌🐮🐂🐃🐄🐷🐖🐗🐽🐏🐑🐐🐪🐫🦙🦒🐘🦏🦛🐭🐁🐀🐹🐰🐇🐿🦔🦇🐻🐨🐼🦥🦦🦨🦘🦡🐾🦃🐔🐓🐣🐤🐥🐦🐧🕊🦅🦆🦢🦉🦩🦚🦜🐸🐊🐢🦎🐍🐲🐉🦕🦖🐳🐋🐬🐟🐠🐡🦈🐙🐚🐌🦋🐛🐜🐝🐞🦗🕷🕸🦂🦟🦠💐🌸💮🏵🌹🥀🌺🌻🌼🌷🌱🌲🌳🌴🌵🌿☘🍀🍁🍂🍃🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🌶🥒🥬🥦🧄🧅🍄🥜🌰🍞🥐🥖🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🥙🧆🥚🥘🍲🥣🥗🍿🧈🧂🥫🍱🍘🍙🍚🍛🍜🍝🍠🍢🍣🍤🍥🥮🍡🥟🥠🥡🦀🦞🦐🦑🦪🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧃🧉🥢🍽🍴🥄🔪🏺🌍🌎🌏🌐🗺🗾🧭🏔⛰🌋🗻🏕🏖🏜🏝🏞🏟🏛🏗🧱🏘🏚🏠🏡🏢🏣🏤🏥🏦🏨🏩🏪🏬🏯🏰💒🗼🗽⛪🕌🛕🕍⛩🕋⛲⛺🌁🌃🏙🌄🌅🌆🌇🌉♨🎠🎡🎢💈🎪🚂🚃🚄🚅🚆🚇🚈🚉🚊🚝🚞🚋🚌🚍🚎🚐🚑🚓🚔🚕🚖🚗🚘🚙🚚🚛🚜🏎🏍🛵🛺🚲🛴🛹🚏🛣🛤🛢⛽🚨🚥🚦🛑🚧⚓⛵🛶🚤🛳⛴🛥🚢🛩🛫🛬🪂💺🚁🚟🚠🚡🛰🛸🛎🧳⌛⏳⌚⏰⏱⏲🕰🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜🌡☀🌝🌞🪐⭐🌟🌠🌌☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌬🌀🌈🌂☂☔⛱⚡❄☃⛄☄🔥💧🌊🎃🎄🎆🎇🧨✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎟🎫🎖🏆🏅🥇🥈🥉⚽⚾🥎🏀🏐🏈🏉🎾🥏🎳🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸🎣🤿🎽🎿🛷🥌🎯🪀🪁🎱🔮🧿🎮🕹🎰🎲🧩🧸♠♥♦♣♟🃏🀄🎴🎭🖼🧵🧶👓🕶🥼👔👕🧣🧥🧦👗👘🥻🩱🩳👙👚👛👜👝🛍🎒👞👟🥾🥿👠👡🩰👢👑👒🎩🧢⛑📿💄💍💎🔇🔈🔉🔊📢📣📯🔔🔕🎼🎵🎶🎙🎚🎛🎧📻🎷🎸🎹🎺🎻🪕🥁📱📲☎📞📟📠🔋🔌🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎞📽🎬📺📷📸📹📼🔍🔎🕯💡🔦🏮🪔📔📕📖📗👁📘📙📚📓📒📃📜📄📰🗞📑🔖🏷💰💴💵💶💷💸💳🧾💹💱💲✉📧📨📩📤📥📦📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝📁📂🗂📅📆🗒🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑🔒🔓🔏🔐🔑🗝🔨🪓⛏⚒🛠🗡⚔🔫🏹🛡🔩⚙🗜🔗⛓🧰🧲⚗🧪🧫🧬🔭📡💉🩸💊🩹🩺🚪🛏🛋🪑🚽🚿🛁🪒🧴🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰⚱🗿🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅⚠🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢☣⬆↗➡↘⬇↙⬅↖↕↔↩↪⤴⤵🔃🔄🔙🔚🔛🔜🔝🛐⚛🕉✡☸☯✝☦☪☮🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂▶⏩⏭⏯◀⏪⏮🔼⏫🔽⏬⏸⏹⏺⏏🎦🔅🔆📶📳📴♾♻⚜🔱📛💢🔰⭕✅☑✔✖❌❎➕➖➗➰➿〽✳✴❇‼⁉❓❔❕❗〰©®™#⃣*🔟🔠🔡🔢🔣🔤🅰🆎🅱🆑🆒🆓ℹ🆔Ⓜ🆕🆖🅾🆗🅿🆘🆙🆚🈁🈂🈷🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳㊗㊙🈺🈵🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔷🔸🔹🔺🔻💠🔘🔳🔲🏁🚩🎌🏴🏳☠🇦🇨🇩🇪🇫🇮🇱🇲🇴🇶🇷🇸🇹🇺🇼🇽Å🇿🇧🇬🇭🇯é🇳🇻🇾ô🇰🇵ç😀😃😄😁😆😅🤣😂🙂🙃😉😊😇🥰😍🤩😘😗☺😚😙😋😛😜🤪😝🤑🤗🤭🤫🤔🤐🤨😐😑😶😏😒🙄😬🤥😌😔😪🤤😴😷🤒🤕🤢🤮🤧🥵🥶🥴😵🤯🤠🥳😎🤓🧐😕😟🙁☹😮😯😲😳🥺😦😧😨😰😥😢😭😱😖😣😞😓😩😫🥱😤😡😠🤬😈👿💀💩🤡👹👺👻👽👾🤖😺😸😹😻😼😽🙀😿😾🙈🙉🙊💌💘💝💓💞💕💟❣💔🧡💛💚💙💜🤎🖤🤍💥💫💦👋🤚🖐✋🖖👌🤏✌🤞🤟🤘🤙👈👉👆🖕👇☝👍👎✊👊🤛🤜👏🙌👐🤲🙏✍💅🤳💪🦾🦿🦵🦶👂🦻👃🧠🦷🦴👀👅👄💗💖🥽🧤👖🧊🩲👲🥲🫠🫢🫣🫡🫥🥸🥹🫤🫱🫲🫳🤌🫴🫰🫵🫀🫁🫦🧋🪸🪞🥷🪷🦭🪨🪙🪳🪃🧌🦬🪵🫘🛞🫕🦫🪪🫧🪰🪱🪲🪜🪝🪣🦣🫒🪟🫙🛗🫐🪶🪛🛖🫑🪤🪢🪠🛻🫖⚧🪬🫔🪅ñ🫓🩻🪄🪥🪗🛼🩼🪫🪹🪦🪆🪡🪩🪴🪖🛝🫂🛟🩴🫗🪺🪚🪘🫅🟰]", word):
                        word = re.sub(r'[a-zA-Z0-9.]', "", word)
                        for words in word:
                            sent.append(str(words))
                            count4 +=1
                            sentcount +=1
                            if str(word) in dictsjen:
                                dictsjen[str(word)] += 1
                            else:
                                dictsjen[str(word)] = 1
                else:
                    sent.append(str(lemmatizer.lemmatize(word)).lower())
                    count4 +=1
                    sentcount +=1
                    if str(word) in dictsjen:
                        dictsjen[str(word)] += 1
                    else:
                        dictsjen[str(word)] = 1
        sents1.append(sent)
        if sentcount > enmax:
            enmax = sentcount
        if sentcount < enmin:
            enmin = sentcount
srten = dict(sorted(dictsjen.items(), key=lambda item: item[1]))
keysen = list(srten.keys())[::-1]
pltse = []
for i in range(50):
    pltse.append(srten[keysen[i]])
print(pltse)
plt.bar(range(50),pltse)
plt.xticks(range(50),keysen[:50],fontproperties=fprop, rotation=90)
plt.title("English Word Frequency")
plt.xlabel("English Word")
plt.ylabel("Frequency")
plt.show()
print(count4/count3)
print(count4)
print(enmax)
print(enmin)
model = models.Word2Vec(sentences=sents, vector_size=100, window=5, min_count=10, workers=4)
model.save("word2vec.model")
model2 = models.Word2Vec(sentences=sents1, vector_size=100, window=5, min_count=10, workers=4)
model2.save("word2vec.model2")
sims = model.wv.most_similar('🤣', topn=20)
sims2 = model.wv.most_similar('😭', topn=20)
sims3 = model.wv.most_similar('💀', topn=20)
sims4 = model.wv.most_similar('😂', topn=20)
sims5 = model.wv.most_similar('笑', topn=20)
sims6 = model.wv.most_similar('w', topn=20)
sims7 = model.wv.most_similar('草', topn=20)
sims8 = model2.wv.most_similar('🤣', topn=20)
sims9 = model2.wv.most_similar('😭', topn=20)
sims10 = model2.wv.most_similar('💀', topn=20)
sims11= model2.wv.most_similar('😂', topn=20)
sims12 = model2.wv.most_similar('lol', topn=20)
sims13 = model2.wv.most_similar('lmao', topn=20)
sims14 = model2.wv.most_similar('lmfao', topn=20)

print("🤣")
# for word in sims:
#     print(word)
for word in sims:
    if word not in sims2:
        print(word)
print("😭")
# for word in sims2:
#     print(word)
for word in sims2:
    if word not in sims:
        print(word)
print("💀")
# for word in sims2:
#     print(word)
for word in sims3:
    if word not in sims:
        print(word)
print("😂")
# for word in sims2:
#     print(word)
for word in sims4:
    if word not in sims:
        print(word)
print("笑")
# for word in sims2:
#     print(word)
for word in sims5:
    if word not in sims:
        print(word)
print("w")
# for word in sims2:
#     print(word)
for word in sims6:
    if word not in sims:
        print(word)
print("草")
# for word in sims2:
#     print(word)
for word in sims7:
    if word not in sims:
        print(word)
print("🤣")
# for word in sims:
#     print(word)
for word in sims8:
    if word not in sims2:
        print(word)
print("😭")
# for word in sims2:
#     print(word)
for word in sims9:
    if word not in sims:
        print(word)
print("💀")
# for word in sims2:
#     print(word)
for word in sims10:
    if word not in sims:
        print(word)
print("😂")
# for word in sims2:
#     print(word)
for word in sims11:
    if word not in sims:
        print(word)
print("lol")
# for word in sims:
#     print(word)
for word in sims12:
    if word not in sims2:
        print(word)
print("lmao")
# for word in sims2:
#     print(word)
for word in sims13:
    if word not in sims:
        print(word)

print("lmfao")
# for word in sims2:
#     print(word)
for word in sims14:
    if word not in sims:
        print(word)