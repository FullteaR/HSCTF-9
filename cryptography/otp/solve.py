import random
from tqdm.auto import tqdm
from Crypto.Util.number import long_to_bytes
from multiprocessing import Pool


#flag = open('flag.txt','rb').read()
#flag = bytes_to_long(flag)

def get(seed):
    l = 328
    for i in range(10000):
        random.seed(seed+i)
        k = random.getrandbits(l)
        flag = 444466166004822947723119817789495250410386698442581656332222628158680136313528100177866881816893557
        flag = flag ^ k # super secure encryption
        if b'ctf4b{' in long_to_bytes(flag):
            print(long_to_bytes(flag))

with Pool() as p:
    imap = p.imap(get, range(10**11//10000))
    list(tqdm(imap, total=10**11//10000))