print('File name and type (file.txt ....)')
file = 'files/' + input("[File] =>  ")


print('How do you want to compress the data?')
print('[1 = BZ]')
print('[2 = GZ]')

type = input('[Number] => ')
import os

# GZIP
def gz():
    import gzip
    import shutil
    with open(file, 'rb') as f_in:
        with gzip.open(file + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("-------------------[DATA SIZE]--------------------")
    print(file)
    print('Default: ',  os.path.getsize(file) / 1000 , 'Kb')
    print('GZ: ',  os.path.getsize(file + '.gz') / 1000 , 'Kb')
    print("----------------------------------------------------")
    

# BZ2ZIP
def bz():
    import bz2
    import shutil
    with open(file, 'rb') as f_in:
        with bz2.open(file + '.bz2', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print("-------------------[DATA SIZE]--------------------")
    print(file)
    print('Default: ',  os.path.getsize(file) / 1000 , 'Kb')
    print('BZ2: ',  os.path.getsize(file + '.bz2') / 1000 , 'Kb')
    print("----------------------------------------------------")

if type == '2':
    gz()

if type == '1':
    bz()

