#Emiliano Nuñez Felix - A01645413
#Dylan Pereyra Lopez - A01540618
#Luis Fernando Valderrábano García - A01644530
#Librerias utilizadas en el programa
import random
import math
import time
from statistics import median

#Funciones
#Diseño de barra de vida monstruin
def generar_lifebar(): #Genera una barra de vida completa
    life_bar=[[0,0,0],[0,0,0],[0,0,0]]
    return life_bar

#Funcion que quita puntos de vida
def remove_life(barra_vida,numvid):
    #Comprueba la longitud de la matriz y si la ultima lista esta vacía, la elimina para poder seguir eliminando vidas
    if len(barra_vida[-1])==0:
        del barra_vida[-1]
    #Comprueba la longitud de la matriz y si la longitud de la ultima lista es 1, elimina la lista y continua segun las vidas que tiene que eliminar
    elif len(barra_vida[-1])==1:
        for j in range(1,numvid+1):
            barra_vida[-j].pop(-1)
        del barra_vida[-1]
    #Si no es ninguna de las a anteriores elimina cierta cantidad de vidas
    else:
        for i in range (numvid):
            barra_vida[-1].pop(-1)
            if len(barra_vida[-1])==0:
                del barra_vida[-1]
    return barra_vida

#Función para crear contador para la funcion quitar vidas de los ciclos while (Español)
def while2num (cont,cont2):
    #Revisa en que pregunta está y regresa contador para quitar vidas
    if cont==1 or cont==2:
        cont2=1
    elif cont==3 or cont==4:
        cont2=2  
    else:
        cont2=3
    #Retorna variable contador
    return cont2

#Funcion que imprime la barra de vida dependiendo si el usuario contesto bien
def printbar(lifebar_consola):
    if len(lifebar_consola)==3:
        print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_consola[0][:],"\033[1;33;40m",lifebar_consola[1][:],"\033[1;32;40m",lifebar_consola[2][:],"\033[0m")
    elif len(lifebar_consola)==2:
        print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_consola[0][:],"\033[1;33;40m",lifebar_consola[1][:],"\033[0m")
    elif len(lifebar_consola)==1:
        print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_consola[0][:],"\033[0m")
    elif len(lifebar_consola)==0:
        print('Parece que debilitaste mucho a monstruin, pero no lo haz derrotado completamente! ')
        regenerarbarra()
    
#Funcion que genera un numero random con el parametro que ingreses
def num_rand(rand):
    x=random.randint(1,rand)
    return x

#Funcion que crea la "animación" de cuando derrotas a monstruin
def printbarfin_p():
    barra=generar_lifebar()
    barra2=[]
    print("\033[1;31;40m",barra[0][:],"\033[1;33;40m",barra[1][:],"\033[1;32;40m",barra[2][:],"\033[0m")
    time.sleep(1)
    print("\033[1;31;40m",barra[0][:],"\033[1;31;40m",barra[1][:],"\033[1;31;40m",barra[2][:],"\033[0m")
    for w in range (2):
        barra=remove_life(barra,3)
        time.sleep(1)
        printbarra_roja(barra)
    time.sleep(1)
    print("\033[1;31;40m",barra2,"\033[0m")
    print('Has derrotado completamente a monstruin!')
        
#Funcion que ayuda a la animacion de la barra
def printbarra_roja(y):
    if len(y)==3:
        print("\033[1;31;40m",y[0][:],"\033[1;31;40m",y[1][:],"\033[1;31;40m",y[2][:],"\033[0m")
    elif len(y)==2:
        print("\033[1;31;40m",y[0][:],"\033[1;31;40m",y[1][:],"\033[0m")
    else:
        print("\033[1;31;40m",y[0][:],"\033[0m")

#Función que imprime la animacion de la barra regenerada
def regenerarbarra():
    listax=[]
    for m in range (3):
        z=[0,0,0]
        listax.append(z)
        regprintbar(listax)
        time.sleep(1)
    print('Monstruin se ha recuperado!')

#Función para cambiar de grado si elimino completamente a monstruin
def next_grade (option,gradopri,gradosec,nivelp,winxd):
    if option==True:
        if nivelp==1:
            if gradopri=='a':
                gradopri='b'
            elif gradopri=='b':
                gradopri='c'
            elif gradopri=='c' and nivelp==1:
                nivelp=2
                gradosec='a'
        elif nivelp==2:
            if gradosec=='a':
                gradosec='b'
            elif gradosec=='b':
                gradosec='c'
            elif gradosec=='c':
                winxd=True 
    if option==False:
        winxd=True             
    option=False
    return option,gradopri,gradosec,nivelp,winxd

#Función que le dice al usuario si es elegible para cambiar de nivel y pregunta su respuesta
def eleg_nextgrade(checkbar0, condt):
    if len(checkbar0) == 0:
        resp = input('Felicidades, bajaste mucho la barra de vida de Monstruin, eres elegible para seguir contestando preguntas del siguiente grado!\n¿Deseas continuar?:\n(a) Sí\n(b) No\nTu respuesta: ')
        resp = resp.lower()
        while resp != 'a' and resp != 'b':
            resp = input('Selecciona solamente "a" o "b"\n¿Deseas continuar?:\n(a) Sí\n(b) No\nTu respuesta: ')
            resp = resp.lower()
        if resp == 'a':
            condt = True
        elif resp == 'b':
            condt = False
    return condt        
#Funcion que convierte a color la animacion de regeneracion
def regprintbar(regbarra):
    if len(regbarra)==3:
        print("\033[1;32;40m",regbarra[2][:],"\033[0m",end=' ')
    elif len(regbarra)==2:
        print("\033[1;33;40m",regbarra[1][:],"\033[0m",end=' ')
    elif len(regbarra)==1:
        print("\033[1;31;40m",regbarra[0][:],"\033[0m",end=' ')

#Función para agregar letras para formato de opciones (PREGUNTAS ESPAÑOL)
def concatenar(a,b,c,d):
    lista=[a,b,c,d]
    opciones=['A) ','B) ','C) ','D) '] #Opciones 
    final=[]
    x=len(lista)
    for i in range(x):
        separado=lista[i].split()#Separar respuesta en caracteres y convertirlo en lista
        y=random.choice(opciones)#Esocger una opción aleatoria
        y_indx=opciones.index(y)#Buscar posición de la opción esocgida
        separado.insert(0,y)#Juntar opción con la respuesta separada
        if y in opciones:#Borrar la opción ya escogida antes para no repetir
            opciones.pop(y_indx)
        z="".join(separado)#Volver a juntar la respuesta en string con opcion
        final.append(z)#Guardar 
    return final #retornar lista convertida a formato de opciones

#Función para separar las lineas del archivo (pregunta y respuestas) (PREGUNTAS ESPAÑOL)
def split_questions(x):
    quest = []
    for l in x:
        question, answer, option2, option3, option4 = l.strip().split(':')
        quest.append((question, answer, option2, option3, option4))
    return quest

#Funcion cuando el ususario termine el juego aparezca un mensaje
def end_game(wincondition,condtion,contin,inc,cor,nivelx,gradopx,gradosx,contadorjug):
    gradopx='Primaria'
    gradosx='Secundaria'
    wincondition=True
    print(f"\033[1;32;40m",'Felicidades 🎉',"\033[0m",f'\nTerminaste el juego!!!\nLlegaste al nivel de {gradopx} {nivelx}\nObtuviste {inc} preguntas incorrectas y {cor} correctas!')
    if contadorjug<5:
        answer=input('Ahora puede intentarlo otro jugador o tu mismo de nuevo!\nDeseas otro intento?\na) Sí, deseo volver a intentarlo\nb) Sí, lo intentará una persona distinta\nc) Salir\nTu respuesta: ')
        answer=answer.lower()
        while answer!='a' and answer!='b' and answer!='c':
            answer=(input('Error.. Solo seleccione "a" o "b" o "c"\nAhora puede intentarlo otro jugador o tu mismo de nuevo!\nDeseas otro intento?\na) Sí, deseo volver a intentarlo\nb) Sí, lo intentará una persona distinta\nc) Salir\nTu respuesta: '))
            answer=answer.lower()
        if answer=='a':
            condtion=False
            wincondition=False
            contin=False
        elif answer=='b':
            condtion=True
            wincondition=False
    return wincondition, condtion, contin

#Función para añadir a la lista jugadores
def addlist(listay,nombre,nivel,gradopy,gradosy,incorrectas,correctas,contadordejug):
    gradofinal=''
    if nivel==1:
        if gradopy=='a':
            gradofinal='4°to de Primaria'
        elif gradopy=='b':
            gradofinal='5°to de Primaria'
        elif gradopy=='c':
            gradofinal='6°to de Primaria'
    elif nivel==2:
        if gradosy=='a':
            gradofinal='1°ro de Secundaria'
        elif gradosy=='b':
            gradofinal='2°do de Secundaria'
        elif gradosy=='c':
            gradofinal='3°ro de Secundaria'

    if contadordejug==1:        
        for i in range (6):
            lista2=[]
            for j in range (4):
                lista2.append('Sin datos')
            listay.append(lista2)

    listay[0][0]='Nombre'
    listay[0][1]='Grado al que llegó'
    listay[0][2]='Preguntas correctas'
    listay[0][3]='Preguntas incorrectas'

    listay[contadordejug][0]=nombre
    listay[contadordejug][1]=gradofinal
    listay[contadordejug][2]=correctas
    listay[contadordejug][3]=incorrectas

    imprimirlista(listay)

    return listay

#Función que imprime la lista de jugadores, y acomoda la longitud de la lista segun el mayor
def imprimirlista(listajugadoresy):
    #Códigos para imprimir de colores las columnas
    colores_columnas=["\033[1;33;40m","\033[1;34;40m","\033[1;36;40m","\033[1;35;40m"]
    #Código para que reestablezca el color despues de cada print
    reset_color="\033[0m"
    #Encontrar la longitud máxima de cada columna
    longitudes_maximas=[]
    longitudes_maximas=[]
    longitudes_maximas=[]
    longitudes_maximas=[]
    for i in range(len(listajugadoresy[0])):
        max_longitud=0
        #Iterar a través de las filas para encontrar la longitud máxima en la columna actual
        for fila in listajugadoresy:
            longitud_actual =len(str(fila[i]))
            if longitud_actual>max_longitud:
                max_longitud=longitud_actual
        longitudes_maximas.append(max_longitud)
    #For para recorrer las filas
    for fila in listajugadoresy:
        #For para recorrer las columnas
        for j in range(len(fila)):
            color_columna=colores_columnas[j]
            valor=str(fila[j])
            longitud=longitudes_maximas[j]
            #Imprimir el valor de la matriz con el color de la columna y su respectiva longitud
            print(f"{color_columna}{valor.rjust(longitud)}{reset_color}", end=' ')
        # Agregar un salto de línea con el color default
        print(reset_color)

def moda(): #Calcula la moda de una lista
    moda_correcto = 0
    lista = []
    contador_moda = [0,0,0,0]
    for i in range(13):
        x = random.randint(1,4)
        lista.append(x)
        contador_moda[x-1] += 1
    conteo = max(contador_moda)
    for j in range(4):
        if contador_moda[j] == conteo:
            moda_correcto = j + 1
    return moda_correcto, lista
   
#Lista para almacenar los datos de los jugadores
listajug=[]

#Menu del juego
print("\n\t\tBienvenido! a","\u001b[31m",'"Derrotar a monstruin!"',"\u001b[37m")
print("\nEste es un juego para que puedas desarrollar tus aprendizajes de Español y Mátematicas e intentar derrotar a Monstruin en cada nivel\n")
print('El funcionamiento del juego es simple!\nA continuación seleccionarás el grado que cursas.\nSi contestas correctamente todas las preguntas para tu nivel, podrás avanzar al siguiente grado y demostrar que tan avanzado estás!')

#Variable que nos servirá para el ciclo while
win=False

#Variable para que el usuario continue
continuar=True

#Contador de jugadores
contjug=1

#Grado
grados=0
gradop=0

#Bucle while que repite esto por si el usuario sube de nivel 
while win==False:
    imprimir=True
    while continuar==True:
        #Contador de respuestas correctas e incorrectas
        contador_correct=0
        contador_incorrect=0
        #Ingresar datos del usuario
        name=input('Ingresa tu nombre: ')
        name=name.capitalize()
        print(f'\nEstas son algunas reglas que tienes que seguir {name}, \n1. Contesta correctamente las preguntas para derrotar a Monstruin \n2. Tomate el tiempo necesario para responder las preguntas \n3. Si contestas las preguntas mal, perderas \n4. Diviertete!!! ')
        nivel=int(input(f'\n¿Qué nivel de estudios estas cursando {name}?\nSelecciona tu nivel:\n1) Primaria\n2) Secundaria\nTu selección: '))
        #Si el usuario no ingresa una opción diferente volver a ingresar opción
        while nivel!=1 and nivel!=2:
            print('Por favor, ingresa "1" o "2" para continuar.')
            nivel=int(input(f'\n¿Qué nivel de estudios estas cursando {name}?\nSelecciona tu nivel:\n1. Primaria\n2. Secundaria\nTu selección: '))

        #El usuario selecciona el grado que cursa
        if nivel==1:
            gradop=(input('\n¿Qué grado de primaria estas cursando?\na) 4to primaria\nb) 5to primaria\nc) 6to primaria\nSu selección: '))
            gradop=gradop.lower()
            while gradop != 'a' and gradop != 'b' and gradop != 'c':
                print('Error...\nSolo seleccione una de las opciones que se le da')
                gradop=(input('\n¿Qué grado de primaria estas cursando?\na) 4to primaria\nb) 5to primaria\nc) 6to primaria\nSu selección: '))
        elif nivel==2:
            grados=(input('\n¿Qué grado de secundaria estas cursando?\na) 1ro secundaria\nb) 2do secundaria\nc) 3ro secundaria\nSu selección: '))
            grados=grados.lower()
            while grados != 'a' and grados != 'b' and grados != 'c':
                print('Error...\nSolo seleccione una de las opciones que se le da')
                grados=(input('\n¿Qué grado de secundaria estas cursando?\na) 1ro secundaria\nb) 2do secundaria\nc) 3ro secundaria\nSu selección: '))
        continuar=False
    #Primaria
    if nivel==1:
        matoesp=input('\n¿Qué elijes?, \na) Matematicas \nb) Español \nTu selección: ')
        matoesp=matoesp.lower()
        while matoesp != 'a' and matoesp != 'b' :
            print('Error...\nSolo seleccione una de las opciones que se le da')
            matoesp=input('\n¿Qué elijes?, \na) Matematicas \nb) Español \nTu selección')
        #Mátematicas
        if matoesp=='a':
            #Grado 'a' es 4to de primaria
            if gradop=='a':
                #Crear barra de vida para este grado
                lifebar_pa=generar_lifebar()
                #Pregunta 1
                base=num_rand(20)
                altura=num_rand(20)
                r1=base*altura
                r=base*altura/2 
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1=float(input(f'La base de un triangulo es de {base}, y su altura es de {altura}, ¿Cúal es su area?\nTu respuesta: '))
                if p1==r:
                    print('Muy bien! avanza')
                    contador_correct+=1 
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                else:
                    print(f'Incorrecto, pero mira la base la cual es {base} y la altura es de {altura} se multiplican, \n lo cual da {r1}, y esto se divide entre 2, lo cual da {r}, espero te ayude')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                #Pregunta 2
                # Agrega aquí una pregunta sobre el cálculo de volumen
                longitud = num_rand(10)
                ancho = num_rand(10)
                altura = num_rand(10)
                volumen_correcto = longitud * ancho * altura
                print('Monstruin continua atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p2 = float(input(f'La longitud de un cubo es {longitud}, el ancho es {ancho} y la altura es {altura}, ¿Cuál es su volumen? \nTu respuesta: '))
                if p2 == volumen_correcto:
                    print('¡Respuesta correcta!')
                    contador_correct+=1
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                else:
                    print(f'Incorrecto, el volumen del cubo es {volumen_correcto}. Recuerda que la fórmula del volumen de un cubo es "L X L X L".')
                    contador_incorrect+=1
                    printbar(lifebar_pa)    
                #Pregunta 3
                #Resta de números usando la lógica
                millas_por_recorrer=num_rand(1000)
                millas_conducidas=num_rand(millas_por_recorrer-1)
                millas_restantes=millas_por_recorrer-millas_conducidas
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p3=int(input(f'Uriel manejo {millas_conducidas} millas de un viaje de {millas_por_recorrer} millas. ¿Cuántas millas más necesita manejar para terminar su viaje? \nTu respuesta: '))
                if p3== millas_restantes:
                    print('Felicidades! Estas logrando derrotar a monstruin!')
                    contador_correct+=1
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                else:
                    print(f'Incorrecto, Jim necesita manejar {millas_por_recorrer - millas_conducidas} millas más para terminar su viaje.\n ')
                    contador_incorrect+=1
                    printbar(lifebar_pa)

                #pregunta 4 
                #Potencia 2 a un número
                np=num_rand(10)
                numero_correcto=np**2
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p4=int(input(f'Cual es el resultado de elevar al cuadrado el numero {np} \nTu respuesta: '))
                if p4==numero_correcto:
                    print('Bien!, Siguiente pregunta:')
                    contador_correct+=1 
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                else:
                    print(f'Incorrecto, recuerda que el cuadrado es la multiplicacion de {numero_correcto} por ese mismo numero')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                #pregunta 5
                #Perímetro de un cuadrado
                perimetro = num_rand(100)
                longitud_lado = perimetro/ 4
                print('Monstruin continua atacando, contesta correctamente para para quitarle 3 puntos de vida y acabar con el! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p5=float(input(f'Si el perimetro de un cuadrado es de {perimetro}, cuanto miden sus lados? \nTu respuesta: '))
                if p5==longitud_lado:
                    print('Correcto!')
                    contador_correct+=1 
                    lifebar_pa=remove_life(lifebar_pa,3)  
                    printbar(lifebar_pa)
                else:
                    print('Incorrecto')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)
            #5to de primaria matemáticas
            elif gradop=='b':
                lifebar_pa=generar_lifebar()
                #pregunta 1 radio de circulo
                diametro=random.randint(2,10)
                radio=diametro/2
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1_5=float(input(f'Si un circulo tiene {diametro} cm de diametro, Cual es su radio? \nTu respuesta: '))
                if p1_5==radio:
                    print('Bien! Siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto, recuerda que el radio es la mitad del diametro')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                #pregunta 2 medir diametro con radio
                radio2=random.randint(1,20)
                diametro2=radio2*2
                print('Monstruin continua atacando, contesta correctamente para quitarle 1 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p2_5=float(input(f'si el radio de una circumferencia es de {radio2}, cuanto mide su diametro? \nTu respuesta: '))
                if p2_5==diametro2:
                    print('Vas bien! Siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto, recuerda que para obtener el diametro tienes que multiplicar el radio X2 ')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                #pregunta 3 grapas por hora
                grapas=random.randint(2000,5000)
                horas=random.randint(2,10)
                grapas_por_hora=grapas*horas
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p3_5=float(input(f'Si una engrapadora pone {grapas} grapas por hora, cuantas pone en {horas} horas? \nTu respuesta: '))
                if p3_5==grapas_por_hora:
                    print('Siguiente Prgunta!')
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto, Tienes que multiplicar la cantidad de grapas por la cantidad de horas')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
        
                #pregunta 4 tipos de triangulos
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                triangulo=input('Cuantos tipos de triangulos hay? \na) 4 \nb) 5 \nc) 3 \nd) 1 \n')
            
                if triangulo=='c':
                    print('Perfecto, Siguiente pregunta!')
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Recuerda que hay 3 tipos de triangulos, los cuales son \n Equilatero \n Isoceles \n Escaleno')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                #pregunta 5 division 
                hijos=random.randint(2,6)
                cantidad=round(6580/hijos)
                margen_error = 1
                print('Monstruin continua atacando, contesta correctamente para quitarle 3 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                dinero=float(input(f'Pablo quiere repartir 6580$ entre sus {hijos} hijos y lo quiere repartir en partes iguales,\n¿Cuanto le toca a cada quien?\nTu respuesta: '))
                if cantidad - margen_error <= dinero <= cantidad + margen_error:
                    print('Bien!, Completaste el nivel de 5 grado')
                    lifebar_pa=remove_life(lifebar_pa,3)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto')
                    contador_incorrect+=1
                    printbar(lifebar_pa)
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)
            #Preguntas sexto grado 
            #PREGUNTAS SEXTO GRADO MATEMATICAS
            elif gradop=='c':
                lifebar_pa=generar_lifebar()
                na=random.randint(1,10)
                nc=na*3
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1_6=int(input(f'¿Cuál es el triple del numero {na}? \nTu respuesta: '))
                if p1_6==nc:
                    print('Bien Siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print(f'Incorrecto, recuerda que tienes que multiplicar "{na}" 3 veces para obtener el resultado')
                    printbar(lifebar_pa)
                    contador_incorrect+=1
        
                #pregunta 2
                radio6=random.randint(1, 20)
                circulo=math.pi*radio6**2
                print('Monstruin continua atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                respuesta_usuario=float(input(f'¿Calcula el area de un círculo que tiene un radio de {radio6}? \nTu respuesta: '))
                respuesta_correcta=round(circulo, 2)
                if abs(respuesta_usuario-respuesta_correcta)<=1.0:
                    print('Excelente, siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto, recuerda multiplicar pi por el radio y te dará el resultado')
                    printbar(lifebar_pa)
                    contador_incorrect+=1
                #pregunta 3
                horas=random.randint(2,8)
                kilometros_recorridos=random.randint(100,400)
                promedio=kilometros_recorridos/horas
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p3_6=float(input(f'Si un carro recorre {kilometros_recorridos} kilometros en {horas} horas, \n¿Cuál es su velocidad promedio?\nTu respuesta: '))
                if p3_6==promedio:
                    print('Bien, Siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto, debes de dividir los kilometros recorridos entre las horas')
                    printbar(lifebar_pa)
                    contador_incorrect+=1
                #pregunta4
                cubo=random.randint(1,10)
                respuesta=cubo**3
                print('Monstruin continua atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p4_6=int(input(f'Resuelve: Eleva {cubo} al cubo\nTu respuesta:  '))
                if p4_6==respuesta:
                    print('Bien! Avanza a la siguiente pregunta')
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print(f'Incorrecto, Tienes que multiplicar {cubo} 3 veces para elevarlo al cubo')
                    printbar(lifebar_pa)
                    contador_incorrect+=1
                #pregunta 5
                print('Monstruin continua atacando, contesta correctamente para quitarle 3 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p5_6=float(input('Cual es el valor de pi (redondealo a 4 decimales)\nTu respuesta: '))
                pi=3.1416
                if pi==p5_6:
                    print('Bien acabaste la sección de primaria matemáticas')
                    lifebar_pa=remove_life(lifebar_pa,3)  
                    printbar(lifebar_pa)
                    contador_correct+=1 
                else:
                    print('Incorrecto el valor es redondeado a 4 decimales 3.1416')
                    printbar(lifebar_pa)
                    contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)

        #Español
        if matoesp=='b':
            #4to de Primaria
            if gradop=='a':
                file = open('quest4PE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()  
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0
                cont2while=1
                while cont_while<5:
                    random_question = random.choice(questions)                        
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        printbar(lifebar_pa)
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)   
            #5to de Primaria
            if gradop=='b':
                file = open('quest5PE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()  
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0
                cont2while=1
                while cont_while<5:
                    random_question = random.choice(questions)                        
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)
            #6to de Primaria
            if gradop=='c':
                file = open('quest5PE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()  
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0
                cont2while=1
                while cont_while<5:
                    random_question = random.choice(questions)                        
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)            
    #Secundaria
    elif nivel==2:
        matoesp=input('¿Qué elijes?, \na) Matematicas \nb) Español \nTu selección: ')
        matoesp=matoesp.lower()
        while matoesp != 'a' and matoesp != 'b' :
            print('Error...\nSolo seleccione una de las opciones que se le da')
            matoesp=input('\n¿Qué elijes?, \na) Matematicas \nb) Español \nTu selección')
        #Matematicas
        if matoesp=='a':
            #1ro de Secundaria
            if grados=='a':
                #Primero de Secundaria - Primera Pregunta - Numeros Negativos Suma y Resta   
                lista_sec1_1 = [] #Creacion de lista
                #Generar 3 numeros random en lista
                #Crear barra de vida para este grado
                lifebar_pa=generar_lifebar()
                for i in range(3):
                    x = random.randint(5,30)
                    lista_sec1_1.append(x)
                p1_correcto = lista_sec1_1[0] - lista_sec1_1[1] + (- lista_sec1_1[2]) #Resultado correcto
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1 = int(input(f"Calcula el resultado de la siguiente operacion: {lista_sec1_1[0]} - {lista_sec1_1[1]} + (-{lista_sec1_1[2]}):\nTu respuesta: ")) #Resultado del usuario
                #Comparacion de resultado correcto con resultado del usuario
                if p1 == p1_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,1)
                    printbar  
                    
                elif p1 != p1_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p1_correcto}")
                    contador_incorrect += 1
                    
                    

                #Primero de Secundaria - Segunda Pregunta - Numeros Negativos Multiplicacion
                lista_sec1_2 = [] #Creacion de lista
                #Generar 3 numeros random en lista
                for i in range(3):
                    x = random.randint(2,10)
                    lista_sec1_2.append(x)
                p2_correcto = lista_sec1_2[0] * -lista_sec1_2[1] * lista_sec1_2[2] #Respuesta correcta
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p2 = int(input(f"\nCalcula el resultado de la siguiente operacion: ({lista_sec1_2[0]})(-{lista_sec1_2[1]})({lista_sec1_2[2]}):\nTu respuesta: ")) #Resultado del usuario
                #Comparacion de resultado correcto con resultado del usuario
                if p2 == p2_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    
                elif p2 != p2_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p2_correcto}")
                    contador_incorrect += 1
                    
                    
                #Primero de Secundaria - Tercera Pregunta - Combinar terminos semejantes
                lista_sec1_3 = [] #Creacion de lista
                #3 numeros random para la lista
                for i in range(3):
                    x = random.randint(3,10)
                    lista_sec1_3.append(x)
                #Combinar terminos semejantes
                semejantes = -lista_sec1_3[1] - lista_sec1_3[2]
                p3_correcto = f"{lista_sec1_3[0]}{semejantes}a"
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p3 = input(f"\nCombina los terminos semejantes de la siguiente operacion: {lista_sec1_3[0]} - {lista_sec1_3[1]}a + (-{lista_sec1_3[2]}a)\nTu respuesta: ")
                p3 = p3.replace(" ","") #Quitar espacios para comparacion
                #Comparacion del usuario a resultado correcto
                if p3 == p3_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,2)  
                                      
                elif p3 != p3_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p3_correcto}")
                    contador_incorrect += 1
                    
                    
                #Primero de Secundaria - Cuarta Pregunta - Problema verbal de impuestos
                precio_pc = random.randint(5000,20000)
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p4 = float(input(f"\nDavid quiere comprar una computadora que cuesta {precio_pc} antes de impuestos. Calcula el precio de la computadora despues del IVA (16%):\nTu respuesta: "))
                p4_correcto = precio_pc + precio_pc * .16 #Respuesta correcta
                p4_correcto = round(p4_correcto,2)
                #Comparacion de resultados
                if p4 == p4_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                     
                        
                if p4 != p4_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p4_correcto}")
                    contador_incorrect += 1
                                     

                #Primero de Secundaria - Quinta Pregunta - Convertir de fraccion a decimal
                lista = []
                for i in range(2):
                    x = random.randint(2,10)
                    lista.append(x)
                p5_correcto = round(lista[0]/lista[1],2)
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 3 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p5 = float(input(f"\nConvierte la fraccion {lista[0]} / {lista[1]} a decimales (redondea a dos digitos):\nTu respuesta: "))
                if p5 == p5_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,3)  
                    
                if p5 != p5_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p1_correcto}")
                    contador_incorrect += 1
                                      
                    
            #2do de Secundaria
            if grados=='b':
                #Crear barra de vida para este grado
                lifebar_pa=generar_lifebar()
                #Segundo de Secundaria - Primera Pregunta - Exponentes
                #-x**2or4 + y**0 - z**1or3or5
                y = random.randint(1,100)
                exponente1 = 0
                exponente2 = 0
                if y > 75:
                    exponente1 = 4
                    exponente2 = 1
                elif y > 50 and y < 75:
                    exponente1 = 4
                    exponente2 = 5
                elif y < 50:
                    exponente1 = 2
                    exponente2 = 3
                    
                lista_sec2_1 = [] #Creacion de lista
                for i in range(3):
                    x = random.randint(2,5)
                    lista_sec2_1.append(x)
                p1_correcto = -lista_sec2_1[0]**exponente1 + lista_sec2_1[1]**0 - lista_sec2_1[2]**exponente2
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1 = int(input(f"\nResuelve la siguiente operacion que utiliza exponentes: -{lista_sec2_1[0]}^{exponente1} + {lista_sec2_1[1]}^0 - {lista_sec2_1[2]}^{exponente2}\nTu respuesta: "))
                if p1 == p1_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)                    
                if p1 != p1_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p1_correcto}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)

                #Segundo de Secundaria - Segunda Pregunta - Algebra
                x1 = random.randint(5,10)
                x2 = random.randint(1,x1-2)
                y1 = random.randint(5,10)
                y2 = random.randint(1,y1-2)
                algebra_correcto = [x1-x2,y1-y2]
                algebra_correctostr = f"{algebra_correcto[0]}x+{algebra_correcto[1]}y"
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p2 = input(f"\nSimplifica la expresión algebraica {x1}x - {x2}x + {y1}y - {y2}y:\nTu respuesta: ")
                p2 = p2.replace(" ","")
                if p2 == algebra_correctostr:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)                    
                if p2 != algebra_correctostr:
                    print(f"Respuesta incorrecta. La respuesta correcta es {algebra_correctostr}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)
                    
                #Segundo de Secundaria - Tercera Pregunta a Quinta Pregunta - Ecuaciones con variables en ambos lados
                #3 - 5x = 8x - 7
                for i in range(3):
                    lista = []
                    for i in range(4):
                        x = random.randint(2,10)
                        lista.append(x)
                        
                    den = -lista[1] - lista[2]
                    num = -lista[3] - lista[0]
                    equis = num/den
                    p2_correcto = round(equis,2)
                    print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    p2 = float(input(f"\nEncuentra el valor de x de la siguiente operacion con la variable en ambos lados: {lista[0]} - {lista[1]}x = {lista[2]}x - {lista[3]}\nx = "))
                    if p2 == p2_correcto:
                        print("Respuesta correcta.")
                        contador_correct += 1
                        lifebar_pa=remove_life(lifebar_pa,2)  
                        printbar(lifebar_pa)
                    elif p2 != p2_correcto:
                        print(f"Respuesta incorrecta. x = {p2_correcto}")
                        contador_incorrect += 1
                        printbar(lifebar_pa)
            #3ro de Secundaria
            if grados=='c':
                #Crear barra de vida para este grado
                lifebar_pa=generar_lifebar()
                #Tercero de Secundaria - Primera Pregunta - MCD
                lista = []
                for i in range(2):
                    x = random.randint(10,100)
                    lista.append(x)
                p1_correcto = math.gcd(lista[0],lista[1])
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 punto de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print('Barra de vida de monstruin: '"\033[1;31;40m",lifebar_pa[0][:],"\033[1;33;40m",lifebar_pa[1][:],"\033[1;32;40m",lifebar_pa[2][:],"\033[0m")
                p1 = int(input(f"\nIdentifica el maximo comun divisor de los siguientes dos numeros: {lista[0]},{lista[1]}\nTu respuesta: "))
                if p1 == p1_correcto:
                    print("Respuesta correcta")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                if p1 != p1_correcto:
                    print(f"Respuesta incorrecta. El minimo comun divisor es {p1_correcto}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)
                    
                #Tercero de Secundaria - Segunda Pregunta - MCM
                lista = []
                for i in range(2):
                    x = random.randint(10,100)
                    lista.append(x)
                p2_correcto = math.lcm(lista[0],lista[1])
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p2 = int(input(f"\nIdentifica el minimo comun multiplo de los siguientes dos numeros: {lista[0]},{lista[1]}\nTu respuesta: "))
                if p2 == p2_correcto:
                    print("Respuesta correcta")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,1)  
                    printbar(lifebar_pa)
                if p2 != p2_correcto:
                    print(f"Respuesta incorrecta. El minimo comun divisor es {p2_correcto}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)
                    
                #Tercero de Secundaria - Tercera Pregunta - Pendiente de una recta
                matriz = []

                for i in range(2):
                    row = []
                    for j in range(2):
                        x = random.randint(2,10)
                        row.append(x)
                    matriz.append(row)

                if matriz[0][0] == matriz[1][0]: #Para que no se divida entre 0
                    matriz[1][0] += 1

                p3_correcto = (matriz[1][1]-matriz[0][1]) / (matriz[1][0]-matriz[0][0]) #Cada lista de la matriz es un punto, tomando pos 0 como x y pos 1 como y
                round(p3_correcto,2)
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 2 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p3 = float(input(f"\nx1 = {matriz[0][0]}, y1 = {matriz[0][1]}\nx2 = {matriz[1][0]}, y2 = {matriz[1][1]}\nCalcula la pendiente de la recta: "))

                if p3 == p3_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    printbar(lifebar_pa)
                if p3 != p3_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p3_correcto}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)
                    
                #Tercero de Secundaria - Cuarta Pregunta - Moda
                moda, lista_moda = moda()
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 1 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                print(f"\nConsidera la siguiente lista de numeros: {lista_moda}")
                print(lista_moda)
                respuesta_moda = int(input(f"Que número representa la moda de la lista?\nTu respuesta: "))
                if respuesta_moda == moda:
                    print("Respuesta correcta")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,2)  
                    
                if respuesta_moda != moda:
                    print(f"Respuesta incorrecta. La moda de la lista es {moda}")
                    contador_incorrect += 1
                    
                #Tercero de Secundaria - Quinta Pregunta - Median
                lista = []
                for i in range(11):
                    x = random.randint(2,7)
                    lista.append(x)
                p5_correcto = median(lista)
                print('¡Rápido! Monstruin está atacando, contesta correctamente para quitarle 3 puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                p5 = float(input(f"Calcula la mediana de los siguientes numeros: {lista}\nTu respuesta: "))
                if p5 == p5_correcto:
                    print("Respuesta correcta.")
                    contador_correct += 1
                    lifebar_pa=remove_life(lifebar_pa,3)  
                    printbar(lifebar_pa)
                elif p5 != p5_correcto:
                    print(f"Respuesta incorrecta. La respuesta correcta es {p5_correcto}")
                    contador_incorrect += 1
                    printbar(lifebar_pa)


        #Español 
        if matoesp=='b':
            #1ro de Secundaria
            if grados=='a':
                #Abrir Archivo correspondiente para las preguntas
                file = open('quest1SE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0    #Contador para ciclos while
                cont2while=1    #Contador 2 para funciones while
                while cont_while<5:
                    random_question = random.choice(questions)  #Escoger pregunta aleatoria
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)            
            #2do de Secundaria
            if grados=='b':
                file = open('quest2SE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()  
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0
                cont2while=1
                while cont_while<5:
                    random_question = random.choice(questions)                        
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)              
            #3ro de Secundaria
            if grados=='c':
                file = open('quest1SE.txt', 'r', encoding='UTF-8')
                lines=file.readlines()  
                file.close()
                questions=split_questions(lines)
                lifebar_pa=generar_lifebar()
                cont_while=0
                cont2while=1
                while cont_while<5:
                    random_question = random.choice(questions)                        
                    question, correct_answ, option2, option3, option4  = random_question
                    options=concatenar(correct_answ,option2,option3,option4)
                    key=options[0]
                    key=key.lower()
                    options.sort()
                    cont_while+=1
                    print(f'\n¡Rápido! Monstruin está atacando, contesta correctamente para quitarle {cont2while} puntos de vida! (ノ ಠ 益 ಠ) ノ 彡 ┻━┻')
                    printbar(lifebar_pa)
                    answ = input(f"\n{question} \n{options[0]}\t\t{options[1]} \n{options[2]}\t\t{options[3]}\n---> ")
                    if answ.lower() == key[0]:
                        print('Correcto')
                        contador_correct+=1
                        cont2while=while2num(cont_while,cont2while)
                        lifebar_pa=remove_life(lifebar_pa,cont2while)  
                    else:
                        print(f'Incorrecto! La respuesta correcta es: {correct_answ} \nNo le quitaste vidas a mounstrin :(')
                        contador_incorrect+=1
                continuar=eleg_nextgrade(lifebar_pa,win)
                continuar,gradop,grados,nivel,win=next_grade(continuar,gradop,grados,nivel,win)
    win,continuar,imprimir=end_game(win,continuar,imprimir,contador_incorrect,contador_correct,nivel,gradop,grados,contjug)
    if imprimir==True:
        listajug=addlist(listajug,name,nivel,gradop,grados,contador_incorrect,contador_correct,contjug)
        contjug+=1
    