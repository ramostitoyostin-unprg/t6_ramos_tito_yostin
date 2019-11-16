import os
#mostrar valores
intensidad_corriente_electrica, resistencia_electrica=0.0, 0.0

#input
intensidad_corriente_electrica=float(os.sys.argv[1])
resistencia_electrica=float(os.sys.argv[2])

#processing
voltaje=(intensidad_corriente_electrica * resistencia_electrica)

#verificador
ahorra_energia=(voltaje<200)

#output
print("##################################")
print("voleta electronica de voltaje")
print("###############################")
print("intensidad de corriente electrica:",intensidad_corriente_electrica)
print("#####################################")
print("resistencia electrica:",resistencia_electrica)
print("####################")
print("volraje=",voltaje)

#condicional simple
if (ahorra_energia==True):
    print("utiliza de forma concientisada el fluido electrico")

#fin_if
