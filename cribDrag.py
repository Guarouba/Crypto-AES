#!/usr/bin/env python 
# -*- coding: Utf-8 -*-
import sys

CA = "FA8t5MYjwXLr1XugGj87qFPrF3aSzDcgoazlg49lUcspTiWuryEaLP4LP0UWbKst\
Set2OX771eaW1H0kXMkeCFIrPC7+PwzheTX8qC29g+Buhw9pmrUOqEvLbNARnPwl\
NpW32P1P2imUGqkWy+hwIUAeETH+B2A0GNqZclMlqxUR0dlRaiiYhBgZaoVnoSr3\
4Vs2izgko+vHWlV1ZfX5pCASLSBW9eoXC/MSbgBb8kaaVsIi/bnc1qQWNYyu/JY1\
tAQpyoYD3+yfLKUtD0KdzpaSrkwaGzJrbSE/Mk2zbo7d2O47+qh6ICi8KbOuUC8A\
HJR8HN+Hp7AJ+Wsy7CRh8VAd6iNaW8j1hZy//qXBeJ/7c3soFMx+WX9vtagZukZ4\
JIpS7uxbjjcMuHGPhnO6vLjU/B7rnInfbNI6YRRgZVE7fll4Bp4rJhQwkMZKCn8a\
ZeG6ZlwoYIYw5nG0m33c0sVTplWbfvb24dvUmiBb130QD/5N9YtbXQv5+vVkW+E7\
CyvUZLvayRvdYhFxZrcw2ILxQJoUEUMx7nhlS9B8k1Zd0DxxDY3CRVd1+e6HuzGK\
IRw="

CB = "EQ4p581ijnW4jGC9Xj8LoULvBjvenzAn7Ii80Ih/WcdiT2aN5ykdLPAXP0UAZf5k\
SeovPHHukveKgGprAIArE1J4a0vddh39bj2ypn7p2PE81Rl5hPQRtEvDd8UOhfYi\
KpSwkbARvACUSaRZjOh2JkMFWCr4RmRxBc+UcxonpUMbhcVcfXqNz30/b4UuvGu7\
7VxinSMj9uPAH186eLuvtToOLQte5ftSGPNWPg9G8kaFX44K/K+XroRXeMHn5tko\
50A114kKm/GZKvFiCgywwZzHo08aHTN0ZjRiGRGNY4+T1qBy7OlhOmDoJrP6dlsq\
WdEzSNuT4uAW5HY4rE9auVkarDIVQtP3k8i4tqfaKtqaaXAoNc1iF3B88PwIsEp4\
L4NP5eVbkSpA20zchlO2uR4N/Bm5j4jDL+s1alV6bwgkH2JkTcwLIVp+r9MURmIT\
ber0ZRhDV88w9zTcknTcksVbuxHMX+22pqjXliRbkmpYCeEE2YYTVQr46PgtNNZ0\
XyqbUffVxQyaZhc0MqtkzYSyQJlNXlA78n8sWN13iR9F02hxNIrdVQM4yqvClDOC\
bHM9t+eBY8wEL/01/sHApU/5xPyX+8qczaMlBT78fZ4dV/JNvlP7sQFSCfIIOSn8\
KtRq3orrBYFwm/AJI0dERm8F59KDS6O7grWCQ/MPmJHwf1qiX4WljWTVzZjckg=="

CC = "DwcmpoghgGnsmmCmDD85u0aiF3+bzDoj8pmx0LI3VMNsC0yc+jwcfvAIO0tzQ/9k\
VOt2ND/60erIxmckTMgFFhc5cEvdIknpYiCpszuzl4U2wlxrm7sOtEvUcM4Qgrkw\
IYixmrkO12ScHKQWn7pyJQwGEDuwFSAlH4qWch09txEN+9pRYHqKy2FvZZJmtS65\
qE55inE9t+TKH0gwbemq8CkZaUVD7vscWfVXPhZI7QOGEJcTqKPGhKxXet6m8s98\
oVEuy5UImo+lI+A7QQq42Z3Hr1tfCC94bHMmGGi/apPc171y6OZ3bm2+JKT3JRQt\
UoUzDpaeqvUetmwk4kRD6kFTrSVQT869/Lyku7+OfZutYjR7LYV2Vn93tboEsR87\
I41U6uEPnSwM/SXf1E+/sQgR/Q65r4bDIvEsYgd3aFE7e0NoBoMwZyB/qcVdFHFX\
KMixdxxDKY4q+3Gd2mPfnIpG6FLaQe69pajimj5X12EWXIdh4d9AUAD+9/1qJsQg\
SC2bee+drA=="

CD = "EQUg5cQjk2i4lGi6Gnp4vUvjFzedgDk18oTzkZc3UcRhAR637jwAY/9FOxccKuoq\
HfE4IXr71/CRyWBjH84PFhcsfVTBNUnmeXSoqTu90bg7yxg4gLJcqEbWasgXn/5x\
J4KnnLNB2iucEPEWmKZ5aEkeHT3kVXkyFsbVch0uqw0RlN9KLzmSxHE6cc4phiX3\
/EB/i3EnufjYExEiabupoicBaEVD7vtSD/RBawBF7xyURIsM5urHwu0ed8qo+ts9\
s0010Mcf3vGDIuA0AA753IGUuExXGnU9QT0xV2m+bpKTzaFy7+FrbnygKKWuahkw\
Q8Q/BNPG4ucWtnMysEdQ4BUdpSMVQdTwj8i4tqfaNam4b3FlJ4V6WXUu2L0DtFAu\
a4FJ7+cXi34eo2CPykGrsx4O61zwh4TeIfI6eRxhbBg3H05+Bsw2Lxtk4NNQAzYI\
aemxMhlRA5s26jTcnH7C3pFarRHsQvC0paj3ljRWkkRSHvAung=="

CE = "DgMp7sEshjv5m26kBmwsugPjBGWbiXgy6Yzk0J57XclzHAO05itJb/4INxAXY+gl\
SfE5Oz/owObFwWAkVs4eBEU9YVDBOA6veTGr4Sryx7g9hxV2z6AUqEvGbNkSlbk+\
NcewnLhBxD3XSbxYneh+MU4XCjf+QX8jGsuBfhAgow0H0c5WYTmI2DxvQoZ9qjn3\
8U13iiJwueyTXF47au6quSYQLRdS9fsTC/5aPghH8gnVQ4EC/L7N1uIQeNiv7cR8\
jgsVksca3qWBOeo0BEKtx53HukBJHDpxYSlwTHK1ZcDc3+4l++FnKyWpKbPvYVsv\
WMI7AdiN7LA88CU0rVtE6lBf6iNdR8m8n5vssKnaNZu3cHVxMYVvX3Qu9r0CuhF4\
BoNS465blysN8WvK0QC4pAsO+x/4nY7eIqI9YgcjdhJyXEkmHZonNVdZkIsYD2Vb\
fOyxMgNNT5ow9j6S2mXf3oRepBHUS6Ksqe3TmnBc0GBDHb1i8YwdGGU="

CF = "Fg4tqsEvkXfxlm68FnA2ugPtBTeTmTQy6ID/lJp7GMtrCQOo5jwBYeJFMgQPb6sm\
WP04dXnowK6XxW9nV8kEBhc5fECIJgz9YTWvqCj4mfEZzgp9gfQIpQ6AZskMg/w/\
J8e3gLxawzfbBrsWmqdzK1kACjv+UzAlEsmdeRwlrQQN3Y1QYTyS2H8ud4lmoWuj\
4E15ijgjovmTUFMjZfSsoyQOLQFS9fcAHL1GdgQJ4gOFXI0a5a/G0O0Yf4y17cYw\
rkc7yo4C1anRPO0rAgr5ypWFo01TDCg9fDt0GGuoYpbSzaty+fp6IGuhMbrrdlss\
UYU/EdSPsPkd8Golr09C8FYA5Hd8QJronoG//rbBZpOvbntmYtV6R3R8tasU/1Y2\
P55J7/cYnX4e8WvA0EW19BoS4hDwiobFJe01LRNscl1vV0krE4IjKwNjqdQYCXBb\
WsWdVlAKd44p9DiS0z2QjpddvljVSqKsqenU3xldxnZFErt6tK5ca0/q9f1qGPUi\
H2XYcfWcxQbWawQzfapxy4jxQJoUGEY4+nApUJhtlR9XnyYzEYHSWEojyqnC3w=="

CG = "Dgkr68RvgGn9lC+mGmsvplHpEDefgjxm4Jjkn5V4VcVyHUy//yEaePQINQkWbeIh\
Trg+NGnskuGAxWAkWtgeBFkre1LNOhCvZC2ytTb4xLgkwhg4ja1crhLCYM4QlO04\
MI63gK4Alg2PSa5elr1xLAwQHX7+SGQ0E4qBfxI94iQbk41aYDSJ2H0jcMBhpi6l\
6Vp1kDgzt+aTW1Ahbfm4oy0EI0Vy/vcBDfRceUFE6QScXIdD6aTMhL8SeMDq/N8x\
ogQy25If0vaFIuYxQReqytiEoEBfBy8wezZjTn6oK43c3a8+4Px6K3voNbmuYAMz\
W8ouDZaGo+IU8ygkoU9a/BUHojJaXMOy1r+kt6rLNZm0aWJtLNFyWH9v+fwGtkw8\
JIEG+PYajDsM8XHHx1T5oBML4VzwmpTEKaIyflVkZRN+TU1nHpViJh50ssJLFXMf\
KOatMgRKRs8g+ieZln7Ak4BcvBHUS6Ksqe2Atj5H12FZGaoitIhWGA3u9/AvJ8B0\
Xy3aZLvdhg3TYQM0YL1+y828UYFcEVd09WplUt16mAVX3jsoVcT4QgMhx+LCui+C\
YX9yuPrFLN5MJ7wV1KzAsUu3kueX7Y7S3L87GWzyOZ0bHv9NsBuejgIRXv8DP3u9\
YtZw1oP8Cc5lz/kWdlwQFnUN89+EUe2mkPLhb/MRid/2Nh2gX4S31Qf/1dHS64iK\
j77Q6cdMbQaXMiWMO+g4cmp6qZwzXZd/jHpirI0LVs7YqhzyRKvFUWJhRtZaDxp0\
ighw7ePg4BRUHBSC9XSmALGE4KPKfS88Qx6ScMjF0x+1UauDuc5s7lBtZIktUgcR\
JiKWJd9oHA3r2Ht9e39qZhrrBwnyzo2my4HTrWWxSG+S6MjeVF6IWA=="

CH = "kvqYOnnAMJe4JI7or6OIcvMys6MuWYj7UGtARSurGHuGvtMKP5no3CS157XJMYGU\
qkjjhaNZCVJrgN+D7iO60+bZw6Z45LgMx+ENQ35NCQHjd8w25QThHdWA1QSuRrmB\
4jd6JVr+DJRDSQ2MKErN9gyiwI8VB8DjpiElqqP8E+FL+32o3+QtGTKfvjC8HsgH\
PvmUKO9wBjJiuhGFs0tnAPKntbWKViuj+6I4zsD4DbZIEDLeWHqIdHCnp3xxWAyM\
fwSKATfTazEh9lTNsdkILilo4CPq+3vNvIOs6KX621NjBx7pWTbD/NhykWhevFuS\
tHXjuAM7QkHyR4p7yP6pSYujd4eF/zhNdTh6Dn5+rita1psokhjLgsGyRWGhYe/u\
m1b2Nbhx2o7lAbV/HAAJZarpsqwuOVNh+VPa3Pkj0MDLjwzbxjzwl8TBQIfo2MbB\
2DoFmqCY81FOT8wsSsEM3jWNGbFrk1JsET1wRICDY5Hm8OEstNIT6NNbJUnxgReE\
k5UAMEsCdtSWDbXDw1PBNz1p5EQUroeEIcn7HGih3aaWbsKA8zQE/Jh1fzUya49W\
IRzNSllVkjq9xv2rFaAxR/8cNDPSSyxsDBvzpqtI0CLwHk6DQM3RMtyul0bWiO7n\
SGWbZVdJnXCMPh1Z0qvg2M3XUAbXu3/0JBxYuUf8PA9SoO19/V32cdFABS1JSFTc\
8AItTRDyg/oCc5ppyzOaqtu7EEZ9ow36ZN6SUB6sjT4H6XhBtRQy87I180Hlz7jv\
P9vGP0AfQ40bookiN8tkSQ5mEGlyp4ug58gn7JauccoNrhJR9z6nX4zRtXjP7N/h\
899PaozRxrgme+rNicvB0cals/hDFDFnO1W3HpsNs95doXoD4PuIgiMQC0y9Mr6M\
6x2vkuSV2suGAOY8u59rBoOXrQXvv7Qk7t3y9A8+W6Wftdj1NNbvfDGzXhK1T8IS\
2TQ6JTds1BpSyZhvCeBMt4uT46vF0mFNvkZ26aa6R2awoYim37PH7pPMIsD7v26N\
vYAD1OtvHFgx24KJ97hzNXGpzjgzlJipOCVUriDtqhE194m0e7qq3lrrJQ7obiA7\
vSh284lqyaYZPiWi/J9Lukc2umCIyjSnGL1dKS7sG5tB6CT0g8vV+zYdnqculFf6\
UkfgSBPmaHZF3Ayp1pykHywD+FX212k2ocAj4LQ1XBISh+nmEPK2KWFVwMTMB//H\
nZSUCymrawvX7734sJ9D9fyXeAJlsKt7zIrtPyMEzk2ZttSaOjT7DzsOuYNd4OTZ\
E7kQI9Wf20XGF1QttKOFNaAenHfGD0QCiDBjaknH3ucOd29MZWaRkzw1onZelmqV\
uZZojdePmw8SHYKT/wiHujWx9Wdq89yo5fxqLg=="

CI = "Fy4k78QtwVf3l2epE3A1r0rqD3jehy0/6Ib4n5V4GN9sGwey+iQcYfBFKg0YZ+kt\
Hes5JXfg2eqWwWBlEYAmDlwwZwTBJQj2cjqvqH72wqg31BVrir8ZoQSAatpegvwy\
JpWtgKQO1SuWGahCnLo9Mk0cGTPlT3wwWYq0dRIqtQIamMNeZnquz3E6cYl9tmui\
411ymT0x9u/JUFogfPO8oCAWLRBV8/0aDPFXMEFi8w2dX4wCqL/K0a4fbMCiqNMm\
rkoz0IAEm+CLIusoAA62g9iIu0hAACx8KDhwU3OvZ5WT0rsw6KhmJX2qJKLmYBci\
GYUJA8OIp+Qb82k24kdF8FsaoTYVR870g4qt/rPFYJ63cnhhMcQ7Qn159KYY/1A0\
PpVP5uQSkDIQ/w8="

CJ = "FhQ9+dxiqDvrkGqjX342rQPLQ3GXgjxm6IOwiZRiMo1EDxmp6mgQY+RFMQsWfasN\
GvV2PXr716ODz3wkRs8fa3U3dl2PJUnudDy1rzm91r0yhwhwivQIpAbFD+4bkPo5\
Oomj1LwO0CGNDK8WiaFpK0R4MTn+TmQ0V96dclMlqwQchadtYHqOz3s1ZsBsuS6l\
8Vx+kT839vPcShEwev6r8D8WYxFS4pQ7DbpBPhJc5Q7VUcIF7a/EzaNQOdiv6cJ8\
ql160ogb3o+oJPBlEwf5xpbHr0ZUHSlyZHN7TWiuK4za0qty6KhwJmGkJdzDfFs0\
WNcvHJaOq+MH5GQ0tkdZ9xlTpy4VXNLlgoCh/qfAcdq5a2FtMa8="

ciphers = [CB, CG]
currentMessages = []
shortest = 0
mode = "cribGuess"  # or cribFollow
tempDecryptedText = ""

# Totally decrypted:
CJPlain = "Trust I seek and I find in you\n'Cause you know I'm here for you\nBody's aching all the time\nReaching a " \
          "fever pitch\nIgnite the light\nTo seize everything you ever wanted\nIt's such a feelin' that my " \
          "love\nYou're in control just like a child\nMy worst distraction, my rhythm and blues\n "
CIPlain = "UHlelo Lobhalomfihlo kuyikhono ukukhuluma phambi sophikisana. Lokhu isayensi kuyisisekelo of security " \
          "computer zanamuhla. Abacwaningi Security ukudala ezokuphepha ubuchule. Kukhona ubuchule eziningi ezinjalo, " \
          "owaziwa kakhulu kuba ukubethela. Ukubethela isinika ithuba ukudlulisa ulwazi oluyimfihlo. "
CDPlain = "Scholars agree that classical information are an interesting new topic in the field of e-voting " \
          "technology, and electrical engineers concur. In this work, we prove the visualization of information " \
          "retrieval systems. In order to fix this obstacle, we verify not only that Scheme and Markov models are " \
          "largely incompatible, but that the same is true for the World Wide Web. \n "
CEPlain = "Leading analysts agree that electronic communication are an interesting new topic in the field of theory, " \
          "and cyberinformaticians concur. After years of confusing research into scatter/gather I/O, we prove the " \
          "visualization of write-ahead logging. Of course, this is not always the case. Moth, our new application " \
          "for voice-over-IP, is the solution to all of these obstacles. \n "
CCPlain = "Man, cartoons are the best! I like Futurama.\nIt is a sci-fi show about future. The story turns around a " \
          "guy from the 20th century\nwho was frozen for many years and then he wakes up in a crazy future!\nThey " \
          "have created 7 seasons and every one of them is just great!\nThey have so many fun characters, " \
          "professor Farnsworth, Doctor Zoiberg, Leela\nand a robot called Bender! You should watch it!\n "
CFPlain = "The implications of multimodal algorithms have been far-reaching and pervasive. Given the current status " \
          "of concurrent technology, information theorists obviously desire the deployment of replication, " \
          "which embodies the private principles of cyberinformatics. In this position paper we introduce a novel " \
          "application for the analysis of RAID (Tamkin), proving that Internet QoS and IPv4 can collaborate to " \
          "fulfill this objective. \n "
CAPlain = "Vienna is the capital of Austria. It is one of its largests cities.\nVienna is 410 square kilometers, " \
          "almost 2 million people live there.\nVienna is situated in the Eastern part of Austria, it is standing on " \
          "Danube river.\nVienna is in the UTC+1 time zone.\nWhen tourists come to Vienna they often visit  " \
          "Sch\xc3\xb6nbrunn Palace, Austrian Parliament,\nCity Hall, and St. Stephen's Cathedral.\nDo not forget to " \
          "go to opera when you visit Vienna.\n "

# Not totally decrypted:
CGPlain = "Local-area networks and autonomous epistemologies have been extensively synthesized by cyberneticists. It " \
          "should be noted that Gob controls hierarchical databases. Existing mobile and real-time heuristics use " \
          "client-server modalities to explore large-scale theory. While conventional wisdom states that this issue " \
          "is generally addressed by the development of the Internet, we believe that a different method is " \
          "necessary. In the opinions of many, we view networking as " \
          "_________________________________________________________ "
CBPlain = "Shame on you! Shame, shame, shame!\nWhat are you trying to do? Are you trying to break my " \
          "cryptosystem?\nDo you know that reading other people's letters is not very nice and not polite?\nI am not " \
          "doing that knind of things!\nWho on earth gets into my personal life like that? And why are you doing " \
          "it?\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nMy messages to Alice are " \
          "strictly confidential! Only me, Alice and the NSA can read this " \
          "e-mails._________________________________________________________ "


def strxor(s1, s2):  # xor two strings of different lengths
    return ''.join(chr(a ^ b) for a, b in zip(bytearray(s1), bytearray(s2)))  # zip locks to smallest size


def shortest_length(ciphers):
    shortest = len(ciphers[0])
    import base64
    for index, value in enumerate(ciphers[1:]):
        xored_result = strxor(base64.b64decode(ciphers[0]), base64.b64decode(ciphers[index]))
        if len(xored_result) < shortest:
            shortest = len(xored_result)
    return shortest


def printMessages(messages, lineLenght=100):
    for i in range(len(messages)):
        temp = list()
        temp.append(messages[i])
        print("Message " + str(i) + ":")

        text_len = len(messages[i])
        for part in range(0, text_len, lineLenght):
            temp = []
            if part > text_len - lineLenght:
                temp.append(messages[i][part:])  # print a list to be able to see the symbol "\n"
                print("    " + str(temp))
            else:
                temp.append(messages[i][part:part + lineLenght])
                print("    " + str(temp))


def printGuess(guesses, toPrint):
    for x in range(len(guesses)):
        if toPrint[x]:
            print('')
            print("Position " + str(x) + ": ")
            for y in range(len(guesses[x])):  # so it's easier to print "\n" symbols
                message_part = [guesses[x][y]]
                print("-> " + str(y) + " " + str(message_part) + " " + str(y))


def init():
    global shortest
    global currentMessages
    shortest = shortest_length(ciphers)
    for i in range(len(ciphers)):
        currentMessages.append("_" * shortest)


def isGoodGuess(guess):  # Don't accept special symbols
    for j in range(len(guess)):
        symbol = guess[j].encode("hex")
        if (symbol > '7e') or (symbol < '20'):
            if symbol != '0a':  # accepte \n
                return False
    return True


def isGoodGuessHard(guess):  # Accepts only [a-z,A-Z] ! : - . , ? \n SPACE
    for j in range(len(guess)):
        symbol = guess[j].encode("hex")
        if (('40' < symbol < '5b') or ('60' < symbol < '7b')
            or (symbol == '2c')
            or (symbol == '21') or (symbol == '27')
            or (symbol == '2e') or (symbol == '2d')
            or (symbol == '3a') or (symbol == '3f')
            or (symbol == '20') or (symbol == '0a')):
            a = 0
        else:
            return False
    return True


def get_temp_decrypted_text(ind):
    global currentMessages

    last_letter_ind = 0
    i = shortest - 1
    while i >= 0:
        if currentMessages[ind][i] != "_":
            last_letter_ind = i
            i = 0  # stop searching
        i -= 1
    return currentMessages[ind][:last_letter_ind + 1]


def switch_mode():
    global mode

    if mode == "cribGuess":
        mode = "cribFollow"
    else:
        mode = "cribGuess"


def is_decrypted(ind):
    index = shortest - 1
    while index >= 0:
        if currentMessages[ind][index] == "_":
            return False
        index -= 1
    return True


# --------------------------------------  MAIN  --------------------------------------

if __name__ == '__main__':

    init()

    choice = ""
    tempDecryptedText = ""

    print("The current messages are:")
    print('')
    printMessages(currentMessages, 128)
    print('')

    while choice != "end":

        cipherNb = int(input("Enter message number: "))

        if (cipherNb < len(ciphers)) and (cipherNb >= 0):
            import base64

            try:
                crib = input(
                    "Enter your crib (have to be between \" \"): ")  # use input() instead of raw_input() to be able to use "\n"

                if mode == "cribFollow":
                    tempDecryptedText = get_temp_decrypted_text(cipherNb)
                    crib = tempDecryptedText + crib

                temp = []  # len = shortest cipher
                toPrint = []
                for i in range(shortest - len(crib) + 1):
                    guesses = []  # len = len(ciphers)
                    printed = True
                    for k in range(len(ciphers)):
                        if cipherNb != k:  # pas de xor avec sois-meme
                            xored = strxor(base64.b64decode(ciphers[cipherNb]), base64.b64decode(ciphers[k]))
                            # xored = strxor(ciphers[cipherNb].decode("base64"), ciphers[k].decode("base64"))
                            guess = strxor(xored[i:i + len(crib)], crib)

                            guesses.append(guess)
                            if not isGoodGuessHard(guess):
                                printed = False

                        else:
                            guesses.append(crib)

                    temp.append(guesses)
                    if printed:
                        toPrint.append(True)
                    else:
                        toPrint.append(False)

                printGuess(temp, toPrint)

                print("")

                choice = input(
                    "Enter the matched position, 'none' for no match, 'switch' to switch to the other decryption "
                    "mode, or 'end' to quit: ")

                if choice != "none" and choice != "end" and choice != "switch":
                    position = int(choice)
                    for i in range(len(currentMessages)):
                        cribLenght = len(temp[position][i])
                        currentMessages[i] = currentMessages[i][:position] + temp[position][i] + currentMessages[i][
                                                                                                 position + cribLenght:]

                    if mode == "cribFollow":
                        tempDecryptedText = crib

                    if is_decrypted(cipherNb):
                        choice = 'end'
                        print("THE SHORTEST MESSAGE HAS BEEN DECRYPTED")

                elif choice == "switch":
                    switch_mode()

                print("The current messages are:")
                print()

                printMessages(currentMessages, 128)
                print()

            except NameError:
                print("Don't forget to write your crib between \" \"")
            except SyntaxError:
                print("Don't forget to write your crib between \" \"")

        else:
            print("Not correct message number, try again.")
            # print(currentMessages)
