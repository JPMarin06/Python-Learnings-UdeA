# Bienvenida al código y se muestra lo que se puede documentar
print("\nBienvenid@ al código en el cual podrá digitar y documentar la información de sus cultivos,"
      "en donde podrá incluir:\n\n "
      "-El nombre del cultivo\n "
      "-Días y horarios de mantenimiento\n "
      "-Días y horarios de regado\n "
      "-Días y horarios de abono\n "
      "-La fase en la que está el cultivo\n")

#Se pide el numero de cultivos que se desean poner y se nombran las listas
numero_cultivos = int(input("Indique el número de cultivos que desea documentar: "))
nombres_lista = []
mantenimientos_lista = []
regado_lista = []
abono_lista = []
fases_lista = []
stopper_while = 1

# Se piden los datos de cada uno de los cultivos y se guardan en las listas
while stopper_while <= numero_cultivos:
    nombre_cultivo = str(input("Indique lo que se cultiva en el cultivo " + str((stopper_while)) + ": "))
    nombres_lista.append(nombre_cultivo)
    mantenimiento_cultivo = str(input("Indique por favor el horario y días del mantenimiento del cultivo de " +
                                      (nombre_cultivo) + ": "))
    mantenimientos_lista.append(mantenimiento_cultivo)
    regado_cultivo = str(input("Indique por favor el horario y días del regado del cultivo de "
                               + (nombre_cultivo) + ": "))
    regado_lista.append(regado_cultivo)
    abono_cultivo = str(input("Indique por favor el horario y días del abono del cultivo de "
                              + (nombre_cultivo) + ": "))
    abono_lista.append(abono_cultivo)
    print("Indique el número de la fase en la que se encuentra el cultivo. Recuerde que:\n"
          "La fase 1 es de establecimiento\n"
          "La fase 2 es de crecimiento rápido\n"
          "La fase 3 es de endurecimiento\n")
    fase_cultivo = int(input("Indique por favor la fase en la que se encuentra el cultivo de "
                             + (nombre_cultivo) + ": "))
    fases_lista.append(fase_cultivo)
    print("")
    stopper_while +=1
    nombre_cultivo = 0
    mantenimiento_cultivo = 0
    regado_cultivo = 0
    abono_cultivo = 0
    fase_cultivo = 0
contador = 0

#Comienza la parte de extraer información, primero se muestra de lo que está hecha la huerta, osea, se muestran los
#cultivos que el usuario documentó
print("SU HUERTA ESTÁ HECHA DE:\n")
for cultivos in range(1, (numero_cultivos+1)):
    print("El cultivo número " + str((cultivos)) + " de " + str((nombres_lista[0+(contador)]) + ":\n" + "Tiene un horario "
            "de mantenimiento de: " + str((mantenimientos_lista[0+(contador)]))) + "\nTiene un horario de regado de: " +
            str((regado_lista[0+(contador)])) + "\nTiene un horario de abono de: " + str((abono_lista[0+contador])) +
          "\nEl cultvo se encuentra en la fase: " + str((fases_lista[0+(contador)])) + "\n")
    contador +=1

stopper_one = 1
stopper_two = 1

#Acá se muestra la informacion de los cultivos
while stopper_one == 1:
    deseo = int(input("Marque un 1 si desea obtener información de algún cultivo, marque un 0 si no lo desea: "))
    #Primero se pregunta si desea obtener informacion
    print("")
    if deseo == 1:
        #Si el usuario desea obtener informacion, se pide el cultivo del que se quiere obtener informacion
        while stopper_two == 1:
            cultivo_deseado = int(input("Marque el número del cultivo del que desea obtener informacion: "))
            if cultivo_deseado > 0 and cultivo_deseado <= numero_cultivos:
                #Si el numero del cultivo está bien, se muestra la informacion
                print("\nCultivo número " + str((cultivo_deseado)) + " de " + (nombres_lista[(cultivo_deseado)-1]) + ":\n"
                      + "Horario mantenimiento: " +
                      mantenimientos_lista[(cultivo_deseado) - 1] + "\n"
                      + "Horario regado: " +
                      regado_lista[(cultivo_deseado) - 1] + "\n"
                      + "Horario abono: " +
                      abono_lista[(cultivo_deseado) - 1] + "\n"
                      + "Fase del cultivo: " + str(fases_lista[(cultivo_deseado) - 1]) + "\n")
                break
            else:
                #Si el numero del cultivo que puso el usuario está mal, se repite
                print("Cultivo desconocido")
    if deseo == 0:
        #Si el usuario no desea obtener informacion, se despide y se cierra el codigo
        print("Muchas gracias por ver la huerta, vuelva pronto")
        stopper_one +=1
        stopper_two +=1
    if deseo > numero_cultivos or deseo < 0:
        #Si el usuario no marcó un código válido, se repite
        print("Código desconocido")












