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
    
catalog = { 'terminales' : None,
                    'user_defined': None }
Leng_structures(catalog) #crea los diccionarios donde se guarda el lenguaje predefinido y el definido por el usuario.
correct = False #empieza suponiendo que el script esta bien escrito.
parentesis = False
    
def verify_sintax():
    fileName = input('Enter file name: ')
    try:
        fh = open(fileName)
        lines = fh.readlines()
    except:
        print('the file you want to open was not found.','Error class: ',sys.exc_info()[0])    
# si todo sale bien empieza a leer el archivo.
    for line in lines: 
        if line=="\n" or line =="\t": 
            continue
        contents = line.strip().split() # la linea del script del robot que se esta examinando.
        #Evalua todos los posibles primeros argumentos.
        verificar_comando(contents)
        
def verificar_comando(contents):
    global parentesis
    if contents[0]== "DEFINE":
            try:
                #verifica que el nombre dado a la variable no sea una palabra reservada del lenguaje.
                if mp.get(catalog['terminales'],contents[1])!= None: 
                 print('Error:')
                 print('El nombre dado para la variable definida no puede ser una de las palabras reservadas\n En:', " ".join(contents))
                # Intenta guardar el valor asignado a la variable por el usuario.
                mp.put(catalog['user_defined'],contents[1],int(contents[2]))
            except ValueError:
                print('Error:')
                print('El valor a guardar en la variable debe ser un numero entero\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=3:
                print('Error:')
                print('Se esperaban solo 3 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "MOVE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "RIGHT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "LEFT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "ROTATE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
        # este tampoco es igual a la mayoria.
    elif contents[0]== "LOOK":
            try:
                if contents[1]!='N' and contents[1]!='E' and contents[1]!='W' and contents[1]!='S':
                    print('Error:')
                    print('El argumento para el comando LOOK no es valido. Los argumentos permitidos son: N, E, W o S.\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "DROP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "FREE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "PICK":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
    elif contents[0]== "POP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=2:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
        # Este tambien es diferente a la mayoria.
    elif contents[0]== "CHECK":
            try:
                if contents[1]!= 'C' and contents[1]!= 'B':
                    print('Error:')
                    print('El argumento para el comando CHECK no es valido. Los argumentos permitidos son: C o B seguidos del numero a revisar.\n En:', " ".join(contents))
                int(contents[2])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[2])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
            if len(contents)!=3:
                print('Error:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
        #Este ya no es igual a los demas.
    elif contents[0]== "BLOCKEDP":
            if len(contents)!=1:
                print('Error:')
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente') 
    elif contents[0]== "NOP":
            if len(contents) != 1:
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente') 
    elif contents[0]== "(BLOCK":
            parentesis = True
            if len(contents) != 1:
                del contents[0]
                verificar_comando(contents)
    elif contents[0] == (")"):
            if parentesis == False:
                print("Error:")
                print ("Primero se debe abrir un bloque de código")
                print('El parser se ha detenido, Corrige tu script he intenta nuevamente')
            if parentesis == True:
                parentesis = False
        
        
        # elif contents[0]== "REAPEAT":
        # elif contents[0]== "IF":
        # elif contents[0]== "TO":
        # elif contents[0]== "OUTPUT":
        # elif contents[0]== "END":
        # else 



#RESPUESTA BUSCADA:
verify_sintax()