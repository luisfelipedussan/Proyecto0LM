from DISClib.ADT.list import newList
import sys
from typing import Any, Mapping
import config
from DISClib.DataStructures import mapstructure as ht
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt


def Leng_structures(catalog : Mapping[str, Any]):
    
    catalog['terminales'] = mp.newMap(numelements=30,maptype = 'CHAINING')
    catalog['user_defined']= mp.newMap(numelements=1000, maptype= 'CHAINING')
    catalog['funciones'] = mp.newMap(numelements=1000, maptype= 'CHAINING')
    catalog['parametros'] = mp.newMap(numelements= 1000,maptype='CHAINING')
    
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
parentesis = False
parentesis2 = True
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
    contador = 1
    for line in lines: 
        if line=="\n" or line =="\t": 
            contador += 1 
            continue
        contents = line.strip().split() # la linea del script del robot que se esta examinando.
        #Evalua todos los posibles primeros argumentos.
        
        verificar_comando(contents,contador)
        if correct == False: # si encuentra un error ya no tiene qeu buscar mas.
            break
        contador += 1
        
    
    #Esta función toma linea por linea y revisa si dicha linea en particular está bien escrita    
def verificar_comando(contents,contador):
    
    global parentesis
    global parentesis2
    global correct
    global output
    global end
    
    if contents[0]== "DEFINE":
            try:
                #verifica que el nombre dado a la variable no sea una palabra reservada del lenguaje.
                if mp.get(catalog['terminales'],contents[1])!= None: 
                 print('Error:')
                 print('El nombre dado para la variable definida no puede ser una de las palabras reservadas\n En:', " ".join(contents))
                 print("\n")
                correct = False
                # Intenta guardar el valor asignado a la variable por el usuario.
                mp.put(catalog['user_defined'],contents[1],int(contents[2]))
            except ValueError:
                print('Error en línea:',contador)
                print('El valor a guardar en la variable debe ser un numero entero\n En:', " ".join(contents))
                print("\n")
                correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=3:
                print('Error en línea:',contador)
                print('Se esperaban solo 3 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "MOVE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "RIGHT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "LEFT":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "ROTATE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
        # este tampoco es igual a la mayoria.
    elif contents[0]== "LOOK":
            try:
                if contents[1]!='N' and contents[1]!='E' and contents[1]!='W' and contents[1]!='S':
                    print('Error en línea:',contador)
                    print('El argumento para el comando LOOK no es valido. Los argumentos permitidos son: N, E, W o S.\n En:', " ".join(contents))
                    print("\n")
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
                print("\n")
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "DROP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
                print("\n")
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                correct = False
                print("\n")
    elif contents[0]== "FREE":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero o una varibale definida','\n En:', " ".join(contents))
                    print("\n")
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
    elif contents[0]== "PICK":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
    elif contents[0]== "POP":
            try:
                int(contents[1])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[1])==None and mp.get(catalog['parametros'], contents[1]== None): # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                print("\n")
                correct = False
            if len(contents)!=2:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
        # Este tambien es diferente a la mayoria.
    elif contents[0]== "CHECK":
            try:
                if contents[1]!= 'C' and contents[1]!= 'B':
                    print('Error en línea:',contador)
                    print('El argumento para el comando CHECK no es valido. Los argumentos permitidos son: C o B seguidos del numero a revisar.\n En:', " ".join(contents))
                    print("\n")
                int(contents[2])
            except ValueError:
                if mp.get(catalog['user_defined'],contents[2])==None: # verifica si el numero de veces a moverse no es una variable previamente definida.
                    print('Error en línea:',contador)
                    print('El argumento para', contents[0] ,'debe ser un numero entero','\n En:', " ".join(contents))
                    print("\n")
                    correct = False
            except IndexError:
                print('Error en línea:',contador)
                print('Faltan argumentos en la entrada\n En:', " ".join(contents))
                correct = False
            if len(contents)!=3:
                print('Error en línea:',contador)
                print('Se esperaban solo 2 argumentos pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
        #Este ya no es igual a los demas.
    elif contents[0]== "BLOCKEDP":
            if len(contents)!=1:
                print('Error en línea:',contador)
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print("\n") 
                correct = False
    elif contents[0] == "NOP" or contents[0] == "NOP]":
            if len(contents) != 1:
                print('Error en línea:',contador)
                print('Se esperaba solo 1 argumento(s) pero se recibieron mas\n En:', " ".join(contents))
                print("\n")
                correct = False
            elif contents[0][-1] == "]":
                if parentesis2== True:
                    print('Error en línea:',contador) 
                    print("Se encontró una cadena de bloque que nunca fue abierta")
                    print("\n")
                    correct = False
                elif parentesis2 == False:
                    parentesis2 = True
    elif contents[0]== "(BLOCK":
            parentesis = True
            if len(contents) != 1:
                del contents[0]
                contador -= 1
                verificar_comando(contents,contador)
    elif contents[0] == (")") or contents[-1][len(contents[-1])-1] == (")"):
            if parentesis == False:
                print('Error en línea:',contador)
                print ("Primero se debe abrir un bloque de código")
                print("\n")
                correct = False
            elif parentesis == True:
                parentesis = False
    elif contents[0]== "IF":
            try:
                contents[1] == "BLOCKEDP" or contents[1] == "!BLOCKEDP" or contents[2][0] == "["  
            except ValueError:
                print('Error en línea:',contador)
                print("Revisa la función IF")
                print("\n")
                correct = False
            if contents[2][0] =="[" or contents[-1] == "[":
                parentesis2= False
    elif contents[0] == "]":
        if parentesis2 == False:
            parentesis2 = True
        if parentesis2 == True:
            print('Error en línea:',contador)
            print("No se abrió previamente ningún bloque")
            print("\n")
            correct = False
    elif contents[0]== "REAPEAT":
        output = True
        #revisa si n es una variable defininda o un número entero
        try:
            if mp.get(catalog['user_defined'],contents[1]) == None: # si es una variable previamente definida esto es false y no entra al if.
                int(contents[1]) # si entra es porque no es una variable definida por el usuario y entonces debe ser un numero entero.
        except ValueError:
            print('Error en línea:',contador)
            print("La variable n no es un entero\n En:", " ".join(contents))
            print("\n")
            correct = False
        try:
            assert contents[2].startswith("[") , "falta el corchete de apertura: [. "
        except:
            print('Error en línea:',contador)
            print("sintaxis incorrecta para definir un comando REPEAT \n En: ", " ".join(contents))
            print("\n")
            correct = False
    elif contents[0]== "TO":
        output = False
        end = False
        #Revisión de la la función definida
        try:
            if  mp.get( catalog['funciones'],str(contents[1])) == None:
                mp.put(catalog['funciones'],str(contents[1]),None)
            else:
                print('Error en línea:',contador)
                print("La función ya estaba definida previamente")
                print("\n")
                correct = False
        except ValueError:
            print('Error en línea:',contador)
            print("El nombre de la función debe ser de tipo str")
            print("\n")
            correct = False
        #revisión de los parametros definidos
        lcon = len(contents)
        if lcon > 1 :
            del contents[0]
            del contents[0]
            for param in contents:
                if param[0] != ":" :
                    print('Error en línea:',contador)
                    print("Para definir un parametro debe comenzar con :")
                    print("\n")
                    correct = False
                else:
                    mp.put(catalog['parametros'],param,None)    
    elif contents[0] == "OUTPUT" or contents[0] == "output":
        if output == False:
            output = True
        elif output == True:
            print("Error en la línea:", contador)
            print(contents)
            print("No existe la apertura de alguna función")
            print(len(contents))
            print("\n")
        if len(contents) > 1:
            del contents[0]
            contador -= 1
            verificar_comando(contents,contador)
    elif contents[0] == "END":
        if end == False:
            end = True
        elif end == True:
            print ("Error en la línea:",contador)
            print("No se le puede poner fin a una función que nunca fue abierta")
            print("\n")
    elif  contents[0] == mp.get(catalog['funciones'],contents[0]) != None:
            for param in range(1,len(contents)):
                if mp.get(catalog['parametros'],param) == None:
                    print("Error en línea:",contador)
                    print("No se ha definido alguno de los parametros")
                    print("\n")
    else:
            print("Error en la línea:", contador)
            print("Lo escrito, no está definido dentro del lenguaje")
            print("\n")
        

# COMENTARIOS:
# Try except es para manejo de excepciones, entonces solo entra en un except si el codigo en el try lazo un error.  
        
        
            
             
                
                

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

        # elif contents[0]== "END":


#RESPUESTA BUSCADA:
