#!/usr/bin/env python 
# -*- coding: Utf-8 -*-



def read_cyphers(team):
    ciphers = []
    import os
    for i in range(10):
        fname = os.path.join(os.path.dirname(__file__), "Source", "team" + str(team),
                             "message" + str(team) + "_" + chr(97 + i) + ".txt.enc")
        with open(fname, 'r') as file:
            ciphers.append(file.read())
    return ciphers


ciphers = read_cyphers(1)
current_messages = []
shortest = 0
mode = "cribGuess"  # or cribFollow
tempDecryptedText = ""

# Totally decrypted (group 9)
CJPlain = "Trust I seek and I find in you\n'Cause you know I'm here for you\nBody's aching all the time\nReaching a fever pitch\nIgnite the light\nTo seize everything you ever wanted\nIt's such a feelin' that my love\nYou're in control just like a child\nMy worst distraction, my rhythm and blues\n"
CIPlain = "UHlelo Lobhalomfihlo kuyikhono ukukhuluma phambi sophikisana. Lokhu isayensi kuyisisekelo of security computer zanamuhla. Abacwaningi Security ukudala ezokuphepha ubuchule. Kukhona ubuchule eziningi ezinjalo, owaziwa kakhulu kuba ukubethela. Ukubethela isinika ithuba ukudlulisa ulwazi oluyimfihlo."
CDPlain = "Scholars agree that classical information are an interesting new topic in the field of e-voting technology, and electrical engineers concur. In this work, we prove the visualization of information retrieval systems. In order to fix this obstacle, we verify not only that Scheme and Markov models are largely incompatible, but that the same is true for the World Wide Web. \n"
CEPlain = "Leading analysts agree that electronic communication are an interesting new topic in the field of theory, and cyberinformaticians concur. After years of confusing research into scatter/gather I/O, we prove the visualization of write-ahead logging. Of course, this is not always the case. Moth, our new application for voice-over-IP, is the solution to all of these obstacles. \n"
CCPlain = "Man, cartoons are the best! I like Futurama.\nIt is a sci-fi show about future. The story turns around a guy from the 20th century\nwho was frozen for many years and then he wakes up in a crazy future!\nThey have created 7 seasons and every one of them is just great!\nThey have so many fun characters, professor Farnsworth, Doctor Zoiberg, Leela\nand a robot called Bender! You should watch it!\n"
CFPlain = "The implications of multimodal algorithms have been far-reaching and pervasive. Given the current status of concurrent technology, information theorists obviously desire the deployment of replication, which embodies the private principles of cyberinformatics. In this position paper we introduce a novel application for the analysis of RAID (Tamkin), proving that Internet QoS and IPv4 can collaborate to fulfill this objective. \n"
CAPlain = "Vienna is the capital of Austria. It is one of its largests cities.\nVienna is 410 square kilometers, almost 2 million people live there.\nVienna is situated in the Eastern part of Austria, it is standing on Danube river.\nVienna is in the UTC+1 time zone.\nWhen tourists come to Vienna they often visit  Sch\xc3\xb6nbrunn Palace, Austrian Parliament,\nCity Hall, and St. Stephen's Cathedral.\nDo not forget to go to opera when you visit Vienna.\n"
CGPlain = "Local-area networks and autonomous epistemologies have been extensively synthesized by cyberneticists. It should be noted that Gob controls hierarchical databases. Existing mobile and real-time heuristics use client-server modalities to explore large-scale theory. While conventional wisdom states that this issue is generally addressed by the development of the Internet, we believe that a different method is necessary. In the opinions of many, we view networking as following a cycle of four phases: refinement, creation, simulation, and creation. Thus, we concentrate our efforts on proving that the partition table and e-business are generally incompatible. \n"
CBPlain = "Shame on you! Shame, shame, shame!\nWhat are you trying to do? Are you trying to break my cryptosystem?\nDo you know that reading other people's letters is not very nice and not polite?\nI am not doing that knind of things!\nWho on earth gets into my personal life like that? And why are you doing it?\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nMy messages to Alice are strictly confidential! Only me, Alice and the NSA can read this e-mails..\nSo, dear hacker, stop it right now!\nBest regards,\nEve.\n"
CHPlain = "Мать с младенцем спасена;\nЗемлю чувствует она.\nНо из бочки кто их вынет?\nБог неужто их покинет?\nСын на ножки поднялся,\nВ дно головкой уперся,\nПонатужился немножко:\n\"Как бы здесь на двор окошко\nНам проделать?\" - молвил он,\nВышиб дно и вышел вон.\nМать и сын теперь на воле;\nВидят холм в широком поле;\nМоре синее кругом,\nДуб зеленый над холмом.\nСын подумал: добрый ужин\nБыл бы нам, однако, нужен.\nЛомит он у дуба сук\nИ в тугой сгибает лук,\nСо креста снурок шелковый\nНатянул на лук дубовый,\nТонку тросточку сломил,\nСтрелкой легкой завострил\nИ пошел на край долины\nУ моря искать дичины.\n"


# Totally decrypted (group 1)
CEPlain = "The synthesis of Lamport clocks is a private question. Here, we disprove the emulation of multicast frameworks. We prove that flip-flop gates and interrupts can cooperate to solve this issue. Our intent here is to set the record straight. \n"
CJPlain = "So close, no matter how far\nLook up to the skies and see\nNow it looks as though they're here to stay\nWe could have had it all\nHe won't have it, he knows his whole back city's ropes\nCards on the table, we're both showing hearts\nFeel so paper-thin\nWhen it gets cold\nI'm down on my knees, I wanna take you there\n"
CIPlain = "Kriptografie is 'n kuns van kommunikasie in die teenwoordigheid van 'n teenstander. Hierdie wetenskap is die fondament van die moderne rekenaar sekuriteit. Sekuriteit navorsers skep sekuriteit algoritmes. Daar is baie sulke algoritmes, die mees bekende is enkripsie. Enkripsie gee ons 'n manier om vertroulike inligting oor te dra.\n"
CFPlain = "Recent advances in flexible epistemologies and unstable communication do not necessarily obviate the need for the World Wide Web. In this paper, we disprove the extensive unification of fiber-optic cables and local-area networks, which embodies the extensive principles of cyberinformatics [5]. Larum, our new methodology for checksums, is the solution to all of these obstacles. \n"
CCPlain = "I like animated cartoons!\nSouth park is a cartoon that is going on for a long time now. They are showing their 20th season right now.\nIt is very funny, they often find interesting ways to talk about contreversial topics of our society\nincluding popular culture, politics and just trendy subjects.\nmain characters in this show are 4 little boys. Their names are \nStan Marsh, Kyle Broflovski, Kenny McCormick and Eric Cartman.\n"
CGPlain = "Reinforcement learning and Moore's Law, while confirmed in theory, have not until recently been considered compelling. A confusing problem in operating systems is the evaluation of the visualization of 128 bit architectures. The usual methods for the understanding of courseware do not apply in this area. The construction of information retrieval systems would improbably degrade the confusing unification of architecture and voice-over-IP.\n"
CAPlain = "The capital of Great Britan is London. It is the biggest city in England. \nIt is situated in the South-East of the UK. London is standing on the river Thames.\nIt's area is just below 2000 square kilometers, about 8.5 million people live there. \nLondon is in the GMT+0 time zone. \nAmong its most famous tourist attractions you may find Tower Bridge, \nTrafalgar Square, London Eye and the Big Ben.\nWhen you visit London, do not forget to say \"Hi!\" to the Queen.\n"
CBPlain = "What are you trying to do? Are you trying to break my cryptosystem?\nDo you know that reading other people's letters is not very nice and not polite?\nI am not doing that knind of things! Shame on you! Shame, shame, shame!\nWho on earth gets into my personal life like that? And why are you doing it?\nIs someone forcing you? No? If not, then what the hell is wrong with you?\nMy messages to Bob are strictly confidential! Only me, Bob and the NSA can read this e-mails..\nSo, dear hacker, stop it right now!\nBest regards,\nAlice.\n"
CDPlain = "Many scholars would agree that, had it not been for the construction of massive multiplayer online role-playing games, the study of SCSI disks might never have occurred. Given the current status of stochastic methodologies, biologists clearly desire the simulation of wide-area networks. We introduce a novel system for the exploration of simulated annealing (Rasp), validating that the producer-consumer problem and Boolean logic are largely incompatible. This is rarely a confirmed goal but has ample historical precedence. \n"
CHplain = "Три девицы под окном\nПряли поздно вечерком.\n\"Кабы я была царица,-\nГоворит одна девица,-\nТо на весь крещеный мир\nПриготовила б я пир\".\n- \"Кабы я была царица,-\nГоворит ее сестрица,-\nТо на весь бы мир одна\nНаткала я полотна\".\n- \"Кабы я была царица,-\nТретья молвила сестрица,-\nЯ б для батюшки-царя\nРодила богатыря\".\n"

def str_xor(a, b):  # xor two strings of different lengths
    """
    Perform xor on 2 strings
    :param a: 1st string
    :param b: 2nd string
    :return: string of xor'ed values
    """
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


def shortest_length(ciphers):
    """
    Find shortest minion
    :param ciphers:
    :return: shortest length in bytes
    """
    shortest = len(ciphers[0])
    for k in range(1, len(ciphers)):
        xored = str_xor(ciphers[0].decode("base64"), ciphers[k].decode("base64"))
        if len(xored) < shortest:
            shortest = len(xored)
    return shortest


def print_messages(messages, line_length=100):
    """
    Print the messages passed in and hope  Antoine can explain this at the presentations
    :param messages:
    :param line_length:
    :return: nothing, nada, zilch, squat
    """
    for index, value in enumerate(messages):
        if(index == 7):
            f = open('workfile.txt', 'w')
            printed = str(value)
            f.write(printed)
            f.close()
        print "Message " + str(index) + ": "
        text_len = len(value)
        for part in xrange(0, text_len, line_length):
            if part > text_len - line_length:
                temp = []
                temp.append(value[part:])
                print("     " + str(temp))
            else:
                temp = []
                temp.append(value[part:part + line_length])
                print ("     " + str(temp))


def print_guess(guesses, to_print):
    """
    Print the guess that Antoine will explain later
    :param guesses: a freaking guess by the software
    :param to_print: string to print
    :return:
    """
    for index_1, value_1 in enumerate(guesses):
        if to_print[index_1]:
            print "\nPosition " + str(index_1) + ": "
            for index_2, value_2 in enumerate(value_1):  # so it's easier to print "\n" symbols
                message_part = [value_2]
                print "-> " + str(index_2) + " " + str(message_part) + " " + str(index_2)


"""
def printGuess(guesses, toPrint):
	f = open('workfile.txt', 'w')
	printed = str(guesses[0][0])
	f.write(printed)
	f.close()
"""


def init():
    """
    Initialise crap
    :return:
    """
    global shortest
    global current_messages
    shortest = shortest_length(ciphers)
    for i in range(len(ciphers)):
        current_messages.append("_" * shortest)


def is_good_guess(guess):  # Don't accept special symbols
    for j in guess:
        symbol = j.encode("hex")
        if (symbol > '7e') or (symbol < '20'):
            if symbol != '0a':  # accepte \n
                return False
    return True


def is_good_guess_hard(guess):  # Accepts only [a-z,A-Z] ! : - . , ? \n SPACE
    """
    Be a magician an guess
    :param guess:
    :return:
    """
    for value in guess:
        symbol = value.encode("hex")
        if (('40' < symbol < '5b') or ('60' < symbol < '7b')
            or (symbol == '2c')
            or (symbol == '21') or (symbol == '27')
            or (symbol == '2e') or (symbol == '2d')
            or (symbol == '3a') or (symbol == '3f')
            or (symbol == '20') or (symbol == '0a')):
            pass
        else:
            return False
    return True


def get_temp_decrypted_text(ind):
    """
    Display temporary decrypted text
    :param ind:
    :return:
    """
    global current_messages
    last_letter_ind = 0
    i = shortest - 1
    while i >= 0:
        if current_messages[ind][i] != "_":
            last_letter_ind = i
            i = 0  # stop searching
        i -= 1
    return current_messages[ind][:last_letter_ind + 1]


def switch_mode():
    """
    Some crap with decoding
    :return: nothing, zilch, squat
    """
    global mode
    if mode == "cribGuess":
        mode = "cribFollow"
    else:
        mode = "cribGuess"


def is_decrypted(ind):
    """
    Check if message identified by index is decrypted
    :param ind:  index of the message to be checked
    :return:  state of decryption
    """
    i = shortest - 1
    while i >= 0:
        if current_messages[ind][i] == "_":
            return False
        i -= 1
    return True


# --------------------------------------  MAIN  --------------------------------------

def root_of_all_decryption():
    global tempDecryptedText
    init()
    choice = ""
    tempDecryptedText = ""
    print("The current messages are:\n\n")
    print_messages(current_messages, 128)
    print''
    while choice != "end":
        cipherNb = int(raw_input("Enter message number: "))
        if (cipherNb < len(ciphers)) and (cipherNb >= 0):
            try:
                crib = input(
                    "Enter your crib (have to be between \" \"): ")  # use input() instead of raw_input() to be able to use "\n"
                if mode == "cribFollow":
                    tempDecryptedText = get_temp_decrypted_text(cipherNb)
                    crib = tempDecryptedText + crib
                temp = []  # len = shortest cipher
                toPrint = []
                for index in range(shortest - len(crib) + 1):
                    guesses = []  # len = len(ciphers)
                    printed = True
                    for k in range(len(ciphers)):
                        if cipherNb != k:  # pas de xor avec sois-meme
                            xored = str_xor(ciphers[cipherNb].decode("base64"), ciphers[k].decode("base64"))
                            guess = str_xor(xored[index:index + len(crib)], crib)
                            guesses.append(guess)
                            #if not is_good_guess_hard(guess):
                            #    printed = False
                        else:
                            guesses.append(crib)
                    temp.append(guesses)
                    if printed:
                        toPrint.append(True)
                    else:
                        toPrint.append(False)
                print_guess(temp, toPrint)
                print("")
                choice = raw_input(
                    "Enter the matched position, 'none' for no match, 'switch' to switch to the other decryption mode, or 'end' to quit: ").strip(
                    " ")
                if choice != "none" and choice != "end" and choice != "switch":
                    position = int(choice)
                    for index in range(len(current_messages)):
                        crib_length = len(temp[position][index])
                        current_messages[index] = current_messages[index][:position] + temp[position][index] + \
                                                  current_messages[index][position + crib_length:]
                    if mode == "cribFollow":
                        tempDecryptedText = crib
                    if is_decrypted(cipherNb):
                        choice = 'end'
                        print("THE SHORTEST MESSAGE HAS BEEN DECRYPTED HUZZAH")
                elif choice == "switch":
                    switch_mode()
                print("The current messages are:\n\n")
                print_messages(current_messages, 128)
                print''
            except (NameError, SyntaxError):
                print("Don't forget to write your crib between \" \"")
        else:
            print("Incorrect message number, try again")


if __name__ == '__main__':
    root_of_all_decryption()
