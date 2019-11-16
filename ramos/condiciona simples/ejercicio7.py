import os
#mostrar valores
trabajo, tiempo =0.0, 0

#input
trabajo=float(os.sys.argv[1])
tiempo=os.sys.argv[2]

#processing
potencia=(trabajo / tiempo)

#verificador
maquina_veloz=(potencia>5000)

#output
print("##################################")
print("boleta de velocidad maquina veloz")
print("###############################")
print("trabajo:",trabajo)
print("#####################################")
print("tiempo:",tiempo)
print("####################")
print("potencia",potencia)

#condicion simple
#si la maquina es veloz entonces, su propietario recibira mas ingresos
if (maquina_veloz==True):
    print("recibira mas ingresos")

#fin_if
