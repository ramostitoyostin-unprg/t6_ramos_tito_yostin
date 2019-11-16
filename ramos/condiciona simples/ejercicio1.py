
import os
#mostrar valores
distancia, tiempo=0.0, 0

#input
distancia=float(os.sys.argv[1])
tiempo=os.sys.argv[2]

#processing
velocidad_permitida=(distancia / tiempo)


#verificador
es_un_infractor=(velocidad_permitida>90)

#output
print("##################################")
print("boleta de velocidad permitida")
print("###############################")
print("distancia:",distancia)
print("#####################################")
print("tiempo:",tiempo)
print("####################")
print("velocidad permitida",velocidad_permitida)

#condicion simple
#si el señor es un infractor, entonces pagara un multa
if (velocidad_permitida==True):
    print("pagaras una multa")

#fin_if

