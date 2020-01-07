import os
# INPUT
velocidad_01=int(os.sys.argv[1])
velocidad_02=int(os.sys.argv[2])
distancia=int(os.sys.argv[3])

# PROCESSING
Tiempo_de_encuentro=(distancia)/(velocidad_01+velocidad_02)

# VERIFICADOR
validar_tiempo_encuentro=(Tiempo_de_encuentro==20)

# OUTPUT
print("##################################")
print(("# BOLETA DE FISICA   "))
print("##################################")
print("#")
print("# velocidad 01:   ",velocidad_01," ")
print("# velocidad 02:   ",velocidad_02," ")
print("# distancia:      ",distancia,"  ")
print("# Tiempo de encuentro:  ",Tiempo_de_encuentro," ")
print("###########################################")

# CONDICIONAL MULTIPLES
# comprobando el tiempo de encuentro si es mayor a 500
if (validar_tiempo_encuentro==True):
    print(" el tiempo es aceptable")
if (validar_tiempo_encuentro>=20 and validar_tiempo_encuentro<=50):
    print(" el tiempo no es aceptable")
if (validar_tiempo_encuentro==False):
    print(" no llega a tiempo ")
# fin_if
