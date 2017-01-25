# - Jeahyeok Han (Jack)

import os, sys
from sqlitedict import SqliteDict

# python version check
#print (sys.version_info)
if sys.version_info.major < 3 :
    print ('Only for the Python3')
    exit()

'''
if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    import base64
    print (base64.b64encode(data).decode())
else:
     # Python 2 code in this block
     print (data.encode("base64"))
'''

file = str(sys.argv[1])
#file = 'intermediate_data.sqlite'

print (str(file))


mydict = SqliteDict(file, autocommit=True)

print (len(mydict)) # etc... all dict functions work
#print (mydict.keys())

for item in mydict:
    print ('---------------------------------------------')
    print (item)
    print (mydict[item])
    

mydict.close()


