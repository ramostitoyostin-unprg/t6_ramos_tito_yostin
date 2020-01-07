import os
# TRAPECIO
# MOSTRAR VALORES
base1= 0.0
base2=0.0
haltura=0.0

# INPUT
base1=float(os.sys.argv[1])
base2=float(os.sys.argv[2])
haltura=float(os.sys.argv[3])

# PROCESSING
area=haltura*(base1+base2)/2

# OUTPUT
print("#################################")
print("        AREA DEL TRAPECIO        ")
print("#################################")
print("BASE NENOR=", base1)
print("BASE MAYOR=", base2)
print("HALTURA=", haltura)
print("#################################")
print("AREA=", area)

# CONDICION MULTIPLE
# si cumple la siguientes condiciones es muy pequeño, regular, grande, muy grande
if(area>5.0 and area<10.0):
    print("muuy pequeño")

if(area>=10.0 and area<15.5):
    print("triangulo regular")

if(area>15.5 and area<20.0):
    print("el triangulo es grande")

if(area>20.0):
    print("muy grande")
# fin_if
