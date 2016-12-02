# -*- coding: utf-8-*
ACCEPTABLE_CHARS = {'41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', 
					'4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', 
					'55', '56', '57', '58', '59', '5a', '61', '62', '63', '64', 
					'65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', 
					'6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', 
					'79', '7a', 'a9', 'a0', 'a7', 'a9', 'b4', '80', '81', '82',
					'86', '87', '88', '8a', '8b', '8c', '8d', '8c', '8d', '8e',
					'8f', '91', '92', '92', '93', '94', '99', '9a', '9b', '9c',
					'9d', 'b8', 'a1', 'a2', 'a6', 'a8', 'aa', 'ab', 'ac', 'ad', 
					'ae', 'af', 'b1', 'b2', 'b3', 'b9', 'ba', 'bb', 'bc', 'bd', 
					'bf', '27', '22'}

def filter(word):
	length = len(word)
	validate_caracter = 0.0
	for caracter in word:
		if caracter.encode("hex") in ACCEPTABLE_CHARS:
			validate_caracter += 1
		elif caracter.encode("hex") == 'c3' or caracter.encode("hex") == 'c5':
			length -=1		

	percent = validate_caracter / length

	if percent >= 0.7:
		return True
	else:
		return False

def get_possible_matching_words_of_max_length(partial, length):
    keys_avail = [i for i in hash_crib_dictionary if partial in i]
    candidates = []
    for itms in keys_avail:
        candidates += [i for i in hash_crib_dictionary[itms] if len(i) <= length]
    print (set(candidates))

def group_word(list_of_word):
	validate_word = 0.0
	for word in list_of_word:
		if filter(word):
			validate_word +=1

	if validate_word !=0:
		percent = validate_word/10

		if percent >= 0.66:
			return True
		else:
			return False
	else:
		return False


w= [,,,,,,,,,]

res= group_word(w)
print(res)

