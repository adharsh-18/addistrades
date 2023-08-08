import hashlib
def secure(x):
    enc_word=x.encode('utf32')
    xs=hashlib.md5(enc_word.strip()).hexdigest()
    return xs

   
print(secure('adharsh'))
