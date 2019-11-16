import os
#mostrar valores
masa, gravedad =0.0 ,0.0

#input
masa=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])

#processing
peso=(masa * gravedad)

#verificador
peso_saludable=(peso<70)

#output
print("##################################")
print("voleta electronica de peso")
print("###############################")
print("masa:",masa)
print("#####################################")
print("gravedad:",gravedad)
print("####################")
print("peso:",peso)

#condicion simple
if(peso_saludable==False):
    print("esta mal de salud")

#fin_if

#condicional doble
else :
    print("debe comer productos con menos grasas")
