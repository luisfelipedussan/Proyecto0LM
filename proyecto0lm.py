import sys
from typing import Any, Mapping
import config
from DISClib.DataStructures import mapstructure as ht
from DISClib.ADT import map as mp


def Leng_structures(catalog : Mapping[str, Any]):
    
    catalog['terminales'] = mp.newMap(numelements=30,maptype = 'CHAINING')
    catalog['user_defined']= mp.newMap(numelements=1000, maptype= 'CHAINING')
    
    mp.put(catalog["terminales"],'MOVE',0)
    mp.put(catalog["terminales"],'RIGHT',0)
    mp.put(catalog["terminales"],'LEFT',0)
    mp.put(catalog["terminales"],'ROTATE',0)
    mp.put(catalog["terminales"],'LOOK',0)
    mp.put(catalog["terminales"],'DROP',0)
    mp.put(catalog["terminales"],'FREE',0)
    mp.put(catalog["terminales"],'PICK',0)
    mp.put(catalog["terminales"],'POP',0)
    mp.put(catalog["terminales"],'CHECK',0)
    mp.put(catalog["terminales"],'BLOCKEDP',0)
    mp.put(catalog["terminales"],'NOP',0)
    mp.put(catalog["terminales"],'BLOCK',0)
    mp.put(catalog["terminales"],'REAPEAT',0)
    mp.put(catalog["terminales"],'IF',0)
    mp.put(catalog["terminales"],'DEFINE',0)
    mp.put(catalog["terminales"],'TO',0)
    mp.put(catalog["terminales"],'OUTPUT',0)
    mp.put(catalog["terminales"],'END',0)
    mp.put(catalog["terminales"],'(',0)
    mp.put(catalog["terminales"],')',0)
    mp.put(catalog["terminales"],'[',0)
    mp.put(catalog["terminales"],']',0)
    mp.put(catalog["terminales"],'!',0)
    


def verify_sintax():
    correct = False #empieza suponiendo que el script esta bien escrito.
    fileName = input('Enter file name: ')
    catalog = { 'terminales' : None,
                    'user_defined': None }
    Leng_structures(catalog) #crea los diccionarios donde se guarda el lenguaje predefinido y el definido por el usuario.
    try:
        fh = open(fileName)
        lines = fh.readlines()
    except:
        print('the file you want to open was not found.','Error class: ',sys.exc_info()[0])    

    for line in lines: # si todo sale bien empieza a leer el archivo.
        if line=="\n" or line=="\t": 
            continue
        contents = line.strip().split() # la linea del script del robot que se esta examinando.
        #Evalua todos los posibles primeros argumentos.
        if contents[0]== "DEFINE":

            try:
                #verifica que el nombre dado a la variable no sea una palabra reservada del lenguaje.
                if mp.get(catalog['terminales'],contents[1])!= None: 
                 print('Error:')
                 print('El nombre dado para la variable definida no puede ser una de las palabras reservadas\n En:',line)
                 return correct
                # Intenta guardar el valor asignado a la variable por el usuario.
                mp.put(catalog['user_defined'],contents[1],int(contents[2]))
            except ValueError:
                print('Error:')
                print('El valor a guardar en la variable debe ser un numero entero\n En:',line)
                return correct
            except IndexError:
                print('Error:')
                print('faltan argumentos en la entrada\n En:',line)
                return correct
            if len(contents)!=3:
                print('Error:')
                print('Se esperaban solo 3 argumentos pero se recibieron mas\n En:',line)
                return correct

        elif contents[0]== "MOVE":
            #verifica que el numero de pasos a mover sea un entero:
            try:
                int(contents[1])
            except ValueError:
                print('Error:')
                print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:',line)
                return correct
            except IndexError:
                print('Error:')
                print('faltan argumentos en la entrada\n En:',line)
                return correct
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:',line)
                return correct
            
        elif contents[0]== "RIGHT":
            #verifica que el numero de pasos a mover sea un entero:
            try:
                int(contents[1])
            except ValueError:
                print('Error:')
                print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:',line)
                return correct
            except IndexError:
                print('Error:')
                print('faltan argumentos en la entrada\n En:',line)
                return correct
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:',line)
                return correct
        
        # elif contents[0]== "LEFT":
        # elif contents[0]== "ROTATE":
        # elif contents[0]== "LOOK":
        # elif contents[0]== "DROP":
        # elif contents[0]== "FREE":
        # elif contents[0]== "PICK":
        # elif contents[0]== "POP":
        # elif contents[0]== "CHECK":
        # elif contents[0]== "BLOCKEDP":
        # elif contents[0]== "NOP":
        # elif contents[0]== "BLOCK":
        # elif contents[0]== "REAPEAT":
        # elif contents[0]== "IF":
        # elif contents[0]== "TO":
        # elif contents[0]== "OUTPUT":
        # elif contents[0]== "END":
        # else 



#RESPUESTA BUSCADA:
verify_sintax()