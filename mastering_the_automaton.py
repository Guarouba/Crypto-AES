def capitalize(val):
    return chr(ord(val[0]) - 32).join(val[1:]) if len(val) > 1 else chr(ord(val) - 32)

