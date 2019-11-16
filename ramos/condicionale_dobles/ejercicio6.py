import os
#mostrar valores
sueldo_empleado1, sueldo_empleado2, sueldo_empleado3, sueldo_mensual=0.0, 0.0, 0.0, 0.0

#input
sueldo_empleado1=float(os.sys.argv[1])
sueldo_empleado2=float(os.sys.argv[2])
sueldo_empleado3=float(os.sys.argv[3])
sueldo_mensual=float(os.sys.argv[4])

#processing
sueldo_total=(sueldo_empleado1+sueldo_empleado2+sueldo_empleado3)

#verificador
empleados_eficientes=(sueldo_total>20000)

#output

print("##################################")
print("voleta electronica de sueldo")
print("###############################")
print("sueldo:",sueldo_mensual)
print("#####################################")
print("el sueldo del empleado1:",sueldo_empleado1)
print("el sueldo del empleado2:",sueldo_empleado2)
print("el sueldo del empleado3",sueldo_empleado3)
print("####################")
print("sueldo total=",sueldo_total)

#condicion simple
#si los empleados son eficientes entonces ganaran un viaje
if (empleados_eficientes==True):
    print("entoces se iran de viaje")

#fin_if

#condicional doble
else :
    print("ganaran un boleto de avion de primera clase")

