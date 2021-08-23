import config
from DISClib.DataStructures import mapstructure as ht
from DISClib.ADT import map as mp

fileName = input('Enter file name: ')
try:
    fh = open(fileName)
    for line in fh:
        print(line.upper().rstrip())
except:
     print('the file you want to open was not found')
     


def comandos():
    catalog = { 'comandos' : None,
               'user_defined': None }
    catalog['comandos'] = mp.newMap(numelements=30,maptype = 'CHAINING')
    catalog['user_derfined']= mp.newMap(numelements=1000, maptype= 'CHAINING')
    
    mp.put(catalog["comandos"],'MOVE',0)
    mp.put(catalog["comandos"],'RIGHT',0)
    mp.put(catalog["comandos"],'LEFT',0)
    mp.put(catalog["comandos"],'ROTATE',0)
    mp.put(catalog["comandos"],'LOOK',0)
    mp.put(catalog["comandos"],'DROP',0)
    mp.put(catalog["comandos"],'FREE',0)
    mp.put(catalog["comandos"],'PICK',0)
    mp.put(catalog["comandos"],'POP',0)
    mp.put(catalog["comandos"],'CHECK',0)
    mp.put(catalog["comandos"],'BLOCKEDP',0)
    mp.put(catalog["comandos"],'NOP',0)
    mp.put(catalog["comandos"],'BLOCKE',0)
    mp.put(catalog["comandos"],'REAPEAT',0)
    mp.put(catalog["comandos"],'IF',0)
    mp.put(catalog["comandos"],'DEFINE',0)
    mp.put(catalog["comandos"],'TO',0)
    mp.put(catalog["comandos"],'OUTPUT',0)
    mp.put(catalog["comandos"],'END',0)
    

    
    

    
   