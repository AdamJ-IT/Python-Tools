### This takes file called "hashme.txt" and ouptuts a list of strings and outputs md5 hash. maybe usafull for ctf's.###

import hashlib
import os
#open file, take list of strings, md5 hash them , output

#open file
z = open("hashme.txt")
x = z.readlines()
#generate a hash

for line in x:
    
    hs = hashlib.md5(line.encode()).hexdigest()
    c = "\n" + line + hs
    print(c)

z.close()
