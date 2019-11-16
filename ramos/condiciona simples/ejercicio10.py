import os

# mostrar valores
empresa, ruc, ingreso_neto,productos_enviados="", 0, 0.0, 0

#input
empresa=os.sys.argv[1]
ruc=(os.sys.argv[2])
ingreso_neto=float(os.sys.argv[3])
productos_enviados=float(os.sys.argv[4])

#processing
impuesto_total=(ingreso_neto*productos_enviados)

#verificador
mediana_empresa=(impuesto_total<10000)

#output
print("##################################")
print("boleta de venta de impuestos")
print("###############################")
print("empresas:",empresa)
print("#####################################")
print("ingreso neto es:",ingreso_neto)
print("productos enviados=",productos_enviados)
print("####################")
print("impuesto total=",impuesto_total)

#condicion simple
if(mediana_empresa==True):
    print("entonces es una mediana empresa")

#fin_if
