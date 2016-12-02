# -*- coding: utf-8-*
ACCEPTABLE_CHARS = {'41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', 
					'4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', 
					'55', '56', '57', '58', '59', '5a', '61', '62', '63', '64', 
					'65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', 
					'6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', 
					'79', '7a'}

def filter(word):
	length = len(word)
	validate_caracter = 0.0
	for caracter in word:
		if caracter.encode("hex") in ACCEPTABLE_CHARS:
			validate_caracter += 1
			print("valid")

	print(validate_caracter, " ", length)
	percent = validate_caracter / length
	print(percent)

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


w= "cs'azertyu'(§è!ç'qsdfghjkdfghjkldefrgthjukl"
res= filter(w)
print(res)

