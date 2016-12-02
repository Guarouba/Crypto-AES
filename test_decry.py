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


def read_cyphers(team):
    ciphers = []
    import os
    for i in range(10):
        fname = os.path.join(os.path.dirname(__file__), "Source", "team" + str(team),
                             "message" + str(team) + "_" + chr(97 + i) + ".txt.enc")
        with open(fname, 'r') as file:
            ciphers.append(file.read())
    return ciphers


def ding():
    cip = [i.decode("base64") for i in read_cyphers(9)[:2]]

    # out_size = shortest_length(cip)
    # out_msg = [["_".join("_" for i in range(out_size))] for j in range(2)]
    # for i in out_msg:
    #     print i
    guess = "Vienna is the capital of Austria."
    l_guess = len(guess)
    msg1 = cip[0][:l_guess]
    msg2 = cip[1][:l_guess]
    print (str_xor(guess, str_xor(msg1, msg2)))


def dong():
    import pickle
    uk = []
    us = []
    with open("Source/dictionary/uk.txt", 'r') as f1:
        uk = [i.strip("\n") for i in f1.readlines()]
    with open("Source/dictionary/us.txt", 'r') as f2:
        us = [i.strip("\n") for i in f2.readlines()]
    if len(uk) > 0 and len(us) > 0:
        print(len(uk))
        print(len(us))
    out = []
    for k, s in zip(uk, us):
        if k != s:
            out.append(k)
            out.append(s)
        else:
            out.append(k)
    print(len(out))
    with open("Source/dictionary/ukus.txt", 'wb') as file2:
        pickle.dump(out, file2)


def load_all_words():
    pass


all_available_words = load_all_words()


def load_word_freq_engligh():
    import pickle
    # print pickle.load(open("Source/dictionary/ukus.txt"))
    return pickle.load(open("Source/dictionary/ukus.txt"))  # loads list of words decreasing frequency


hash_crib_dictionary = {}  # {'ar':[car,bar,Mars,...],'ea':[sea,tea,..]}


def capitalize(val):
    return chr(ord(val[0]) - 32).join(val[1:]) if len(val) > 1 else chr(ord(val) - 32)


def create_indiv_crib_hash(word):
    global hash_crib_dictionary
    crib_size = 1
    l_word = len(word)
    while crib_size <= l_word:
        for i in range(l_word - crib_size + 1):
            temp_l = hash_crib_dictionary.get(word[i:i + crib_size], set())
            temp_l.add(word)
            hash_crib_dictionary[word[i:i + crib_size]] = temp_l
        crib_size += 1


mof = "a---cdef----gikx--eds------m------"


# def fin_spaces(word):
#     global mof
#     ranges = []
#     start, end = -1, -1
#     temp = -1
#     for index, item in enumerate(word):
#         if item == "*":
#             if index>end&&


def fill_partial_words(phrase):
    print(phrase.split("-"))
    phrase = phrase.split("-")
    cter = -1
    tmp = -1
    res = []
    found = False
    for index, val in enumerate(phrase):
        if not found and val == "":
            tmp = index
            cter = 1
            found = True
        else:
            if val == "":
                cter += 1
            else:
                res.append((tmp, cter))
                cter = 0
                found = False
    if found:
        res.append((tmp, cter))
    return res[1:] if len(res) > 1 else None


def create_hash_crib():
    global hash_crib_dictionary
    ll = load_word_freq_engligh()
    for current_word in ll:
        create_indiv_crib_hash(current_word)
        # print ll
        # for i, j in sorted(hash_crib_dictionary.iteritems()):
        #     print (i + "->" + str(j))
    print(len(hash_crib_dictionary))


def get_possible_matching_words_of_max_length(partial, length):
    keys_avail = [i for i in hash_crib_dictionary if partial in i]
    candidates = []
    for itms in keys_avail:
        candidates += [i for i in hash_crib_dictionary[itms] if len(i) <= length]
    print (set(candidates))

def validate_word(word):
    if word in all_available_words:
        return True



if __name__ == '__main__':
    # fin_spaces(mof)
    # create_hash_crib()
    # get_possible_matching_words_of_max_length("he", 6)
    fill_partial_words(mof)
