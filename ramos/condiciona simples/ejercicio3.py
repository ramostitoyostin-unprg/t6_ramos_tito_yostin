import os
#mostrar valores
fuerza, distancia=0.0, 0.0

#input
fuerza=float(os.sys.argv[1])
distancia=float(os.sys.argv[2])

#procesing
trabajo=(fuerza * distancia)

#verificador
maquina_eficiente=(trabajo>200)

#output
print("##################################")
print("voleta electronica de trabajo ")
print("###############################")
print("fuerza:",fuerza)
print("#####################################")
print("distancia:",distancia)
print("####################")
print("trabajo:",trabajo)

#condicion simple
#sila maquina realiza mayor trabajo entonces sera eficiente
if (maquina_eficiente==True):
    print("la maquina tendra mas trabajo")

#fin_if

