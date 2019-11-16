import os
#mostrar valores
cliente,igv, pu, comprador="", 0.0, 0.0, ""

#input
señora=os.sys.argv[1]
pu=float(os.sys.argv[2])
igv=float(os.sys.argv[3])
comprador=os.sys.argv[4]

#procesing
importe_total=(pu + igv)

#verificador
comprador_compulsivo=(importe_total>5)


#output
print("##################################")
print("voleta de venta electronica")
print("###############################")
print("cliente:",cliente)
print("#####################################")
print("comprador compulsivo:",comprador_compulsivo)
print("precio unitario=",pu)
print("igv=",igv)
print("####################")
print("importe total=",importe_total)

#condicion simple
#si el cliente es comprador compulsivo esntonces tendra descuentos
if (comprador_compulsivo==True):
    print("usted tiene decuentos especiales")


#fin_if
