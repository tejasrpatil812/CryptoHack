from Crypto.Util import *

st= '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

st_ord = [e for e in number.long_to_bytes(int(st,16))]
beg_ord = [ord(c) for c in 'crypto{']
key_ord = [beg_ord[i]^st_ord[i] for i in range(len(beg_ord))]

#print(''.join(chr(e) for e in key_ord))
        #Out -> 'myXORke'
        #i'll ad the character 'y'
key_ord.append(ord('y'))

res = []
for i in range(len(st_ord)):
        res.append(st_ord[i]^key_ord[i%8])
print(''.join(chr(e) for e in res))