from DISClib.ADT.list import newList
import sys
from typing import Any, Mapping
import config
from DISClib.DataStructures import mapstructure as ht
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt


def Leng_structures(catalog : Mapping[str, Any]):
    
    catalog['terminales'] = mp.newMap(numelements=30,maptype = 'CHAINING')
    catalog['user_defined']= mp.newMap(numelements=100, maptype= 'CHAINING')
    catalog['funciones'] = mp.newMap(numelements=100, maptype= 'CHAINING')
    catalog['parametros'] = mp.newMap(numelements= 100,maptype='CHAINING')
    
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
            'user_defined': None,
            'funciones': None,
            'parametros' : None
                    }
Leng_structures(catalog) #crea los diccionarios donde se guarda el lenguaje predefinido y el definido por el usuario.
correct = True #empieza suponiendo que el script esta bien escrito.
parentesis = 0
brackets = 0
output = True
end = True
    
def verify_sintax():
    fileName = input('Enter file name: ')
    print("\n")
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
        if correct == False: # si encuentra un error ya no tiene qeu buscar mas.
            break
        
    
#Esta función toma linea por linea y revisa si dicha linea en particular está bien escrita    
def verificar_comando(contents):
    global parentesis
    global brackets
    global correct
    global output
    global end
   # print(contents)

    # aqui entra cuando el comando ingresado contiene un cierre: ] o ):
    if contents[-1].endswith("]") or contents[-1].endswith(")"):
        cadena = ""
        if contents[-1].endswith("]"):
            cadena = contents[-1].replace("]","",1)
            brackets -=1 
        elif contents[-1].endswith(")"):
            cadena = contents[-1].replace(")","",1)
            parentesis -=1
        contents[-1] = cadena
        if len(contents[-1])>0:
            verificar_comando(contents)
    elif contents[0]== "DEFINE": # en clase dijeron que las variables se sobre escriben. 
            try:
                #verifica que el nombre dado a la variable no sea una palabra reservada del lenguaje.
                if mp.get(catalog['terminales'],contents[1])!= None: 
                 print('Error:')
                 print('El nombre dado para la variable definida no puede ser una de las palabras reservadas\n En:', " ".join(contents))
                 print("\n")
                 correct = False
                # Intenta guardar el valor asignado a la variable por el usuario.
                #reemplaza el valor (permite sobreescribir una variable)
                mp.put(catalog['user_defined'],contents[1],int(contents[2]))
            except ValueError:
                print('Error en línea:')
                print('El valor a guardar en la variable debe ser un numero entero\n En:', " ".join(contents))
                print("\n")
                correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>3:
                print('Error en línea:')
                print('Se esperaban solo 3 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "MOVE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "RIGHT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "LEFT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "ROTATE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    # este tampoco es igual a la mayoria.
    elif contents[0]== "LOOK":
            try:
                if contents[1]!='N' and contents[1]!='E' and contents[1]!='W' and contents[1]!='S':
                    print('Error en línea:')
                    print('El argumento para el comando LOOK no es valido. Los argumentos permitidos son: N, E, W o S.\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
                print("\n")
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "DROP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
                print("\n")
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                correct = False
                print("\n")
    elif contents[0]== "FREE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "PICK":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)>2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "POP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1])== None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
        # Este tambien es diferente a la mayoria.
    elif contents[0]== "CHECK":
            try:
                if contents[1]!= 'C' and contents[1]!= 'B':
                    print('Error en línea:')
                    print('El argumento para el comando CHECK no es valido. Los argumentos permitidos son: C o B seguidos del numero a revisar.\n En:', " ".join(contents))
                    print("\n")
                    correct = False
                int(contents[2])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[2])==None and mp.get(catalog['parametros'],contents[2])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:')
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una variable o un parametro','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:')
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
            if len(contents)>3:
                print('Error en línea:')
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
        #Este ya no es igual a los demas.
    elif contents[0]== "BLOCKEDP":
            if len(contents)!=1:
                print('Error en línea:')
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print("\n") 
                correct = False
    elif contents[0] == "NOP" :
            if len(contents) != 1:
                print('Error en línea:')
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "(BLOCK":
            parentesis +=1
            if len(contents) != 1:
                del contents[0]
                verificar_comando(contents)
    elif contents[0] == (")") or contents[-1].endswith(")"):
            if  parentesis==0:
                print('Error en línea:')
                print("Error En:", " ".join(contents))
                print ("Primero se debe abrir un bloque de código")
                print("\n")
                correct = False
            elif parentesis>=1:
                parentesis -= 1
    elif contents[0]== "IF":
            try:
               assert (contents[1] == "BLOCKEDP" or contents[1] == "!BLOCKEDP") and contents[2][0] == "["  
            except:
                print('Error en línea:')
                print("Error En:", " ".join(contents))
                print("El IF debe contener el booleano BLOCKEDP ademas de la apertura del corchete.")
                print("\n")
                correct = False
            try:
                if contents[2][0] =="[" or contents[-1] == "[":
                    brackets +=1
                if len(contents[2])>1:
                    del contents[0]
                    del contents[0]
                    cadena = contents[0].replace("[","",1)
                    contents[0] = cadena
                    verificar_comando(contents)
            except:
                print('Error en línea:')
                print("Error En:", " ".join(contents))
                print("Revisa la función IF")
                print("\n")
                correct = False
    elif contents[0] == "]":
        if brackets >=1:
            brackets -=1
        if brackets == 0:
            print('Error en línea:')
            print("Error En:", " ".join(contents))
            print("No se abrió previamente ningún bloque")
            print("\n")
            correct = False
    elif contents[0]== "(REAPEAT":
        parentesis += 1
        #revisa si n es una variable defininda o un número entero
        try:
            if mp.get(catalog['user_defined'],contents[1]) == None and mp.get(catalog['parametros'],contents[1])==None: # si es una variable previamente definida esto es false y no entra al if.
                int(contents[1]) # si entra es porque no es una variable definida por el usuario y entonces debe ser un numero entero.
        except ValueError:
            print('Error en línea:')
            print("La variable n no es un entero\n En:", " ".join(contents))
            print("\n")
            correct = False
        try:
            assert contents[2].startswith("[")
            if len(contents[2])>1: # si tiene un comando seguido del corchete.
                del contents[0] # borra REPEAT
                del contents[0] # borra n
                cadena = contents[0].replace("[","",1)
                contents[0] = cadena
                verificar_comando(contents)
        except:
            print('Error en línea:')
            print("Sintaxis incorrecta para definir un comando REPEAT, falta corchete de apertura: [. \n En: ", " ".join(contents))
            print("\n")
            correct = False
    elif contents[0]== "TO":
        output = False
        end = False
        #Revisión de la la función definida
        if  mp.get(catalog['funciones'],contents[1]) == None:
            if len(contents)>2:
                mp.put(catalog['funciones'],contents[1], contents[2:]) 
                for param in contents[2:]:
                    if param[0].startswith(":")==False:
                        print('Error en línea:')
                        print("Error En:", " ".join(contents))
                        print("Para definir un parametro debe comenzar con :")
                        print("\n")
                        correct = False
                    else:
                        mp.put(catalog['parametros'],param,None)   
            else:
                mp.put(catalog['funciones'],contents[1], None)
        else:
            print('Error en línea:')
            print("Error En:", " ".join(contents))
            print("La función ya estaba definida previamente")
            print("\n")
            correct = False 
    elif contents[0] == "OUTPUT":
        if output == False:
            output = True
        elif output == True:
            print("Error en la línea:",)
            print("Error En:", " ".join(contents))
            print("No existe la apertura de alguna función")
            print("\n")
            correct = False
        if len(contents) > 1:
            del contents[0]
            verificar_comando(contents)
    elif contents[0] == "END":
        if end == False:
            end = True
        elif end == True:
            print ("Error en la línea:")
            print("Error En:", " ".join(contents))
            print("No se le puede poner fin a una función que nunca fue abierta")
            print("\n")
            correct = False
        if len(contents) > 1: # No puede haber nada justo antes o despues del END.
            print('Error en línea:')
            print('Se esperaba solo 1 argumento pero se recibieron mas\n En:', " ".join(contents))
            print("\n")
            correct = False
        
    else:
        if  mp.get(catalog['funciones'],contents[0])!= None: # si entra es porque el comando ingresado es un llamado a una FUNCION.
            # verifica que la funcion se este llamando correctamente:
            listaP = mp.get(catalog['funciones'],contents[0])['value']
            if listaP != None:
                if len(contents[1:]) != len(listaP): #verifica que el numero de argumentos ingresados coicida con el numero de parametros definidos en la funcion.
                    print("Error En:", " ".join(contents))
                    print("el numero de argumentos ingresados NO coicide con el numero de parametros definidos en la funcion.")
                    print("\n")
                    correct = False
        else:
            print("Error En:", " ".join(contents))
            print("Lo escrito, no está definido dentro del lenguaje")
            print("\n")
            correct = False
#COMENTARIOS:
# variables se tienen que buscar tanto en user defined como en parameters de funciones. (caso OUTPUT DROP :o) LISTO.
# repeat tiene tambien parentesis de apertura y cierre. LISTO
# Cualquier comando puede empezar o terminar por [] porque puede aparecer como primer o ultimo comando en un IF o en un REPEAT. LISTO.
# en REPEAT porque hay un output = true?
# Se tiene que permitir sobreescribir variables (en DEFINE). LISTO.
#Revisar elif en linea 334. solo debe verificar si el UNICO contenido en el comando es ) de cierre. lo otro que verifica interfiere con el comentario 3. LISTO.


verify_sintax()
if correct == False:
    print("\n")
    print("**********")
    print("El código está incorrectamente escrito")
    print("**********")
    print("\n")
else:
    print("\n")
    print("**********")
    print("El código está correctamente escrito")
    print("**********")
    print("\n")
