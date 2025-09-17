



#Se da la bienvenida al programa y se indica su uso

print("Bienvenido a la aplicacion donde podras ingresar tu tienda,"
      "vender y mantener tus cuentas al dia\n")
#Se pide el capital disponible para la tienda

capital = int(input("Ingrese el capital invertido: "))

#Se pedirá registro de cuantos productos a vender se desea ingresar
#Primero se piden los nombres de los productos que desea ingresar

stopper_while = 1
cantidad_productos = int(input("Ingrese la cantidad de productos que desea vender: "))
numeral = cantidad_productos
nombres_productos = []
contador_productos = 1
while cantidad_productos >= stopper_while:
      nombres_productos.append(str(input("Indique el nombre del producto " +
                                         str((contador_productos)) + ": ")))
      contador_productos = int(contador_productos)
      contador_productos +=1
      cantidad_productos -=1

#Luego se piden los precios de cada uno de los productos

cantidad_productos2 = numeral
contador_precios = 1
contador_productos2 = 1
precios_productos = []
while cantidad_productos2 >= contador_precios:
      precios_productos.append(str(input("Indique el precio del producto " +
                                         str((contador_productos2)) + " (COP): ")))
      cantidad_productos2 -=1
      contador_productos2 +=1

#Luego se pide el porcentaje de ganancias que se le saca a cada producto

cantidad_productos3 = numeral
contador_ganancias = 1
contador_productos3 = 1
ganancias_productos = []
while cantidad_productos3 >= contador_ganancias:
      ganancias_productos.append(str(input("Indique el porcentaje sin incluir el simbolo % que le gana al producto " +
                                           str((contador_productos3)) + ": ")))
      cantidad_productos3 -=1
      contador_productos3 +=1

#Luego se pide la cantidad que se tiene por cada producto

cantidad_productos4 = numeral
contador_cada_producto = 1
contador_productos4 = 1
cantidad_cada_producto = []
while cantidad_productos4 >= contador_cada_producto:
      cantidad_cada_producto.append(str(input("Indique la cantidad que se tiene del producto " +
                                              str((contador_productos4)) + ": ")))
      cantidad_productos4 -=1
      contador_productos4 +=1

#Luego por pantalla se da cuenta de los valores registrados contando con
# nombre del producto, precio, porcentaje de ganancia y cantidad

cantidad_productos_ofrecer = numeral
referencia_producto = 0
N_producto = 1
print("")
print("La tienda ofrece los siguientes productos:\n")
while N_producto <= cantidad_productos_ofrecer:
      print("El producto " + str((N_producto)) + " llamado " + str((nombres_productos[referencia_producto])) +
            " tiene un precio de " + str((precios_productos[referencia_producto])) + " pesos (COP), se le gana un " +
            str((ganancias_productos[referencia_producto])) + "% y se tienen " + str((cantidad_cada_producto[referencia_producto])) +
            " de estos")
      referencia_producto +=1
      N_producto +=1

#Luego cada producto es ingresado a una lista a manera de
# diccionario con el fin de que luego puedan ser ofrecidos los productos

cantidad_productos_finales = numeral
segundo = 0
stopper = 1
productos_listado = []
while stopper <= cantidad_productos_finales:
      productos_listado.append({"Nombre":nombres_productos[0+(segundo)],
                                "Precio":precios_productos[0+(segundo)],
                                "Porcentaje_de_ganancia":ganancias_productos[0+(segundo)],
                                "Cantidad":cantidad_cada_producto[0+(segundo)]})
      segundo+=1
      stopper+=1

#Luego se pasará al cliente, en donde él pedirá ahora los productos que desea
#Primero se muestra el código con el que se identifica cada uno de los productos

print("\n")
print("SE ABRE LA TIENDA")
print("\n")

#Se definen las variables que se tendrán en cuenta a continuacion para la parte de ventas
primer_eje = 1
parte_codigos = 0
identificacion_producto = numeral - 1
suma_factura_total = 0
ganancias_del_dia = 0
ganancias_del_dia_porcentaje = 0
suma_factura_total_mostrar = 0
ganancias_del_dia_porcentaje_mostrar = 0
vendido = []
while primer_eje == 1:
      while parte_codigos <= identificacion_producto: #Se muestra por pantalla los productos disponibles y su código si se quiere comprar alguno
            print("El producto " + str(productos_listado[0 + parte_codigos].get("Nombre"))
                  + " tiene un precio de " + str((productos_listado[0 + parte_codigos].get("Precio")))
                  + ". Inserte el numero " + str((parte_codigos)) + " si desea este producto")
            parte_codigos += 1
      deseo = int(input("\nSi desea comprar algo, ponga un 1, sino ponga un 0: ")) #Se pregunta si de lo ofrecido quiere comprar algo
      parte_codigos = parte_codigos - identificacion_producto - 1
      if deseo == 1:
            print("")
            peticion = int(input(("Indique el numero del producto que desea: "))) #Se pide el producto que quiere
            if peticion < len(productos_listado) and peticion >= 0:
                  print("Este es su producto: " + str(productos_listado[peticion].get("Nombre"))
                  + " y este es su precio: " + str((productos_listado[peticion].get("Precio"))))
                  #Se pide la cantidad que se quiere
                  cantidad_vendido = int(input("Cuantos de estos quiere: "))
                  #Se almacen en variables los valores introducidos para luego ser mostrados en las ventas totales del dia
                  #y en la factura que se le saca a cada cliente
                  compra = (int(productos_listado[peticion].get("Precio")) * cantidad_vendido)
                  vendido.append(str(productos_listado[peticion].get("Nombre")) + " " + str(cantidad_vendido))
                  suma_factura_total = suma_factura_total + compra
                  suma_factura_total_mostrar = suma_factura_total_mostrar + suma_factura_total
                  ganado_por_compra = ((compra * int(productos_listado[peticion].get("Porcentaje_de_ganancia"))) / 100)
                  ganancias_del_dia_porcentaje = ganancias_del_dia_porcentaje + ganado_por_compra
                  ganancias_del_dia_porcentaje_mostrar = ganancias_del_dia_porcentaje_mostrar + ganancias_del_dia_porcentaje
                  #Se pide si quiere comprar algun otro producto
                  comprar_mas = int(input("Si desea comprar algo mas, ponga un 1, sino ponga un 0: "))
                  if comprar_mas == 0: #Si no quiere comprar mas se muestra la factura y el precio total de su compra, sino vuelve el codigo y se digita el o los productos adicionales
                        print("Le recibo " + str(suma_factura_total) + " pesos")
                        ganancias_del_dia = ganancias_del_dia + suma_factura_total
                        deseo = 0
                        if deseo == 0: #Si el usuario desde el principio no quiso comprar nada, se despide
                              print("Muchas gracias por su visita, vuelva pronto")
                        #Se muestra si llega otro cliente se le dice para repetir el codigo, sino para parar las ventas del dia
                        nuevo_cliente = int(input("Si llega un nuevo cliente, ponga un 1, sino ponga un 0: "))
                        if nuevo_cliente == 0: #Si cierra la tienda se muestra, en dinero lo que se vendio,
                              # la ganancia de ese dinero, lo que falta para poder recuperar lo invertido desde un inicio
                              #y la lista de productos que fueron vendidos en el dia
                                    print("Se ha cerrado la tienda")
                                    print("Hoy se ganaron: " + str((suma_factura_total_mostrar)) + " pesos")
                                    print("Al total de los productos vendidos se le sacó " + str(ganancias_del_dia_porcentaje_mostrar) + " pesos")
                                    print("Con respecto a los " + str((capital)) + " pesos invertidos faltan por recuperar "
                                          + str((capital - ganancias_del_dia_porcentaje_mostrar)) + " pesos")
                                    print("Y esto fue lo que se vendió hoy")
                                    print(vendido)
                              #Cierra el codigo
                                    break
                        if nuevo_cliente == 1:
                              primer_eje = 1

            else: #Si el usuario introducio un codigo no valido, se le pide hasta que digite uno valido
                  while peticion >= len(productos_listado) or peticion < 0:
                        print("Este código no se conoce")
                        #Cuando digite uno valido comienza a pedir de nuevo los datos y basicamente repite el codigo
                        peticion = int(input(("Indique el numero del producto que desea de nuevo: ")))
                        if peticion < len(productos_listado) and peticion >= 0:
                              print("Este es su producto: " + str(productos_listado[peticion].get("Nombre"))
                                    + " y este es su precio: " + str((productos_listado[peticion].get("Precio"))))
                              cantidad_vendido = int(input("Cuantos de estos quiere: "))
                              compra = (int(productos_listado[peticion].get("Precio")) * cantidad_vendido)
                              vendido.append(str(productos_listado[peticion].get("Nombre")) + " " + str(cantidad_vendido))
                              suma_factura_total = suma_factura_total + compra
                              ganado_por_compra = ((compra * int(productos_listado[peticion].get("Porcentaje_de_ganancia"))) / 100)
                              ganancias_del_dia_porcentaje = ganancias_del_dia_porcentaje + ganado_por_compra
                              comprar_mas = int(input("Si desea comprar algo mas, ponga un 1, sino ponga un 0: "))
                              if comprar_mas == 0:
                                    print("Le recibo " + str(suma_factura_total) + " pesos")
                                    ganancias_del_dia = ganancias_del_dia + suma_factura_total
                                    deseo = 0
                                    if deseo == 0:
                                          print("Muchas gracias por su visita, vuelva pronto")
                                          suma_factura_total = 0
                                          ganancias_del_dia_porcentaje = 0
                                    nuevo_cliente = int(
                                          input("Si llega un nuevo cliente, ponga un 1, sino ponga un 0: "))
                                    if nuevo_cliente == 0:
                                          print("Se ha cerrado la tienda")
                                          print("Hoy se ganaron: " + str(suma_factura_total_mostrar) + " pesos")
                                          print("Al total de los productos vendidos se le sacó " + str(ganancias_del_dia_porcentaje) + " pesos")
                                          print("Con respecto a los " + str(
                                                (capital)) + " pesos invertidos faltan por recuperar "
                                                + str((capital - ganancias_del_dia_porcentaje)) + " pesos")
                                          print("Y esto fue lo que se vendió hoy")
                                          print(vendido)
                                          primer_eje = primer_eje + 1
                                          break
                                    if nuevo_cliente == 1:
                                          primer_eje = 1
      if deseo == 0: #Si el usuario miro los productos y no quiso nada se le despide
            print("Muchas gracias por su visita, vuelva pronto")
            suma_factura_total = 0
            ganancias_del_dia_porcentaje = 0
            #Se pide de nuevo si viene un nuevo cliente o si se cierran las ventas del dia
            nuevo_cliente = int(input("Si llega un nuevo cliente, ponga un 1, sino ponga un 0: "))
            if nuevo_cliente == 0: #Si se cierra, se muestran los valores antes mencionados
                  print("Se ha cerrado la tienda")
                  print("Hoy se ganaron: " + str(suma_factura_total_mostrar) + " pesos")
                  print("Al total de los productos vendidos se le sacó " + str(ganancias_del_dia_porcentaje) + " pesos")
                  print("Con respecto a los " + str((capital)) + " pesos invertidos faltan por recuperar "
                        + str((capital - ganancias_del_dia_porcentaje)) + " pesos")
                  print("Y esto fue lo que se vendió hoy")
                  print(vendido)
                  primer_eje = primer_eje + 1
                  break
            if nuevo_cliente == 1:
                  primer_eje = 1


#Solo quiero decir que este fue el programa que mas me ha tomado tiempo hasta ahora y me siento muy orgulloso de lo
#realizado















      




























