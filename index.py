file = 'files/' + input("FILE: ")



# GZIP
import gzip
import shutil
with open(file, 'rb') as f_in:
    with gzip.open(file + '.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

# BZ2ZIP
import bz2
import shutil

with open(file, 'rb') as f_in:
    with bz2.open(file + '.bz2', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

import os
 
print("----------------------------------------------------")
print(file)
print('Default: ',  os.path.getsize(file) / 1000 , 'Kb')
print('BZ2: ',  os.path.getsize(file + '.bz2') / 1000 , 'Kb')
print('GZ: ',  os.path.getsize(file + '.gz') / 1000 , 'Kb')
print("----------------------------------------------------")