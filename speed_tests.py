#!/usr/bin/env python
# -*- coding: latin-1 -*-
## -*- coding: Utf-8 -*-



def read_cyphers(team):
    ciphers = []
    import os
    for i in range(10):
        fname = os.path.join(os.path.dirname(__file__), "Source", "team" + str(team),
                             "message" + str(team) + "_" + chr(97 + i) + ".txt.enc")
        with open(fname, 'r') as file:
            ciphers.append(file.read())
    return ciphers


ciphers = read_cyphers(9)
current_messages = []
shortest = 0
mode = "cribGuess"  # or cribFollow
tempDecryptedText = ""

# Totally decrypted:
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


def str_xor(a, b):  # xor two strings of different lengths
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


def shortest_xor(chiphers):
    deflt = ciphers[0].decode("base64")
    xored = [len(str_xor(deflt, ciphers[k].decode("base64"))) for k in range(1, len(ciphers))]
    sorted(xored)
    return xored[0]


def shortest_xor_length(ciphers):
    """
    Find shortest minion
    :param ciphers:
    :return:
    """
    shortest = len(ciphers[0])
    deflt = ciphers[0].decode("base64")
    for k in range(1, len(ciphers)):
        xored = str_xor(deflt, ciphers[k].decode("base64"))
        if len(xored) < shortest:
            shortest = len(xored)
    return shortest


if __name__ == '__main__':
    import timeit

    start_time = timeit.default_timer()
    for i in range(10000):
        shortest_xor(ciphers)
    elapsed_my = timeit.default_timer() - start_time
    start_time = timeit.default_timer()
    for i in range(10000):
        shortest_xor_length(ciphers)
    elapsed_ant = timeit.default_timer() - start_time
    print("my version: {0}".format(elapsed_my))
    print("ant version: {0}".format(elapsed_ant))
