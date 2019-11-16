import os
#mostrar valores
cliente, precio, cantidad_producto, monto_total="", 0.0, 0, 0.0

#input
cliente=os.sys.argv[1]
precio=float(os.sys.argv[2])
cantidad_producto=float(os.sys.argv[3])
monto_total=float(os.sys.argv[4])

#processing
monto_pagar=(precio*cantidad_producto)

#verificador
cliente_diamante=(monto_pagar>500)

#output
print("##################################")
print("voleta electronica de voltaje")
print("###############################")
print("cliente:",cliente)
print("#####################################")
print("precio:",precio)
print("####################")
print("monto a pagar=",monto_pagar)

#condicional simple
if (cliente_diamante==True):
    print("usted tendra usted tendra un descuento especial")

#fin-if

#condicional doble
else:
    print("usted ganara la tarjeta dorada")
