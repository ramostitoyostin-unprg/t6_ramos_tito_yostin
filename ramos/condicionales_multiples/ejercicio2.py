import os
# BOLETA CON PREMIO
# MOSTRAR VALORES
cliente, producto, precio, cantidad= "", "", 0.0, 0

# INPUT
cliente=os.sys.argv[1]
producto=(os.sys.argv[2])
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])

# PROCESSING
monto_total=round(cantidad*precio,2)

# OUTPUT
print("###############################")
print("#      BOLETA DE VENTA        #")
print("###############################")
print("# cliente:", cliente)
print("# producto:", producto)
print("# p.u:", precio)
print("# cantidad:", cantidad)
print("# total:", monto_total)
print("###############################")

# CONDICION MULTIPLE
# si el cumple las condiciones sera casi gana, siga intentando, gano
if(monto_total>80.5 and monto_total<100.0):
    print("CASI GANA EL PREMIO")

if(monto_total<80.5):
    print("SIGA INTENTANDO")

if(monto_total>100.0):
    print("GANO LA TARJETA DORADA")
# fin_if
